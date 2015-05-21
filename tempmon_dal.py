import sqlite3


dbpath = '/srv/data/PiShared/data/bighomedata.db'
#dbpath = 'C:/DATA/PiShared/data/bighomedata.db'
def insertMessWert(datum,sensorid,temp,hum,locid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO messwerte(timestamp,sensorid,temp ,hum,locationid)
                  VALUES(?,?,?,?,?)''', (datum,sensorid, temp,hum,locid))
        db.commit()
        res=cursor.lastrowid
        db.close()
    except Exception as e:
        res=-1
        raise e
    finally:
        return res

def getSensorLocId(sensorid):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        locid=(0,)
        cursor.execute('''SELECT locationid FROM sensors WHERE idsensor=?''', (sensorid,))
        locid = cursor.fetchone()
        res=locid[0]
        db.close()
    except Exception as e:
        res=-1
        raise e
    finally:
        return res
