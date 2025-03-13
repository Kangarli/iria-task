import csv

def read_csv_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]