from PyQt4 import QtCore, QtGui
from threading import Thread
import rospy
from std_msgs.msg import Float32
import sys
from subprocess import call
import application as pyqt_application


class GuiThread(Thread):
    def __init__(self):
        Thread.__init__(self)
 
    def run(self):
        app = QtGui.QApplication(sys.argv)
        av = pyqt_application.Application()
        timer = QtCore.QTimer()  # set up your QTimer
        timer.timeout.connect(av.plot)  # connect it to your update function
        timer.start(1)
        av.show()
        sys.exit(app.exec_())

def callback(data):
    rospy.loginfo("I heard %s",data.data)
                             
if __name__ == '__main__':
   pyqt_thread = GuiThread()
   pyqt_thread.setName('QT_Thread')
   rospy.init_node('node_name')
   rospy.Subscriber("sensor_temperature", Float32, pyqt_application.callback)
   pyqt_thread.start()
   rospy.spin()
   