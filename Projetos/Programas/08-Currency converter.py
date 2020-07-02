EUR = 1
USD = 1.13789
GBP = 0.857679
RUB = 74.9470


def currencyConverter():
    chosenCurrency = input("Do you wish to convert your euros into \n1)USD \n2)RUB \n3)GBP\n\n")
    print(('-' * 36) + '\n')
    print(chosenCurrency, '\n\n' + ('-' * 36))

    if chosenCurrency == "1":
        eurAmount = round(float(input("How many euros do you wish to convert into USD? ")))
        print(('-' * 36) + '\n')
        print(eurAmount, "euro is", round(eurAmount * USD, 2), "US dollars.\n\n" + ('-' * 36),
              "\nThank you for using my program!")

    elif chosenCurrency == "2":
        eurAmount = round(float(input("How many euros do you wish to convert into RUB? ")))
        print(('-' * 36) + '\n')
        print(eurAmount, "euro is", round(eurAmount * RUB, 2), "rubles.\n\n" + ('-' * 36),
              "\nThank you for using my program!")

    elif chosenCurrency == "3":
        eurAmount = round(float(input("How many euros do you wish to convert into GBP? ")))
        print(('-' * 36) + '\n')
        print(eurAmount, "euro is", round(eurAmount * GBP, 2), "pounds.\n\n" + ('-' * 36),
              "\nThank you for using my program!")

    else:
        print("Error, please try again. \nEnter 1 for USD, 2 for RUB or 3 for GBP")


currencyConverter()