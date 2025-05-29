import random
from hangmanstages import stages
from hangmanwords import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Press enter a letter ").lower()

    # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word: For User Display.
    placeholder = ""
    for position in range(len(chosen_word)):
        placeholder = placeholder + "_"
    print(placeholder)    

    #TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    display = ""
    if guess in chosen_word:
        correct_letters.append(guess)
    
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)      

    if guess in correct_letters:
        print(f"You already guessed {guess} that letter.")
        

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Lives left: {lives}")
        if lives == 0:
            print("You lose!. The word was:", chosen_word)
            game_over = True      

    if "_" not in display:
        print("You win!")
        game_over = True

    print(stages[lives])    