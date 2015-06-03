library (sqldf)
library(RPostgreSQL) 

data <- read.table("c:/DATA/PiShared/KlimaLogBak/MissingDta/klimalog.log", sep="\t",header=TRUE,col.names=c("datum","temp","hum"))


options(sqldf.RPostgreSQL.user ="user", 
        sqldf.RPostgreSQL.password ="pwd",
        sqldf.RPostgreSQL.dbname ="env_measures",
        sqldf.RPostgreSQL.host ="10.77.0.1", 
        sqldf.RPostgreSQL.port =5432)

tstamps<-sqldf("select distinct timestamp from messwerte where sensorid=99")

sqldf("select strftime('%Y-%m-%d %H:%M:%S', datum),temp,hum from data",drv="SQLite")

missingdat<-sqldf("SELECT * from data where strftime('%Y-%m-%d %H:%M:%S', datum) not in (select distinct timestamp from tstamps)",drv="SQLite")

mindat<-sqldf("insert ")

migdata<-sqldf(paste("select datum,99 as sensorid,temp,hum,1 as locationid from data where datum < '",mindat,"'",sep=""))

# transfer<-sqldf("insert into messwerte select datum, sensorid,temp,hum,locationid from migdata",dbname=dbfile)

## Testscenerario
sqldf("create table messwerte_bak as select * from messwerte",dbname = dbfile)

sqldf("select * from messwerte_bak",dbname = dbfile)



transfer<-sqldf("insert into messwerte select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 99,temp,hum,1 from missingdat where temp is not null")
transfer
sqldf("select * from messwerte limit 100")

sqldf("select to_timestamp(datum, 'YYYY-MM-DD HH24:MI:SS'), 99,temp,hum,1 from missingdat where temp is not null")

sqldf("SELECT * from data where datum  in (select distinct timestamp from tstamps)",drv="SQLite")
