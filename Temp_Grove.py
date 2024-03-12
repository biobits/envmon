# Temp_Mon.py
#
#
# In this project, the Temperature and humidity from the DHT sensor is printed on the DHT sensor
 
import datetime

from grovepi import *
import tempmon_bol as tpm

dht_sensor_port = 7  # Connect the DHt sensor to port 7
tmp_list = list()
hum_list = list()

errorlog = '/srv/data/DataLogs/error.log'
klimalog = '/srv/data/PiShared/data/klimalog.log'
klimadatalog = '/srv/data/DataLogs/klimadatalog.log'


def median(x):
    x = [value for value in x if not math.isnan(value)]
    m, r = divmod(len(x), 2)
    if r:
        return sorted(x)[m]
    return sum(sorted(x)[m - 1:m + 1]) / 2.0


while True:
    try:
        [temp, hum] = dht(dht_sensor_port, 2)  # Get the temperature and Humidity from the DHT sensor
        tmp_list.append(temp)
        hum_list.append(hum)
        # print  "\ttemp =", temp, "C\thumadity =", hum,"%"
        if len(tmp_list) == 301 or len(hum_list) == 301:
            temp = median(tmp_list)
            hum = median(hum_list)
            t = str(temp)
            h = str(hum)
            d = datetime.datetime.now()
            s = str(d)

            try:
                foneres = tpm.SchreibeMessWertToFile(d, 99, temp, hum, klimalog)

            except Exception as e:

                tpm.SchreibeErrorLog(d, 'Temp_Grove - Logging to shared file', e.message, errorlog)

            try:

                ftwores = tpm.SchreibeMessWertToFile(d, 99, temp, hum, klimadatalog)
            except Exception as e:

                tpm.SchreibeErrorLog(d, 'Temp_Grove - Logging to local file', e.message, errorlog)

            # try:
            #     res = tpm.schreibeMessWert(99, temp, hum)
            # except Exception as e:
            #     errortext = s + '\t' + 'Temp_Grove - DB' + '\t' + e.message
            #     k = open(errorlog, 'a')
            #     k.write(errortext)
            #     k.close()
                
            try:
                res = tpm.SchreibeMessWertDuck(d, 99, temp, hum)
            except Exception as e:
                tpm.SchreibeErrorLog(d, 'Temp_Grove - DuckDB', e.message, errorlog)

            try:
                res = tpm.SchreibeMessWertPg(d, 99, temp, hum)
            except Exception as e:
                tpm.SchreibeErrorLog(d, 'Temp_Grove - PG-DB', e.message, errorlog)

            del tmp_list[:]
            del hum_list[:]
    except (IOError, TypeError) as e:

        tpm.SchreibeErrorLog(d, 'Temp_Grove - Main', e.message, errorlog)
