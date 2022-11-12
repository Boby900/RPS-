import random
quit = False
computer_score=0
your_score=0

while quit == False:
    choices= ["rock","paper","scissor"]
    user_input= input("choose rock,paper,scissor or quit\n").lower()
    computer_input= random.choice(choices)
    
    if user_input == "quit":
        print("you ended the game")
        print(f"your total score is {your_score}"+" and "+f"computer total score is {computer_score}")
        quit=True
        if computer_score < your_score:
            print("You Won 🏆🏆🏆")
        elif computer_score> your_score:
            print("computer won 😭😭")
        else:
            print("match tie")
    elif user_input == "rock":
        if computer_input == "rock":
            print("computer input is rock")
            print("your input is also rock")
            print("it is tie")
        elif computer_input =="scissor":
            print("computer input is scissor")
            print("your input is rock")
            print("you won")
            your_score+=1
        elif computer_input =="paper":
            print("computer input is paper")
            print("your input is rock")
            print("computer won")
            computer_score+=1
    elif user_input == "paper":
        if computer_input == "paper":
            print("computer input is paper")
            print("your input is also paper")
            print("it is tie")
        elif computer_input =="scissor":
            print("computer input is scissor")
            print("your input is paper")
            print("computer won")
            computer_score+=1
        elif computer_input =="rock":
            print("computer input is rock")
            print("your input is paper")
            print("you won")
            your_score+=1
    elif user_input == "scissor":
        if computer_input == "scissor":
            print("computer input is scissor")
            print("your input is also scissor")
            print("it is tie")
        elif computer_input =="rock":
            print("computer input is rock")
            print("your input is scissor")
            print("computer won")
            computer_score+=1
        elif computer_input =="paper":
            print("computer input is paper")
            print("your input is scissor")
            print("you won")
            your_score+=1
    elif user_input != "rock" or user_input !="scissor" or user_input !="paper":
        print("Invalid input")                