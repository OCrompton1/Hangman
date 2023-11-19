import random
class Hangman:
    '''
    This class is used to represent a game of Hangman.
   
    Attributes:
        word_list (list): Contains list of words to be used in the game of Hangman.
        num_lives (int): Number of livesthe user has. Default value is 5.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # The list of words that can be used in the game.
        self.num_lives = num_lives # The number of lives the user has.
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list.
        self.word_guessed = ["_" for char in self.word] # Contains a list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(set(self.word)) # The number of unique letters in the word that have not been guessed yet.
        self.list_of_guesses = [] # A list of the guesses that have been tried.
    def check_guess(self, guess):
        '''
        This method checks whether the user's guess is a letter in the word

        Args:
            guess (str): The user's guess for a letter in the word
        '''
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
        '''
        This method allows the user to input a guess and calls check_guess(guess) to check if the letter is contained in the word.
        It also checks that the guess was valid (a single alphabetical character).
        
        Args:
            guess (str): The user's guess for a letter in the word
        
        '''
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
    # This function pulls class methods together with conditions to simulate the game.
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