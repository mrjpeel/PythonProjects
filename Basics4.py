'''Programs help us do human things, but faster.
We use then to solve human problems.'''


def timesTable(multi): # def defines a FUNCTION called timesTable and uses 7
    answer = []     #LIST
    for numberOftimes in range(1,13): # sets up a FOR loop 1 to 12
        answer.append(numberOftimes * multi) # PRINTS out item * 7
    return answer


# Takes an integer as input and makes it a number
multi = int(input('''Please enter a number\n''')) # if i input 7 here

answer = timesTable(multi) # Calls the FUNCTION with multi as an argument
# So this is the same as saying timesTable(7)
print('For the number ' + str(multi) + ' The table is')
print(answer)   # How could we format the output of this better?














'''By we need to think about what we are changing
sometimes we want to only change a value for a
specific need or answer.  Consider this.'''

#SUPERHERO WORLD
def superHero(mortal):

    if(mortal == "Clark"):
        mortal = "\nSuperman"
        print("Clark will become...", mortal)
        # USING RETURN I can give the information to the main program
        # This is even though the mortal variable is LOCAL to this FUNCTION
        return mortal
    elif(mortal == "Bruce"):
        mortal = "\nBatman"
        print("Bruce will become...", mortal)
        # For BATMAN I don't have a RETURN, so I can't give back
        # information to my main program
    else:
        print("\n\nYour mortal is unknown\n\n")

# REAL WORLD
getMortal = input("\n\nPlease enter the mortal name of a superhero \n")
gotHero = superHero(getMortal)
print("Your mortal was", getMortal)
print("Your super hero is", gotHero)