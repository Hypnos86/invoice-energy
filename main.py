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
            invoice_data = (input("Data faktury: "))
            nr_invoice = input("Nr faktury: ")
            cost = input("Kwota brutto: ")
            print(invoice_data)
            print(nr_invoice)
            print(cost)
            input_date = []
            input_date.append(input_date)
            input_date.append(nr_invoice)
            input_date.append(cost)
            print(input_date)

            repo = RepositoryFunction()
            post = repo.post(input_date, nr_invoice,cost)

        elif option == 3:
            pass

        elif option == 4:
            pass

        elif option == 5:
            repo = RepositoryFunction()
            repo.exit_program()

        else:
            print("Nie wybrano poprawnie opcji")









