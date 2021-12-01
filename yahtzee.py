import random

i = 5
opgeslagen = []
beurt = 0
saving = 0
score = 0
sScore = 0
EenList = []
TweeList = []
DrieList = []
VierList = []
VijfList = []
ZesList = []
FourOfAKindList = []
ThreeOfAKindList = []
FullHouseList = []
SmallStraightList = []
LargeStraightList = []
ChanceList = []
YahtzeeList = []


def roll():
    global beurt
    global i
    global dobbelstenen
    dobbelstenen = []
    while beurt < 3:
        for x in range(i):
            nummer = random.randint(1,6)
            dobbelstenen.append(nummer)
        print("Dit zijn uw dobbelstenen:", dobbelstenen)
        save()

def save():
    global beurt
    global i
    global saving
    while saving < 3:
        opslaan = input("Welke stenen wilt u opzij leggen? (12345/stop) ")
        if opslaan == "1":
            opgeslagen.append(dobbelstenen[0])
            i -= 1
        elif opslaan == "2":
            opgeslagen.append(dobbelstenen[1])
            i -= 1
        elif opslaan == "3":
            opgeslagen.append(dobbelstenen[2])
            i -= 1
        elif opslaan == "4":
            opgeslagen.append(dobbelstenen[3])
            i -= 1
        elif opslaan == "5":
            opgeslagen.append(dobbelstenen[4])
            i -= 1
        elif opslaan == "stop":
            beurt += 1
            saving += 1
            if saving < 3:
                print("U heeft gekozen om opnieuw te rollen. Dit zijn uw opgeslagen dobbelstenen:",opgeslagen)
                roll()
            else:
                keuzes()
        else:
            print("Niet geldig, probeer opnieuw")
            save()


def keuzes():
    global score
    print("Alle opties: 'Een', 'Twee', 'Drie', 'Vier', 'Vijf', 'Zes', 'ThreeOfAKind', 'FourOfAKind', 'FullHouse', 'SmallStraight', 'LargeStraight', 'Chance' and 'Yathzee'")
    question = input("Welke categorie wil je "+ str(opgeslagen)+ " in opslaan? ")
    if question == "Een":
        EenList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*EenList,1),"punten")
        score += sScore
        print("Je score is:",score)
        roll()
    if question == "Twee":
        TweeList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*TweeList,2),"punten")
        score += sScore
        print("Je score is:",score)
    if question == "Drie":
        DrieList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*DrieList,3),"punten")
        score += sScore
        print("Je score is:",score)
    if question == "Vier":
        VierList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*VierList,4),"punten")
        score += sScore
        print("Je score is:",score)
    if question == "Vijf":
        VijfList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*VijfList,5),"punten")
        score += sScore
        print("Je score is:",score)
    if question == "Zes":
        ZesList.append(opgeslagen)
        print("Je krijgt",checkSingleValues(*ZesList,6),"punten")
        score += sScore
        print("Je score is:",score)
    if question == "ThreeOfAKind":
        ThreeOfAKindList.append(opgeslagen)
        if checkThreeOfAKind(*ThreeOfAKindList) == True:
            print("Je hebt ThreeOfAKind! +"+str(sum(*ThreeOfAKindList))+" punten")
            score += sum(*ThreeOfAKindList)
            print("Je score is:",score)
        else:
            print("Je hebt geen ThreeOfAKind, probeer opnieuw.")
            keuzes()
    if question == "FourOfAKind":
        FourOfAKindList.append(opgeslagen)
        if checkFourOfAKind(*FourOfAKindList) == True:
            print("Je hebt FourOfAKind! +"+str(sum(*FourOfAKindList))+" punten")
            score += sum(*FourOfAKindList)
            print("Je score is:",score)
        else:
            print("Je hebt geen FourOfAKind, probeer opnieuw.")
            keuzes()
    if question == "FullHouse":
        FullHouseList.append(opgeslagen)
        if checkFullHouse(*FullHouseList) == True:
            print("Je hebt FullHouse! +25 punten")
            score += 25
            print("Je score is:",score)
        else:
            print("Je hebt geen FullHouse, probeer opnieuw.")
            keuzes()
    if question == "SmallStraight":
        SmallStraightList.append(opgeslagen)
        if checkSmallStraight(*SmallStraightList) == True:
            print("Je hebt SmallStraight! +30 punten")
            score += 30
            print("Je score is:",score)
        else:
            print("Je hebt geen SmallStraight, probeer opnieuw.")
            keuzes()    
    if question == "LargeStraight":
        LargeStraightList.append(opgeslagen)
        if checkLargeStraight(*LargeStraightList) == True:
            print("Je hebt LargeStraight! +40 punten")
            score += 40
            print("Je score is:",score)
        else:
            print("Je hebt geen LargeStraight, probeer opnieuw.")
            keuzes()
    if question == "Chance":
        ChanceList.append(opgeslagen)
        print("Je hebt chance ingevuld, het totaal aantal van je dobbelstene wordt bij elkaar opgeteld en aan je score gevoegd.")
        print("Je krijgt "+str(sum(*ChanceList))+" punten erbij.")
        score += sum(*ChanceList)
        print("Je score is:",score)
    if question == "Yahtzee":
        YahtzeeList.append(opgeslagen)
        if checkYathzee(YahtzeeList) == True:
            print("Je hebt Yatzhee! +50 punten")
            score += 50
            print("Je score is:",score)
        else:
            print("Je hebt geen Yahtzee, probeer opnieuw.")
            keuzes()

def checkSingleValues(list,value):
    global sScore
    for die in list:
        if die == value:
            sScore += die
    return sScore
    
def checkYathzee(list):
    if len(set(*list)) == 1:
        return True
    return False

def checkFourOfAKind(FourOfAKindList):
    FourOfAKindList.sort()
    if FourOfAKindList[0] == FourOfAKindList[3] or FourOfAKindList[1] == FourOfAKindList[4]:
        return True
    return False

def checkThreeOfAKind(ThreeOfAKindList):
    ThreeOfAKindList.sort()
    if ThreeOfAKindList[0] == ThreeOfAKindList[2] or ThreeOfAKindList[1] == ThreeOfAKindList[3] or ThreeOfAKindList[2] == ThreeOfAKindList[4]:
        return True
    return False

def checkFullHouse(FullHouseList):
    FullHouseList.sort()
    if (len(set(FullHouseList))) != 2:
        return False
    elif FullHouseList[0] != FullHouseList[3] and FullHouseList[1] != FullHouseList[4]:
        return True
    return False

def checkLargeStraight(LargeStraightList):
    LargeStraightList.sort()
    if len(set(LargeStraightList)) == 5 and LargeStraightList[4] == 6 and LargeStraightList[0] == 2:
        return True
    elif len(set(LargeStraightList)) == 5 and LargeStraightList[4] == 5 and LargeStraightList[0] == 1:
        return
    return False

def checkSmallStraight(SmallStraightList):
    SmallStraightList.sort()
    if len(set(SmallStraightList)) == 4 and SmallStraightList[0] == 1 and SmallStraightList[4] == 4:
        return True
    elif len(set(SmallStraightList)) == 4 and SmallStraightList[0] == 2 and SmallStraightList[4] == 5:
        return True
    elif len(set(SmallStraightList)) == 4 and SmallStraightList[0] == 3 and SmallStraightList[4] == 6:
        return True
    return False

roll()