#This is a dice simulator on a computer

import random

#These are the numbers on the dice
Numbers_Of_Dice = [1, 2, 3, 4, 5, 6]

#This is the function of rolling the dice
while True:
    Dice_Rolling = input("Do you want to roll the dice: ")
    Output = random.choice(Numbers_Of_Dice)
    if Dice_Rolling.lower() == "yes":
        print(Output)
    elif Dice_Rolling.lower() == "no":
        break
    else:
        print("Please enter a valid choice")