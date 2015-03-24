
from pylab import *
import pandas as pd
import scipy.interpolate

#Cargas Datos
xl = pd.ExcelFile('temperaturas.xlsx') #esto descarga el archivo de Excel, distingue entre las sheet que quiero importar e imprime el inicio 
xl.sheet_names 
[u'temperaturas'] 
dfinit = xl.parse("temperaturas") #variable que guarda las columnas del archivo df

#Arreglo de ciudades analizadas
cities = ['Bogota', 'Ipiales', 'Cali', 'Barranquilla', 'Bucaramanga']

#Esta funcion convierte las fechas para poderlas graficar cm tal
def conver(d):
    dates=[]   
    for fecha in d:
        date = datetime.datetime.strptime(fecha,"%Y-%m-%d")
        dates.append(date)
    dates = matplotlib.dates.date2num(dates)
    dates = sort(dates)
    return dates

#Esta funcion grafica las interpolaciones en cuadros diferentes
def graficar(dates,lin,spl):
    figure(figsize=(15,10))
    plt.subplot(3, 1, 1)
    plot_date(dates, t, 'mv')
    plot_date(dates,(lin.iloc[:,2]), 'b', c='g' )
    plt.title(c)
    plt.ylabel(u"Temeperatura (Celsius)")
    plt.legend([u'Datos', u'Interpolacion Lineal'])
    plt.subplot(3, 1, 2)
    plot_date(dates, t, 'mv')
    plot_date(dates,(spl.iloc[:,2]), 'b', c='b' )
    plt.ylabel(u'Temperatura(Celsius)')
    plt.legend([u'Datos', u'Interpolacion Splines'])
    plt.savefig(c+'.pdf')
 
#Esta funcion grafica en un rango pequenno para hacer una mejor comparacion de las graficas
def graficarzoom(dates,lin,spl):
    figure(figsize=(15,3))    
    plot_date(dates, t, 'mv')
    plot_date(dates,(lin.iloc[:,2]), 'b', c='g' )
    plot_date(dates,(spl.iloc[:,2]), 'b', c='b' )
    plt.title(c+' Zoom')
    plt.ylabel(u"Temeperatura (Celsius)") 
    plt.ylabel(u'Temperatura(Celsius)')
    plt.legend([u'Datos', u'Interpolacion Lineal', u'Interpolacion Splines'])
    plt.savefig(c+'zoom.pdf')
    xlim(dates[3],dates[50])

#Hacer las interpolaciones y graficarlas
for ciudad in cities:
    df = dfinit[dfinit.ciudad == ciudad]
    df = df.iloc[:,[2,3,4]]
    d = df.iloc[:,0]
    t = df.iloc[:,2]
    c = df.iloc[5,1]
    dates = conver(d)
    lin = df.interpolate()
    spl = df.interpolate(method='spline', order=3)
    graficar(dates,lin,spl)
    graficarzoom(dates,lin,spl)
