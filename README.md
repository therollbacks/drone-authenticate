# drone-authenticate
Ardupilot Authentication
Autonomous Internet-of-Things (IoT) are comprised of moving objects such as drones and rovers that use self-control techniques to accomplish a mission while following a path. However, losing control in such systems usually by spoofing their sensors or hijacking with misleading commands can lead to catastrophic safety consequences. In this project, we close the gap by authenticating the behavior of autonomous IoT systems during operation. In particular, we check the behavior of a moving IoT object(drone) by evaluating its time-series telemetry traces during the flight. In this program we apply three machine learning techniques on the collected data, namely, K-Nearest Neighbour (KNN), Support Vector Machine (SVM), and Logistic Regression (LR). 


## Table of Contents
1. [Features](#Features)
2. [Known Application Bugs](#Known-Application-Bugs)
3. [Installation](#Installation)
4. [Run the Ardupilot environment](#Run-the-PyScan-virtual-environment)
5. [Converting from BIN to CSV](#converting)
6. [Performance Matrix](#matrix)
7. [Troubleshooting](#Troubleshooting)



## Features:
**Ardupilot simulator** - Maps the routes and settings of a simulated drone flight. ArduPilot (sometimes known as APM) is the leading open source autopilot system supporting multi-copters, fixed wing aircraft, rovers, submarines and antenna trackers. The code is open-source and written in CPP. <br>
**Pymavlink BIN to CSV converter** - Formats drone data into a usable format and gets rid of noise. <br>
**Data preprocessor** - Detailed preprocessor for formatting and cleaning data into a usable format. <br>
**One class SVM** - Machine learning model #1 that authenticates the true drone data. <br>
**KNN** - Performs K nearest neighbour to sort each data points into real or fake data classfication. <br>
**Logistic Regression** - Performs calculations to determine which group each data point belongs. <br>


## Known Application Bugs
- The labeling process may be too specific which can cause overfitting; other flight modes may not be compatible with our machine learning models. <br>
- KNN takes a significanlty longer time to run compared to One Class SVM and Logistic regression. <br>
- All of our data is stored locally and on github. It is not ideal and prone to security and processing issues. <br>

## Installation:

### Install Python
Refer to the [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) to properly configure and install Python. \
For our program, we used Python 3.6. 

### Install Git
Download Git from [here](https://git-scm.com/downloads). You will need this to clone the GitHub repository.

### Install Arudpilot
1.	You should clone the Ardupilot source code from the repository first
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule init
git submodule update
Tools/scripts/install-prereqs-ubuntu.sh -y
sudo apt-get install cmake
. ~/.profile

#LOG OUT AND LOG BACK IN

2. for target specific platform use --board
./waf configure --board px4-v2
./waf copter

3. for target specific platform use --board
./waf configure --board px4-v2
./waf copter


## Run the Ardupilot Environment:

4. Once installed, to run the drone simulation, follow the commands: 
Go to folder ArduCopter:
cd ~/../ardupilot/ArduCopter

Then run: <br> 
sim_vehicle.py -j4 --console --map <br> 
STABILIZE > wp load ../Tools/autotest/ArduPlane-Missions/CMAC-toff-loop.txt <br> 
STABILIZE > wp load ../Tools/autotest/ArduPlane-Missions/good_flight.txt <br> 
STABILIZE > wp load ../Tools/autotest/ArduPlane-Missions/bad_flight.txt <br> 
STABILIZE> mode guided <br> 
STABILIZE> GUIDED> arm throttle <br> 
GUIDED> takeoff 20 <br> 
GUIDED> mode auto <br> 
AUTO> mode rtl <br> 
AUTO> RTL> mode land <br> 

## Converting from BIN to CSV:
-----razqi ryon write here. As detailed as possible. and ryong add ur conversion scripts if they not on github already.
----- i dont remember the part here
Once all the BIN files are converted to csv, place the true and false paths into the unformatted_auto folder. Afterwards run the convert_csv.py file using:
sudo python convert_csv.py

## Comparing CSV files:
-----yeet if anyone remembers or if i forgot anything you know? :)

This section will use our comparison method created to detect the false path in the flight data.
After Converting all files from BIN to CSV, Rename the the true and false path CSVs. The true path is named dp_001 and the false path is named gp_001.
run:
sudo python compare_csv.py

All compared paths will appear in the compared folder and is ready to be used for testing.

## Performance Matrix: 
For each of our machine learning models, we use an in house performance matrix for the purpose of evaluation and tweaking. There are four variables, TP, FP, FN, TN.
1) TP(True Positives/ sensitivity): TP / (TP + FN) 
2) TN(True Negatives/ specificity): TN / (TN + FP)
3) Accuracy: (TP + TN) / (TP + FN + FP + TN)




