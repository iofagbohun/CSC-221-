import arcade
import random

# Variables
miles_traveled = 0
thirst = 0
camel_tiredness = 0
native_traveled = -20
canteen = 3


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    get_input()


def get_input(native_traveled=-20, camel_tiredness=0, miles_traveled = 0, thirst = 1):
    done = False
    while not done:
        natives_behind = miles_traveled - native_traveled
        fullspeed = random.randrange(10, 21)
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("what is your choice? ")
        if user_choice.upper() == 'Q':
            print("thanks for playing")
            done = True
        # status check
        elif user_choice.upper() == "e":
            print("Miles traveled", miles_traveled)
            print("Drinks in canteen", canteen)
            print("your camel has", camel_tiredness, "amount of fatigue")
            print("The natives are", natives_behind, "miles behind you")
        # stop for the night
        elif user_choice.upper() == "d":
            camel_tiredness *= 0
            print("camel is happy")
            native_traveled += random.randrange(7, 15)
#moving full speed ahead
        elif user_choice.upper() == "c":
            print("you traveled ", fullspeed, "miles")
            miles_traveled += fullspeed
            thirst += 1
            camel_tiredness +=random.randrange(1,4)
            native_traveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)



main()
