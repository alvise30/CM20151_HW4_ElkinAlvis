library(ggplot2)
library(tidyr)
library(plyr)
library(dplyr)
library(lubridate)

llenar <- function(x) match(tolower(x), tolower(month.abb))
Ciudades <- c('bogota', 'quilla', 'bucaramanga', 'cali', 'ipiales')
a = c() #Serie vacia
tidy = data.frame(a,a,a) # DataFrame vacio. En este data frame se van a guardar los datos tidy
for(C in Ciudades) {
  tmp <- read.table(
    file = paste(C,".txt",sep=""),
    header = TRUE)  
  datos <- c("año","mes", "temperatura")
  tmp <- gather(tmp, mes, temperatura, JAN:DEC, na.rm = TRUE)
  names(tmp)[1] <- "año"
  tmp <- tmp[,datos,drop=FALSE] 
  tmp <- mutate(tmp, fecha = paste(año, llenar(mes), "1", sep="/"))
  tmp$ciudad = C
  tmp <- tmp[c("año", "mes", "fecha", "ciudad", "temperatura")]
  tmp[tmp == 999.9] <- NA
  tidy = rbind(tmp,tidy) #Agrupar todos los datos en un unico DataFrame  
}

write.csv(tidy, file = "temperaturas.csv")


a <- ggplot(tidy, aes(x=fecha,y = temperatura, , color=ciudad)) + geom_point()
a <- a + labs(title="Temperatura en algunas Capitales de Colombia 1967-2015") + facet_grid(~ ciudad, scales = "free")
ggsave(filename='temperaturas.png', plot = a)
print(a)