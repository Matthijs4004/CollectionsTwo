import random

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

nameList = ["Justin Case", "Error404","average_student","minecraftkid2013","lucifer_morningstar","supermario420","PeppaPig", "NoLifer", "MarkZuckerberg","BillGates","MyNameJeffBezos","MarkRutteOpFiets","Swagman","Steve","Alex"]

# KaartenLijst = {
# "blauw" : 19, 
# "groene": 19,
# "rode": 19,
# "gele": 19,
# "neem-twee rood": 2,
# "neem-twee geel": 2,
# "neem-twee blauw": 2,
# "neem-twee groen": 2,
# "Uno reverse rood": 2,
# "Uno reverse blauw": 2,
# "Uno reverse groen": 2,
# "Uno reverse geel": 2,
# "Skip rood": 2,
# "Skip geel": 2,
# "Skip blauw": 2,
# "Skip groen": 2,
# "KeuzeKaart": 4,
# "Neem-4": 4
# }

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
print("\nHallo",username,", vandaag speel je UNO tegen")
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