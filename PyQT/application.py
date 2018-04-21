from PyQt4 import QtCore, QtGui
import sys
from pysensor import Ui_MainWindow as Py_Sensor_Ui # Importa todos os recursos graficos do QT
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random

current_temperature = 0

def callback(sensor_temperature):
    print "Here"
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

    def plot_setup(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtGui.QVBoxLayout(self.ui.matplot_frame)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def change_stack_button(self):
        if int( self.ui.stackedWidget.currentIndex() ) == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def plot(self):
        global current_temperature 
        print "Current_temperature = " + str(current_temperature)
        # random data
        current_temperature = int(current_temperature)
        self.ui.lcdNumber.display(current_temperature)
        data = [random.random() for i in range(10)]
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.clear()
        # plot data
        ax.plot(data, '*-')
        # refresh canvas
        self.canvas.draw()