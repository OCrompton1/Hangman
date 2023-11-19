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
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for character in range(len(self.word)):
                if guess == self.word[character]:
                    self.word_guessed[character] = guess
            self.num_letters = self.num_letters - 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives = self.num_lives -1
            print(f"You have {self.num_lives} lives left")
                
    def ask_for_input(self, guess):
        while True:
            guess = input("Enter a single letter \n")
            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")   
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.extend(guess)
                print(self.word_guessed)
                
                break
            
            
def play_game(word_list):
    num_lives = 5
    guess = str()
    game = Hangman(word_list)    
    while True:
        if game.num_lives == 0: 
            print("You lost!")
            break
        elif game.num_letters > 0: 
            game.ask_for_input(guess)
        else:
            print("Congratulations. You won the game!")
            break
play_game(['apple', 'banana', 'cherry', 'date', 'elderberry'])