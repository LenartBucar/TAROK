import random
import argparse
from tqdm import trange


def get_random_deck(n):
    cards = list(range(1, n+1))
    random.shuffle(cards)
    return cards



def divide_cards(deck):
    return [deck[n*12:(n+1)*12] for n in range(4)]


def check_legal(players):
    return all([min(p) < 22 for p in players])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cycles', help='How much cycles to do?', type=int)
    args = parser.parse_args()
    valid = 0
    t = trange(1, args.cycles+1)
    for x in t:
        if check_legal(divide_cards(get_random_deck(54))):
            valid += 1
        if x%10000 == 0 and x != args.cycles:
        #    print("\nSem pri partiji {}".format(x))
        #    print("Trenutno je bilo legalnih {}% rok.".format((valid*100/x)))
        #    print("Nelegalnih je bilo {}% rok.".format((100-(valid*100/x))))
            t.set_postfix(valid=valid*100/x, invalid=(x-valid)*100/x)
    print("\n\nKONEC")
    print("Legalnih je bilo {}% rok.".format((valid*100/args.cycles)))
    print("Nelegalnih je bilo {}% rok.".format((args.cycles-valid)*100/args.cycles))

if __name__ == '__main__':
    main()
