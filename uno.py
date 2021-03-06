import random, os, time


blueCards = ["blauw 0 ","blauw 1","blauw 2","blauw 3","blauw 4","blauw 5","blauw 6","blauw 7","blauw 8","blauw 9","blauw 1","blauw 2","blauw 3","blauw 4","blauw 5","blauw 6","blauw 7","blauw 8","blauw 9"]
redCards = ["rood 0 ","rood 1","rood 2","rood 3","rood 4","rood 5","rood 6","rood 7","rood 8","rood 9","rood 1","rood 2","rood 3","rood 4","rood 5","rood 6","rood 7","rood 8","rood 9"]
yellowCards = ["geel 0 ","geel 1","geel 2","geel 3","geel 4","geel 5","geel 6","geel 7","geel 8","geel 9","geel 1","geel 2","geel 3","geel 4","geel 5","geel 6","geel 7","geel 8","geel 9"]
greenCards = ["groen 0 ","groen 1","groen 2","groen 3","groen 4","groen 5","groen 6","groen 7","groen 8","groen 9","groen 1","groen 2","groen 3","groen 4","groen 5","groen 6","groen 7","groen 8","groen 9"]
taketwoCards = ["blauw neem-twee","blauw neem-twee","rood neem-twee","rood neem-twee","geel neem-twee","geel neem-twee","groen neem-twee","groen neem-twee"]
reverseCards = ["blauw reverse","blauw reverse","rood reverse","rood reverse","geel reverse","geel reverse","groen reverse","groen reverse",]
skipturnCards = ["blauw skip-turn","blauw skip-turn","rood skip-turn","rood skip-turn","geel skip-turn","geel skip-turn ","groen skip-turn","groen skip-turn",]
choiceCards = ["Wild","Wild","Wild","Wild"]
takefourCards = ["Wild neem-vier","Wild neem-vier","Wild neem-vier","Wild neem-vier"]
allCards = blueCards + redCards + yellowCards + greenCards + taketwoCards + reverseCards + skipturnCards + choiceCards + takefourCards
pile = []
Reverse = 0

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
splitCard = pile

def gewonnen(name):
    print("\n",name,"heeft 0 kaarten over en heeft dus gewonnen.")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def mostFrequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

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

def beurtSpeler():
    global cardAmount, playedCard, Reverse
    random.shuffle(allCards)
    if len(MainPlayerDeck) == 0:
        print("\nJe hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    while True:
        print()
        mainDeck()
        #tegenstanderDeck()
        #print(pile)
        print("Bovenste open kaart:",pile[-1])
        cardAmount = len(MainPlayerDeck)
        for i in range(cardAmount):
            print(str(i + 1), MainPlayerDeck[i])
        playedCard = int(input("Welke kaart wilt u spelen? 1234567 of 0 om een kaart te pakken "))
        if playedCard > cardAmount:
            print("\nDie kaart zit niet in jouw deck.\n")
        elif playedCard == 0:
            MainPlayerDeck.append(random.choice(allCards))
            print("\nJe hebt een kaart van de stapel gepakt.\n")
            AI2(player2Name)
        else:
            splitCard = pile[-1].split(" ",1)
            splitCard2 = MainPlayerDeck[(playedCard-1)].split(" ",1)
            currentColor = splitCard[0]
            playedColor = splitCard2[0]
            currentValue = splitCard[-1]
            playedValue = splitCard2[-1]
            if currentColor == playedColor or currentValue == playedValue:
                if playedValue == "neem-twee":
                    print("\nJe hebt neem-twee opgelegd, de volgende speler pakt 2 kaarten")
                    print(player2Name,"krijgt 2 kaarten\n")
                    removeCard = MainPlayerDeck[playedCard-1]
                    pile.append(removeCard)
                    MainPlayerDeck.pop(playedCard - 1)
                    for x in range(2):
                        plusTwee = random.choice(allCards)
                        player2Deck.append(plusTwee)
                        allCards.remove(plusTwee)
                    AI2(player2Name)
                elif playedValue == "neem-vier":
                    print("\nJe hebt neem-vier opgelegd, de volgende speler pakt 4 kaarten")
                    print(player2Name,"krijgt 4 kaarten\n")
                    removeCard = MainPlayerDeck[playedCard-1]
                    pile.append(removeCard)
                    MainPlayerDeck.pop(playedCard - 1)
                    for x in range(4):
                        plusTwee = random.choice(allCards)
                        player2Deck.append(plusTwee)
                        allCards.remove(plusTwee)
                    AI2(player2Name)
                else:
                    removeCard = MainPlayerDeck[playedCard-1]
                    pile.append(removeCard)
                    MainPlayerDeck.pop(playedCard - 1)
                    AI2(player2Name)
            elif playedColor == "Wild" or currentColor == "Wild":
                removeCard = MainPlayerDeck[playedCard-1]
                pile.append(removeCard)
                MainPlayerDeck.pop(playedCard - 1)
                AI2(player2Name)
            else:
                print("\nDat is niet de juiste kleur.\n")
                beurtSpeler()

def AI2(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player2Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player2Deck)):
            card = player2Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player2Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 3:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player3Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 2:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 3:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player3Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 2:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 2:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 3:
        time.sleep(1)
        AI3(player3Name)

