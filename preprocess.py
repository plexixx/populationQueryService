import os
import glob
import numpy as np
import matplotlib as ml
from osgeo import gdal
import json
import rasterio
from rasterio.mask import mask
import geojson


def Clip(Tiff, Geodata):
    rasterfile = Tiff
    geoms = json.loads(Geodata)  # 解析string格式的geojson数据
    rasterdata = rasterio.open(rasterfile)
    member = 0.0  # 记录总人数
    Gridnumber = 0  # 记录相交区域总像素点数
    Transform = rasterdata._transform  # 得到影像六参数

    # 掩模得到相交区域
    out_image, out_transform = mask(rasterdata, Geodata, all_touched=True, crop=True, nodata=rasterdata.nodata)
    out_list = out_image.tolist()
    out_list = out_list[0]

    for k in range(len(out_list)):
        for j in range(len(out_list[k])):
            if out_list[k][j] >= 0:
                member += out_list[k][j]
                Gridnumber += 1
    # 人数单位为万人，小数点后保留两位
    print(round(member / 2500, 2))
    # 面积单位为平方公里，小数点后保留两位
    print(round(Gridnumber * Transform[0] * Transform[3] / 250000, 2))
 
if __name__ == '__main__':
    geojson = "{\"type\":\"Polygon\",\"coordinates\":[ \
        [[80.0,50.0], [83.0,50.0], [83.0,53.0],[80.0,53.0]]]}"
    Clip("out0.tif",geojson)
"""
if __name__ == "__main__":
    path = 'D:\Vscode_py\*.asc'
    i = 0
    for name in glob.glob(path):
        gdal.BuildVRT('out'+ str(i) + '.vrt', name)
        gdal.Translate('out'+ str(i) + '.tif', 'out'+ str(i) + '.vrt')
        i += 1
"""