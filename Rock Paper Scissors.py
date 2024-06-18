import random

print("Welcome to rock paper scissor game!")
while True:
    
    user_choice=int(input("Enter choice:Type 0 for rock,1 for papeer,2 for scissors:"))
    
    if user_choice >= 3 or user_choice < 0:
        print("You entered invalid numbre,You lose.")
    
    else:
        computer_choice=random.randint(0,2)
        print("compuuter choose:")
        print(computer_choice)

        if (computer_choice == user_choice):
            print("It's a tie")

        elif computer_choice > user_choice:
            print("you lose")

        elif user_choice > computer_choice:
            print("you win")

        elif computer_choice == 0  and user_choice==2:
            print("you lose")

        elif computer_choice==2 and user_choice==0:
            print("you win")

    print("\n")
    print("1) Play Again")
    print("2) Quit")
    user_choice=int(input("Enter choice:"))

    if(user_choice==2):
        break
                  
