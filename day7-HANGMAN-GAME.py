#HANGMAN
import random
display = []
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
for j in range(len(chosen_word)):
    display.append("_")

guess = input("Guess a letter : ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter==guess:
        display[position] = letter


print(display)
