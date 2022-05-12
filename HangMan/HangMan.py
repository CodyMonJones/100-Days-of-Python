import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["Cat", "Dog", "Mouse", "Bird", "Moose"]
blanks_list = []

#grabs a random word from the list and determines length
word_to_guess = random.choice(word_list).lower()
word_length = len(word_to_guess)

#creates guess blanks for words
for _ in range(word_length):
    blanks_list.append("_")

#main game function
number_of_guesses = 6
winner = False
while not winner:
    print(stages[number_of_guesses])
    print(blanks_list)
    print(f"Guesses left: {number_of_guesses}")
    user_letter = input("Guess a letter: ").lower()

    if user_letter not in word_to_guess:
        number_of_guesses -= 1
    else:    
        for position in range(word_length):
            letter = word_to_guess[position]
            if user_letter == letter:
                blanks_list[position] = letter
    
    if number_of_guesses == 0:
        winner = True
        print(f"{stages[number_of_guesses]}\n {number_of_guesses} guesses left the word was {word_to_guess}. Sorry you lose")
    elif "_" not in blanks_list:
        winner = True
        print(f"Congratulations you win! The word was {word_to_guess}!")
        break