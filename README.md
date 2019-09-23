# drone-authenticate
Ardupilot Authentication
Uses the data collected from running a predefined drone path to authenticate real drone data from fake ones.


## Table of Contents
1. [Features](#Features)
2. [Known Application Bugs](#Known-Application-Bugs)
3. [Installation](#Installation)
4. [Run the Ardupilot environment](#Run-the-PyScan-virtual-environment)
6. [Troubleshooting](#Troubleshooting)



## Features:
**Data preprocessor** - Run data preprocessor.py to format drone data into a usable format and gets rid of noise. <br>
**One class SVM** - Load a .obj or .ply file to classify its shape
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
