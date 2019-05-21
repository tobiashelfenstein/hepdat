"""
setup_cxfreeze_x64.py - setup file for cx_Freeze

Copyright (C) 2019 Tobias Helfenstein <tobias.helfenstein@wald-rlp.de>

This file is part of hepdat.

hepdat is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

hepdat is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""


import sys
import os
from cx_Freeze import setup, Executable

# delete old build folder
os.system("rd /s /q build")


executables = [
    Executable('hepdat.py',
               targetName = 'hepdat.exe')
]

setup(name='hepdat',
      version = '0.1',
      description = 'hepdat für Landesforsten Rheinland-Pfalz',
      executables = executables)
