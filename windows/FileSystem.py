"""
FileSystem.py
- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
"""
## FileSystem
## This file contains some default directories of your system

import os

## Special Directories
CurrentPath = os.getcwd()
User = os.environ['USERPROFILE']
ApplicationData = f'{User}/AppData/Roaming/'
Desktop = f'{User}/Desktop/'
Documents = f'{User}/Documents/'
Downloads = f'{User}/Downloads/'
LocalAppData = f'{User}/AppData/Local/'
Temp = f'{LocalAppData}Temp'
Pictures = f'{User}/Pictures/'
Favorites = f'{User}/Favorites/'