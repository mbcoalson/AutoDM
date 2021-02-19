import argparse
import random
from . import loot
from . import equip

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--partylevel", type=int, default = 1)
    parser.add_argument("cmd")
    args = parser.parse_args()

    if args.cmd == "loot":
        loot.randmoney(args.partylevel)
    elif args.cmd == "weapon":
        equip.randweapon(args.partylevel)
    elif args.cmd == "magicweapon":
        equip.randweapon(args.partylevel, random.choice(["bonus", "cursed"]))
    else:
        print("Invalid option.")