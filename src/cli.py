import argparse
import random
from . import loot
from . import equip

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--partylevel", type=int)
    args = parser.parse_args()
    print(args.partylevel)

    loot.randmoney(args.partylevel)
    equip.randweapon(args.partylevel)