import csv
from random import sample

# Way1
# samplefile = open('/Users/jlatha/data/code/routerlist.csv')
# samplereader= csv.reader(samplefile)
# sampledata=list(samplereader)
# print(sampledata)
# print(sampledata[0][1])

# Way2
with open("/Users/jlatha/data/code/routerlist.csv") as fh:
    csv_data=csv.reader(fh)
    # print(list(csv_data))
    for row in csv_data:
        # print(row)
        device_name = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device_name} is in {location} and has IP: {ip}")

