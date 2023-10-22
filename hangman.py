import random
from hangman_words import *
from hangman_art import *

chosen_word = random.choice(word_list)

print(logo)

#create a blank space in list
display = []
chosen_word_length = len(chosen_word)

for _ in range(chosen_word_length):
    display += "_"

end_of_game = False

lifes = 6

used_letters = []

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    
    if guess in display:
        print(display)
    else:
        used_letters.append(guess)
        lifes -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Lifes: {lifes}. Used letters {used_letters}.\n- - - - - -\n{stages[lifes]}")
    
    if "_" not in display and lifes != 0:
        end_of_game = True
        print(f"You win!\n{congrats}")
    elif "_" in display and lifes == 0:
        print(f"You lose.\nThe correct answer was {chosen_word}.")
        end_of_game = True

