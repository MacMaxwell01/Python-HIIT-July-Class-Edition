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
game_images = [rock, paper, scissors]

users_input = int(input("Input 0 for rock, 1 for paper and 2 for scissors\n"))
if users_input >= 3 or users_input < 0:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[users_input])
pc_select = random.randint(0,2)
print("computer chose")
print(game_images[pc_select])

if users_input >= 3 or users_input < 0:
    print("You typed an invalid number. You lose")
elif users_input == 0 and pc_select == 2 :
    print("You Wins!")
elif pc_select == 0 and users_input == 2 :
    print("You Loose!")
elif pc_select > users_input :
    print("You Lose!")
elif users_input > pc_select:
    print("You Win!")
elif users_input == pc_select:
    print("It's a tie!")
else:
    print("You typed an invalid number. You lose")