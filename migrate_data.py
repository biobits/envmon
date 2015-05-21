import sqlite3
import psycopg2

#########
#
# Script to import data from sqlite into postgresql db
#
#########

dbpath = '/srv/data/PiShared/data/bighomedata.db'
#dbpath = 'C:/DATA/PiShared/data/bighomedata.db'
pgcon="host=10.77.0.1 dbname=env_measures  user=user password=pass"

#Postgresql
def GetRecentTimestamp():
    pconn = psycopg2.connect(pgcon)
    pcur = pconn.cursor()
    pcur.execute("SELECT timestamp FROM messwerte order by timestamp desc limit 1;")
    pres=pcur.fetchone()
    pcur.close()
    pconn.close()
    return(pres[0])

def InsertNewMesswerte(messwerte):
    try:
        pconn = psycopg2.connect(pgcon)
        pcur = pconn.cursor()
        pcur.executemany('''INSERT INTO messwerte VALUES(%s,%s,%s,%s,%s)''', messwerte)
        pconn.commit()
        #pcur.close()
        pconn.close()
        res=1
    except Exception as e:
        res=-1
        raise e
    finally:
        return res


def GetNewMesswerte(datum):
    try:
        db = sqlite3.connect(dbpath)
        cursor = db.cursor()
        cursor.execute('''Select distinct timestamp,sensorid,temp ,hum,locationid from messwerte
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
        cursor.execute('''Select count(distinct timestamp) from messwerte
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
tst=GetRecentTimestamp()
#tst='2015-01-10 00:00:00'
#newmes=CountNewMesswerte(tst)
ndat=0
#result=GetNewMesswerte('2015-01-01 00:00:00')
while (CountNewMesswerte(tst)>1):
    result=GetNewMesswerte(tst)
    print(result.__len__())
    insres=InsertNewMesswerte(result)
    ndat=ndat+result.__len__()
    print 'Bis jetzt %d Measures inserted\n' %(ndat)
    tst=GetRecentTimestamp()
    print 'Neuer Zeitpunkt:'+str(tst)
    newmes=CountNewMesswerte(tst)
    print 'Noch %d Messwerte zu verarbeiten' %(newmes)

print(insres)
