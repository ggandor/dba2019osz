"""
Házi feladat no. 2: ASCII-kommunikáció A marsi alapján

(A vonatkozó jelenetek a filmben nagyjából az 50. perc körül
találhatóak.)

Az első részben egy hexadecimális számsorozatként elküldött üzenetet
kell dekódolnunk, ahogyan Matt Damon karaktere teszi a filmben, de mi
jó programozók lévén nem vesződünk kézi átírással, hanem automatizáljuk
a feladatot.

A második részben segítünk a NASA-nak is, és írunk nekik egy szoftvert,
amely a begépelt üzenet alapján automatikusan a kívánt irányokba
forgatja a Pathfinder kameráját.

Lépésről lépésre haladjatok, ha van megoldásotok egy-egy részproblémára,
teszteljétek le, próbáljátok ki néhány értéken. A kód maga nagyon rövid
lesz, a fő kihívás fejben összerakni a lépéseket.

https://www.businessinsider.com/the-martian-hexidecimal-language-2015-9
https://hu.wikipedia.org/wiki/ASCII
https://hu.wikipedia.org/wiki/Tizenhatos_sz%C3%A1mrendszer
https://matekarcok.hu/szamiras-szamrendszerek/
"""

# Watney
# ------

hex_message = "484F57414C495645"

# Először is végig kell mennünk egy ciklussal, és minden körben ki kell
# vágnunk egy 2 karakter hosszú szeletet (amely egy kétjegyű
# hexadecimális számot - vagyis 10-es alapon 0-255 tartományban lévő
# értéket - reprezentál, ez pedig az ASCII-táblázat alapján egy szöveges
# karaktert).

# Most a végéről kezdjük, és visszafelé haladunk. A `chr` függvény
# vissza tudja adni az adott ASCII-kódhoz tartozó karaktert - ez lesz az
# utolsó lépés. Ezt a kódot (számértéket) azonban egy integerként,
# normál, decimális formában várja, nekünk viszont egyelőre van egy
# hexadecimális számra utaló stringünk.

# Hogyan lesz tehát pl. a kezdő '48' stringünkből egy barátságos, 10-es
# alapú integer (vagyis 72), amit már használhatunk a `chr` függvényhez? 

# Itt jön képbe az `int` függvény, amit már ismerünk. Ö ugyanis nem csak
# 10-es számrendszerben megadott stringeket tud integerré konvertálni -
# második, opcionális argumentumként megadható az alapszám, vagyis,
# hogy milyen számrendszerben kapja az első argumentumot.

# Egy példa binárisan megadott argumentumra:
# int('0b100', 2) --> 4

# A fentiből sejthető, hogy a '48' stringünk a célra még nem lesz
# teljesen alkalmas - a hexadecimális számokat ugyanis a Python,
# hasonlóan a bináris (2-es alapú) és oktális (8-as alapú) számokhoz,
# speciális formában reprezentálja. A `hex` függvénnyel ezt meg is
# nézhetjük, amely visszaadja egy normál, 10-es alapú integer 16-os
# alapú reprezentációját:
# hex(15) --> '0xf'
# hex(67) --> '0x43'

# Ahogyan fent látható, a hexadecimális értékek egy speciális stringként
# jelennek meg, amelyek mindig egy '0x' előtaggal kezdődnek a konkrét
# számérték előtt (F ill. 43). A kettes, ill. nyolcas számrendszerbeli
# számok is hasonlóan, '0b' ("b" mint "bináris") ill. '0o' ("o" mint
# "oktális") előtaggal reprezentáltak. (Megjegyzés: kis- és nagybetűk
# ezekben a stringekben nem számítanak.)

# A hexadecimális számunkat tehát a megfelelő formában, előtaggal kell
# beküldenünk a függvénybe. Ha mindezt összeraktuk, innen már nincs más
# hátra, mint kiprintelni, vagy egy listához hozzáadni a dekódolt
# karaktert - és így tovább, minden ciklusban.




# NASA
# ----

message_to_send = "BRINGSJRNROUT"  # bring Sojourner out

# Feladat: kódoljuk be az üzenetet hexadecimális ASCII-értékek láncába,
# a fentihez hasonlóan. Ennek már önállóan is mennie kell, itt egyetlen
# új függvény szükséges: az `ord` - a `chr` kvázi párjaként - visszaadja
# a beadott karakter ASCII-kódját (pontosabban a Unicode reprezentációt,
# de alap latin betűk esetén a kettő ugyanaz).
# Ne feledjétek, hogy a stringek sok szempontból úgy működnek, mint a
# listák, rajtuk is használható a legtöbb tanult művelet (vagdosás és
# hasonlók)!




# Bónusz (innentől nem kötelező)
# ------------------------------
# A következő lépés a kamera forgatása. 0-F-ig a szimbólumok 16 részre
# osztják a kört, tehát 22.5 fokos lépésekben kell fordulni. Miután
# megvan a hexadecibe bekódolt stringünk (ld. fent), pakoljuk be egy
# listába a megfelelő szögértékeket egymás után, tehát ha pl. 'A'-n
# állunk, és '8'-as következik, akkor -2*22.5 = -45 fokot kell
# fordulnunk, ezt kell a listába tegyük (mi pedig elképzeljük, hogy egy
# `turn_camera` függvényt már megírtak az okos kollégák, amely egy ilyen
# bemeneti lista alapján megoldja a többit).

# Ne felejtsük el, hogy itt most nem közvetlenül a hex számértékeket
# küldjük át, hanem a string egyes karaktereit külön-külön (tehát
# egy-egy hex helyiértéket), ezeket kell egymás után szögekre
# lefordítani - az a vevő feladata lesz, hogy összerakja a párokat
# számértékekké, és végül lefordítsa az üzenetet.

# 180 foknál többet ne forduljunk, mindig a közelebbi irányba induljunk
# (az `abs` függvény használható az abszolút értékhez).


