
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice using loops, conditionals, strings, and lists to create a complete interactive game.

## 📝 Tasks

### 🛠️	Create the Game Setup

#### Description
Create the initial game state by defining a list of possible words, choosing one word at random, and preparing the variables needed to run the game.

#### Requirements
Completed program should:

- Define a predefined list of words to choose from.
- Randomly select one word for the current game.
- Initialize the hidden word display using underscores (for example, `_ _ _ _`).
- Set a fixed number of incorrect guesses allowed.


### 🛠️	Implement the Guessing Loop

#### Description
Build the main loop that asks the player for letter guesses, updates game progress, and ends with a win or loss message.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only for incorrect guesses.
- End the game when the full word is guessed or no attempts remain.
- Display a clear win or lose message at the end of the game.
