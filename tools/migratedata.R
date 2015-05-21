library (sqldf)

dbfile<-"C:/data/PiShared/data/bighomedata.db"
data <- read.table("c:/data/PiShared/data/klimalog.log", sep="\t",header=TRUE,col.names=c("datum","temp","hum"))


dbdata<-sqldf("select * from messwerte",dbname = dbfile)
locdata<-sqldf("select * from location",dbname = dbfile)

mindat<-sqldf("select min(timestamp) as t from messwerte where sensorid=99",dbname = dbfile)$t

migdata<-sqldf(paste("select datum,99 as sensorid,temp,hum,1 as locationid from data where datum < '",mindat,"'",sep=""))

# transfer<-sqldf("insert into messwerte select datum, sensorid,temp,hum,locationid from migdata",dbname=dbfile)

## Testscenerario
sqldf("create table messwerte_bak as select * from messwerte",dbname = dbfile)

sqldf("select * from messwerte_bak",dbname = dbfile)



transfer<-sqldf("insert into messwerte_bak select datum, sensorid,temp,hum,locationid from migdata",dbname=dbfile)
transfer
sqldf("select * from messwerte_bak",dbname = dbfile)

sqldf("drop table  messwerte_bak",dbname = dbfile)
