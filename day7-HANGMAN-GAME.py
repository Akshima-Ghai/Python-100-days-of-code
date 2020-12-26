# HANGMAN

import random
import sys
import hangman_design
import hangman_word

print(hangman_design.logo)
display = []
lives = 6

chosen_word = random.choice(hangman_word.word_list)

for j in range(len(chosen_word)):
    display.append("_")
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        if lives == 0:
            end_of_game = True
            print("You Lose")
            print(f"The correct word was {chosen_word}")

        else:
            print(f"You guessed {guess} , that's not in a word . You lose a life. ")
            lives -= 1
            print(hangman_design.stages[lives])
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win.")
