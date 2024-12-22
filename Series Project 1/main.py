
from random import randint

'''
Plan Is Very Sime :
    Allow User To Set The Numbers Of Dot
    Allow User To Randomly Rool A Dice
    Tip:
        Use Ai For Better User Experiance
'''

def roll_dice():
    return randint(1, 6)
def add_dot():
    user_choice = int(input("Enter The Number Of Dots: "))
    if(user_choice>=7):
        print("You Cannot Print More Than 6 Dots Beacause Dice Have Only 6 Dots")
    else:
        for i in range(user_choice):
            print("*", end=" ")
def print_dice_pattern(number):
    patterns = {
        1: ["     ", "  *  ", "     "],
        2: ["*    ", "     ", "    *"],
        3: ["*    ", "  *  ", "    *"],
        4: ["*   *", "     ", "*   *"],
        5: ["*   *", "  *  ", "*   *"],
        6: ["*   *", "*   *", "*   *"]
    }
    for line in patterns[number]:
        print(line)

def add_dot():
    user_choice = int(input("Enter The Number Of Dots: "))
    if user_choice < 1 or user_choice > 6:
        print("You Cannot Print More Than 6 Dots Because Dice Have Only 6 Dots")
    else:
        print_dice_pattern(user_choice)
def main():
    print("Welcome To The Dice Simulator")
    print("1. Roll The Dice")
    print("2. Add Dots")
    user_choice = int(input("Enter Your Choice: "))
    if(user_choice == 1):
        print("Dice Number Is: ", roll_dice())
    elif(user_choice == 2):
        add_dot()
    else:
        print("Invalid Choice")
    try_again = input("Do You Want To Try Again (y/n): ")
    if(try_again == 'y'):
        main()
    else:
        print("Thanks For Using The Dice Simulator")
main()
