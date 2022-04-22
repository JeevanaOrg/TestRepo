import csv
from random import sample

from pyparsing import empty

# Way1
# samplefile = open('/Users/jlatha/data/code/routerlist.csv')
# samplereader= csv.reader(samplefile)
# sampledata=list(samplereader)
# print(sampledata)
# print(sampledata[0][1])

# Way2
def read_from_csv(csv_file_location):
    with open(csv_file_location) as fh:
        csv_data=csv.reader(fh)
        # print(list(csv_data))
        if csv_data is empty:
            return "no data"
        for row in csv_data:
            # print(row)
            device_name = row[0]
            location = row[2]
            ip = row[1]
            print(f"{device_name} is in {location} and has IP: {ip}")
        
def write_into_csv(csv_file_location):
    with open(csv_file_location,"a",newline='\n')as fh:
        user_data = user_input_list()
        # print(user_data)
        csv_writer = csv.writer(fh,csv.QUOTE_ALL)
        csv_writer.writerow(user_data)

def user_input_list():
    hostname = input("Enter host name: ")
    ip = input("What is the ip address: ")
    location=input("What is the location: ")

    router =[hostname,ip,location]
    return router


def main():
    csv_file_location = "code/routerlist.csv"
    read_from_csv(csv_file_location)
    write_into_csv(csv_file_location)
    read_from_csv(csv_file_location)

main()

