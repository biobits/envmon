import sqlite3
import psycopg2
#import duckDBHelper as dbh
import pandas as pd


dbpath = 'KlimaPi.sqlite'
pgcon = "host=192.168.77.177 dbname=env_measures  user=stb password=9Hyperion&10"
#duckdbconn='KlimaPi.duckdb'

def insertMessWert(datum, sensorid, temp, hum, locid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO measurements(timestamp,sensor_id,temperature_celsius ,humidity,location_id)
                  VALUES(?,?,?,?,?)''', (datum, sensorid, temp, hum, locid))
        db.commit()
        res = cursor.lastrowid
        db.close()
    except Exception as e:
        res = -1
        raise e
    finally:
        return res

def CheckMessWertExists(datum, sensorid, temp, hum, locid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''select count (*) as anz from  measurements where 
                       timestamp=?
                       and sensor_id=?
                       and temperature_celsius=?
                       and humidity=?
                       and location_id=?''', (datum, sensorid, temp, hum, locid))
        res = cursor.fetchone()[0]
        db.close()
    except Exception as e:
        res = -1
        raise e
    finally:
        return res   


def InsertNewMesswertePg(datum, sensorid, temp, hum, locid):
    s = str(datum)
    try:
        pconn = psycopg2.connect(pgcon)
        pcur = pconn.cursor()
        pcur.execute("INSERT INTO messwerte VALUES(%s,%s,%s,%s,%s)", (datum, sensorid, temp, hum, locid))
        pconn.commit()
        pconn.close()
        res = 1
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res

""" def InsertNewMesswerteDuck(datum, sensorid, temp, hum, locid):
    
    try:
        res = dbh.InsertOrUpdateDuckDB("INSERT INTO measurements (\"timestamp\", sensor_id, temperature_celsius, humidity, location_id) VALUES(?,?,?,?,?)", [datum, sensorid, temp, hum, locid])
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
 """
def getSensorLocId(sensorid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        locid = (0,)
        cursor.execute('''SELECT location_id FROM sensors WHERE id=?''', (sensorid,))
        locid = cursor.fetchone()
        res = locid[0]
        db.close()
    except Exception as e:
        res = -1
        raise e
    finally:
        return res


def GetSensorLocIdPg(sensorid):
    try:
        pconn = psycopg2.connect(pgcon)
        pcur = pconn.cursor()
        pcur.execute("SELECT locationid FROM sensors WHERE idsensor=%s;", (sensorid,))
        pres = pcur.fetchone()
        pcur.close()
        pconn.close()
        res = pres[0]
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res

""" def GetSensorLocIdDuck(sensorid):
    try:
        resp = dbh.ExecuteDuckDBQuery("SELECT location_id FROM sensors WHERE id=?;",[sensorid])
        res=resp[0][0]
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res """
