import random

def get_hint(secret_word, guess):
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append('_')
    return ' '.join(hint)

def main():
    secret_word = "vaniele"  
    word_length = len(secret_word)
    
    print("Welcome to the word guessing game!")
    print("Your hint is: " + '_ ' * word_length)

    guess_count = 0

    while True:
        guess = input("What is your guess? ").strip().lower()
        guess_count += 1
        
        if len(guess) != word_length:
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed it!")
            print(f"It took you {guess_count} guesses.")
            break

        hint = get_hint(secret_word, guess)
        print("Your hint is: " + hint)

if __name__ == "__main__":
    main()