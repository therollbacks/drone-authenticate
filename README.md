# drone-authenticate
Ardupilot Authentication
Autonomous Internet-of-Things (IoT) are comprised of moving objects such as drones and rovers that use self-control techniques to accomplish a mission while following a path. However, losing control in such systems usually by spoofing their sensors or hijacking with misleading commands can lead to catastrophic safety consequences. In this project, we close the gap by authenticating the behavior of autonomous IoT systems during operation. In particular, we check the behavior of a moving IoT object(drone) by evaluating its time-series telemetry traces during the flight. In this program we apply three machine learning techniques on the collected data, namely, K-Nearest Neighbour (KNN), Support Vector Machine (SVM), and Logistic Regression (LR). 


## Table of Contents
1. [Features](#Features)
2. [Known Application Bugs](#Known-Application-Bugs)
3. [Installation](#Installation)
4. [Run the Ardupilot environment](#Run-the-PyScan-virtual-environment)
6. [Troubleshooting](#Troubleshooting)



## Features:
**Ardupilot simulator** - Maps the routes and settings of a simulated drone flight. ArduPilot (sometimes known as APM) is the leading open source autopilot system supporting multi-copters, fixed wing aircraft, rovers, submarines and antenna trackers. The code is open-source and written in CPP. <br>
**Pymavlink BIN to CSV converter** - Formats drone data into a usable format and gets rid of noise. <br>
**Data preprocessor** - Detailed preprocessor for formatting and cleaning data into a usable format. <br>
**One class SVM** - Machine learning model #1 that authenticates the true drone data.
**KNN** - Performs K nearest neighbour to sort each data points into real or fake data classfication.
**Logistic Regression** - Performs calculations to determine which group each data point belongs.



## Known Application Bugs
- The labeling process for one class svm can be vague.

## Installation:

### Install Python
Refer to the [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) to properly configure and install Python. \
For our program, we used Python 3.6. 

### Install Git
Download Git from [here](https://git-scm.com/downloads). You will need this to clone the GitHub repository.

### Install Arudpilot
