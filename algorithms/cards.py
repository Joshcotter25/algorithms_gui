import random

def create_deck():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def fisher_yates_shuffle(deck):
    a = deck[:]
    for i in range(len(a) - 1, 0, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a