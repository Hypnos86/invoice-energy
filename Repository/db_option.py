import json
class RepositoryFunction():
    def __init__(self):
        self.file = "invoice.json"

    def get(self):
        try:
            print("Lista zapisanych faktur")
            with open(self.file, "r") as file_open:
                file = json.load(file_open)
                for invoice in file:
                    print(invoice)
        except FileNotFoundError:
            print("Plik JSON o podanej nazwie nie istnieje.")
        except json.JSONDecodeError:
            print("Nie można zdekodować zawartości pliku JSON.")
        except Exception as ex:
            print("Ups, coś poszło nie tak:", ex)

    def post(self, data_1, data_2, data_3):
        try:
            with open(self.file, "r") as file_open:
                data_list = json.load(file_open)
                print(data_list)

            if not isinstance(data_list, list):
                raise ValueError("Zawartość pliku JSON nie jest listą")

            with open(self.file, 'w') as file:
                # Wczytaj istniejącą zawartość pliku jako listę obiektów
                if not data_list:
                    id_counter = 1
                else:
                    id_counter = data_list[-1]["identyfikator"] + 1

                # Dodaj nowy obiekt do listy
                date_format = {"identyfikator": id_counter, "data": data_1, "nr_faktury": data_2, "koszt_brutto": data_3}
                data_list.append(date_format)

                # Zapisz zmienione dane z powrotem do pliku JSON
                json.dump(data_list, file, indent=4)

        except FileNotFoundError:
            print("Plik JSON o podanej nazwie nie istnieje.")
        except json.JSONDecodeError:
            print("Nie można zdekodować zawartości pliku JSON.")
        except Exception as ex:
            print("Ups, coś poszło nie tak:", ex)

    def delete(self, id):
        pass

    def exit_program(self):
        exit()
