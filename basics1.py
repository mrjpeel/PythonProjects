__author__ = 'MrPeel'

# the line below uses the variable __author__
print('hello how are you?', __author__)

# below we will create a variable with a data structure
animals = ['mouse', 'cat', 'dog', 'pig', 'cow', 'chicken']
print('I want the animal: dog')
print(animals[2])
print(animals[0])
# data structures start with a 0 to count
# we use square brackets to indicate the index position of the value we want
print(animals)
joiner = '; '
print(joiner.join(animals))
# .join is when it prints the variable without the square brackets and between each list or string it adds the chosen character (e.g. ;)
# it is formating the string so it looks presentable to the reader
# .joins the contents of a list together and makes it look presentable

# .join is one of many METHODS.
# METHODS are special functions that work with an individual object

sentence = 'ask not what your country can do for you ask what you can do for your country'
print(sentence[18:25])
print(sentence[30:33])
print(sentence[41:77])
print(sentence[0:40])
# using [] we can find just part of our variable
print(sentence[41:])
print(sentence[:40])
# leaving part of the range out means that it will assume that you mean everything up to that point or everything after that point
words = sentence.split()
print(words[4])
# the use of the method .split allows us to break up a variable into different parts and put these in a list



myStr = "this is a sentence,"

# Change the text of a string
print(myStr.upper())
print(myStr.lower())

# Find part of a string
print(myStr.find("is"))  # This will give the answer 2

print(myStr, myStr[:10] + 'donkey')  # This will change the part of the sentence

myStr2 = "carrot"

print(myStr, myStr[:10] + myStr2)  # Use one variable to change the content of another variable

myStr3 = "That's great! \nYour Score is "  # let's print over more lines
myScore = str(123)
# \n means NEW LINE

print(myStr3[:-1] + " " + myScore)
print(myStr3[:-15] + myScore)  # SEE HOW THIS GETS RID OF LINE TWO

# To get a response from someone we use INPUT
myQuestion = input("Who are you?")
# what the USER types in is what myQuestion becomes
# Their INPUT is ASSIGNED to the variable
print(myQuestion)  # The answer will be what you type in!

newInput = int(input("Please enter a number between 1 and 10"))
nextInput = int(input("Please enter another number between 10 and 20"))
maths = newInput * nextInput
print(maths)