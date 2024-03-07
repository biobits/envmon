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


def median(numbers):
    return (sorted(numbers)[int(round((len(numbers) - 1) / 2.0))] + sorted(numbers)[
        int(round((len(numbers) - 1) // 2.0))]) / 2.0


while True:
    try:
        [temp, hum] = dht(dht_sensor_port, 2)  # Get the temperature and Humidity from the DHT sensor
        tmp_list.append(temp)
        hum_list.append(hum)
	#comment in prod
        print  "\ttemp =", temp, "C\thumadity =", hum,"%"
        if len(tmp_list) == 300 or len(hum_list) == 300:
            t = str(median(tmp_list))
            h = str(median(hum_list))
            d = datetime.datetime.now()
            s = str(unicode(d))

            logtext = s + '\t' + t + '\t' + h + '\n'
            #comment in prod
	    print logtext
            f = open('/srv/data/PiShared/data/klimalog.log', 'a')
            f.write(logtext)
            f.close()

            del tmp_list[:]
            del hum_list[:]
    except (IOError, TypeError) as e:
        print e  # "Error"



