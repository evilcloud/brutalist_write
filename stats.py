import csv

def count_sessions():
    with open("2019-11-20.bru") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for row in csv_reader:
            if row