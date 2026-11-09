#Wczytaj liczbę całkowitą
liczba=int(input())
#1. Czy liczba jest dodatnia (czy jest większa od zera)
if liczba>0:
    print("Dodatnia")
#2. Czy liczba jest parzysta (reszta z dzielenia przez 2 wynosi 0)
if liczba % 2 ==0:
    print("Parzysta")