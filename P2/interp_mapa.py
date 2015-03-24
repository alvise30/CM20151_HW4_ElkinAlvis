
from pylab import *
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

#Cargar Datos
nc = Dataset('air.mon.ltm.nc')
air = nc.variables['air'][0,:,:] #Seleccionando los datos necesarios
lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]

#Grafiacando
plt.figure(figsize=(15,10))
lon2d, lat2d = meshgrid(lon, lat)
b = Basemap(lon_0=180) #This defines the center of the map, 180 since longitudes go from 0 to 360
x, y = b(lon2d, lat2d)
b.contourf(x, y, air, cmap=get_cmap('Greens'))
b.drawcoastlines()
b.colorbar();
plt.savefig('temp_med.pdf')
