#!/bin/sh
# temp_ser_launcher.sh
#

DIR=/srv/data/PiShared/Temp_Monitor
SCRIPT=$DIR/Temp_Ser.py

sudo python $SCRIPT

# to run as cronjob at boottime via crontab (contab -e)
# @reboot sh /srv/data/PiShared/Temp_Monitor/temp_launcher.sh >/srv/data/PiShared/logs/temp_cronlog 2>&1

