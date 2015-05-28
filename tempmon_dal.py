import sqlite3

import psycopg2

dbpath = '/srv/data/PiShared/data/bighomedata.db'
pgcon = "host=10.77.0.1 dbname=env_measures  user=user password=pass"


def insertMessWert(datum, sensorid, temp, hum, locid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO messwerte(timestamp,sensorid,temp ,hum,locationid)
                  VALUES(?,?,?,?,?)''', (datum, sensorid, temp, hum, locid))
        db.commit()
        res = cursor.lastrowid
        db.close()
    except Exception as e:
        res = -1
        raise e
    finally:
        return res


def InsertNewMesswertePg(datum, sensorid, temp, hum, locid):
    try:
        pconn = psycopg2.connect(pgcon)
        pcur = pconn.cursor()
        pcur.executemany('''INSERT INTO messwerte VALUES(%s,%s,%s,%s,%s)''', (datum, sensorid, temp, hum, locid))
        pconn.commit()
        pconn.close()
        res = 1
    except Exception as e:
        res = -1
        raise e
    finally:
        return res


def getSensorLocId(sensorid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        locid = (0,)
        cursor.execute('''SELECT locationid FROM sensors WHERE idsensor=?''', (sensorid,))
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
        pcur.execute('''SELECT locationid FROM sensors WHERE idsensor=?''', (sensorid,))
        pres = pcur.fetchone()
        pcur.close()
        pconn.close()
        res = pres[0]
    except Exception as e:
        res = -1
        raise e
    finally:
        return res
