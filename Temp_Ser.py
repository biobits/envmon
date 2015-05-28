import datetime

import serial
import tempmon_bol as tmb

s = serial.Serial('/dev/ttyUSB0',9600)

actsenslist=[1,2] # Liste der aktiven Sensoren, sollte aus DB kommen

while True:
    wert = s.readline()
    d = datetime.datetime.now()
    dw = str(unicode(d))
    f=open('/srv/data/PiShared/data/klimalogSer.log','a')
    logtext = dw + '\t' + wert
    f.writelines(logtext)
    f.close()
    for num in actsenslist:
        temp=tmb.holeTemperatur(wert,num)
        hum=tmb.holeSaturierung(wert,num)
        try:
            res=tmb.schreibeMessWert(num,temp,hum)
            res2 = tmb.SchreibeMessWertPg(d, num, temp, hum)

            print(res)
        except Exception as e:
            res=-1
            print(e.message)

