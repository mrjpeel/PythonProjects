from turtle import *

prev = 0
start = 1
fibno = 1
sqs = input("How many Squares do you want? ")
for i in range(int(sqs)):
    # Show numbers to make sure things are correct...
    print(str(i) + ". " + str(fibno))

    # Draw a square
    color('red')
    for f in range(6):
        forward(5 * fibno)
        if f < 5: right(90)

    # Sort out numbers
    fibno = start + prev
    prev = start
    start = fibno