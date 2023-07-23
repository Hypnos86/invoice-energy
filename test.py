import json
#
#
# # try:
# #     with open('invoice.json', 'r') as file:
# #         lines = file.readlines()
# #         print(lines)
# # except Exception as ex:
# #     print('Plik nie istnieje', ex)
#
# def test(dane):
#
#     file_name = "invoice.json"
#
#     try:
#         with open(file_name, "r") as open_file:
#             data_list = json.load(open_file)
#             print(data_list)
#
#         if not isinstance(data_list, list):
#             raise ValueError("Zawartość pliku JSON nie jest listą")
#
#         with open(file_name, 'w') as file:
#             # Wczytaj istniejącą zawartość pliku jako listę obiektów
#             if not data_list:
#                 id_counter = 1
#             else:
#                 id_counter = data_list[-1]["id"] + 1
#
#             # Dodaj nowy obiekt do listy
#             date_format = {"id": id_counter, "date": dane[0], "nr_invoices": dane[1], "cost": dane[2]}
#             data_list.append(date_format)
#
#             # Zapisz zmienione dane z powrotem do pliku JSON
#             json.dump(data_list, file, indent=4)
#
#     except FileNotFoundError:
#         print("Plik JSON o podanej nazwie nie istnieje.")
#     except json.JSONDecodeError:
#         print("Nie można zdekodować zawartości pliku JSON.")
#     except Exception as ex:
#         print("Ups, coś poszło nie tak:", ex)
#
#
# dane = ["2023-05-02", "FV-456-2023", 2500]
# test(dane)
#
# import json
#
# class RepositoryFunction():
#     def __init__(self):
#         self.file = "invoice.json"
#
#     # ... (reszta kodu)
#
#     def delete(self, id_to_delete):
#         try:
#             with open(self.file, "r") as file_open:
#                 data_list = json.load(file_open)
#
#             if not isinstance(data_list, list):
#                 raise ValueError("Zawartość pliku JSON nie jest listą")
#
#             # Szukamy faktury o podanym id do usunięcia
#             index_to_delete = None
#             for index, invoice in enumerate(data_list):
#                 if invoice.get("id") == id_to_delete:
#                     index_to_delete = index
#                     break
#
#             # Jeżeli nie znaleziono faktury o podanym id, zgłaszamy błąd
#             if index_to_delete is None:
#                 raise ValueError("Nie znaleziono faktury o podanym identyfikatorze.")
#
#             # Usuwamy fakturę o podanym id z listy
#             deleted_invoice = data_list.pop(index_to_delete)
#
#             # Zapisujemy zmienione dane z powrotem do pliku JSON
#             with open(self.file, 'w') as file:
#                 json.dump(data_list, file, indent=4)
#
#             print(f"Faktura o id {id_to_delete} została usunięta:")
#             print(deleted_invoice)
#
#         except FileNotFoundError:
#             print("Plik JSON o podanej nazwie nie istnieje.")
#         except json.JSONDecodeError:
#             print("Nie można zdekodować zawartości pliku JSON.")
#         except Exception as ex:
#             print("Ups, coś poszło nie tak:", ex)
#
# # Przykład użycia:
# repo = RepositoryFunction()
# repo.delete(3)  # Usuwa fakturę o id = 3
file = "invoice.json"

invoice_id = 3

with open(file, "r") as file_open:
    data_list = json.load(file_open)
    print(data_list)

if not isinstance(data_list, list):
    raise ValueError("Zawartość pliku JSON nie jest listą")

# Szukamy faktury o podanym id do usunięcia
index_to_delete = None
print(index_to_delete)
for index, invoice in enumerate(data_list):
    print(index, invoice)
    print(invoice.get("id"))
    if invoice.get("id") == invoice_id:
        index_to_delete = index
        print(index_to_delete)
        break