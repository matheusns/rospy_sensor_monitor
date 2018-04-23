
# Rospy Sensor Monitor

<p align="justify">
The Rospy Sensor Monitor is an undergraduate project that aims to develop an interface to monitors the values retrieved from a temperature sensor. The Arduino board is used to acquire the raw data and through the <a href="http://wiki.ros.org/rosserial">rosserial package</a>  make the values available on ROS topics. The interface was build using PyQt, which has a ros node that listens to the values published from the rosserial node and plot them into a matplot graph. 

# Contents

  * [Requirements](#requirements)
  * [Installation](#instala%C3%A7%C3%A3o)
  * [Usage ](#uso)
  * [Documentation](#documentação)
  * [Contributiton](#contribuicoes)
  * [Credits](#creditos)
  * [License](#licenciamento)
  * [Background IP](#background-ip)
  * [Acknowledgments](#acknowledgments)

# Requirements 

  * [Ubuntu 16.04.5 LTS (Xenial Xerus)](http://releases.ubuntu.com/14.04/) 
  * [Python 2.7](https://www.python.org/download/releases/2.7/) 
  * [QT4](https://www1.qt.io/download-open-source/)
  * [PyQT4](https://pypi.python.org/pypi/PyQt4)

## Credits

* **Matheus Nascimento**  - [matheusns](https://github.com/matheusns)