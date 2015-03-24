
from pylab import *
from mpl_toolkits.basemap import Basemap


#Cargar datos
array = np.genfromtxt("datos.csv",delimiter=",") #sube el csv
LAT = array[:150,3] #elige las columnas de interes
LON = array[:150,2] 

#Hacer grafica en el mapamundi
plt.figure(figsize=(15,10))
b = Basemap(lon_0=180)
x, y = b(LON, LAT)
b.drawcoastlines()
b.drawmeridians(np.arange(0, 360, 30))
b.drawparallels(np.arange(-90, 90, 30))
b.scatter(x,y,c='m')
plt.savefig('top_150.png')
