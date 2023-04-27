#blackjack
import random

def playerBalanceIfWin(playerMoney, bet):  
    playerMoney += bet
    print(f'Your Balance is now: {playerMoney}')
    

    
def playerBalanceIfLose(playerMoney, bet):
    playerMoney -= bet
    print(f'Your Balance is now: {playerMoney}')




def dealCards(turn, deck):
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

def revealDealerHand(dealerHand):
    if len(dealerHand) == 2:
          return dealerHand[0]
    elif len(dealerHand) > 2:
          return dealerHand[0], dealerHand[1]



def playerInputCards(playerHand, dealerHand, deck):
    playerIn = True
    dealerIn = True
    while playerIn or dealerIn:

        print(f'Dealer has {revealDealerHand(dealerHand)} and X')
        print(f'You have {playerHand} for a total of {total(playerHand)}')

        if playerIn:
            hitOrStay = input('1: Hit\n2: Stay\n')    
        if total(dealerHand) >= 17:
            dealerIn = False
        else:
            dealCards(dealerHand, deck)
        if hitOrStay == '1':
            dealCards(playerHand, deck)
        else:
            playerIn = False
        
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break
        
def whoWon(playerMoney, playerHand, dealerHand, bet):
    if total(playerHand) == 21:
        print('BlackJack! You Win! =)')
        playerBalanceIfWin(playerMoney, bet)


    elif total(dealerHand) == 21:
        print(f'Dealer has the cards {dealerHand}\nDealer has BlackJack!\nDealer Wins!')
        playerBalanceIfLose(playerMoney, bet)
        print(playerMoney)

    elif total(playerHand) > 21:
        print(f'Your hand {playerHand} has a total of {total(playerHand)}\nYou bust! Dealer Wins!')
        playerBalanceIfLose(playerMoney, bet)
   

    elif total(dealerHand) > 21:
        print(f'You have {playerHand} \nDealers hand {dealerHand} has a total of {total(dealerHand)}\nDealer busts! You Win!')
        playerBalanceIfWin(playerMoney, bet)


    elif total(playerHand) > total(dealerHand):#player wins since closer to 21
        print(dealerHand)
        print(f'Youre hand: {total(playerHand)} is greater than dealers {total(dealerHand)}.\nYou Win!')
        playerBalanceIfWin(playerMoney, bet)
  

    elif total(playerHand) < total(dealerHand):#dealer wins since closer to 21
        print(dealerHand)
        print(f'Youre hand: {total(playerHand)} is less than dealers {total(dealerHand)}.\nDealer Wins!')
        playerBalanceIfLose(playerMoney, bet)
       

    else: #tie
        print(f'Dealer hand: {dealerHand}')
        print(f'Your hand: {playerHand}')
        print('Push!')
        playerBalanceIfLose(playerMoney, bet)        

def main():
    playerMoney = 100
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 
        'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']
    playerHand = []
    dealerHand = []
    turn = []
    print(f'Current Balance: {playerMoney}')
    bet = int(input('Bet Amount: \n'))
    if bet > playerMoney:
        print(f'Bet of {bet} is greater than your {playerMoney} balance.\nTry again.')
        bet = int(input('Bet Amount: \n'))
    elif bet <= 0:
        print(f'Bet of {bet} is invalid\nTry again')
        bet = int(input('Bet Amount: \n'))

    total(turn)
    revealDealerHand(dealerHand)
    for _ in range(2):
        dealCards(dealerHand, deck)
        dealCards(playerHand, deck)
    playerInputCards(playerHand, dealerHand, deck)
    whoWon(playerMoney, playerHand, dealerHand, bet)



main()
