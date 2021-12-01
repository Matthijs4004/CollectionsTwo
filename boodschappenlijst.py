

boodschap = 0
itemList = []
itemDict = {}

while boodschap == 0:
    item = input("Welk product heeft u nodig? ")
    qty = int(input("Hoeveel "+ item +" heeft u nodig? "))
    for i in range(qty):
        if not item in itemDict:
            itemDict[item] = 1
        else:
            itemDict[item] += 1
    print(itemDict)
    
    question = input("Wil je nog iets op het boodschappenlijstje zetten? ").lower()
    if question == "nee":
        print("\nDit is uw boodschappenlijstje:\n" + str(itemDict))
        break