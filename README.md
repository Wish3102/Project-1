# Hangman Game in Python

A console-based Hangman game implemented in Python, featuring object-oriented design for modularity and clarity. This game randomly selects a word from a predefined list and challenges the player to guess it, letter by letter or by the full word, with a limited number of attempts.

## Features
- **Random Word Selection**: Each game session starts with a randomly chosen word.
- **Hangman Stages Display**: Visual representation of the Hangman figure, updating with each incorrect guess.
- **User Input Handling**: Accepts both single-letter and full-word guesses, with input validation and feedback for duplicate or invalid guesses.
- **Victory and Loss Conditions**: The game ends with either a congratulatory message or a reveal of the word after all tries are used.

## How to Play
1. Run the game from the command line.
2. Guess letters or the entire word.
3. For each incorrect guess, one try is deducted, and the Hangman figure is updated.
4. Win by guessing all letters or the full word before running out of tries.

## Code Structure

- **Class Structure**: The game is encapsulated within a `Hangman` class, which organizes the game's state and methods.
- **Methods**:
  - `get_word()`: Selects a word at random from a predefined list.
  - `display_hangman()`: Displays the hangman figure based on remaining tries.
  - `play()`: Main game loop, handles input, guess checking, and updating game state.

## Usage
To start the game, run the following command in a terminal:
```bash
python hangman.py
