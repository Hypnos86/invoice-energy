from Repository.db_option import RepositoryFunction


if __name__ == "__main__":
    repo = RepositoryFunction()
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
            get = repo.get()

        elif option == 2:
            print("Wprowadz dane nowej faktury")

            formatted_data = repo.validate_and_formated_date(input("Data faktury [dzień.miesiąć.rok]: "))

            nr_invoice = input("Nr faktury: ")

            # odbieranie inputu od uzytkownika
            input_cost = input("Kwota brutto: ")
            # zamiana , na .
            formatted_cost = input_cost.replace(",", ".")
            # żytowanie na typ float
            float_cost = float(formatted_cost)
            # zaokrąglanie do 2ch miejsc po przecinku
            round_cost = round(float_cost, 2)

            decision = int(input("Czy chcesz zapisać dane do tabeli?"+"\n"+ "1 - Tak"+"\n"+"2 - Nie"+"\n"+"Twój wybór: "))
            if decision == 1:
                post = repo.post(formatted_data, nr_invoice, round_cost)
                print("\n"+"---- Zapisano do bazy ----"+"\n")
                repo.get()

        elif option == 3:
            pass

        elif option == 4:
            repo.get()
            delete_invoice = int(input("Wprowadz id faktury aby ją usunąć: "))
            print(f"Czy jesteś pewien, że chcesz usunąć fakture z id {delete_invoice}?")
            decision = int(input("1- Tak"+"\n"+"2 - Nie"+"\n"+"Twój wybór: "))
            if decision == 1:
                repo.delete(delete_invoice)

        elif option == 5:
            repo.exit_program()

        else:
            print("Nie wybrano poprawnie opcji")