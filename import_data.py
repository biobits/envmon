import sqlite3
import pandas as pd
import datetime as  dt
import tempmon_dal as tmd
#########
#
# Script to import data from textfiles into sqlite 
#
#########

dbpath = 'KlimaPi.sqlite'

file_to_import='klimadatalogTest.log'
#DB Connection
con = sqlite3.connect(dbpath)

# Read CSV CLimatedata
headers=['timestamp','sensorid','temp','hum']

kdat=pd.read_csv(file_to_import,sep='\t',header=None,  names=headers)#,parse_dates=[0])

# Read existing data in DB
dbdat=pd.read_sql_query("SELECT * FROM measurements",con)


# Iterate over CSV Climatedata
for index, row in kdat.iterrows():
    # get locationid
    locid=tmd.getSensorLocId(row['sensorid'])
    res=tmd.insertMessWert(row['timestamp'],row['sensorid'],row['temp'],row['hum'],locid)
    #print(res)

con.close()



def GetNewMesswerte(datum):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''Select distinct timestamp,sensorid,temp ,hum,locationid from measurements
                  where timestamp >? order by timestamp limit 1000''', (datum,))
        db.commit()
        res=cursor.fetchall()
        db.close()
    except Exception as e:
        res=-1
        raise e
    finally:
        return res

def CountNewMesswerte(datum):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''Select count(distinct timestamp) from measurements
                  where timestamp >? ''', (datum,))
        db.commit()
        res=cursor.fetchone()
        db.close()
    except Exception as e:
        res=-1
        raise e
    finally:
        return res[0]
#
# Task

