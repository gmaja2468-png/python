#Wczytaj w trzech liniach pierwszą liczbę, operator i drugą liczbę
liczba1=float(input())
operator=input()
liczba2=float(input())
#Obsługa dodawania
if operator == "+":
    print(liczba1+liczba2)
#Obsługa dodawania
if operator == "-":
    print(liczba1-liczba2)
#Obsługa mnożenia
if operator == "*":
    print(liczba1*liczba2)
#Obsługa dzielenia i sprawdzenie dzielnika
if operator =="/":
    if liczba2 !=0:
        print (liczba1/liczba2)
    else:
        print("Nie można dzielić przez zero")

