# ------
# Listák
# ------

numbers = [1,5,17]
pets = ["macska", "kutya", "egér", "hörcsög"]
# nincs megkötés a típusokat illetően, keverni is lehet őket (ez nem
# magától értetődő, és nem minden nyelvben van így!)
list_with_mixed_types = [1, 2, "macska", 3.25, True]

# lista hosszának lekérése a `len` függvénnyel:
# (a stringek is sok esetben listákként használhatók)
len(pets)  # 4
len("hello")   # 5

# index
# -----
# 0-tól!
pets[0]  # "macska"
pets[1]  # "kutya"
pets[len(pets) - 1]  # "hörcsög", vagyis az utolsó elem
# pets[4] --> hiba

# slice
# -----
# lemásolódik, nem az eredeti módosul!
# szintaxis:
# lista[-tol : -ig (ez az elem már nem lesz benne!) : lepes (opcionális)]
[0,1,2,3][1:3]  # --> 0 [1 2] 3
pets_2nd_3rd = pets[1:3]  # ["kutya", "egér"]

# negatív indexelés
# -----------------
# a végéről visszafelé haladva
# ugyanaz, mintha `somelist[len(somelist) - n]`-t írnánk
# (a már emlegetett "syntactic sugar" esete ez is)
pets[-1]  # "hörcsög"
pets[-2]  # "egér"

# lépés megadása (opcionális)
# ---------------------------
# a megadott szeleten belül minden n-edik elem legyen csak benne
pets[0:3:2]  # ["macska", "egér"]

# ha 0-tól és/vagy a legvégéig szeletelnénk, akkor a megfelelő helyekre
# nem kell kiírni az indexet:
pets[:2]  # az első két elem
pets[1:] # a másodiktól a végéig
pets[:]  # a teljes lista (lényegében lemásoljuk)
pets[::2]  # a teljes lista minden második eleme

# `in` kulcsszó
# -------------
# True/False-t ad vissza, akár az összehasonlító operátorok
print("Van kutya a listában?",
        'kutya' in pets)
print("Igaz, hogy nincs medve a listában?",
        'medve' not in pets)
print()

# listákon értelmezett függvények
# -------------------------------
# ezeket lista.fuggvenynev() módon kell hívni
# (később szóba kerül, pontosan miben is különböznek ezek az eddig
# látott függvényektől)

# megtalálni egy elemet - `index`
pets.index('kutya')  # 1
# ha nincs a listán, hibát dob
#pets.index('aranyhal')  # --> error

# elem hozzáadása a lista végéhez - `append`
pets.append('aranyhal')
print("aranyhal hozzáadva:", pets)
print()

# továbbiak: insert, remove, stb.


# ----------
# for-ciklus
# ----------

# iterálás a lista elemein - most így csinálnánk:
print("while-ciklussal: ")
i = 0
while i < len(pets):
    print(pets[i], end=' ')
    i += 1
print("\n")

# for-ciklus
# `pet` helyett bármilyen nevet adhatnék a ciklusváltozónak, a lényeg,
# hogy minden körben a `pets` lista következő eleme csatolódik hozzá
# értékként.
print("for-ciklussal: ")
for pet in pets:
    print(pet, end=' ')
print("\n")

# voltaképpen ez történik egy for-ciklusban: 
# 1: pet = pets[0]
#    print(pet, end=' ')
# 2: pet = pets[1]
#    print(pet, end=' ')
# 3: pet = pets[2]
#    print(pet, end=' ')
# ...
# n: pet = pets[-1]
#    print(pet, end=' ')

# a lista hosszának megtudakolása len() függvény helyett for-ciklussal
# (ennek persze semmi gyakorlati értelme)
length_of_pets = 0
# az `_`-t mint változót nem is használjuk, csak azért kell, hogy
# le tudjon futni n-szer a ciklus
for _ in pets:
    length_of_pets += 1

print("pets hossza:", length_of_pets, end='\n\n');

# lista felépítése looppal
# (persze list.copy() vagy list[:] egyszerűbb)
pets_copy = []
for pet in pets:
    pets_copy.append(pet)

print("pets másolat:", pets_copy, end='\n\n')

# A stringek is listaként viselkednek (sok tekintetben), indexelve
# vannak, vághatók, lekérhető az n-edik elemük, hosszuk, stb.
pets_string = ""
for pet in pets[:-1]:
    pets_string += (pet + " és ")
pets_string += pets[-1]

print('állatok a listán:', pets_string)
