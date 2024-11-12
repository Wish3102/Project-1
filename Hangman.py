import random  # Importing the random module to randomly select a word for the game

class Hangman:
    def __init__(self):
        # Initializes the game by setting up the word, guessed status, and other attributes
        self.word = self.get_word().upper()  # Randomly selects and stores the word to guess, in uppercase
        self.word_completion = "_" * len(self.word)  # Represents the word with underscores for each letter
        self.guessed = False  # Boolean to check if the word has been guessed
        self.guessed_letters = []  # List to store letters guessed by the player
        self.guessed_words = []  # List to store whole words guessed by the player
        self.tries = 6  # Number of tries or attempts the player has

    def get_word(self):
        # Chooses a random word from a predefined list of words
        words = ["python", "hangman", "computer", "programming", "artificial", "intelligence"]
        return random.choice(words)  # Randomly selects and returns one word

    def display_hangman(self):
        # Displays the hangman figure based on the number of tries left
        stages = [
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            --------
            """,  # 6 tries remaining
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            --------
            """,  # 5 tries remaining
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            --------
            """,  # 4 tries remaining
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            --------
            """,  # 3 tries remaining
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            --------
            """,  # 2 tries remaining
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            --------
            """,  # 1 try remaining
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            --------
            """  # 0 tries left, no figure
        ]
        return stages[self.tries]  # Returns the current hangman stage based on remaining tries

    def play(self):
        # Main function to run the game loop
        print("Let's play Hangman!")
        print(self.display_hangman())
        print(self.word_completion)  # Displays initial state of the word (all underscores)
        print("\n")

        # Game loop: continues until word is guessed or tries run out
        while not self.guessed and self.tries > 0:
            guess = input("Please guess a letter or word: ").upper()  # Get input and convert to uppercase
            if len(guess) == 1 and guess.isalpha():  # If guess is a single letter
                if guess in self.guessed_letters:
                    print("You already guessed the letter", guess)  # Already guessed this letter
                elif guess not in self.word:
                    print(guess, "is not in the word.")  # Letter is not in the word
                    self.tries -= 1  # Lose a try
                    self.guessed_letters.append(guess)  # Add to guessed letters
                else:
                    print("Good job!", guess, "is in the word!")  # Letter is in the word
                    self.guessed_letters.append(guess)
                    word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess  # Update word completion with guessed letter
                    self.word_completion = "".join(word_as_list)
                    if "_" not in self.word_completion:
                        self.guessed = True  # All letters guessed
            elif len(guess) == len(self.word) and guess.isalpha():  # If guess is a full word
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)  # Already guessed this word
                elif guess != self.word:
                    print(guess, "is not the word.")  # Incorrect word guess
                    self.tries -= 1  # Lose a try
                    self.guessed_words.append(guess)  # Add to guessed words
                else:
                    self.guessed = True  # Correct word guess
                    self.word_completion = self.word
            else:
                print("Not a valid guess.")  # Invalid input

            # Display current hangman state and word completion status
            print(self.display_hangman())
            print(self.word_completion)
            print("\n")

        # Outcome message based on game result
        if self.guessed:
            print("Congrats! You guessed the word:", self.word, "You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + self.word + ". Better luck next time!")

if __name__ == "__main__":
    game = Hangman()  # Create an instance of the Hangman class
    game.play()  # Start the game by calling the play method
