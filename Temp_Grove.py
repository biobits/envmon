# Temp_Mon.py
#
#
# In this project, the Temperature and humidity from the DHT sensor is printed on the DHT sensor

from grovepi import *
import datetime
import tempmon_bol as tpm

dht_sensor_port = 7  # Connect the DHt sensor to port 7
tmp_list = list()
hum_list = list()

errorlog = '/srv/data/PiShared/data/klimaerror.log'
klimalog = '/srv/data/PiShared/data/klimalog.log'


def median(numbers):
    return (sorted(numbers)[int(round((len(numbers) - 1) / 2.0))] + sorted(numbers)[
        int(round((len(numbers) - 1) // 2.0))]) / 2.0


while True:
    try:
        [temp, hum] = dht(dht_sensor_port, 2)  # Get the temperature and Humidity from the DHT sensor
        tmp_list.append(temp)
        hum_list.append(hum)
        # print  "\ttemp =", temp, "C\thumadity =", hum,"%"
        if len(tmp_list) == 300 or len(hum_list) == 300:
            temp = median(tmp_list)
            hum = median(hum_list)
            t = str(temp)
            h = str(hum)
            d = datetime.datetime.now()
            s = str(unicode(d))

            logtext = s + '\t' + t + '\t' + h + '\n'
            # print logtext
            f = open(klimalog, 'a')
            f.write(logtext)
            f.close()
            try:
                res = tpm.schreibeMessWert(99, temp, hum)
            except Exception as e:
                errortext = s + '\t' + 'Temp_Grove - DB' + '\t' + e.message
                k = open(errorlog, 'a')
                k.write(errortext)
                k.close()

            del tmp_list[:]
            del hum_list[:]
    except (IOError, TypeError) as e:
        fehlerlog = s + '\t' + 'Temp_Grove - Main' + '\t' + e.message
        er = open(errorlog, 'a')
        er.write(fehlerlog)
        er.close()



