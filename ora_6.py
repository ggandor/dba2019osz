# Szógyakoriság-számlálás feat. William Blake és Szabó Lőrinc

# Ha kipróbáljátok, értelemszerűen a txt fájlt is másoljátok be
# a program mellé.

# Lenyesi a szóvégi írásjeleket a beadott stringről (később fog kelleni).
def trimmed_word(word):
    # "Ha az utolsó karakter szerepel az írásjelek alábbi listáján..."
    if word[-1] in ['.', ',', ';', ':', '!', '?']:
        return word[:-1] 
    else:
        return word

# Olvassuk be a fájl szöveges tartalmát (a karakterkódolást külön
# meg kell adni a magyar szöveg miatt).
with open('blake.txt', encoding='utf-8') as poem:
    text_content = poem.read()

# A split defaultból szóközök mentén szeleteli a stringet egy listába
# (sep=... argumentummal megadható más).
words_raw = text_content.split()
trimmed_words = [trimmed_word(word) for word in words_raw]
# A fenti sor ugyanaz, mintha:
# trimmed_words = []
# for word in words_raw:
#     trimmed_words.append(trimmed_word(word))

# Hogy a kis- és nagybetűk ne tévesszék meg a statisztikát,
# mindent lekonvertálunk kisbetűre.
blake_words = [word.lower() for word in trimmed_words]

# Először írjuk meg a függvényt, ami egy {szó: előfordulás, ...} kinézetű
# szótárat ad vissza egy szólista (no pun intended) alapján:
def frequency_dict_from(words):
    frequencies = {}  # üres szótár, ezt töltjük fel majd a ciklussal
    for word in words:
        # Alapból a kulcsok között keres, ha értékek között keresnénk,
        # azt `... in frequencies.values()` módon tudnánk megtenni
        # (jelen esetben kiírhatjuk, hogy frequencies.keys(),
        # de redundáns).
        if word not in frequencies:
            # Ha még nem találkoztunk a szóval, azaz még nincs
            # a szótárban, akkor betesszük.
            frequencies[word] = 1
        else:
            # Máskülönben megnöveljük az előfordulások számát.
            frequencies[word] += 1
    # Ne felejtsük el visszaadni az eredményt:
    return frequencies

# Majd a függvényünket felhasználva írjuk ki az eredményeket
# egy új szövegfájlba:
with open('blake_szavak.txt', 'w') as output_file:  # 'w' - írás
    frequency_dict = frequency_dict_from(blake_words)
    # A zárójel a ciklusváltozók körül egyébként redundáns.
    for (word, frequency) in frequency_dict.items():
        output_file.write(word + ": " + str(frequency) + "\n")

# Fakultatív házi: lehet még játszani vele, hogy gyakoriság szerinti
# sorban nyomtassuk ki a szavakat, vagy hogy az egyes gyakoriságok után
# soroljuk fel a vonatkozó szavakat, stb. 

