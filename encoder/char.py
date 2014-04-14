def stringtolist(string):
	list = []
	
	for x in range(0,len(string)):
		list.append(ord(string[x]))
	
	return list

def correctstring(str):
	name = str.replace(unichr(252),'ue')
	name = name.replace(unichr(228),'ae')
	name = name.replace(unichr(246),'oe')
	return name
		
def int_to_bytearray(groesse):
	eingabe = "111"
	Input = ""
	
	for x in range(0,groesse):
		Input = Input + "0"
	
	Input = Input + "111"
	
	for x in range(groesse,255):
		Input = Input + "0"	
	
	return Input

def name_to_list(string):	
	namliste = []
	ls = stringtolist(string)
	
	for element in ls: 
		array = int_to_bytearray(element)
		namliste.append(array)
		
	return namliste
