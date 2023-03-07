import random

print("Welcome to Guess My Number")

# Create a secret number a random number between 1 and 100
secret_number = random.randint(1, 100)
# print("During development cheat", secret_number)
# print(f"During development cheat.  ans {secret_number}")

# Create a guess counter variable set to 0
counter = 0

# Within the loop:
#   Ask the user to guess a number (input)
#   Increment the guess counter by 1
#   If the guessed number was higher than the secret number
#     Tell the user "Too High"
#   If the guessed number was lower than the secret number
#     Tell the user "Too Low"
#   If the guess is correct then exit the loop
#     break

while True:
    guess = int(input("Guess a number: "))
    # counter = counter + 1
    counter += 1
    # if guess > secret_number:
    #     print("Too High")
    # if guess < secret_number:
    #     print("Too Low")
    # if guess == secret_number:
    #     break

    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        break

# Tell the user how many guesses they used.
print(f"Great job.  You guessed it in {counter} guesses.")
