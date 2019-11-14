import re


# ----------------------------------------------------
# match --> összehasonlítja az elejétől, illeszkedik-e
# ----------------------------------------------------

re.match('Graham', 'Graham Chapman')  # <re.Match object; span=(0, 6), match='Graham'>
re.match('Chapman', 'Graham Chapman')  # None

# ha az érdekel, a teljes string egyezik-e: fullmatch
re.fullmatch('Graham', 'Graham Chapman')  # None


# ----------------------------------------
# search --> az első találatot adja vissza
# ----------------------------------------

pythons = 'Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, Michael Palin' 
match_obj = re.search('T\w+', pythons)  # <re.Match object; span=(29, 34), match='Terry'>
print(match_obj.start())  # 29
print(match_obj.end())  # 34
print(match_obj.group())  # Terry


# ----------
# subgroupok
# ----------
# későbbi hivatkozás céljából zárójelek között kijelölhetők alcsoportok
# (sorrend szempontjából - egymásba ágyazott csoportoknál - a nyitó
# zárójel pozíciója számít)

match_obj = re.search('((J\w+) (C\w+)),', pythons)
full_match = match_obj.group()  # group () == group(0) 
full_name = match_obj.group(1)
first_name = match_obj.group(2)
last_name = match_obj.group(3)
print(full_match)  # John Cleese,
print(full_name)  # John Cleese
print(first_name)  # John
print(last_name)  # Cleese


# --------------------------------------------------
# findall --> az összes találat listáját adja vissza
# --------------------------------------------------

words = "boszorkányper, ni, kerekasztal, grál, hering"
print("\n5 karakternél hosszabb szavak:",
        re.findall('\w{5,}', words), end="\n\n")

with open('holy_grail_characters.txt') as f:
    holy_grail_characters = f.read()

# King Arthur; king_arthur@camelot.co.uk; 555-555-5551;
# Servant Patsy; patsy@camelot.co.uk; 555-555-5552;
# Sir Lancelot; lancelot@roundtable.co.uk; (555) 555 5553;
# Black Knight; guardian@thebrigde.co.uk; (555)-555-5554;
# Enchanter Tim; tim@caerbannog.co.uk; (555)-5555555;

# ismétlés:
# [abcd] - bármelyik karakter a halmazból
# [a-z] - karaktertartomány (unicode sorrend)
# [^abcd] - bármi, kivéve a felsorolt elemek

# \(, \) kell, mert szó szerint zárójeleket keresünk,
# nem csoportot akarunk
# a kötőjel elé is \ kell, hogy ne range-ként értse a []-en belül,
# vagy az első helyre kell írni
phone_nums = re.findall(r'\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}',
        holy_grail_characters)
print("telefonszámok:", phone_nums, end="\n\n")

e_mails = re.findall(r'[.\-\w\d]+@[.\-\w\d]+', holy_grail_characters)
print("e-mail címek:", e_mails, end="\n\n")

# Az r"..." stringekkel kapcsolatban:
# A probléma, hogy a Python a stringekben bizonyos karaktereket nem
# szó szerint értelmez, hanem speciális módon kezel, mint azt már láttuk
# (\n, \t, stb.). Ezzel az a gond, hogy a reguláris kifejezéseknek
# ugyanígy saját metakarakterei vannak, és a kettő adott eseben ütközhet.
# Ha például egy regexben le szeretném írni, hogy \b (vagyis szóhatárt
# keresek), azt a Python egy backspace-nek értelmezi a stringben, és úgy
# adja tovább a regex-feldolgozónak.
# Ezért vagy \\b-t kell írni, jelezve, hogy a 'b' előtti \ szó szerint
# \ akar lenni, vagy ún raw stringeket lehet használni - a string elé írt
# r-rel lehet jelezni, hogy ebben a stringben most mindent értsen
# szó szerint, ne keressen metakaraktereket. A regex minták esetén
# egyszerűbb megszokni, hogy automatikusan raw stringeket használjon
# az ember, mintsem hogy belefusson valami ilyen gondba.
# (https://docs.python.org/3.6/howto/regex.html#the-backslash-plague)


# A findall egy listát ad vissza, a találat-stringekkel, de mi van,
# ha csoportokat is szeretnénk definiálni a találatokban?

# -----------------------------------------------------
# finditer --> match objektumok iterátorát* adja vissza
# -----------------------------------------------------

# *Az iterátor olyan objektum, amelyből egy-egy elemet lehet lekérni,
# sorrendben, egymás után, amíg ki nem fogy (a `next` fügvénnyel),
# illetve ciklusban is felhasználható, végig lehet menni rajta,
# akár pl. egy listán - viszont ő csak ezt tudja, semmi mást, nem lehet
# elemeket hozzáadni, módosítani, stb.
# (https://www.programiz.com/python-programming/iterator)

# A match objektumokból már lekérhetők a találat különböző attribútumai,
# köztük a csoportok is.

pattern = r'([A-z]+) ([A-z]+);'
names = re.finditer(pattern, holy_grail_characters)

print("jelzők/titulusok:")
for match_obj in names:
    print(match_obj.group(1))  # titulus/jelző


# --------------------
# nevesített csoportok
# --------------------

#(?P<csoportnev>...keresőminta...)

# Ugyanaz, mint fent, de elnevezve:
pattern_with_named_groups = '(?P<attribute>[A-z]+) (?P<name>[A-z]+);'

# Megjegyzés: az iterátor objektumot, amit a finditer visszaad,
# csak egyszer lehetne felhasználni, vagyis végigmenni rajta ciklussal,
# ezért csinálok listát belőle a list() függvénnyel.
names = list(re.finditer(pattern_with_named_groups, holy_grail_characters))

# így már név szerint is elérhetjük a csoportot
print("\nnevek:")
for match_obj in names:
    print(match_obj.group('name'))

# groupdict -> szótár {csoportnév: találat, ...} formában
print("\njelzők/titulusok és nevek:")
for match_obj in names:
    print(match_obj.groupdict())


# -----------------------------
# re.sub() --> keresés és csere
# -----------------------------

# probléma: string.replace() csak szó szerinti kifejezéseket tud kezelni
# megoldás: re.sub()
censored_string = re.sub('damn|crap', '***', 'Damn this piece of crap!',
        flags=re.IGNORECASE)  # kis-nagybetű ne számítson a keresésben

print(censored_string)  # *** this piece of ***!
