import random

words = ["apple", "mango", "tiger", "chair", "python"]

word = random.choice(words)
guess_word = ""
chance = 6

while chance > 0:
    for ch in word:
        if ch in guess_word:
            print(ch, end=" ")
        else:
            print("_", end=" ")

    print()
    letter = input("Guess a letter: ").lower()

    if letter in word:
        guess_word += letter
        print("Correct guess!")
    else:
        chance -= 1
        print("Wrong guess! Chances left:", chance)

    if all(ch in guess_word for ch in word):
        print("You Win!")
        break

if chance == 0:
    print("Game Over!")
    print("Correct word was:", word)