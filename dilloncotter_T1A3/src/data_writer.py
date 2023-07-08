import csv

class DataWriter:
    @staticmethod
    def write_csv(filename, data):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)