"""
Mac.py
- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
"""
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

from mac import SplashScreen
from mac import MacApp
from system import Requirements

def Mac():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    SplashScreen.Show()

    ## Lets check system requirements
    Requirements.CheckVersion()

    ## Start App for Mac
    MacApp.Run()