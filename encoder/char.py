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
	name_list = []
	ls = stringtolist(string)
	
	for element in ls: 
		array = int_to_bytearray(element)
		name_list.append(array)		
	return name_list

def show_only_actives(string):
	pos_list = []
	for x in range(0,len(string)):
		if string[x] == "1":
			pos_list.append(x)
	return pos_list
		
