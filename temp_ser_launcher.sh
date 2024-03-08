#!/bin/sh
# temp_mon_launcher.sh
#
 
DIR=/srv/scripts/Temp_Monitor
SCRIPT=$DIR/Temp_Ser.py

sudo python $SCRIPT

# now entry in crontan (contab -e)
# @reboot sh /srv/scripts/Temp_Monitor/temp_ser_launcher.sh >/srv/data/PiShared/logs/temp_cronlog 2>&1

