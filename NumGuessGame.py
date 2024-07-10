import random

number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
  print("You guessed correctly!")

while guess != number:
  if guess < number:
    print("Your guess was too low. Try again.")
    guess = int(input("Guess a number between 1 and 10: "))
  elif guess > number:
    print("Your guess was too high. Try again.")
    guess = int(input("Guess a number between 1 and 10: "))