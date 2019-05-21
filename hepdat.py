"""
hepdat.py - main file

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
import os, shutil
import csv
from string import Template

# command line arguments
if len(sys.argv) != 4:
    print("Fehler: hepdat.exe <hab_muster.dat> <pef_muster.dat> <daten.csv>")
    sys.exit(1)

# define fields from csv file
FIELDNAMES = ['forstamt', 'fu', 'betrieb', 'jahr', 'mb', 'dateiname']

# always delete old files
if os.path.isdir("habs_bearbeitet"):
    shutil.rmtree("habs_bearbeitet")

# create empty output directory
os.mkdir("habs_bearbeitet")

# read the csv source file
with open(sys.argv[3], newline='') as csvFile:
    csv.register_dialect('excel', delimiter=';')
    habDict = csv.DictReader(csvFile, fieldnames=FIELDNAMES)
    for row in habDict:
        # repalce placeholder in HAB file
        with open(sys.argv[1], "r") as sourceFile:
            tpl = Template(sourceFile.read())

        with open("habs_bearbeitet" + os.sep + "hab_" + row['dateiname'] + ".dat", "w") as destFile:
            destFile.write(tpl.safe_substitute(
                forstamt='{:>3}'.format(row['forstamt']),
                fu='{:>2}'.format(row['fu']),
                betrieb='{:>4}'.format(row['betrieb']),
                jahr='{:>4}'.format(row['jahr']),
                mb='{:>4}'.format(row['mb']),
            ))
        print("Datei: hab_" + row['dateiname'] + ".dat erzeugt")

        # repalce placeholder in PEF file
        with open(sys.argv[2], "r") as sourceFile:
            tpl = Template(sourceFile.read())

        with open("habs_bearbeitet" + os.sep + "pef_" + row['dateiname'] + ".dat", "w") as destFile:
            destFile.write(tpl.safe_substitute(
                forstamt='{:>3}'.format(row['forstamt']),
                fu='{:>2}'.format(row['fu']),
                betrieb='{:>4}'.format(row['betrieb']),
                jahr='{:>4}'.format(row['jahr']),
                mb='{:>4}'.format(row['mb']),
            ))
        print("Datei: pef_" + row['dateiname'] + ".dat erzeugt")
