
secret_word = "pizza"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):#CHANGING THE VALUE OF A KEY
    if guess_count < guess_limit:
        guess = input("Please enter a word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("SUCCESS!!")
else:
    print("Sorry, you are out of guesses.")

