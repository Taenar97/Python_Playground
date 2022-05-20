import random

print("What is your name?")
name = input()

print("Hello ", name, "! Nice to meet you.")
print("I'm thinking of a number between 1 and 20. Can you guess it?")

number = random.randint(1,20)

number_of_guesses = 1
while number_of_guesses <= 6:
    print("Your guess: ")
    guess = int(input())
    if guess == number:
        print("Yay, you guessed right! You needed ", number_of_guesses, " trys.")
        quit()
    elif guess < number:
        print("You guessed too low. Try again!")
        number_of_guesses += 1
    elif guess > number:
        print("You guessed too high. Try again!")
        number_of_guesses += 1 

print("I'm sorry but you only had 6 guesses!")  