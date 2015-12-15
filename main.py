import pond_rasters
import resample_timeseries
import matplotlib.pyplot as plt

#--------------------------------------------------------
#Execute Program
#--------------------------------------------------------

filename = r'C:\Users\konrad\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\ET\Master_Resampled.csv'
freq_path = r'C:\Users\konrad\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\freqwet_10m_BRAT100.tif'
dep_path = r'C:\Users\konrad\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\ponddepth_10m_ACT.tif'
dep_path1 = r'C:\Users\konrad\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\ponddepth_10m_BRAT50.tif'
dep_path2 = r'C:\Users\konrad\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\Raster\ponddepth_10m_BRAT100.tif'

df_new = resample_timeseries.getDf(filename)
df_start = df_new
df_new['No Ponds'] = pond_rasters.calcET(df_start, freq_path, dep_path, 2)
df_new['Ponds Actual'] = pond_rasters.calcET(df_start, freq_path, dep_path, 3)
df_new['Ponds 50% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path1, 3)
df_new['Ponds 100% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path2, 3)

df_new.drop(df_new.columns[[0,1,2,3]], axis=1, inplace=True)

#print df_new

df_new = df_new.cumsum()


plt.figure; df_new.plot();
plt.show()
