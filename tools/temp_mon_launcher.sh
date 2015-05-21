#!/bin/sh
# temp_mon_launcher.sh
#

DIR=/srv/data/PiShared/Temp_Monitor
SCRIPT=$DIR/Temp_Mon.py

sudo python $SCRIPT

# now entry in crontan (contab -e)
# @reboot sh /srv/data/PiShared/Temp_Monitor/temp_mon_launcher.sh >/srv/data/PiShared/logs/temp_mon_cronlog 2>&1
