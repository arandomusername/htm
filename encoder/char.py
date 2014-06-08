def string_to_list(string):
    string_list = []

    for x in range(0, len(string)):
        string_list.append(ord(string[x]))

    return string_list


def correct_string(string):
    name = string.replace(unichr(252), 'ue')
    name = name.replace(unichr(228), 'ae')
    name = name.replace(unichr(246), 'oe')
    return name

def int_to_binarray(groesse):
    return str(bin(groesse)[2:])

def int_to_bytearray(groesse):
    byte_array = ""

    for x in range(0, groesse):
        byte_array += "0"
    byte_array += "111"

    for x in range(groesse, 255):
        byte_array += "0"

    return byte_array


def name_to_list(string):
    name_list = []
    ls = string_to_list(string)

    for element in ls:
        array = int_to_bytearray(element)
        name_list.append(array)
    return name_list


def show_only_actives(string):
    pos_list = []
    for x in range(0, len(string)):
        if string[x] == "1":
            pos_list.append(x)
    return pos_list
		
