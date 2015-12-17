#Konrad Hafen
#Hydrology
#Final Project

import pandas as pd
import numpy as np
from osgeo import gdal

def calcET(df_et, freq_path, dep_path, pond):
    freqDS = gdal.Open(freq_path, gdal.GA_ReadOnly)
    depDS = gdal.Open(dep_path, gdal.GA_ReadOnly)
    freq_band = freqDS.GetRasterBand(1)
    dep_band = depDS.GetRasterBand(1)
    freq_data = freq_band.ReadAsArray()
    dep_data = dep_band.ReadAsArray()

    dry_data = np.where(freq_data > 0.0, 1, 0)
    wet_data = np.where(dep_data > 0.0, dep_data, 0)
    nDry = np.count_nonzero(dry_data)
    nWet = np.count_nonzero(wet_data)
    sumWet = np.sum(wet_data)

    geot = freqDS.GetGeoTransform()
    cellArea = abs(geot[1]*geot[5])
    cellArea_mm2 = cellArea*1000*1000
    toM3 = pow(10,-9)
    wetVolume = sumWet*cellArea

    et_list = df_et.values.tolist()
    et_noPond = []
    et_pond = []
    et_diff = []

    for i in et_list:
        noPond = (nDry * i[1]) * cellArea_mm2 * toM3
        pondVal = (((nDry - nWet) * i[1] * cellArea_mm2) + ((nWet * i[1] * 1.05) * cellArea_mm2)) * toM3

        et_noPond.append(noPond)
        et_pond.append(pondVal)
        et_diff.append(pondVal-noPond)

    print 'dry area: ' + str(nDry*cellArea) + ' wet area: ' + str(nWet*cellArea) + ' pond volume: ' + str(wetVolume) + ' et pond: ' + str(sum(et_pond)) + ' et no pond: ' + str(sum(et_noPond))

    if pond == 1:
        return et_pond
    elif pond == 2:
        return et_noPond
    elif pond == 3:
        return et_diff
    else:
        print 'not returning anything'
