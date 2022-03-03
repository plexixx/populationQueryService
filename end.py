from sanic import Sanic
from sanic.request import Request, RequestParameters
from sanic.response import HTTPResponse, raw, redirect, text, json, stream
from sanic.exceptions import NotFound, ServerError
import json as JSON
from os import abort
import asyncio, aiofiles
import numpy as np
from shapely import geometry
import matplotlib.pyplot as plt
from osgeo import gdal, gdal_array


Search_Schema = {
    "type": "polygon",
    "num": 0,
    "coordinates": []
}

NO_DATA = -9999
reqJSON = {}
ds = [] # gdal Dataset list
data = [] # numpy array list to store grid stats
X = [-180, -90, 0, 90, -180, -90, 0, 90]
Y = [0, 0, 0, 0, -90, -90, -90, -90]

def readFile():
    d = []
    for i in range(4):
        ds.append(gdal.Open('gpw_v4_population_count_rev11_2020_30_sec_'+str(i+1)+'.asc'))
        if i == 3:
            d.append(gdal_array.DatasetReadAsArray(ds[i]))
        else:
            d.append(np.ndarray([1,2,3]))
    data.append(d)
    
def splitCoor(n, rawCoordinates):
    print(type(rawCoordinates))
    print(rawCoordinates)
    co = rawCoordinates.split(sep='_')
    lis = []
    for i in range(n):
        lis.append([float(co[i*2]), float(co[i*2+1])])
    print(type(lis[0]))
    return lis

# 经纬度转换为矩阵坐标
def world2xyz(lon, lat):
    if lon >= X[0] and lon < X[1]:
        i = 0 if lat >= Y[0] else 4
    elif lon >= X[1] and lon < X[2]:
        i = 1 if lat >= Y[1] else 5
    elif lon >= X[2] and lon < X[2]:
        i = 2 if lat >= Y[2] else 6
    else:
        i = 3 if lat >= Y[3] else 7

    basex = X[i]
    basey = Y[i]
    x = ((lon - basex)*3600)//30 + 1
    y = ((lat - basey)*3600)//30 + 1
    return int(x), int(y), i

def getCellPopulation(cellLon, cellLat):
    x, y, i = world2xyz(cellLon, cellLat)
    print(f'x, y, i: {x, y, i}')
    print(f'data:{data[0][i][x][y]}')
    return data[0][i][x][y]

def calcPopulation(lonLats):
    print("----------calcPopulation-----------")
    polygon = geometry.Polygon(lonLats)
    (lonMin, latMin, lonMax, latMax) = polygon.bounds
    step = 30 / 3600 # 步长为30角秒，转换为角度
    cellArea = geometry.Polygon.from_bounds(0, 0, step, step).area
    total = 0
    ret = []
    print(lonMin, latMin, lonMax, latMax)
    for lon in np.arange(lonMin, lonMax, step):
        #print(f'lon:{lon}')
        r = []
        for lat in np.arange(latMin, latMax, step):
            #print(f'lat:{lat}')
            cellLon1 = lon - lon % step - step
            cellLon2 = lon - lon % step + step
            cellLat1 = lat - lat % step - step
            cellLat2 = lat - lat % step + step
            cellPolygon = geometry.Polygon.from_bounds(cellLon1, cellLat1, cellLon2, cellLat2)
            interArea = cellPolygon.intersection(polygon).area
            if interArea > 0.0:
                print(f'lon:{lon},lat:{lat},inter:{interArea}')
                p = getCellPopulation(cellLon=cellLon1, cellLat=cellLat1) 
                if p != NO_DATA:
                    total += p * (interArea / cellArea)
                print(f'p:{p}')
                r.append(p)
            else:
                r.append(NO_DATA)
        ret.append(r)
    print(ret)    
    print(f'total:{total}')
    return total, lonMin, latMin, lonMax, latMax, ret


app = Sanic('GlobalPopulationApp')

@app.middleware('request')
async def checkArg(req):
    schema = {
        "type": req.args.get('type'),
        "num": req.args.get('num'),
        "coordinates": req.args.get('co')
    }
    if schema["num"] != None:
        Search_Schema.update(schema)
    print(Search_Schema)


@app.route('/pop', methods=["PATCH", "GET", "POST"])
async def get_population(request):
    try:
        if Search_Schema.get("type")=="polygon":
            Search_Schema["coordinates"] = splitCoor(int(Search_Schema["num"]), Search_Schema["coordinates"])
            total, lonMin, latMin, lonMax, latMax, ret = calcPopulation(Search_Schema['coordinates'])
            print(total)
            print(ret)
            stat = []
            for i in range(len(ret)):
                for j in range(len(ret[i])):
                    dic = {"Data": ret[i][j]}
                    stat.append(dic)
            retJSON = [{
                "TotalPopulation": total,
                "lonMin": lonMin,
                "latMin": latMin,
                "lonMax": lonMax,
                "latMax": latMax,
                "row": len(ret),
                "col": len(ret[0]),
                "GridStats": stat
            }]
            print(retJSON)
            print("dumps")
            print(JSON.dumps(retJSON))
            print(JSON.loads(JSON.dumps(retJSON)))
            return json(JSON.loads(JSON.dumps(retJSON)))
        
        else:
            return text("Invalid File Format!")

    except Exception as e:
        return text("lol, an accident just happened.")

@app.exception(NotFound)
async def ignore_404s(request: Request,
                      exception: NotFound) -> HTTPResponse:
    return text("Oops, That page couldn't found.")


async def server_error_handler(request, exception):
    return text('Oops, Sanic Server Error! Please contact the blog owner',
                status=500)

if __name__ == "__main__":
    readFile()
    app.run(host="127.0.0.1", port=8000)