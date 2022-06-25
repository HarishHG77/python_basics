import random
number=random.randint(1, 10)
player_name=input("hello,what's your name?\n")
number_of_guesses = 0
print("okay! "+ player_name+  " I am gueesing a number between 1 and 10:")
print("enter your guess")

while number_of_guesses < 5:
    guess=int(input())
    number_of_guesses += 1
    if guess < number:
        print("your guess is too low")
    if guess > number:
        print("your guess is too high")
    if guess == number:
        break
if guess == number:
        print("you guessed correct number in" +str(number_of_guesses)+  "tries")
else:
        print("you did not guess the number,the number is"+str(number))