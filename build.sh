#!/bin/bash

clear 
cd ~/python_sensor/
# rm PyQT/pysensor.py PyQT/matplot.py PyQT/aboutscreen.py
rm PyQT/pysensor.py 
pyuic4 QT/pyino_sensor_display/pysensormain.ui -o PyQT/pysensor.py 
# pyuic4 QT/pyino_sensor_display/matplot.ui -o PyQT/matplot.py 
# pyuic4 QT/pyino_sensor_display/aboutscreen.ui -o PyQT/aboutscreen.py 
# pyuic4 QT/pyino_sensor_display/frame.ui -o PyQT/frame.py 
rm PyQT/pyino_sources_rc.py
pyrcc4 -o PyQT/pyino_sources_rc.py QT/pyino_sensor_display/pyino_sources.qrc
cd PyQT/ && python main.py