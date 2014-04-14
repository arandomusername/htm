import csv
import char

def open_file(pfad):
	List = []
	
	with open(pfad,"rb") as csvfile:
		reader	= csv.reader(csvfile)
		for row in reader:
			List.append(row)
	return List

def convert_row(row):
	List = []
	
	for element in row:
		List.append(char.name_to_list(element))
	
	return List
		
