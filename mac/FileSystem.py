﻿"""
FileSystem.py
- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
"""
## FileSystem
## This file contains some default directories of your system

import os

## Special Directories
CurrentPath = os.getcwd()
User = f'/Users/{os.environ["USER"]}/'
Applications = f'{User}Applications/'
Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Movies = f'{User}Movies/'
Music = f'{User}Music/'
Pictures = f'{User}Pictures/'
Public = f'{User}Public/'