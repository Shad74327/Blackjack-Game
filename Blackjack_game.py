import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = [random.choice(cards), random.choice(cards)] 
print(user)
dealer = [random.choice(cards), random.choice(cards)]
print(dealer)
should_continue = True

def operation(user, dealer, cards):
  draw_card = input("Do you want to draw another card? Type 'y' or 'n'> ")
  if draw_card=="y":
    user.append(random.choice(cards))
    print(user)
    return True
  elif draw_card=="n":
    while sum(dealer)<17:
      dealer.append(random.choice(cards))
      print(dealer)
    if sum(dealer)>21:
      print("You win.")
      return False
      
    else: 
      if sum(user)>sum(dealer):
        print("You win.")
        return False
        
      elif sum(user)<sum(dealer):
        print("You lose.")
        return False
        
      else:
        print("Draw.")
        return False
        
  
while should_continue:
  user_value = sum(user)
  dealer_value = sum(dealer)
  if user_value==21:
    print("Blackjack! You win.")
    should_continue=False
  elif dealer_value==21:
    print("You lose.")
    should_continue=False
  else:
    if user_value>21:
      if 11 in user:
        for i in range(len(user)):
          if user[i]==11:
            user[i]=1
        if sum(user)>21:
          print("You lose.")
          should_continue=False
        else:
          should_continue=operation(user,dealer, cards)


      else:
        print("You lose.")
        should_continue=False
        
    else:
      should_continue=operation(user, dealer, cards)