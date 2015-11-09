library (sqldf)
library(RPostgreSQL) 

data <- read.table("F:/PiShared/PiShared/KlimaLogBak/20151009/klimadatalogSer.log", sep="\t",header=FALSE,col.names=c("datum","ID","temp","hum"))


options(sqldf.RPostgreSQL.user ="usr", 
        sqldf.RPostgreSQL.password ="pass",
        sqldf.RPostgreSQL.dbname ="env_measures",
        sqldf.RPostgreSQL.host ="192.168.2.211", 
        sqldf.RPostgreSQL.port =5432)

tstamps<-sqldf("select distinct date(timestamp) as tag from messwerte where sensorid !=99")
data<-cbind(data,tag=as.Date(data$datum,"%Y-%m-%d"))
# nur tage
# sqldf("select strftime('%Y-%m-%d', datum) as dat,datum from data",drv="SQLite")

missingdays<-sqldf("SELECT distinct tag from data where tag not in (select distinct tag from tstamps)",drv="SQLite")


missingdat<-sqldf("SELECT * from data where tag in (select distinct tag from missingdays)",drv="SQLite")

mindat<-sqldf("insert ")

migdata<-sqldf(paste("select datum,99 as sensorid,temp,hum,1 as locationid from data where datum < '",mindat,"'",sep=""))

# transfer<-sqldf("insert into messwerte select datum, sensorid,temp,hum,locationid from migdata",dbname=dbfile)

## Testscenerario
sqldf("create table messwerte_bak as select * from messwerte",dbname = dbfile)

sqldf("select * from messwerte_bak",dbname = dbfile)

mda<-missingdat%>%filter(ID==2)%>%select(datum,ID,temp=as.numeric(temp),hum=as.numeric(hum),tag)
head(mda)
transfer<-sqldf("insert into messwerte select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 2,
                cast(temp as real),cast(hum as real), 3 from mda where temp is not null ")
transfer
sqldf("select * from messwerte limit 100")

sqldf("select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 99,temp,hum,1 from missingdat where temp is not null")

sqldf("SELECT * from data where datum  in (select distinct timestamp from tstamps)",drv="SQLite")
