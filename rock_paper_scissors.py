#define list
options = ["r", "p", "s"]

#tell computer to make a random selection
import random
computer_choice = (random.choice(options))

#tell user to make a selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

#compare selection to user input

#define rules
#rock beats scissors
#paper beats rock
#scissors beats paper
#rock ties rock, paper ties paper, scissors ties scissors

if user_choice == "r" and computer_choice == "s":
    print("Computer chose Scissors, User Wins")
elif user_choice == "r" and computer_choice == "p":
    print("Computer chose Paper, Computer Wins")
elif user_choice == "r" and computer_choice == "r":
    print("No winner Try again")
elif user_choice == "p" and computer_choice == "r":
    print("Computer chose Rock, User Wins")
elif user_choice == "p" and computer_choice == "s":
    print("Computer chose Scissors, Computer Wins")
elif user_choice == "p" and computer_choice == "p":
    print("No Winner Try again")
elif user_choice == "s" and computer_choice == "p":
    print("Computer chose Paper, User Wins")
elif user_choice == "s" and computer_choice == "r":
    print("Computer chose Rock, Computer Wins")
elif user_choice == "s" and computer_choice == "s":
    print("No Winner Try again")
elif user_choice != "r" or "p" or "s":
    print("Must select r, p, or s")

User_choice = input("Do you want to go again? (Y)es or (N)o")
for y()


