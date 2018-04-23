 #-*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
from pysensor import Ui_MainWindow as Py_Sensor_Ui # Importa todos os recursos graficos do QT
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
import datetime
import numpy as np
import matplotlib.pyplot as plt

current_temperature = 0
time_sec = 0
x = []
y = []

def callback(sensor_temperature):
    global current_temperature
    current_temperature = sensor_temperature

class Application(QtGui.QMainWindow):

    def __init__(self):
        self.data = "aldkal"
        QtGui.QMainWindow.__init__(self)
        self.ui = Py_Sensor_Ui()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        num = self.ui.stackedWidget.count()
        self.plot_setup()
        print num

    def plot_setup(self, toolbar = True):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        if toolbar:
            self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtGui.QVBoxLayout(self.ui.matplot_frame)
        if toolbar:
            layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot_graph = False

    def change_stack_button(self):
        if int( self.ui.stackedWidget.currentIndex() ) == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def pause_button_state(self):
        self.plot_graph = False
        self.ui.pause_button.setEnabled(False)
        self.ui.play_button.setEnabled(True)

    def play_button_state(self):
        self.plot_graph = True
        self.ui.play_button.setEnabled(False)
        self.ui.pause_button.setEnabled(True)

    def plot(self):
        global current_temperature 
        global time_sec 
        global x
        global y

        current_temperature_str = str(round(current_temperature.data,2))+u"°"
        self.ui.temp_display.setText(current_temperature_str)
        
        time_sec = time_sec+1 
        x.append(time_sec)
        y.append(round(current_temperature.data,2)) 
        
        if (self.plot_graph):
            ax = self.figure.add_subplot(111)
            ax.clear()
            ax.plot(x, y, color='green', alpha=0.5, linestyle='--', linewidth = 2.0)
            ax.plot(x, y, 'go')
            ax.grid(True)
            self.canvas.draw()