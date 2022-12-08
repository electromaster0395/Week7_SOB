import random

def formatNumber(num):
        if(len(num) < 4):
            num = "0"*(4-len(num)) + num
            print(num)
        return num
        
def compare_numbers(number, user_guess):
    ## your code here
    cow = 0
    bull = 0
    for i in range(0, len(number)):
        if(number[i] == user_guess[i]):
            bull += 1

    cow = 4-bull
    
    return cow, bull

playing = True #gotta play the game
number = formatNumber(str(random.randint(0,9999))) #random 4 digit number
print(number)
guesses = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while True:
    user_guess = formatNumber(input("Give me your best guess!"))
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
