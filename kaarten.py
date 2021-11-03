import random
#kaarten.py

#Het deck bestaat uit 4 “kleuren” (harten, klaveren, schoppen & ruiten)
#Iedere kleur heeft 13 kaarten (2 t/m 10, een boer, een vrouw, een heer en een aas) ook 2 jokers
kaarten = ["kaart 1", "kaart 2", "kaart 3", "kaart 4", "kaart 5", "kaart 6", "kaart 7"]
harten = ["harten boer " , "harten vrouw" , "harten heer" , "harten aas" , "harten 2" , "harten 3", "harten 4", "harten 5", "harten 6", "harten 7", "harten 8", "harten 9", "harten 10"]
klaveren = ["klaveren boer", "klaveren vrouw" , "klaveren heer", "klaveren aas" , "klaveren 2" , "klaveren 3", "klaveren 4", "klaveren 5", "klaveren 6", "klaveren 7", "klaveren 8", "klaveren 9", "klaveren 10"]
schoppen = ["schoppen boer", "schoppen vrouw", "schoppen heer", "schoppen aas" , "schoppen 2" , "schoppen 3", "schoppen 4", "schoppen 5", "schoppen 6", "schoppen 7", "schoppen 8", "schoppen 9", "schoppen 10"]
ruiten = ["ruiten boer", "ruiten vrouw", "ruiten heer", "ruiten aas" , "ruiten 2" , "ruiten 3", "ruiten 4", "ruiten 5", "ruiten 6", "ruiten 7", "ruiten 8", "ruiten 9", "ruiten 10"]
spelKaarten = harten + klaveren + schoppen + ruiten + ["joker", "joker"]

random.choices(spelKaarten, k=7)

for item_a, item_b in zip(kaarten, random.choices(spelKaarten, k=7)):
    print(item_a + ":", item_b)
print("\ndeck:" , spelKaarten)