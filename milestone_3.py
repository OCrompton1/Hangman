import random
word_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
word = random.choice(word_list)
def ask_for_input():
    while True:
        guess = input("Enter a single letter \n")
        if len(guess) == 1 and guess.isalpha() == True:
            break   
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)  
 
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
ask_for_input()