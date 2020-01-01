no = 13    # The no to be guessed
i = 1   # For running the loop
ch = 9  # No of chances
print("\nGuess Game\nThe no is between 1 - 20.\nYou will have 9 chances to guess the no correctly")    # Info

# Starting of th loop
while i<10:
    guess = int(input("\nEnter your guess no = "))    # Taking guessed no from the user as input

    # Matching the input with the no and displaying the result accordingly
    if (guess<no):
        print("You are below the no please think of some higher no...!!")
        i += 1    # Increment for the loop
        ch -= 1   # Decrement of the choice by 1
        
        # Checking whether more chance is left or not
        if (ch == 0):
            print("\nGAME OVER...!!\nYou dont have any more chances\nYou Loose")
        
        else:
            print("You are left with ", ch, " Chances")
            
    elif (guess>no):
        print("You are higher than the no please think of some smaller no...!!")
        i += 1    # Increment for the loop
        ch -= 1   # Decrement of the choice by 1

        # Checking whether more chance is left or not
        if (ch == 0):
            print("\nGAME OVER...!!\nYou dont have any more chances\nYou Loose")
                    
        else:
            print("You are left with ", ch, " Chances")
    
    # If user guessed corectly then this will be displayed
    else:
        print("Well done you guessed the no correctly in ", i, " Chances")
        break
