import random
# Vraag namen op van deelnemers
# Controleer telkens of een ingevoerde naam wel uniek is
# Als er meer dan 2 namen zijn opgegeven kunnen er lootjes worden getrokken
# Maak lootjes voor alle namen
# Trek voor alle namen willekeurig (random) een lootje
# Iedereen heeft dus één uniek lootje
# Niemand mag het lootje van zichzelf hebben getrokken
# Print een lijst met namen en bijbehorende lootjes

names1 = []
names2 = []
lootjes = {}


players = int(input("Hoeveel mensen doen mee met lootjes trekken? "))

for i in range(players):
    name = input("Naam "+str(i+1)+": ")
    if name in names1:
        print("Deze naam zit er al in.")
    else:
        names1.append(name)
        names2.append(name)

while names1:
    name1 = names1[random.randint(0, len(names1) - 1)]
    name2 = names2[random.randint(0, len(names2) - 1)]

    if name1 == name2:
        if len(names1) == 1:
            print(name1 + " is helaas alleen.")
            break
    else:
        print(name1 + " heeft " + name2 + " als lootje getrokken.\n")
        names1.remove(name1)
        names2.remove(name2)




