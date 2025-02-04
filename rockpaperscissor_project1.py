# SCISSORS_GAME
# RUles
# Rock wins agaimst scisssor
# scissor wins against paper
# paper wins against rock
# 0 for rock
# 1 for paper 
# 2 for scissor

import random
rock = '''
     --------
----     ------)
        (------)
        (------)
        (-----)
 ----   (---)
    '''

paper = '''
    --------
--- ----)----
      -----)
     -------)
     -------)'
  ---- -----)
  '''
scissors = '''
   ------
--- ----)----
     ----)
  ---------)
  (----)
---(---)
'''
game_images = [rock,paper,scissors]
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper,2 for Scissor.:"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number, You loose.")
else:  
    print(game_images[user_choice])   
    computer_choice = random.randint(0,2)
    print("Computer Choose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's Draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you loose")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")   
    elif computer_choice > user_choice:
        print("You Loose.")
    elif user_choice > computer_choice:
        print("You Win")



















