# This is a game: the computer "think" a random integer number which the user should find out in 6 guesses\
#  and there's a little help: the computer says if the guess number is too low or high.

import random  # import the module which implements pseudo-random number generators

guessesTaken = 0  # assign 0 to the variable guessesTaken

print('Hello! What is your name?')  # print the given parameters (string, included parenthesis) to console
myName = input()  # assign an input -that returns the string of characters you typed- to the variable myName

number = random.randint(1, 20)  # assign a random integer (between 1 and 20) to the variable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print the given parameters (strings and the value of variable myName) to console
while guessesTaken < 6:  # loop, repeatedly executes the target statements as long as the value of the variable guessesTaken is lower than 6
    print('Take a guess.')  # print the given paramethers (string, included parenthesis) to console (while guessesTaken < 6)
    guess = input()  # assign an input (returns the string of characters you typed) to the variable guess
    guess = int(guess)  # reassign the variable guess by converting its value to an integer

    guessesTaken += 1  # reassign the variable guessTaken by add number one to its previous value

    if guess < number:  # condition, if the value of left operand (guess) is lower than the value of right operand (number), it becomes true
        print('Your guess is too low.')  # if the condition above is true, the given paramethers (string) are printed to console

    if guess > number:  # condition, if the value of left operand (guess) is greater than the value of right operand (number), it becomes true
        print('Your guess is too high.')  # if the condition above is true, the given paramethers (string) are printed to console

    if guess == number:  # condition, if the values of two operands (guess and number) are equal, it becomes true
        break  # if the condition above is true, exit from the while loop

if guess == number:  # condition, when the values of two operands (guess and number) are equal, it becomes true
    guessesTaken = str(guessesTaken)  # if the above condition is true, reassign the variable guessTaken by converting its value to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print the given parameters (strings and the value of variable guessesTaken) to console

if guess != number:  # condition, when the values of two operands (guess and number) are NOT equal, the condition becomes true
    number = str(number)  # reassign the variable number by converting its value to string, if the condition above is true
    print('Nope. The number I was thinking of was ' + number)  # print the paramethers (strings, included parenthesis) to console
