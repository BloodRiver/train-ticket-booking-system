from random import randint
from time import sleep

computer_choice = randint(1, 3)

options = ["Rock", "Paper", "Scissors"]

print("1. Rock")
print("2. Paper")
print("3. Scissors")
user_choice = int(input("Enter your choice: "))


# sleep(number_of_seconds) causes the program to freeze for given number of seconds

print("Rock")
sleep(1)
print("Paper")
sleep(1)
print("Scissor")
sleep(1)

print("You chose:", options[user_choice - 1])
sleep(1)
print("Computer chose:", options[computer_choice - 1])
sleep(1)

'''
if user_choice == 1:  # Rock
    if computer_choice == 1:  # Rock
        print("Draw")
    elif computer_choice == 2:  # Paper
        print("Computer Wins")
    else:  # Scissors
        print("You win")
elif user_choice == 2:  # Paper
    if computer_choice == 1:  # Rock
        print("You win")
    elif computer_choice == 2:  # Paper
        print("Draw")
    else:  # Scissors
        print("Computer Wins")
elif user_choice == 3: # Scissors
    if computer_choice == 1:  # Rock
        print("Computer Wins")
    elif computer_choice == 2:  # Paper
        print("You win")
    else:  # Scissors
        print("Draw")
'''

if (user_choice == computer_choice):
    print("Draw")
elif ((user_choice - computer_choice) == 1) or ((computer_choice - user_choice) == 2):
    print("You win")
elif ((computer_choice - user_choice) == 1) or ((user_choice - computer_choice) == 2):
    print("Computer Wins")
