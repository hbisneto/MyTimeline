"""
SplashScreen.py

- This file contains information about your project
"""
## SplashScreen File
## This file contains information about your project

from datetime import date

CurrentYear = date.today().year
SoftwareName = "MyTimeline"
Version = "1.0"
CopyrightName = "Heitor"

def Show():
   print("="*80)
   print(f'[{SoftwareName} for Mac] - Running...')
   print("="*80)

   print(f'Name: {SoftwareName}')
   print(f'Version: {Version}')
   print(f'Created By: {CopyrightName}')

   if CurrentYear == 2021:
      print(f'Copyright © {CurrentYear} | {CopyrightName}. All rights reserved.')
      print("="*80)
   else:
      print(f'Copyright © 2021 - {CurrentYear} | {CopyrightName}. All rights reserved.')
      print("="*80)
   print()