from random import randint

def get_user():
    print('The min and max possibilities are 2 and 12')
    user_choice = int(input("Enter your choice: "))
    if (user_choice<=12 and user_choice>=2):
        return user_choice
    else:
        print("Enter valid number")
        get_user()

def get_computer():
    computer_choice = randint(2,12)
    return computer_choice

def choose( user_choice=get_user(),computer_choice=get_computer() ):
    print("You choose: %d" %user_choice)
    print("Opp choose: %d" %computer_choice)
    if user_choice == computer_choice:
        print("Wow! you got it right")
    else:
        print("Beteer luck nxt time")

choose()