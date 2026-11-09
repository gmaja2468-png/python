#Wczytaj dwa teksty
t1=input()
t2=input()
#1. Połączenie tekstów operatorem +
print(t1+t2)
#2. Trzykrotne powtórzenie pierwszego tekstu operatorem * 
print(t1*3)
#3. Próba wykonania działań na "8" i "2"/"8" i 2
#Python zgłasza tutaj bład TypeError (nie można odejmować tekstów ani dodawać tekstu do liczby bezpośrednio)
#print(t1-t2)
#print(t1+t2)
#4. Uzyskanie wyników 6 i 10 na odpowiednich konwersjach na int:
print(int(t1)-int(t2))
print(int(t1)+2)
      