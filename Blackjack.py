import random
import math

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]
random.shuffle(cards)

playerCards = []
botCards = []

playerCards.append(cards.pop(0))
botCards.append(cards.pop(0))
playerCards.append(cards.pop(0))

def stats():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| Bot cards: {}".format(botCards))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| Your cards: {}".format(playerCards))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
stats()

choice = input("Do you want to hit or stay?\n")
if choice == "hit":
    playerCards.append(cards.pop(0))
    botCards.append(cards.pop(0))
    stats()
    if sum(botCards) < 17:
        botCards.append(cards.pop(0))
    

    
if choice == "stay":
    botCards.append(cards.pop(0))
    if sum(botCards) < 17:
        botCards.append(cards.pop(0))
    
























'''
if choice == "hit":
    playerCards.append(cards.pop(0))
    botCards.append(cards.pop(0))
    stats()
    if sum(playerCards) > 21:
        print("You LOST!")
    if sum(botCards) > 21:
        print("You WON!")
    if sum(playerCards) > sum(botCards):
        if sum(playerCards) <= 21:
            print ("You WON!")
        elif sum(botCards) > sum(playerCards):
            if sum(botCards) <= 21:
                print ("You LOST!")
 
elif choice == "stay":
    if sum(botCards) <= 12:
        botCards.append(cards.pop(0))
    stats()
    if sum(botCards) < sum(playerCards):
        print("You won!")
'''