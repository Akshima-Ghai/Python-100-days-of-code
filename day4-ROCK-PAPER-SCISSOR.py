#ROCK PAPER SCISSOR

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player1 = int(input("What do you choose ? 0 for Rock , 1 for Paper , 2 for scissors"))
rock_paper_scissors = [rock , paper , scissors]
player1_move = rock_paper_scissors[player1]
print(player1_move)

player2 = random.randint(0,2)
player2_move = rock_paper_scissors[player2]
print(player2_move)

if player1_move==player2_move:
    print("Draw , Try Again")
elif player1_move == rock:
    if player2_move == scissors:
        print("You Win")
    elif player2_move == paper:
        print("You Lose")
elif player1_move == paper:
    if player2_move == rock:
        print("You Win")
    elif player2_move == scissors:
        print("You Lose")
elif player1_move == scissors:
    if player2_move == paper:
        print("You Win ")
    elif player2_move == rock:
        print("You Lose")
