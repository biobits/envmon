import serial
import datetime
import tempmon_bol as tmb
s = serial.Serial('/dev/ttyUSB0',9600)

actsenslist=[1,2] # Liste der aktiven Sensoren, sollte aus DB kommen

while True:
    wert = s.readline()
    f=open('/srv/data/PiShared/data/klimalogSer.log','a')
    f.writelines(wert)
    f.close()
    for num in actsenslist:
        temp=tmb.holeTemperatur(wert,num)
        hum=tmb.holeSaturierung(wert,num)
        try:
            res=tmb.schreibeMessWert(num,temp,hum)
            print(res)
        except Exception as e:
            res=-1
            print(e.message)



    





