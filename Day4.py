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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice = int(input())
if user_choice >= 3:
    print("Number must be lower than 3")
else:
    cpu_choice = random.randint(0, 2)
    print(game_images[user_choice])
    print("Computer chose:\n")
    print(game_images[cpu_choice])

    if user_choice == 2 and cpu_choice == 0:
        print("Computer wins!")
    elif user_choice == 0 and cpu_choice == 2:
        print("You win!")
    elif user_choice > cpu_choice:
        print("You win!")
    elif user_choice < cpu_choice:
        print("Computer wins!")
    else:
        print("Draw!")                

