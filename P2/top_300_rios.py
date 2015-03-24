
from pylab import *
import pandas as pd

#Cargar datos
xl = pd.ExcelFile('coastal-stns-byVol-updated-oct2007.xlsx') #esto descarga el archivo de Excel, distingue entre las sheet que quiero importar e imprime el inicio 
xl.sheet_names 
[u'hoja1'] 
dfini = xl.parse("hoja1") #variable que guarda las columnas del archivo df

#Filtrar datos y generar .csv con los 300 rios de mayor flujo
df = dfini.iloc[:,(0,1,2,3,4,5)]
df = df.sort(columns = 'm2s_ratio', ascending = False)
df300 = df.iloc[:300,:]
df300.to_csv('top_300_rios.csv', index=False)
