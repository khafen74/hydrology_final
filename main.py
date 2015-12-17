import pond_rasters
import resample_timeseries
import matplotlib.pyplot as plt

#--------------------------------------------------------
#Execute Program
#--------------------------------------------------------

#set paths to files for analysis
filename = r'C:\Users\khafe\Desktop\Classes\CEE_6400_Hydrology\FinalProject\Data\ET\Master_Resampled.csv'
out_csv = 'C:/Users/khafe/Desktop/Classes/CEE_6400_Hydrology/FinalProject/Results/csv/allvalues.csv'
in_base = 'C:/Users/khafe/Desktop/Classes/CEE_6400_Hydrology/FinalProject/Results/Raster/'
freq_path = in_base + 'freqwet_total.tif'
dep_path = in_base + 'dep_BRAT25.tif'
dep_path1 = in_base + 'dep_BRAT50.tif'
dep_path2 = in_base + 'dep_BRAT75.tif'
dep_path3 = in_base + 'dep_BRAT100.tif'

#create dataframe containing ET values
df_new = resample_timeseries.getDf(filename)
#copy dataframe
df_start = df_new

#set return type (difference from no ponds = 3, actual values = 1, ET with no ponds =2)
returnType = 3

#calculate ET volumes for period of interest
df_new['No Ponds'] = pond_rasters.calcET(df_start, freq_path, dep_path, 2)
df_new['Ponds 25% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path, returnType)
df_new['Ponds 50% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path1, returnType)
df_new['Ponds 75% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path2, returnType)
df_new['Ponds 100% BRAT'] = pond_rasters.calcET(df_start, freq_path, dep_path3, returnType)

#drop unnecessary data columns
df_new.drop(df_new.columns[[0,1,2,3]], axis=1, inplace=True)

#print dataframe to csv
#df_new.to_csv(out_csv)

#calculate cumulative sum
df_new = df_new.cumsum()

#plot values
ax = df_new.plot();
ax.set_ylabel('ET, cumulative difference (m^3)')
ax.set_xlabel('Date')
plt.tight_layout()
plt.show()
