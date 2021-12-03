import random, os, time


blueCards = ["blauw 0 ","blauw 1","blauw 2","blauw 3","blauw 4","blauw 5","blauw 6","blauw 7","blauw 8","blauw 9","blauw 1","blauw 2","blauw 3","blauw 4","blauw 5","blauw 6","blauw 7","blauw 8","blauw 9"]
redCards = ["rood 0 ","rood 1","rood 2","rood 3","rood 4","rood 5","rood 6","rood 7","rood 8","rood 9","rood 1","rood 2","rood 3","rood 4","rood 5","rood 6","rood 7","rood 8","rood 9"]
yellowCards = ["geel 0 ","geel 1","geel 2","geel 3","geel 4","geel 5","geel 6","geel 7","geel 8","geel 9","geel 1","geel 2","geel 3","geel 4","geel 5","geel 6","geel 7","geel 8","geel 9"]
greenCards = ["groen 0 ","groen 1","groen 2","groen 3","groen 4","groen 5","groen 6","groen 7","groen 8","groen 9","groen 1","groen 2","groen 3","groen 4","groen 5","groen 6","groen 7","groen 8","groen 9"]
taketwoCards = ["neem-twee blauw","neem-twee blauw","neem-twee rood","neem-twee rood","neem-twee geel","neem-twee geel","neem-twee groen","neem-twee groen"]
reverseCards = ["reverse blauw","reverse blauw","reverse rood","reverse rood","reverse geel","reverse geel","reverse groen","reverse groen",]
skipturnCards = ["skip-turn blauw","skip-turn blauw","skip-turn rood","skip-turn rood","skip-turn geel","skip-turn geel","skip-turn groen","skip-turn groen",]
choiceCards = ["keuzekaart","keuzekaart","keuzekaart","keuzekaart"]
takefourCards = ["neem-vier","neem-vier","neem-vier","neem-vier"]
allCards = blueCards + redCards + yellowCards + greenCards + taketwoCards + reverseCards + skipturnCards + choiceCards + takefourCards


MainPlayerDeck = []
player2Deck = []
player3Deck = []
player4Deck = []
player5Deck = []
player6Deck = []
player7Deck = []
player8Deck = []
player9Deck = []
player10Deck = []


nameList = ["Justin Case", "Error404","average_student","minecraftkid2013","lucifer_morningstar","supermario420","PeppaPig", "NoLifer", "MarkZuckerberg","BillGates","MyNameJeffBezos","MarkRutteOpFiets","Swagman","Steve","Alex"]


player2Name = random.choice(nameList)
nameList.remove(player2Name)
player3Name = random.choice(nameList)
nameList.remove(player3Name)
player4Name = random.choice(nameList)
nameList.remove(player4Name)
player5Name = random.choice(nameList)
nameList.remove(player5Name)
player6Name = random.choice(nameList)
nameList.remove(player6Name)
player7Name = random.choice(nameList)
nameList.remove(player7Name)
player8Name = random.choice(nameList)
nameList.remove(player8Name)
player9Name = random.choice(nameList)
nameList.remove(player9Name)
player10Name = random.choice(nameList)
nameList.remove(player10Name)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)



def kaartenVedelen(name):
    print("De kaarten van speler ",name," worden verdeeld")
    time.sleep(0.5)
    i = 0
    if name == username:
        while True:
            kaart = random.choice(allCards)
            MainPlayerDeck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player2Name:
        while True:
            kaart = random.choice(allCards)
            player2Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player3Name:
        while True:
            kaart = random.choice(allCards)
            player3Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player4Name:
        while True:
            kaart = random.choice(allCards)
            player4Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player5Name:
        while True:
            kaart = random.choice(allCards)
            player5Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player6Name:
        while True:
            kaart = random.choice(allCards)
            player6Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player7Name:
        while True:
            kaart = random.choice(allCards)
            player7Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player8Name:
        while True:
            kaart = random.choice(allCards)
            player8Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player9Name:
        while True:
            kaart = random.choice(allCards)
            player9Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break
    if name == player10Name:
        while True:
            kaart = random.choice(allCards)
            player10Deck.append(kaart)
            allCards.remove(kaart)
            i += 1
            if i == 7:
                break

def mainDeck():
    print("\nDeck",username,":",MainPlayerDeck)

def tegenstanderDeck():
    for x in range(playerAmount):
        if x == 1:
            print("Deck",player2Name,":",player2Deck)
        if x == 2:
            print("Deck",player3Name,":",player3Deck)
        if x == 3:
            print("Deck",player4Name,":",player4Deck)
        if x == 4:
            print("Deck",player5Name,":",player5Deck)
        if x == 5:
            print("Deck",player6Name,":",player6Deck)
        if x == 6:
            print("Deck",player7Name,":",player7Deck)
        if x == 7:
            print("Deck",player8Name,":",player8Deck)
        if x == 8:
            print("Deck",player9Name,":",player9Deck)
        if x == 9:
            print("Deck",player10Name,":",player10Deck)
        

def start():
    global username
    global playerAmount
    playerAmount = int(input("Hoeveel spelers doen er mee met Uno? "))
    if playerAmount < 2:
        print("Niet genoeg spelers.")
        start()
    elif playerAmount > 10:
        print("Het maximum spelers is 10.")
        start()
    else:
        username = input("Vul je eigen gebruikers naam in: ")


start()
print("\nHallo",username,", je speelt vandaag tegen:")
if playerAmount== 2:
    print(player2Name,"\n")
elif playerAmount == 3:
    print(player2Name+" en "+ player3Name)
elif playerAmount == 4:
    print(player2Name+", "+player3Name+" en ", player4Name)
elif playerAmount == 5:
    print(player2Name+", "+player3Name+", "+player4Name+" en "+ player5Name)
elif playerAmount == 6:
    print(player2Name+", "+player3Name+", ",player4Name+", "+player5Name+" en "+ player6Name)
elif playerAmount == 7:
    print(player2Name+", ",player3Name+", "+player4Name+", "+player5Name+", "+player6Name+" en "+ player7Name)
elif playerAmount == 8:
    print(player2Name+", "+player3Name+", "+player4Name+", "+player5Name+", "+player6Name+", "+player7Name+" en "+ player8Name)
elif playerAmount == 9:
    print(player2Name+", "+player3Name+", "+player4Name+", "+player5Name+", "+player6Name+", "+player7Name+", "+player8Name+" en "+ player9Name)
elif playerAmount == 10:
    print(player2Name+", "+player3Name+", "+player4Name+", "+player5Name+", "+player6Name+", "+player7Name+", "+player8Name+", "+player9Name+" en "+ player10Name)

for i in range(playerAmount):
        if i == 0:
            kaartenVedelen(username)
        elif i == 1:
            kaartenVedelen(player2Name)
        elif i == 2:
            kaartenVedelen(player3Name)
        elif i == 3:
            kaartenVedelen(player4Name)
        elif i == 4:
            kaartenVedelen(player5Name)
        elif i == 5:
            kaartenVedelen(player6Name)
        elif i == 6:
            kaartenVedelen(player7Name)
        elif i == 7:
            kaartenVedelen(player8Name)
        elif i == 8:
            kaartenVedelen(player9Name)
        elif i == 9:
            kaartenVedelen(player10Name)
        else:
            print("")

mainDeck()
tegenstanderDeck()