def AI3(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    if len(player3Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player3Deck)):
            card = player3Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player3Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 4:
                for x in range(2):
                    neemTwee3 = player4Deck.append(random.choice(allCards))
                    allCards.remove(neemTwee3)
            elif playerAmount == 3:
                for x in range(2):
                    neemTwee = MainPlayerDeck.append(random.choice(allCards))
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 3:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player3Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 2:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        player3Deck.remove(possibleR)
    if playerAmount == 3:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 4:
        time.sleep(1)
        AI4(player4Name)

def AI4(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player4Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player4Deck)):
            card = player4Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player4Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 5:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player5Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 4:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 5:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player5Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 4:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 4:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 5:
        time.sleep(1)
        AI5(player5Name)

def AI5(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player5Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player5Deck)):
            card = player5Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player5Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 6:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player6Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 5:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 6:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player6Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 5:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 5:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 6:
        time.sleep(1)
        AI6(player6Name)

def AI6(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player6Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player6Deck)):
            card = player6Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player6Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 7:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player7Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 6:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 7:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player7Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 6:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 6:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 7:
        time.sleep(1)
        AI7(player7Name)
           
def AI7(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player7Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player7Deck)):
            card = player7Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player6Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 8:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player8Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 7:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 8:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player8Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 7:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 7:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 8:
        time.sleep(1)
        AI8(player8Name)

def AI8(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player8Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player8Deck)):
            card = player8Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player6Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 9:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player9Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 8:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 9:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player9Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 8:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 8:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 9:
        time.sleep(1)
        AI9(player9Name)

def AI9(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player9Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player9Deck)):
            card = player9Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player6Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 10:
                for x in range(2):
                    neemTwee2 = random.choice(allCards)
                    player10Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 9:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount >= 10:
                for x in range(4):
                    neemTwee2 = random.choice(allCards)
                    player10Deck.append(neemTwee2)
                    allCards.remove(neemTwee2)
            elif playerAmount == 9:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 9:
        time.sleep(1)
        beurtSpeler()
    elif playerAmount >= 10:
        time.sleep(1)
        AI10(player10Name)

def AI10(name):
    print(name,"is aan de beurt.")
    time.sleep(0.5)
    possible = []
    x = 0
    global Reverse
    if len(player10Deck) == 0:
        print("\n",name,"hebt geen kaarten meer over en daarmee heb je het spel gewonnen, gefeliciteerd!")
        exit()
    for i in range(len(player10Deck)):
            card = player10Deck[x]
            split = card.split(" ",1)
            split2 = pile[-1].split(" ",1)
            if split[0] == "Wild":
                possible.append(card)
                possibleR = random.choice(possible)
            if split[0] != "Wild":
                if split[0] == split2[0]:
                    possible.append(card)
                    possibleR = random.choice(possible)
                if split[-1] == split2[-1]:
                    possible.append(card)
                    possibleR = random.choice(possible)
            x+=1
    if len(possible) == 0:
        player6Deck.append(random.choice(allCards))
        print(name,"heeft een kaart gepakt.")
    elif len(possible) > 0:
        print(name, "heeft",possibleR,"gespeeld.")
        pile.append(possibleR)
        posSplit = possibleR.split(" ",1)
        if posSplit[-1] == "neem-twee":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount == 10:
                for x in range(2):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
        elif posSplit[-1] == "neem-vier":
            print(name,"heeft neem-twee opgelegd, de volgende speler krijgt dus 2 kaarten")
            if playerAmount == 10:
                for x in range(4):
                    neemTwee = random.choice(allCards)
                    MainPlayerDeck.append(neemTwee)
                    allCards.remove(neemTwee)
    if playerAmount == 10:
        time.sleep(1)
        beurtSpeler()
        

def namen():
    print("\nHallo",username,", je speelt vandaag tegen:")
    if playerAmount== 2:
        print(player2Name)
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
        
# def canPlay(colour, value, playerHand):
#     for card in playerHand:
#         if "Wild" in card:
#             return True
#         elif colour in card or value in card:
#             return
#     return False    

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
namen()

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


playing = True
pile.append(random.choice(allCards))
beurtSpeler()
while playing == True:
    for i in range(playerAmount):
        if i == 0:
            if len(MainPlayerDeck) == 0:
                gewonnen(username)
                playing = False
        elif i == 1:
            if len(player2Deck) == 0:
                gewonnen(player2Name)
                playing = False
        elif i == 2:
            if len(player3Deck) == 0:
                gewonnen(player3Name)
                playing = False
        elif i == 3:
            if len(player4Deck) == 0:
                gewonnen(player4Name)
                playing = False
        elif i == 4:
            if len(player5Deck) == 0:
                gewonnen(player5Name)
                playing = False
        elif i == 5:
            if len(player6Deck) == 0:
                gewonnen(player6Name)
                playing = False
        elif i == 6:
            if len(player7Deck) == 0:
                gewonnen(player7Name)
                playing = False
        elif i == 7:
            if len(player8Deck) == 0:
                gewonnen(player8Name)
                playing = False
        elif i == 8:
            if len(player9Deck) == 0:
                gewonnen(player9Name)
                playing = False
        elif i == 9:
            if len(player10Deck) == 0:
                gewonnen(player10Name)
                playing = False
        else:
            print("")