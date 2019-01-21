# Article to CSV
# - Takes link, content and score from article and writes it into a CSV file
#
# Input: Link (str), article (str), score (float)
# Output: New CSV file

import re
import csv
import datetime
import os
import shutil

now = datetime.datetime.now()
month = now.strftime("%b")
day = str(now.day)
hyp = '-'
date = month+hyp+day
source = ""
dest1 = "/Users/Master Soe/webscrap/Stock Articles"

def Article_to_CSV(link,article,score):
    e0 = link.split("/")
    e1 = e0[len(e0)-1]
    title = e1.split(".html")[0]
    csv_filename = title + ".csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({now})
        writer.writerow({link})
        writer.writerow({article.encode("utf-8")})
        writer.writerow({str(score)})
    try:
        shutil.move(csv_filename, dest1)
    except OSError as err:
        #print('Duplicate found')
        os.remove(csv_filename)
        pass
    return csv_filename
