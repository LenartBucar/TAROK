import random
import argparse
import time
# from tqdm import trange

start=time.time()

def divide_cards(deck):
    return [deck[n*12:(n+1)*12] for n in range(4)]


def check_legal(players):
    return all((min(p) < 22 for p in players))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cycles', help='How many cycles to do? ', type=int)
    args = parser.parse_args()
    valid = 0
    n = 54
    # t = trange(1, args.cycles+1)
    deck = list(range(1, n+1))
    for x in t:
        random.shuffle(deck)
        if check_legal(divide_cards(deck)):
            valid += 1
        if x%100 == 0:
            t.set_postfix(valid=valid*100/x, invalid=(x-valid)*100/x)
    print("\n\nKONEC")
    print("Legalnih je bilo {}% rok.".format((valid*100/args.cycles)))
    print("Nelegalnih je bilo {}% rok.".format((args.cycles-valid)*100/args.cycles))
    print("Porabljen cas: " + str((time.time() - start)))

if __name__ == '__main__':
    main()
