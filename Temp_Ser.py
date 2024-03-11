import datetime

import serial
import tempmon_bol as tmb

s = serial.Serial('/dev/ttyUSB0', 9600)

actsenslist = [1, 2]  # Liste der aktiven Sensoren, sollte aus DB kommen

errorlog = '/srv/data/DataLogs/error.log'
klimalog = '/srv/data/PiShared/data/klimadatalogSer.log'
klimadatalog = '/srv/data/DataLogs/klimadatalogSer.log'

while True:
    wert = s.readline().decode()
    d = datetime.datetime.now()

    for num in actsenslist:
        temp = tmb.holeTemperatur(wert, num)
        hum = tmb.holeSaturierung(wert, num)

        try:
            # res=tmb.schreibeMessWert(num,temp,hum)
            res = tmb.SchreibeMessWertPg(d, num, temp, hum)

        except Exception as e:
            res = -1
            print(e.message)
            tmb.SchreibeErrorLog(d, 'Serielle Klimadaten - PG-DB', e.message, errorlog)

        try: 
            res=tmb.SchreibeMessWertDuck(d,num,temp,hum)
        except Exception as e:
            res = -1
            print(e.message)
            tmb.SchreibeErrorLog(d, 'Serielle Klimadaten - DuckDB', e.message, errorlog)
            

        try:

            tmb.SchreibeMessWertToFile(d, num, temp, hum, klimalog)

        except Exception as e:
            print(e.message)
            tmb.SchreibeErrorLog(d, 'Serielle Klimadaten - Shared File', e.message, errorlog)

        try:

            tmb.SchreibeMessWertToFile(d, num, temp, hum, klimadatalog)

        except Exception as e:
            print(e.message)
            tmb.SchreibeErrorLog(d, 'Serielle Klimadaten - Local File', e.message, errorlog)
