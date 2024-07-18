############### Blackjack Project #####################

import random
#random list ganerater 
def random_list(card):
  """its use for choice the random no 
  """
  choice_my = random.choice(card)
  
  
  return choice_my
  
#add the total 
def add_list(list):
  add_no = 0
  for x in list:
    add_no = x+add_no
  return add_no

def winner(my_total,com_total):
  if my_total > com_total and my_total < 22 and com_total < 22:
    if '11' in com_radom:    
      com_deck.remove(11)
      com_deck.append(1)
      com_total = add_list(com_deck)
      winner(my_total,com_total)
    return "you win"

  
  elif my_total < com_total and my_total < 22 and com_total < 22:
    if '11' in my_radom:    
      my_deck.remove(11)
      my_deck.append(1)
      my_total = add_list(my_deck)
      winner(my_total,com_total)
    return "you lose"

  
  elif my_total == com_total and my_total < 22 and com_total < 22:
    return "draw"
  else :
    if my_total > 21:
      if '11' in my_radom:
        my_deck.remove(11)
        my_deck.append(1)
        my_total = add_list(my_deck)
        winner(my_total,com_total)
      return "you lose"
  
# primary decks for both   
my_deck = [1,11,2,3,4,5,6,7,8,9,10,10,10,10]
com_deck = [1,11,2,3,4,5,6,7,8,9,10,10,10,10]

# score counter 
score_my =0
score_com = 0

my_radom = []
com_radom = []
# for loop for random choice
while score_my < 2:
  my_radom.append(random_list(my_deck))
  my_deck.remove(my_radom[score_my])
  com_radom.append(random_list(com_deck))
  com_deck.remove(com_radom[score_my])
  score_my+=1

score_my =0

print(my_radom) # list of my deck
print(com_radom)# list of com deck

# add the total
total_my = add_list(my_radom)
total_com = add_list(com_radom)


while total_com < 22 and total_my < 22:
  print("Do you want to add a cards?")
  choice = input("yes or no")
  if choice == "yes":
    my_radom.append(random_list(my_deck))
    my_deck.remove(my_radom[len(my_radom)-1])
    com_radom.append(random_list(com_deck))
    com_deck.remove(com_radom[len(com_radom)-1])
    total_my = add_list(my_radom)
    total_com = add_list(com_radom)
    print(f"the total of com  is {total_my} the total of my is {total_com}")
  else:
    break

print(winner(total_my,total_com))

print(my_radom) # list of my deck
print(com_radom)