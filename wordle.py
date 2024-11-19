
import random

class WordleGame:
    def __init__(self):
        self.words = self.load_words()
        self.target_word = random.choice(self.words).upper()
        self.max_attempts = 6

    def load_words(self):
        # Load a predefined list of words or use a file to import words
        return ["APPLE", "BERRY", "CHERRY", "MANGO", "PEACH", "PLUM", "GRAPE"]

    def validate_word(self, word):
        # Validate the word exists in the word list
        return word.upper() in self.words

    def evaluate_guess(self, guess):
        # Check the guess against the target word and provide feedback
        feedback = []
        guess = guess.upper()
        for i in range(len(self.target_word)):
            if guess[i] == self.target_word[i]:
                feedback.append("🟩")  # Correct letter in correct position
            elif guess[i] in self.target_word:
                feedback.append("🟨")  # Correct letter in wrong position
            else:
                feedback.append("⬜")  # Incorrect letter
        return "".join(feedback)

    def play(self):
        print("Welcome to Wordle!")
        print(f"You have {self.max_attempts} attempts to guess the 5-letter word.")

        attempts = 0
        while attempts < self.max_attempts:
            guess = input("Enter your guess: ").strip()
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid input. Enter a 5-letter word.")
                continue

            if not self.validate_word(guess):
                print("Word not in the list. Try again.")
                continue

            attempts += 1
            feedback = self.evaluate_guess(guess)
            print(f"Attempt {attempts}: {feedback}")

            if guess.upper() == self.target_word:
                print("🎉 Congratulations! You guessed the word!")
                break
        else:
            print(f"Game over! The correct word was {self.target_word}.")

if __name__ == "__main__":
    game = WordleGame()
    game.play()
