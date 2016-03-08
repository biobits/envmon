library (sqldf)
library(RPostgreSQL) 
library(dplyr)


data <- read.table("c:/DATA/PiShared/KlimaLogBak/20151220/klimadatalogSer.log", sep="\t",header=FALSE,col.names=c("datum","ID","temp","hum"))
#data <- read.table("c:/DATA/PiShared/KlimaLogBak/20151220/klimalog.log", sep="\t",header=TRUE,col.names=c("datum","temp","hum"))


options(sqldf.RPostgreSQL.user ="stb", 
        sqldf.RPostgreSQL.password ="jz43ed97",

        sqldf.RPostgreSQL.dbname ="env_measures",
        sqldf.RPostgreSQL.host ="10.77.0.1", 
        sqldf.RPostgreSQL.port =5432)


tstamps<-sqldf("select distinct date(timestamp) as tag from messwerte where sensorid =99")
data<-cbind(data,tag=as.Date(data$datum,"%Y-%m-%d"))
# nur tage
# sqldf("select strftime('%Y-%m-%d', datum) as dat,datum from data",drv="SQLite")

missingdays<-sqldf("SELECT distinct tag from data where tag not in (select distinct tag from tstamps)",drv="SQLite")


missingdat<-sqldf("SELECT * from data where tag in (select distinct tag from missingdays)",drv="SQLite")

# 
#tstamps<-sqldf("select distinct timestamp from messwerte where sensorid=99")

#sqldf("select strftime('%Y-%m-%d %H:%M:%S', datum),temp,hum from data",drv="SQLite")

#missingdat<-sqldf("SELECT * from data where strftime('%Y-%m-%d %H:%M:%S', datum) not in (select distinct timestamp from tstamps)",drv="SQLite")


mindat<-sqldf("insert ")

migdata<-sqldf(paste("select datum,99 as sensorid,temp,hum,1 as locationid from data where datum < '",mindat,"'",sep=""))

# transfer<-sqldf("insert into messwerte select datum, sensorid,temp,hum,locationid from migdata",dbname=dbfile)

## Testscenerario
sqldf("create table messwerte_bak as select * from messwerte",dbname = dbfile)

sqldf("select * from messwerte_bak",dbname = dbfile)

mda<-missingdat%>%filter(ID==99)%>%select(datum,ID,temp=as.numeric(temp),hum=as.numeric(hum),tag)
head(mda)
transfer<-sqldf("insert into messwerte select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 99,
                cast(temp as real),cast(hum as real), 1 from mda where temp is not null 
                --and temp !='None'
                and hum is not null")
transfer
sqldf("select * from messwerte limit 100")

sqldf("select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 99,temp,hum,1 from missingdat where temp is not null")

sqldf("SELECT * from data where datum  in (select distinct timestamp from tstamps)",drv="SQLite")
