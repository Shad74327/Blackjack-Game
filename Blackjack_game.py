import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
dealer = [] 
user.append(random.choice(cards))
print(f"Your first hand is {user[0]}")
dealer.append(random.choice(cards))
print(f"Dealer's first hand is {dealer[0]}")
user.append(random.choice(cards))
print(f"Your second hand is {user[1]}")
dealer.append(random.choice(cards))


should_continue = True

def final_result(user, dealer):
  user_score = sum(user)
  dealer_score = sum(dealer)

  print(f"Your total score is {user_score}")
  print(f"Dealer's total score is {dealer_score}")

def operation(user, dealer, cards):
  draw_card = input("Do you want to draw another card? Type 'y' or 'n'> ")
  if draw_card=="y":
    user.append(random.choice(cards))
    print(f"You have {user}")
    return True
  elif draw_card=="n":
    while sum(dealer)<17:
      dealer.append(random.choice(cards))
      
      
    if sum(dealer)>21:
      final_result(user, dealer)
      print("You win.")
      return False
      
    else: 
      if sum(user)>sum(dealer):
        final_result(user, dealer)
        print("You win.")
        return False
        
      elif sum(user)<sum(dealer):
        final_result(user, dealer)
        print("You lose.")
        return False
        
      else:
        final_result(user, dealer)
        print("Draw.")
        return False
        
  
while should_continue:
  
  if sum(user)==21:
    final_result(user, dealer)
    print("Blackjack! You win.")
    should_continue=False
  elif sum(dealer)==21:
    final_result(user, dealer)
    print("You lose.")
    should_continue=False
  else:
    if sum(user)>21:
      if 11 in user:
        for i in range(len(user)):
          if user[i]==11:
            user[i]=1
        if sum(user)>21:
          final_result(user, dealer)
          print("You lose.")
          should_continue=False
        else:
          should_continue=operation(user,dealer, cards)


      else:
        final_result(user, dealer)
        print("You lose.")
        should_continue=False
        
    else:
      should_continue=operation(user, dealer, cards)