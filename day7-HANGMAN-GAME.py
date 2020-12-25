#HANGMAN
import random
display = []
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
for j in range(len(chosen_word)):
    display.append("_")
