from art import logo
from random import choice
def return_total(deck):
  total = 0
  for c in deck:
    total += c
  return total
def win_announce(a,b,c):
  if a == "C":
    print(f"Winner is Computer, user card: {user_card}, Computer cards: {computer_card}")
  elif a == "U":
    print(f"Winner is User, user card: {user_card}, Computer cards: {computer_card}")
  elif a== "D":
    print(f"DRAW, user card: {user_card}, Computer cards: {computer_card}")
  
def decide_winner(u_card,c_card):
  if return_total(u_card) > return_total(c_card):
    return "U"
  elif return_total(u_card) < return_total(c_card):
    return "C"
  else:
    return "D"


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ur_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if ur_choice == "y":
  print(logo) 
  user_card =[choice(cards), choice(cards)]
  computer_card = [choice(cards), choice(cards)]
  winner = ""
  print(f"Your cards: {user_card}")
  print(f"Computer's first card: {computer_card}")
  winner = ""
  if 11 in user_card and 10 in user_card:
    if 11 in computer_card and 10 in computer_card:
      print("Both having BLACKJACK...Draw...U: {user_card} and C: {computer_card}")
    else:
      print("You having BLACKJACK...You win...U: {user_card} and C: {computer_card}")
  elif 11 in computer_card and 10 in computer_card:
    print("Computer having BLACKJACK...Computer wins...U: {user_card} and C: {computer_card}")
  else:
    print("Rest  code goes here")
    loop1 = True
    while loop1:
      if(return_total(user_card) > 21):
        print(f"user card > 21: U : {user_card}")
        if 11 in user_card:
          print(f"11 in user card: U : {user_card}")
          user_card[user_card.index(11)] = 1
          print(f"User card after replacing11 with 1: U : {user_card}")
          if (return_total(user_card) > 21):
            print(f"User card after replacing11 with 1 > 21: u : {user_card}")
            winner = "C"
            loop1 = False 
          else:
            print(f"User card after replacing11 with 1 < 21: u : {user_card}")
            ch = input("'y' for Hit, 'n' for stand: ").lower()
            if ch == "y":
              loop1 = True
              user_card.append(choice(cards))
              print(f"User card after adding new card 1 : u : {user_card}")
            else:
              loop1 = False
              print(f"User card : u : {user_card}")
        else:
          winner = "C"
          loop1 = False 
      else:
        ch = input("'y' for Hit, 'n' for stand: ").lower()
        if ch == "y":
          loop1 = True
          user_card.append(choice(cards))
          print(f"User card after adding new card 2 : u : {user_card}")
        else:
          loop1 = False
          print(f"User card : u : {user_card}")
    #callCompPLay for 17
    if winner != "":
      win_announce(winner,user_card,computer_card)
    else:
      loop2 = True
      while loop2:
        if  return_total(computer_card) < 17:
          next_card = choice(cards)
          print(f"NC:{next_card}")
          if next_card == 11:
            if return_total(computer_card)+next_card > 21:
              computer_card.append(1)
            elif return_total(computer_card)+next_card == 21:
              computer_card.append(next_card)
              win_announce("C",user_card,computer_card)
              loop2=False
          else:
            if return_total(computer_card)+next_card < 21:
              computer_card.append(next_card)
            else:
              computer_card.append(next_card)
              win_announce("U",user_card,computer_card)
              loop2=False
        else:
          winner = decide_winner(user_card,computer_card)
          win_announce(winner,user_card,computer_card)
          loop2=False
 

else:
  print("Bye...")

