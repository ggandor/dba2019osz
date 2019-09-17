"""
Házi feladat no. 1: minimalista kő-papír-olló játék

Gyakorlásnak bónusz: kő-papír-olló-gyík-Spock - egyszerűsítések nélkül
25 lehetséges vizsgálandó eset
(szabályok:
https://en.wikipedia.org/wiki/Rock-paper-scissors#Additional_weapons;
illetve: https://www.youtube.com/watch?v=x5Q6-wMx-K8)

A .py fájlt a gyorgy.andorka@protonmail.com címre küldjétek el lehetőleg
szombat estig, ha kérdés van, vagy segítség kell, akkor is írjatok
bátran.

(Megjegyzés: a három idézőjellel keretezett szöveg szintén kommentnek
számít - vagyis a program átugorja -, ez azonban nem ér véget a sor
végén, mint a kettőskeresztes kommentek, hanem egészen a záró tripla
idézőjelig tart, akárhol is legyen - hasznos ilyen esetekben, ha
többsoros, hosszú szöveget akarunk írni.)
"""

# A következő kódsorokat megadom, bőséges megjegyzésekkel ellátva, mert
# a szükséges dolgokat még nem vettük az órán.

# Ebben a sorban csupán elérhetővé tesszük a `random` modul tartalmát,
# amelyben megtalálhatjuk a később használt `choice` függvényt.
import random

# A szögletes zárójelek között egy ún. listát tudunk megadni, így több
# értéket is csomagolva csatolhatunk egy változóhoz.
# (Ha a gyík-Spock verziót csináljátok, ne felejtsétek el beírni a
# további lehetőségeket.)
possible_moves = ["kő", "papír", "olló"]

# A `while` kulcsszó után írt, mindig igazra kiértékelődő feltétellel
# végtelen ismétlést tudunk előállítani, tehát a program újra és újra
# meg fogja kérdezni a lépésünket, és kiszámítja az eredményt.
# Figyeljétek meg, hogy az összes további kód be van húzva, jelezve,
# hogy a `while` "hatókörébe" tartozik - a Pythonban, a legtöbb más
# nyelvvel ellentétben, ez kötelező, mivel nincs más nyelvtani elemünk a
# blokkok lehatárolására.
while True:
    # A `choice` függvény szuperképessége, hogy a bemenetként
    # ("argumentumként") beadott listából véletlenszerűen választ egy
    # elemet, és visszadja (ez tehát a "kő", a "papír", vagy az "olló"
    # string lesz, ahogyan a fenti listában látható); ezt az értéket
    # elmentjük egy változóba, ez lesz a gép lépése.
    computers_move = random.choice(possible_moves)

    # TODO - itt jön a ti feladatotok

    # Az `input` függvénnyel kérjük be a felhasználó lépését (valamilyen
    # üzenet kíséretében), és mentsük el egy változóba.


    # A játékszabályok szerint hasonlítsuk össze a gép lépését és a
    # felhasználó lépését, és a lehetséges eseteknek megfelelően írjunk
    # ki egy üzenetet a `print` függvénnyel (mit lépett a gép, és mi a
    # végeredmény). A legnaivabb megoldás szerint 9 (3x3) feltételes ágat
    # (if/elif/else) kell megírni, ez persze csökkenthető.

    # P.S.: Gondolom rájöttetek volna, de az órán elfelejtettük
    # megjegyezni azt a nélkülözhetetlen infót, hogy a `==` és a többi
    # összehasonlító operátor stringekkel is használható. Az
    # egyenlőségen kívül a többire itt nem lesz szükségetek, azonban
    # érdemes kipróbálnotok őket, mert nem feltétlenül triviális a
    # használatuk - próbáljatok rájönni, milyen elv szerint működik pl.
    # a `<` string értékek esetén (két lépcsője is van az
    # összehasonlításnak).


    # Bónuszként még írhattok egy plusz ellenőrzést is, hogy ki
    # tudjatok lépni a "végtelen" programból anélkül, hogy le kelljen
    # lőnötök kívülről Ctrl-C-vel (vagy a Thonny-ban Ctrl-F2-vel). Ha
    # pl. "exit"-et ír be a felhasználó, akkor szakítsátok meg a
    # while-ciklust (hint: `break` kulcsszó).

    # Továbbá azt is ellenőrizhetitek, hogy a játékos értelmes lépést
    # írt-e be - ha a lehetséges lépéseken kívül valami mással
    # próbálkozik, kérjetek újra inputot (hint: `!=`, `or`, valamint
    # `continue` kulcsszó).




