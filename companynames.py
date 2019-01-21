import re
import csv
import os
import shutil

path = "/Users/Master Soe/webscrap/Stock Companies/A-Z_companies.csv"
file = open(path, newline='')
reader = csv.reader(file)
data = [row for row in reader]


with open("/Users/Master Soe/webscrap/Stock Companies/companynames.txt", mode='w', newline='') as f:
    for companydetails in data:
        companyname = companydetails[1]
        f.write(companyname)
        f.write("\n")
       

