import random  # finds the secret number
import sys     # exits program after the number guessing is successful
import time

print("-----------------------")
print("NUMBER GUESSING GAME")
print("-----------------------")

time.sleep(1)

secret_number = random.randint(1, 50)  # number stored in secret_number
max_attempts = 6
attempt_count = 0

print("\nI have chosen a number between 1 and 50.")
print("You have 6 attempts to guess it correctly.\n")

# creating a while loop which will keep running till 6 attempts
while attempt_count < max_attempts:
    attempt_count = attempt_count + 1
    remaining = max_attempts - attempt_count

    try:
        guess = int(input(f"[{attempt_count}/{max_attempts}] Enter guess: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")
        attempt_count -= 1  # Invalid input par attempt count nahi hoga
        continue
#used conditional statements(if,elif,else)
    if guess == secret_number:
        print("\n----------------------------------")
        print("CONGRATULATIONS! You guessed it right!")
        print(f"Correct number: {secret_number}")
        print(f"Total Attempts: {attempt_count}")
        print("----------------------------------")
        sys.exit()

    elif guess < secret_number:
        print("Too low! Try a higher number.")
        print(f"Remaining Attempts: {remaining}\n")

    else:
        print("Too high! Try a lower number.")
        print(f"Remaining Attempts: {remaining}\n")

    time.sleep(0.5)

print("GAME OVER! Out of attempts.")
print(f"The secret number was: {secret_number}")
print("----------------------------------") 
#here the game exits 
