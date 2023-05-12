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
User = f'/home/{os.environ["USER"]}/'

Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Music = f'{User}Music/'