#blackjack
import random
#deck of cards
playerIn = True
dealerIn = True
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 
       'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card) 

def total(turn):
    total = 0
    faceCard = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in faceCard:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

def revealDealerHand():
    if len(dealerHand) == 2:
          return dealerHand[0]
    elif len(dealerHand) > 2:
          return dealerHand[0], dealerHand[1]

for _ in range(2):
     dealCards(dealerHand)
     dealCards(playerHand)

while playerIn or dealerIn:
    print(f'Dealer has {revealDealerHand()} and X')
    print(f'You have {playerHand} for a total of {total(playerHand)}')

    if playerIn:
        hitOrStay = input('1: Hit\n2: Stay\n')    
    if total(dealerHand) >= 17:
        dealerIn = False
    else:
        dealCards(dealerHand)
    if hitOrStay == '1':
        dealCards(playerHand)
    else:
        playerIn = False
    
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print('BlackJack! You Win! =)')
elif total(dealerHand) == 21:
    print(f'Dealer has the cards {dealerHand}\nDealer has BlackJack!\nDealer Wins!')
elif total(playerHand) > 21:
    print(f'Your hand {playerHand} has a total of {total(playerHand)}\n You bust! Dealer Wins!')
elif total(dealerHand) > 21:
    print(f'Dealers hand {dealerHand} has a total of {total(dealerHand)}\n Dealer busts! You Win!')
elif total(playerHand) > total(dealerHand):#player wins since closer to 21
    print(dealerHand)
    print(f'Youre hand: {total(playerHand)} is greater than dealers {total(dealerHand)}.\n You Win!')
elif total(playerHand) < total(dealerHand):#dealer wins since closer to 21
    print(dealerHand)
    print(f'Youre hand: {total(playerHand)} is less than dealers {total(dealerHand)}.\n Dealer Wins!')
else: #tie
    print(f'Dealer hand: {dealerHand}')
    print(f'Your hand: {playerHand}')
    print('Push!')
        

