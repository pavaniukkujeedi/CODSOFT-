import random
choices=["rock","paper","scissors"]
print("=== Rock Paper Scissors Game ===")
while True:
    user_choice=input("enter rock,paper,or scissors:").lower()
    if user_choice not in choices:
        print("invalid choice!please try again.")
        continue
    computer_choice=random.choice(choices)
    print("you choose:",user_choice)
    print("computer choose:",computer_choice)
    if user_choice ==computer_choice:
        print("Its's a Tie!")
    elif(user_choice =="rock" and computer_choice =="scissors") or\
    (user_choice =="paper" and computer_choice =="rock") or \
    (user_choice =="scissors" and computer_choice =="paper"):
        print("Congratulations! you win!")
    else:
        print("computer wins!")
    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
       print("thanks for playing!")
       break   
    