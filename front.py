from os import sep
import aiohttp
import asyncio
import argparse
import pprint
import json
import numpy as np
import matplotlib.pyplot as plt

NO_DATA = -9999

def paintPopulation(X, Y):
    fig = plt.figure()
    plt.scatter(X, Y, marker='o', color='darkgray')
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(loc="best")
    plt.title("Population Distribution Diagram",fontsize=16)
    plt.show()

def getAxisList(lonMin, lonMax, latMin, latMax, ret):
    step = 30 / 3600
    xList = []
    yList = []
    i = 0
    for lon in np.arange(lonMin, lonMax, step):
        j = 0
        for lat in np.arange(latMin, latMax, step):
            if ret[i][j] != NO_DATA and ret[i][j] > 0:
                xList.append(lon)
                yList.append(lat)
    return xList, yList


async def main(host, port, type, num, co):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://{host}:{port}/pop?type={type}&num={num}&co={co}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            #json_to_process = await response.json()
            json_to_process = [{'TotalPopulation': 4174.176958676027, 'lonMin': 135.0, 'latMin': 45.0, 'lonMax': 135.1, 'latMax': 45.2, 'row': 12, 'col': 25, 'GridStats': [{'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901342}, 
{'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 
4.901342}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901341}, {'Data': 4.901342}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, 
{'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': -9999}, {'Data': -9999}, 
{'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': 4.902053}, {'Data': 
4.902053}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902054}, {'Data': 4.902053}, {'Data': 4.902053}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, 
{'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': 4.903478}, {'Data': 4.903479}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': 4.904191}, {'Data': 4.904192}, {'Data': -9999}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904902}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904902}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904902}, 
{'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904903}, {'Data': 4.904902}, {'Data': 4.904903}, {'Data': 4.904902}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905614}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905616}, {'Data': 4.905614}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.905616}, {'Data': 4.905615}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906328}, {'Data': 4.906326}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.906328}, {'Data': 4.906327}, {'Data': 4.90704}, {'Data': 4.90704}, {'Data': 4.90704}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.90704}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': 4.907039}, {'Data': 4.90704}, {'Data': -9999}, {'Data': 4.907752}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': 4.907752}, {'Data': 4.90775}, {'Data': 
4.907752}, {'Data': 4.90775}, {'Data': 4.907752}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': 4.907752}, {'Data': 4.90775}, {'Data': 4.907752}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': 4.907752}, {'Data': 4.90775}, {'Data': 4.907752}, {'Data': 4.907751}, {'Data': 4.907751}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908462}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908463}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': 4.908463}, {'Data': 4.908464}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}, {'Data': -9999}]}]
            json_to_process = json_to_process[0]
            x_list = []
            y_list = []
            r_list = []
            stat = json_to_process.get('GridStats')
            total = json_to_process.get('TotalPopulation')
            cols = json_to_process.get('col')
            rows = json_to_process.get('row')
            lonMin = json_to_process.get('lonMin')
            lonMax = json_to_process.get('lonMax')
            latMin = json_to_process.get('latMin')
            latMax = json_to_process.get('latMax')
            print(f'Total Population: {total}')
            print(stat)
            for i in range(rows):
                l = []
                for j in range(cols):
                    l.append(stat[i*rows+j].get('Data'))
                r_list.append(l)
            x_list, y_list = getAxisList(lonMin=lonMin, lonMax=lonMax, latMin=latMin, latMax=latMax, ret=r_list)
            print('----------')
            print(len(x_list))
            print(len(y_list))
            paintPopulation(np.array(x_list), np.array(y_list))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='world population client')
    parser.add_argument('--type', dest='type')
    parser.add_argument('--num', dest='num', type=int)
    parser.add_argument('--co', dest='co')
    parser.add_argument('host')
    parser.add_argument('port')
    args = parser.parse_args()
    print(f'{args}')

    asyncio.run(main(args.host, args.port, args.type, args.num, args.co))