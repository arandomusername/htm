import encoder
import htm
import Cognition


region_groesse = 10
datei_pfad = "daten/test.csv"

if __name__ == "__main__":
    input_region = encoder.InputRegion(258)
    region = htm.Region(region_groesse)
    region.initialize_dendrites(input_region)

    opened_file = encoder.open_file(datei_pfad)
    for row in opened_file:
        for name in row:
            print(name)
            converted_name = encoder.name_to_list(name)
            for value in converted_name:
                b = encoder.show_only_actives(value)
                input_region.new_input(b)
                Cognition.do()