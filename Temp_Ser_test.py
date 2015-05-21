import tempmon_bol as tmb


# /home/stb/klimalogSer.log
# $1;1;;23,0;25,0;;;;;;;30;27;;;;;;;;;;;;0
# $1;1;;23,0;25,0;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,0;25,0;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,0;25,1;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,1;25,1;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,1;25,1;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,1;25,1;;;;;;;30;25;;;;;;;;;;;;0
# $1;1;;23,1;25,1;;;;;;;30;25;;;;;;;;;;;;0

measure="$1;1;;23,1;25,1;;;;;;;30;25;;;;;;;;;;;;0"


print("Temp Sensor 1: ",tmb.holeTemperatur(measure,1))
print("Hum Sensor 1: ",tmb.holeSaturierung(measure,1))

print("Temp Sensor 2: ",tmb.holeTemperatur(measure,2))
print("Hum Sensor 2: ",tmb.holeSaturierung(measure,2))

res=tmb.schreibeMessWert(1,tmb.holeTemperatur(measure,1),tmb.holeSaturierung(measure,1))

print(res)

