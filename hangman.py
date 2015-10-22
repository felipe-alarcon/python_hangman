import random

'''**************************************************
*                                                   * 
* A small Hangman game written in python version 2.7*
*                                                   *  
**************************************************''' 


welcome = """
***********************************************************************************
* Hello, this game is to be played by one or two people.                          *
***********************************************************************************
"""
            
print welcome

file_object = open('words.txt', "r")

with file_object as word_list:
    words = word_list.read().split()
file_object.close()

words_length = len(words)

random_number = random.randint(0, words_length)

word = words[random_number]

word_split = list(word)

word_length = len(word_split)

print "The word you have to guess has", word_length, "characters"

word_stars = list("*" * word_length)

while True:
    
    guess = raw_input("\nGuess a character: ")[0].lower()
    
    guess_position = word.find(guess)
    
    indices = [i for i, x in enumerate(word_split) if x == guess]
    
    if guess_position == -1:
        print "character not found in word!"
    else:
        for i in indices:
            word_stars[i] = guess
    
    for i in word_stars:
        print i,
        
        
    guessed_word = ''.join(word_stars)
    
    if guessed_word == word:
        break
    
        
    
        
print "\nGame over!"


