#Game of Hangman

import random
from words import words
#import string to use string.ascii_uppercase constants
import string

#check if the random word choice is valid, if it contains ' ' or '-' then 
#computer has to choose again
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#hangman processes
def hangman():
    #using get_valid_word to check if word from words is valid and stores in
    word = get_valid_word(words)
    #make all the letters in the word a set
    word_letters = set(word)
    #creates the string of uppercase ascii letters into a set and stores in alphabet
    alphabet = set(string.ascii_uppercase)
    #letters already guessed by the user
    used_letters = set()

    lives = 10

    #gets user input
    #while the length of the word and lives is greater than zero
    while len(word_letters) > 0 and lives > 0:
        #each loop, updates lives and used letters
        print('You have ', lives, 'lives left and You have guessed these letters: ', ' '.join(used_letters))
        #what the current word is, replace * with guessed letter (ie: W * R D)
        #list of every letter users guessed, is shown, otherwise is a star
        word_list = [letter if letter in used_letters else '*' for letter in word]
        #put togther all letter with space using join 
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Current word: ',' '.join(word_list))

        #gets user input and convert to upper case
        user_letter = input('Guess a letter: ').upper()
        #if user_letter is a valid character in the alphabet that haven't been used
        if user_letter in alphabet - used_letters:
            #add user_letter to used letters
            used_letters.add(user_letter)
            #and if user guess correctly
            if user_letter in word_letters:
                #remove user letter in word letter
                #which keeps track of all the letters in word
                #word letter will decrease in size
                word_letters.remove(user_letter)
                #print('')
            else:
                #if wrong, life - 1
                lives -= 1
                print("\nYou letter,", user_letter, 'is not in the word. Guess again!')
        
        #checks if letter has already been entered
        elif user_letter in used_letters:
            print("You have already used this letter! Guess again")

        #means character just entered is not in the alphabet
        else:
            print("Invalid character! Guess again")
    
    if lives == 0:
        print('Sorry, you lost! The word was: ', word)

    print('Yay! you won! The word was: ', word)

if __name__ == '__main__':
    hangman()