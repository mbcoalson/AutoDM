import random

def randmoney(lvl):
    
    basevalue = 1

    upper_plat = random.randint(0, 5 if lvl>3 else 0)
    upper_gold = random.randint(0, 50)
    upper_silver = random.randint(0, 100)
    upper_copper = random.randint(0, 500)
    
    n_plat = random.randint(0, basevalue*upper_plat*lvl)
    n_gold = random.randint(0, basevalue*upper_gold*lvl)
    n_silver = random.randint(0, basevalue*upper_silver*lvl)
    n_copper = random.randint(0, basevalue*upper_copper*lvl)
     

    print("{}pp, {}gp, {}sp, {}cp".format(n_plat, n_gold, n_silver, n_copper))  