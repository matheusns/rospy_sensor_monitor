#!/bin/bash

clear 
cd ~/rospy_sensor_monitor/
rm PyQT/pysensor.py 
pyuic4 QT/pyino_sensor_display/pysensormain.ui -o PyQT/pysensor.py 
rm PyQT/pyino_sources_rc.py
pyrcc4 -o PyQT/pyino_sources_rc.py QT/pyino_sensor_display/pyino_sources.qrc
cd PyQT/ && python main.py
