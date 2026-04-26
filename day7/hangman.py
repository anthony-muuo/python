# hangman game
import random

hangman_pics = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',]

word_list = ["mouse", "baboon", "camel"]

# randomly choose a word form the word list

chosen_word = random.choice(word_list)
print(chosen_word)

#empthy display to add the letter
display = []
word_length = len(chosen_word)

lives = 6


# display dashes
for _ in range(word_length):
    display += '_'


#while loop to make the game continue
end_game = False
while not end_game:
    # user to guess the letter
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # check if the letter guessed is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # wrong guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, That's not in the word. You lose a life")
        lives -= 1
    # current state
    print(" ".join(display))
    print(hangman_pics[lives])

    if lives ==0:
        end_game = True
        print("You Lose!")

    if "_" not in display:
        end_game = True
        print("You Win!")
