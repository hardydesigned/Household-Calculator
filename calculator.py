categories = {
    'Fixkosten' : 0.0,
    'Vergnügen' : 0.0,
    'Essen' : 0.0,
    'Auto' : 0.0,
    'Online Shopping' : 0.0,
    'Sparen M' : 0.0,
    'Sparen L' : 0.0,
    'Einnahmen' : 0.0,
}

expenses = []


def getInput():
    print("Gebe in folgendem Format ein: {+/-Betrag} {Name} {Kategorie als Buchstabe}")
    print("Beispiel: -10 Kino V")
    print("Beispiel: 10 Gehalt E")

    while(True):
        user_input = input("Ein/Ausgabe: ")

        input_array = user_input.split(" ")

        if user_input == "ende":
            break

        if len(input_array) != 3:
            print("Falsches Format!")
            continue


        expenses.append(user_input)

        if input_array[2] == "F":
            categories['Fixkosten'] += float(input_array[0])
        elif input_array[2] == "V":
            categories['Vergnügen'] += float(input_array[0])
        elif input_array[2] == "E":
            categories['Essen'] += float(input_array[0])
        elif input_array[2] == "A":
            categories['Auto'] += float(input_array[0])
        elif input_array[2] == "O":
            categories['Online Shopping'] += float(input_array[0])
        elif input_array[2] == "M":
            categories['Sparen M'] += float(input_array[0])
        elif input_array[2] == "L":
            categories['Sparen L'] += float(input_array[0])
        elif input_array[2] == "I":
            categories['Einnahmen'] += float(input_array[0])


def getAll():
    all_expenses = 0
    all_incomes = 0


    for category, cost in categories.items():
        if(category != "Einnahmen"):
            all_expenses += cost
        else:
            all_incomes += cost

    print(f"Gesamtausgaben: {all_expenses}")
    print(f"Gesamteinnahmen: {all_incomes}")
    print(f"Überschuss: {all_incomes - all_expenses}")
    print("Kategorien:")
    for category, cost in categories.items():
        print(f"    {category}: {cost}")

def getExpenses():
    for expense in expenses:
        print(expense)


def getCategories():
    print("Kategorien:")
    for category in categories.keys():
        if category != "Einnahmen":
            print(f"    {category}: {category[0]}")
        else:
            print(f"    {category}: I")
    
    print("Kategorie ändern? (j/n)")
    user_input = input("Ein/Ausgabe: ")

    if user_input == "j":
        while(True):
            print("Welche Kategorie möchtest du ändern?")
            user_input = input("Kategorie: ")

            if user_input == 'ende':
                break

            if user_input not in categories:
                print("Kategorie nicht gefunden!")
                continue

            print("Neuer Name:")
            new_name = input("Name: ")

            categories[new_name] = categories.pop(user_input)

            print("Kategorie geändert!")


print("Willkommen zum Budget Calculator!")

while(True):
    print("Wähle eine Funktion:")
    print("     eingabe == Ein/Ausgaben eingeben")
    print("     gesamt == Gesamt Ein und Ausgaben anzeigen")
    print("     kategorien == Kategorien anzeigen und ändern")
    print("     umsaetze == Alle Ein/Ausgaben ansehen")
    print("     ende == Beenden")

    user_input = input("Funktion: ")

    if user_input == "eingabe":
        getInput()
    elif user_input == "gesamt":
        getAll()
    elif user_input == "kategorien":
        getCategories()
    elif user_input == "umsaetze":
        getExpenses()

    elif user_input == "ende":
        break
    else:
        continue



