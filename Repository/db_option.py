import json
from datetime import datetime


class RepositoryFunction():
    def __init__(self):
        self.file = "invoice.json"

    def get(self):
        try:
            print("Lista zapisanych faktur")
            with open(self.file, "r") as file_open:
                file = json.load(file_open)
                print("| Identyfikator |"+"-"*10+"| Data faktury |"+"-"*10+"| Nr faktury |"+"-"*10+"| Wartość faktury |")
                sum = 0
                for invoice in file:
                    print(invoice, end="\n")
                    sum += invoice.get("koszt_brutto")
                print(f"SUMA FAKTUR: {sum}")
                print("\n")
        except FileNotFoundError:
            print("Plik JSON o podanej nazwie nie istnieje.")
            print("Ewidencja jest pusta", end="\n")
        except json.JSONDecodeError:
            print("Nie można zdekodować zawartości pliku JSON.")
        except Exception as ex:
            print("Ups, coś poszło nie tak:", ex)

    def post(self, date, no_fv, cost):
        try:
            with open(self.file, "r") as file_open:
                data_list = json.load(file_open)

            if not isinstance(data_list, list):
                raise ValueError("Zawartość pliku JSON nie jest listą")

            with open(self.file, 'w') as file:
                # Wczytaj istniejącą zawartość pliku jako listę obiektów
                if not data_list:
                    id_counter = 1
                else:
                    id_counter = data_list[-1]["id"] + 1

                # Dodaj nowy obiekt do listy
                date_format = {"id": id_counter, "data_faktury": date, "nr_faktury": no_fv,
                               "koszt_brutto": cost}
                data_list.append(date_format)

                # Zapisz zmienione dane z powrotem do pliku JSON
                json.dump(data_list, file, indent=4)

        except FileNotFoundError:
            print("Plik JSON o podanej nazwie nie istnieje.")
        except json.JSONDecodeError:
            print("Nie można zdekodować zawartości pliku JSON.")
        except Exception as ex:
            print("Ups, coś poszło nie tak:", ex)

    def delete(self, invoice_id):
        try:
            with open(self.file, "r") as file_open:
                data_list = json.load(file_open)

            if not isinstance(data_list, list):
                raise ValueError("Zawartość pliku JSON nie jest listą")

            # Szukamy faktury o podanym id do usunięcia
            index_to_delete = None
            for index, invoice in enumerate(data_list):
                if invoice.get("id") == invoice_id:
                    index_to_delete = index
                    break

            # Jeżeli nie znaleziono faktury o podanym id, zgłaszamy błąd
            if index_to_delete is None:
                raise ValueError("Nie znaleziono faktury o podanym identyfikatorze."+"\n")

            # Usuwamy fakturę o podanym id z listy4
            deleted_invoice = data_list.pop(index_to_delete)

            # Zapisujemy zmienione dane z powrotem do pliku JSON
            with open(self.file, 'w') as file:
                json.dump(data_list, file, indent=4)

            print(f"Faktura o id {invoice_id} została usunięta:")
            print(deleted_invoice)

        except FileNotFoundError:
            print("Plik JSON o podanej nazwie nie istnieje.")
        except json.JSONDecodeError:
            print("Nie można zdekodować zawartości pliku JSON.")
        except Exception as ex:
            print("Ups, coś poszło nie tak:", ex)

    def exit_program(self):
        exit()

    def validate_and_formated_date(self, user_input):
        try:
            # Analiza wprowadzonej daty w formacie "dd.mm.yyyy"
            input_date = datetime.strptime(user_input, "%d.%m.%Y")

            formatted_date = input_date.strftime("%Y-%m-%d")
            return formatted_date

        except ValueError as ex:
            return None
        except Exception as ex:
            print("Inny błąd:", ex)
