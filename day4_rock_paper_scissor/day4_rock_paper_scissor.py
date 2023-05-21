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
done = False
while not done:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors | Press 3 to quit:"))
    computer_choice = random.randint(0,2)
    if user_input == 0:
        print(rock,"\n")
        print(f"Computer chose {computer_choice}: \n")
        if computer_choice == 0:
            print(rock,"\n Draw!")
        elif computer_choice ==1:
            print(paper, "\n You Lost!")
        elif computer_choice ==2:
            print(scissors, "\n You Won!")
    elif user_input == 1:
        print(paper, "\n")
        print(f"Computer chose {computer_choice}: \n")
        if computer_choice == 0:
            print(rock,"\n You Won!")
        elif computer_choice ==1:
            print(paper, "\n Draw!")
        elif computer_choice ==2:
            print(scissors, "\n You Lost!")
    elif user_input ==2:
        print(scissors, "\n")
        print(f"Computer chose {computer_choice}: \n")
        if computer_choice == 0:
            print(rock,"\n You Lost!")
        elif computer_choice ==1:
            print(paper, "\n You Win!")
        elif computer_choice ==2:
            print(scissors, "\n Draw!")
    elif user_input==3:
        print("Thanks for playing the rockpaperscissors game!")
        done = True
    else:
        print("Please make a valid entry!")
