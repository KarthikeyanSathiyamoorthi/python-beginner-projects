import random
from words import randomWords
import string

# get a valid word in randomWords
def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list
    while '-' in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(randomWords)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #string.acii gives the english 26 letters
    used_letters=set() # what the user has gussed
   
    lives = 6

    # getting the user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        # ' '.join(['a', 'b', 'c', 'd']) --> 'a b cd'
        print('You have',lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: # this if condition checks the user_letter is in alphabet but not in used letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
               word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter isn't in word.")
        elif user_letter in used_letters:
            print("you have already used that character. please try again! ")
    
        else:
          print("Invalid character. Please try again!")

    # gets here when len(word_letters) == 0 and lives == 0
    if lives == 0:
       print("You died sorry. The word was ", word)
    else:
        print("You guessed the word ", word, '[]')

hangman()
