import random

samoglasnici = ["a", "e", "i", "o", "u"]
suglasnici = ["b", "c", "d", "f", "g", "h", "k", "m"]
rijec = []

def biram_samoglasnik():
    abc = samoglasnici[random.randint(0, 4)]
    return abc

def biram_suglasnik():
    abc = suglasnici[random.randint(0, 7)]
    return abc

print("Dobrodosli u kviz brojke i slova")
igrac = input('Vase ime je: \n')

for i in range(0, 10):
    print(f"Ovo je {i + 1}. slovo.")
    print(igrac + ", izaberite slova: ")
    print("1 - SAMOGLASNIK   2 - SUGLASNIK \n")
    slovo = input()

    if slovo != "1" or slovo != "2":
        slovo = "1"
    
    if slovo == "1":
        rand_samo = biram_samoglasnik()
        rijec.append(rand_samo)
    if slovo == "2":
        rand_sug = biram_suglasnik()
        rijec.append(rand_sug)

print(f"Kombinaciaj slova je: {str(rijec).upper()}")
    




