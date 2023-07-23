from Repository.db_option import RepositoryFunction


if __name__ == "__main__":
    print("--------------------------------")
    print("Program Energia-ZZP WIiR KWP P-ń")
    print("--------------------------------")
    while True:
        print("1 - Odczyt ewidencji")
        print("2 - Zapisz do ewidencji")
        print("3 - Edytuj")
        print("4 - Usuń z ewidencji")
        print("5 - Wyjdz z programu"+"\n")
        option = int(input("Wybież opbję: "))

        if option == 1:
            repo = RepositoryFunction()
            get = repo.get()

        elif option == 2:
            print("Wprowadz dane nowej faktury")
            invoice_data = input("Data faktury: ")
            nr_invoice = input("Nr faktury: ")
            cost = input("Kwota brutto: ")
            input_date = []
            input_date.append(invoice_data)
            input_date.append(nr_invoice)
            input_date.append(cost)
            decision = int(input("Czy chcesz zapisać dane do tabeli?"+"\n"+ "1 - Tak"+"\n"+"2 - Nie"+"\n"+"Twój wybór: "))
            if decision == 1:
                repo = RepositoryFunction()
                post = repo.post(invoice_data, nr_invoice,cost)
                print("\n"+"---- Zapisano do bazy ----"+"\n")
                repo.get()

        elif option == 3:
            pass

        elif option == 4:
            repo = RepositoryFunction()
            repo.get()

            delete_invoice = int(input("Wprowadz id faktury aby ją usunąć: "))
            print(f"Czy jesteś pewien, że chcesz usunąć fakture z id {delete_invoice}?")
            decision = int(input("1- Tak"+"\n"+"2 - Nie"+"\n"+"Twój wybór: "))
            if decision == 1:
                repo.delete(delete_invoice)

        elif option == 5:
            repo = RepositoryFunction()
            repo.exit_program()

        else:
            print("Nie wybrano poprawnie opcji")