import random

def randweapon(lvl):
    weapons = ["long sword", "short sword", "mace", "dagger", "long bow", "short bow", "cross bow", "hand crossbow"]
    adj = ["rusty", "silvered", "ornate", "chipped", "orcish", "elvish", "busted"]
    selectedadj = random.choice(adj)
    selectedweapon = random.choice(weapons)

    aword = "a"

    if selectedadj[0] in ["a", "e", "i", "o", "u"]:
        aword = "an"


    print("You found {} {} {}!".format(aword, selectedadj, selectedweapon))
     