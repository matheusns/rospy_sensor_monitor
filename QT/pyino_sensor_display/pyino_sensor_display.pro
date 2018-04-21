#-------------------------------------------------
#
# Project created by QtCreator 2018-04-17T11:32:38
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = pyino_sensor_display
TEMPLATE = app


SOURCES += main.cpp\
        pysensor.cpp

HEADERS  += pysensor.h

FORMS    += \
    pysensormain.ui \
    aboutscreen.ui \
    matplot.ui \
    frame.ui \
    form.ui

RESOURCES += \
    pyino_sources.qrc

DISTFILES +=
