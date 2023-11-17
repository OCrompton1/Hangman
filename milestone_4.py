import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for char in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word")
            for character in range(len(self.word)):
                if self.guess == self.word[character]:
                    self.word_guessed[character] = character
            self.num_letters = self.num_letters - 1
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            self.num_lives = self.num_lives -1
            print(f"You have {self.num_lives} left")
                
    def ask_for_input(self, guess):
        while True:
            self.guess = input("Enter a single letter \n")
            if len(self.guess) != 1 or self.guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")   
            elif self.guess in self.list_of_guesses == True:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.extend(self.guess)

x = Hangman(["apple", "banana", "cherry", "date", "elderberry"])               
x.ask_for_input(x)        
