#Konrad Hafen
#Hydrology
#Final Project

import pandas as pd
import numpy as np
from osgeo import gdal

def calcET():
    #get ET values
    inData = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\ET\Master_Resampled.csv'
    df_et = pd.DataFrame.from_csv(inData)

    #set raster paths
    freq_path = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\freqwet_10m.tif'
    dep_path = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\ponddepth_10m_580.tif'

    freqDS = gdal.Open(freq_path, gdal.GA_ReadOnly)
    depDS = gdal.Open(dep_path, gdal.GA_ReadOnly)
    freq_band = freqDS.GetRasterBand(1)
    dep_band = depDS.GetRasterBand(1)
    freq_data = freq_band.ReadAsArray()
    dep_data = dep_band.ReadAsArray()

    dry_data = np.where(freq_data > 0.0, 1, 0)
    wet_data = np.where(dep_data > 0.0, 1, 0)
    nDry = np.count_nonzero(dry_data)
    nWet = np.count_nonzero(wet_data)

    geot = freqDS.GetGeoTransform()
    cellArea = abs(geot[1]*geot[5])
    cellArea_mm2 = cellArea*1000*1000
    toM3 = pow(10,-9)

    et_list = df_et.values.tolist()
    et_noPond = []
    et_pond = []

    for i in et_list:
        noPond = (nDry * i[1]) * cellArea_mm2 * toM3
        pond = (((nDry - nWet) * i[1] * cellArea_mm2) + ((nWet * i[1] * 1.05) * cellArea_mm2)) * toM3

        et_noPond.append(noPond)
        et_pond.append(pond)
        print noPond, pond

    print et_list
    print len(et_list)
    print geot[1]
    print geot[5]
    print toM3

