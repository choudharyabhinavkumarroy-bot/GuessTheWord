stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]
word_list = ["aardvark","baboon","camel"]

# ToDo 1

import random
# crate a variable called "lives" to keep track of the number of lives left.
# set "lives" equal to 6
lives = 6






choosen_word = random.choice(word_list)
print(choosen_word)

# create a "placeholder" with the same number of blanks as the choosen_word
placeholde = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholde += "_"
print(placeholde)


# use a while loop to let the user guess again
game_over = False
correct_letter =[]

while not game_over:

    # ToDo 2
    guess =input("Guess the letter:").lower()
    print(guess)

    # Create a "display" that puts the guess letter in the right position and _ in the rest of the string.

    display =""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    # If guess is not a letter in the chosen_word, Then reduce "lives" by 1.
    # If lives goes down to 0 then the game should stop and it should print "Your lose"
    if guess not in choosen_word:
        lives -=1
        if lives ==0:
            game_over = True
            print("Your lose")

    

    if "_" not in display:
        game_over = True
        print("You win.")





# ToDo 3
for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


# print ASCII art from stage
    print(stages[lives])