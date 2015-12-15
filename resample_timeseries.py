# -*- coding: utf-8 -*-
"""
CEE 6400
Fall 2015
Author: Daniel Hamill
"""

import pandas as pd
import os

def resampleTimeseries():
    #Build file paths to exported csv's

    path_fb = os.path.normpath(os.path.join('c:\\','workspace','Fall_2015','CEE_6400','Final_Project','iUTAH_GAMUT_LR_FB_C_RawData_2014.csv'))
    path_tg = os.path.normpath(os.path.join('c:\\','workspace','Fall_2015','CEE_6400','Final_Project','iUTAH_GAMUT_LR_TG_C_RawData_2014.csv'))
    path_exp = os.path.normpath(os.path.join('c:\\','workspace','Fall_2015','CEE_6400','Final_Project','iUTAH_GAMUT_LR_TWDEF_C_RawData_2014.csv'))
    op = os.path.normpath(os.path.join('c:\\','workspace','Fall_2015','CEE_6400','Final_Project','Output'))

    path_fb = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\iUTAH_GAMUT_LR_FB_C_RawData_2014.csv'
    path_tg = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\iUTAH_GAMUT_LR_TG_C_RawData_2014.csv'
    path_exp = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\iUTAH_GAMUT_LR_TWDEF_C_RawData_2014.csv'
    op = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\ET'

    outfile = ['\FB_Resapmpled.csv','\TG_Resampled.csv','\EXP_Resampled.csv']

    list = [path_fb,path_tg,path_exp]
    rs_list = []
    n=0
    for file in list:
        df = pd.DataFrame.from_csv(file)
        df2 = df.resample('D', how='mean')
        outname =op + str(outfile[n])
        rs_list.append(outname)
        df2.to_csv(outname, sep=',')
        n += 1

    del df, df2

    n= 0

    for file in rs_list:
        if n==0:
            df = pd.DataFrame.from_csv(file)
            n += 1
        elif n==1:
            df2= pd.DataFrame.from_csv(file)
            df = df.append(df2)
            del df2

    df3 = df.resample('D', how='mean')
    oname = op +'\Master_Resampled1.csv'
    df3.to_csv(oname, sep=',')

    return df3

def getDf(filename):
    df = pd.DataFrame.from_csv(filename)
    return df

def getDfDates(df):
    list = df.tolist()
    return list
