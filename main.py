import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  a = random.choice(cards)
  return a


user_cards = []
computer_cards = []

def ge21():
  
  if sum(user_cards) == 21:
    return 0
  elif sum(computer_cards) == 21:
    return 1
  elif sum(user_cards) > 21:
    return 100

def ge212():
  
  if sum(user_cards) == 21:
    print("You win 😁")
  elif sum(computer_cards) == 21:
    print("You Lose ☹")
  elif sum(user_cards) > 21:
    print("You Lose ☹")

def ace():
  
  for card in user_cards:
    if card == 11 and sum(user_cards) > 21:
      user_cards.remove(11)
      user_cards.append(1)

  for card in computer_cards:
    if card == 11 and sum(computer_cards) > 21:
      computer_cards. remove(11)
      computer_cards.append(1)

def yes():
  
  b3 = deal_card()
  user_cards.append(b3)
  ace()
  print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}")

  b4 = deal_card()
  computer_cards.append(b4)
  ace()
  
  if sum(user_cards) >= 21 or sum(computer_cards) >= 21:
    ge212()
  else:
    print(f"Computer's first card: {computer_cards[0]}")
    x = input("Type 'y' to get another card, type 'n' to pass: ")
    yorn(x)

def no():
  
  print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
  
  while(sum(computer_cards) <= 17):
    b5 = deal_card()
    computer_cards.append(b5)

  print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
  
  if sum(user_cards) > sum(computer_cards):
    print("You win 😁")
  elif sum(user_cards) < sum(computer_cards) and sum(computer_cards) <= 21:
    print("You Lose ☹")
  elif sum(computer_cards) > 21:
    print("You win 😁")
  else :
    print("Draw")

def yorn(x):
  if x == 'y':
    yes()
  else:
    no()

def calculate_score(cards):
  for i in range(0,2):
    b1 = deal_card()
    b2 = deal_card()
    user_cards.append(b1)
    computer_cards.append(b2)
  
  if sum(user_cards) > 21 or sum(computer_cards) > 21:
    ace()
  
  print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}")
  print(f"Computer's first card: {computer_cards[0]}")

  s = ge21()
  return s


x = 'y'

score1 = calculate_score(cards)
if score1 == 0:
  print("You win 😁")
elif score1 == 1 or score1 == 100:
  print("You Lose ☹")
else:
  x = input("Type 'y' to get another card, type 'n' to pass: ")
  yorn(x)
