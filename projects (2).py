
# region importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, num2date
import time, calendar, datetime, numpy
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
# endregion

# region extract file
file_path = 'project/customers.csv'
data = pd.read_csv(file_path,"r")
dataframe = pd.DataFrame(data)
# endregion

# region findout data info
print("\nData Types:")
print(dataframe.dtypes)

print("\nDataFrame Info:")
dataframe.info()

print("\nDataFrame Shape:", dataframe.shape)
print("DataFrame Dimensions:", dataframe.ndim)
# endregion

# region find and handle missing data
print("\nMissing Data Summary:")
print(dataframe.isna().sum())

# Drop rows with any missing values
dataframe = dataframe.dropna()
print("\nAfter cleaning:")
dataframe.info()
# endregion

# region plot customers country

# data downloaded from the form at
# http://coastwatch.pfeg.noaa.gov/erddap/tabledap/apdrcArgoAll.html
filename, headers = urlretrieve("https://erddap.ifremer.fr/erddap/tabledap/ArgoFloats-index.nc?date%2Clatitude%2Clongitude&date%3E=2010-01-01&date%3C=2010-01-08&latitude%3E=-90&latitude%3C=90&longitude%3E=-180&longitude%3C=180&distinct()")
lats = dataframe["Latitude"].values
lons = dataframe["Longitude"].values

os.remove(filename)
m = Basemap(projection='hammer',lon_0=180)
x, y = m(lons,lats)
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
m.scatter(x,y,17,marker='o',color='k')
plt.show()

# endregion

# region plot customers creditlimit with mean line

mean_value = dataframe["creditLimit"].mean
plt.plot(dataframe["creditLimit"])
mean_value = dataframe["creditLimit"].mean()  # Compute mean first
plt.plot([0, 120], [mean_value, mean_value], "g--", label="mean")
plt.legend
plt.show()

# endregion



