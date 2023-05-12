"""
Windows.py
- This file is used to implement code used to run scripts for Windows
- Codes implemented here, will run before the main script starts running
"""
## Windows File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the script starts running.

from windows import SplashScreen
from windows import WindowsApp
from system import Requirements

def Windows():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    SplashScreen.Show()

    ## Lets check system requirements
    Requirements.CheckVersion()

    ## Start App for Mac
    WindowsApp.Run()