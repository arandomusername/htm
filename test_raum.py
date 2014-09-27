import encoder
import htm

region_groesse = 8
datei_pfad = "daten/test.csv"

if __name__ == "__main__":

    htm = htm.HTM(1, 8, 258)
    opened_file = encoder.csv_reader.open_file(datei_pfad)

    for row in opened_file:
        for name in row:
            print(name)
            converted_name = encoder.char.name_to_list(name)
            for value in converted_name:
                new_input = encoder.char.show_only_actives(value)
                htm.process(new_input)