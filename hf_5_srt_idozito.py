"""
Házi feladat no. 5: Felirat-időzítés

A feladat egy srt feliratfájlok szinkronizálására szolgáló program
elkészítése.

Lépések: 
1. Beolvasni a feliratfájlt.
2. Az összes timecode-ot a megadott értékkel megnövelni vagy csökkenteni.
- Timecode string átalakítása időértékké (pl. milliszekundum).
  (`split` ezúttal nem használható, csak regex metódusok.)
- Összeadás/kivonás elvégzése.
- A kapott érték visszaalakítása az srt timecode formátumának megfelelő
stringgé. (Ezt a függvényt előre megírtam.)
3. Visszaírni fájlba a tartalmat a módosított timecode-okkal.
"""

from math import floor

# A konstans számértékeket mindig szervezzük ki változóba és adjunk
# nevet nekik, ne használjunk "varázsszámokat" a kódon belül.
MSECS_PER_SEC = 1000
MSECS_PER_MIN = 1000 * 60
MSECS_PER_HOUR = 1000 * 60 * 60
SECS_PER_MIN = 60
MINS_PER_HOUR = 60


def msecs_to_timecode(n_msecs):

    def pad_with_zeros(s, slots_to_fill):
        return '0' * (slots_to_fill - len(s)) + s

    # % -> modulo ("a mod b" = a/b maradéka)
    # floor -> alsó egészrész (lefelé kerekítés)
    hours = floor(n_msecs / MSECS_PER_HOUR)
    mins = floor(n_msecs / MSECS_PER_MIN) % MINS_PER_HOUR
    secs = floor(n_msecs / MSECS_PER_SEC) % SECS_PER_MIN
    msecs = n_msecs % MSECS_PER_SEC

    hours, mins, secs = map(
            lambda s: pad_with_zeros(s, slots_to_fill=2),
            map(str, (hours, mins, secs)))
    msecs = pad_with_zeros(str(msecs), slots_to_fill=3)

    return f"{hours}:{mins}:{secs},{msecs}"

