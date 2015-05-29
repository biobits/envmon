import datetime

import tempmon_dal as tmdal

klimalog = '/srv/data/PiShared/data/klimalogSerFile.log'


def schreibeMessWertToFile(timest, sensorid, temp, hum, logfile):
    locid = -1
    resid=-1
    s = str(unicode(timest))

    try:
        locId = tmdal.GetSensorLocIdPg(sensorid)
    except Exception:
        locId = -2

    try:
        logtext = s + '\t' + sensorid + '\t' + temp + '\t' + hum + '\n'
        f = open(logfile, 'a')
        f.write(logtext)
        f.close()
        resid=1

    except Exception:
        resid = -2

    return resid


def schreibeMessWert(sensorid, temp, hum):
    jetzt = datetime.datetime.now()

    LocId = tmdal.getSensorLocId(sensorid)

    resid = tmdal.insertMessWert(jetzt, sensorid, temp, hum, LocId)

    return resid


def SchreibeMessWertPg(timest, sensorid, temp, hum):
    locId = tmdal.GetSensorLocIdPg(sensorid)

    resid = tmdal.InsertNewMesswertePg(timest, sensorid, temp, hum, locId)

    return resid


def holeTemperatur(messwert, sensornum):
    sn = 2 + sensornum
    try:

        wert = messwert.split(";")
        temp = wert[sn]
        res = float(temp.replace(',', '.'))

    except Exception:
        res = None
    return res


def holeSaturierung(messwert, sensornum):
    hops = 10 + sensornum
    try:

        wert = messwert.split(";")
        temp = wert[hops]
        res = float(temp.replace(',', '.'))

    except Exception:
        res = None
    return res
