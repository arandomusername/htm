import encoder
import htm
import Cognition


region_groesse = 10
datei_pfad = "daten/test.csv"

if __name__ == "__main__":
    input_region = encoder.InputRegion(258)
    region1 = htm.Region(region_groesse)
    region2 = htm.Region(region_groesse)
    region3 = htm.Region(region_groesse)
    region4 = htm.Region(region_groesse)

    cognitor = Cognition.Cognitor()

    region1.connect_to_inputregion(input_region)
    region2.connect_to_inputregion(region1)
    region3.connect_to_inputregion(region2)
    region4.connect_to_inputregion(region3)

    opened_file = encoder.open_file(datei_pfad)
    for row in opened_file:
        for name in row:
            print(name)
            converted_name = encoder.name_to_list(name)
            for value in converted_name:
                b = encoder.show_only_actives(value)
                input_region.new_input(b)

                cognitor.assign_and_execute(region1)
                cognitor.assign_and_execute(region2)
                cognitor.assign_and_execute(region3)
                cognitor.assign_and_execute(region4)