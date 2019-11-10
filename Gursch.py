import random
h1=1; h2=2; h3=3; h4=4; h5=5; h6=6; h7=7; h8=8; h9=9; h10=10; hJ=11; hQ=12; hK=13; hA=14
cards = [h1,h2,h3,h4,h5,h6,h7,h8,h8,h10,hJ,hQ,"hK","hA","d1","d2","d3","d4","d5","d6","d7","d8","d9","d10","dJ","dQ","dK","dA","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","sJ","sQ","sK","sA","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","cJ","cQ","cK","cA"]
playerHand = []
botHand = []
takenCards = []
revealedCardsByPlayer = []
revealedCardsByBot = []

def cardDealing():
    deal2player1position = random.randint(1,len(cards))
    deal2bot1position = random.randint(1,len(cards))

    deal2player1 = cards[deal2player1position]
    deal2bot1 = cards[deal2bot1position]

    playerHand.append(deal2player1)
    botHand.append(deal2bot1)

    cards.pop(deal2player1position)
    cards.pop(deal2bot1position)

    takenCards.append(deal2player1)
    takenCards.append(deal2bot1)

cardDealing()
cardDealing()
cardDealing()
cardDealing()
cardDealing()

print ("You have {}".format(playerHand))
print ("Bot has {}".format(botHand))

revealedCardsByPlayer.append(playerHand[4])
revealedCardsByBot.append(botHand[4])



'''
if revealedCardsByPlayer > revealedCardsByBot:
    print("You start! ")
elif revealedCardsByBot > revealedCardsByPlayer:
    print("The bot begins!")
'''