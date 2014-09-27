import csv
from encoder import char

def open_file(pfad):
    row_list = []
    with open(pfad, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_list.append(row)
    return row_list


def convert_row(row):
    byte_list = []

    for element in row:
        byte_list.append(char.name_to_list(element))

    return byte_list
