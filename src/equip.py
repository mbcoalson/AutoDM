import random

def randweapon(lvl, magictype = None):
    weapons = ["long sword", "short sword", "mace", "dagger", "long bow", "short bow", "cross bow", "hand crossbow"]
    adj = ["rusty", "silvered", "ornate", "chipped", "orcish", "elvish", "busted"]
    selectedadj = random.choice(adj)
    selectedweapon = random.choice(weapons)

    aword = "a"

    if selectedadj[0] in ["a", "e", "i", "o", "u"]:
        aword = "an"

    if magictype is not None:
        magiceffect = randmagiceffect(magictype)
        print("You found {} {} {}, with the following {} effect: {}!".format(aword, selectedadj, selectedweapon, magictype, magiceffect))

    else:
        print("You found {} {} {}!".format(aword, selectedadj, selectedweapon))  

def randmagiceffect(magictype):
    if magictype == "bonus":
        return random.choice(["+1 fire damage", "+2 cold damage"])
    elif magictype == "cursed":
        return "max hp drain -1"
    else:
        return None


