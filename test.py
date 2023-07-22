import json


# try:
#     with open('invoice.json', 'r') as file:
#         lines = file.readlines()
#         print(lines)
# except Exception as ex:
#     print('Plik nie istnieje', ex)

def test(dane):

    file_name = "invoice.json"

    try:
        with open(file_name, "r") as open_file:
            data_list = json.load(open_file)
            print(data_list)

        if not isinstance(data_list, list):
            raise ValueError("Zawartość pliku JSON nie jest listą")

        with open(file_name, 'w') as file:
            # Wczytaj istniejącą zawartość pliku jako listę obiektów
            if not data_list:
                id_counter = 1
            else:
                id_counter = data_list[-1]["id"] + 1

            # Dodaj nowy obiekt do listy
            date_format = {"id": id_counter, "date": dane[0], "nr_invoices": dane[1], "cost": dane[2]}
            data_list.append(date_format)

            # Zapisz zmienione dane z powrotem do pliku JSON
            json.dump(data_list, file, indent=4)

    except FileNotFoundError:
        print("Plik JSON o podanej nazwie nie istnieje.")
    except json.JSONDecodeError:
        print("Nie można zdekodować zawartości pliku JSON.")
    except Exception as ex:
        print("Ups, coś poszło nie tak:", ex)


dane = ["2023-05-02", "FV-456-2023", 2500]
test(dane)
