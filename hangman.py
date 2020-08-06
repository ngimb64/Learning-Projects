import random
from collections import Counter

# Defines list of words used for hangman #
bandList = '''beetles chicago kiss'''

# Splits bandlist so the individual entries
# can be treated separately from each other #
bandList = bandList.split(' ')

# Chooses random word in bandList
# to be used for the game #
word = random.choice(bandList)

if __name__ == '__main__': 

    print('Guess the rock or metal band!!!')
    print()
    print('Please use lower case letters only') 
    
    # Creates empty word template to convey 
    # how many entries are in the word #
    for i in word: 

        print('_', end = ' ')         
    print() 
  
    playing = True
     
    letterGuessed = ''                 
    chances = len(word) + 5
    correct = 0
    flag = 0
    try: 
        # Sets loop and stopping point 
        # when certain values are reached #
        while (chances != 0) and flag == 0:  
            print() 
            chances -= 1
  
            # Prompts user to guess a letter #
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # These provide some handling of invalid inputs #
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If a correct letter is guessed the letter is added 
            # to the word template displayed on the screen #
            if guess in word: 
                k = word.count(guess) 
                for _ in range(k):     
                    letterGuessed += guess 
  
            # Checks to see if the word has missing 
            # entries or has been fully guessed #
            for char in word: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                
                # If all the words entries have 
                # been accurately guessed # 
                elif (Counter(letterGuessed) == Counter(word)):  
 
                    print("The word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break  
                    break 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If the users runs out of guesses and
        # has not guessed the full word #
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 