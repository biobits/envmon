import datetime

import tempmon_dal as tmdal


def schreibeMessWert(sensorid, temp, hum):
    jetzt = datetime.datetime.now()

    LocId = tmdal.getSensorLocId(sensorid)

    resid = tmdal.insertMessWert(jetzt, sensorid, temp, hum, LocId)

    return resid


def SchreibeMessWertPg(timest, sensorid, temp, hum):
    locId = tmdal.getSensorLocId(sensorid)

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
