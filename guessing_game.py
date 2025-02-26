print("You will get 3 chances to guess the number ")
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You won!")
        break
    guess_count += 1
else:
    print("You failed!")