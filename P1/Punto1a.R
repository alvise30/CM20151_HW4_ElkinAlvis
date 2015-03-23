library(ggplot2)
library(reshape2)
library(plyr)
library(dplyr)
library(lubridate)
library(RColorBrewer)

bogota = read.table("bogota.txt", header = TRUE)
cali = read.table("cali.txt", header = TRUE)
bucaramanga = read.table("bucaramanga.txt", header = TRUE)
barranquilla = read.table("quilla.txt", header = TRUE)
ipiales = read.table("ipiales.txt", header = TRUE)

Ciudades <- c('bogota', 'quilla', 'bucaramanga', 'cali', 'ipiales')
a = c() #Serie vacia
tidy = data.frame(a,a,a) # DataFrame vacio. En este data frame se van a guardar los datos tidy
for(C in Ciudades) {
  datos <- c("año","mes", "temperatura")
  C <- gather(C, mes, temperatura, JAN:DEC, na.rm = TRUE)
  names(C)[1] <- "año"
  C <- C[,datos,drop=FALSE]
}
  #Cargar datos
  no_tidy <- read.table(
    file = paste(C,".txt",sep=""),
    header = TRUE)
  n <- names(no_tidy)[1:13] #Seleccionar los nombres de las columnas a usar
  no_tidy <- no_tidy[c(n)] #Guardar solo las 13 primeras columnas
  # Tidy data. Hacer melt para generar datos tidy
  tidy <- melt(
    data = no_tidy,
    id = "YEAR",
    variable.name = "MONTH",
    value.name = "TEMPERATURE"
  )
  #Agregar columnas de Ciudad y dia
  tidy$DAY = 1
  tidy$CITY = C
  tidy = rbind(no_tidy,tidy) #Agrupar todos los datos en un unico DataFrame
  

}

