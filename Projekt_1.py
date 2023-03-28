'''
author =
'''
import pprint
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]


"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Denis Hemr
email: dennis.hemmr@gmail.com
discord: Denis H.
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Registrovaní uživatelé:
# +------+-------------+
# | user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123   |
# +------+-------------+

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "=-" * 12
oddelovac2 = "-" * 24
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Přihlášení (Uživatel)
print(oddelovac)
uzivatel = input("Zadejte jméno uživatele, bez velkých písmen:\n")

if uzivatel not in user:
    print("Uživatel není registrovaný, ukončuji program!")
    exit()
else:
    print("Vítejte v aplikaci!", uzivatel)
    print(oddelovac)
    heslo = input("Nyní zadejte heslo pro uživatele " + uzivatel + ":\n")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

if heslo == user[uzivatel]:
    print("Přihlášení proběhlo úspěšně!")
else:
    print("Neplatné heslo, ukončuji program!")
    exit()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


vyber = input("Zadej číslo textu k analýze (1-" + str(len(TEXTS)) + "): ")
print(oddelovac)
if not vyber.isdigit() or int(vyber) not in range(1, len(TEXTS) + 1):
    print("Zadané číslo textu není platné, program se ukončí!")
    exit()
else:
    text = TEXTS[int(vyber) - 1]
    print("Vybral jsi text číslo " + vyber + ":\n")


text = TEXTS[int(vyber) - 1]
slova = text.split()
pocet_slov = len(slova)
zacinajicim_velkym_pismem = 0
psany_velkym_pismem = 0
psany_malym_pismem = 0
pocet_cisel = 0
soucet = 0

for slovo in slova:
    if slovo.istitle():
        zacinajicim_velkym_pismem += 1
    elif slovo.isupper():
        psany_velkym_pismem += 1
    elif slovo.islower():
        psany_malym_pismem += 1
    elif slovo.isnumeric():
        pocet_cisel += 1
        soucet += int(slovo)

print(f"Počet slov: {pocet_slov}|")
print(oddelovac2)
print(f"Počet slov začínajících velkým písmenem: {zacinajicim_velkym_pismem}|")
print(oddelovac2)
print(f"Počet slov psaných velkými písmeny: {psany_velkym_pismem}|")
print(oddelovac2)
print(f"Počet slov psaných malými písmeny: {psany_malym_pismem}|")
print(oddelovac2)
print(f"Počet čísel: {pocet_cisel}|")
print(oddelovac2)
print(f"Součet čísel: {soucet}|")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Vytvoření seznamu délek slov
delka_slova = [len(slovo) for slovo in text.split()]

# Vytvořený slovník pro ukládání délek slov
delka_slov_dict = {}
for delka in delka_slova:
    if delka in delka_slov_dict:
        delka_slov_dict[delka] += 1
    else:
        delka_slov_dict[delka] = 1

# Vypsání sloupcového grafu
print(f"{oddelovac}")
print(f"| Délka | Nález v textu |")
print(f"{oddelovac}")


for delka, pocet in sorted(delka_slov_dict.items()):
    print(f"{oddelovac}|")
    print(f"{delka}: {'*' * pocet}")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
