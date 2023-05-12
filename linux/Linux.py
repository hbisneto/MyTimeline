"""
Linux.py
- This file is used to implement code used to run scripts for Linux
- Codes implemented here, will run before the main script starts running
"""
## Linux File
## This file is used to implement code used to run scripts for Linux
## Codes implemented here, will run before the script starts running.

from linux import SplashScreen
from linux import LinuxApp
from system import Requirements

def Linux():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    SplashScreen.Show()

    ## Lets check system requirements
    Requirements.CheckVersion()

    ## Start App for Mac
    LinuxApp.Run()