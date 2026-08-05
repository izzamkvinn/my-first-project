import random

target_number = random.randint(1, 100)
attempts = 0

print("🎮 Guess the secret number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too low! Try higher.")
    elif guess > target_number:
        print("Too high! Try lower.")
    else:
        print(f"🎉 Spot on! You guessed it in {attempts} tries.")
        break