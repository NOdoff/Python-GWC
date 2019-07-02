import random
import string
# A list of words that
potential_words = ['awkward', 'banjo', 'ostracize', 'Oxygen', 'Bungler',
'Croquet',
'Crypt',
'Dwarves',
'Fervid',
'Fishhook',
'Fjord',
'Gazebo',
'Gypsy',
'Haiku',
'Haphazard'
'Hyphen',
'Ivory',
'Jazzy',
'Jiffy',
'Jinx',
'Jukebox',
'Kayak',
'Kiosk',
'Klutz',
'Memento',
'Mystify',
'Pajama',
'Phlegm',
'Pixel',
'Polka',
'Quad',
'Quip',
'Rhythmic',
'Rogue',
'Sphinx',
'Squawk',
'Swivel',
'Toady',
'Twelfth',
'Unzip',
'Waxy',
'Wildebeest',
'Yacht',
'Zealous',
'Zigzag',
'Zippy',
'Zombie']

word_original = random.choice(potential_words)

fullH = '''
   ____
  |    |
  |    O
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|
'''
start ='''
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|'''
mistake1 = '''
   ____
  |    |
  |    O
  |
  |
  |
 _|_
|   |______
|          |
|__________|'''
mistake2 = '''
   ____
  |    |
  |    O
  |    |
  |
  |
 _|_
|   |______
|          |
|__________|'''
mistake3 ='''
   ____
  |    |
  |    O
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|'''
mistake4 = '''
   ____
  |    |
  |    O
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|'''
mistake5 ='''
   ____
  |    |
  |    O
  |   /|
  |    |
  |   /
 _|_
|   |______
|          |
|__________|'''
mistake6 = '''
   ____
  |    |
  |    O
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|'''
mistake7 = '''
   ____
  |    |
  |    O
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|'''
# Use to test your code:
# print(word_original)

# Converts the word to lowercase
word_original = word_original.lower()
word = list(word_original)
# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
for letter in word:
    current_word.append("_")

# Some useful variables
guessesC = []
guessesW = []
maxfails = 7
fails = 0

answer1 = input('''Hey! Welcome to the hangman game! Are you ready for the fun stuff?''')
positiveAnswers = ['yes', 'y']
negativeAnswers = ['no', 'n']
if (answer1.lower() in positiveAnswers):
    print('''Alright! I like your enthusiasm, so let's jump  into it!''')
elif (answer1.lower() in negativeAnswers):
    print('''Hey, do not be so negative! If you are here, you are interested in playing for sure!
Since you are so shy, I will move on for you.^_^''')
else:
    print('''OK, lets just move on.^_^''')
while fails < maxfails and '_' in current_word:
    # print(word)
    if fails == 0:
        print(start)
    elif fails == 1:
        print(mistake1)
    elif fails == 2:
        print(mistake2)
    elif fails == 3:
        print(mistake3)
    elif fails == 4:
        print(mistake4)
    elif fails == 5:
        print(mistake5)
    elif fails == 6:
        print(mistake6)
    elif fails == 7:
        print(mistake7)
    correct_guesses = ''
    incorrect_guesses = ''
    print("Correct guesses:")
    for i in guessesC:
        print(i)
    print("Incorrect guesses:")
    for i in guessesW:
        print(i)
    print_string = ""
    for i in current_word:
        print_string+=(i+" ")
    print(print_string)
    guess = input("Guess a letter: \n")
    if(len(guess) !=1):
        print("Sorry, I did not understand that. Try again")
        continue
    if guess not in "qwertyuiopasdfghjklzxcvbnm":
        print("Sorry, I did not understand that. Try again")
        continue
    if guess in guessesC or guess in guessesW:
        print("You already guessed that. Try again.")
        continue
    if(guess in word):
        print("Correct! You are on the path to winning!")
        guessesC.append(guess)#append to correct guesses
        # for letter in word:#GOES through the each letter in the word
        #     if(guess == letter):#IF THE guess is e
        #         guess_index = word.index(letter)#
        #         current_word[guess_index] = letter
        #         word[guess_index] = "*"
        #         if(guess not in guessesC):
        #             guessesC.append(guess)
        for index in range(0,len(word)):
            if(guess == word[index]):
                current_word[index] = guess
                word[index] = '*'
                if(guess not in guessesC):
                    guessesC.append(guess)
        print("You have " + str(maxfails - fails) + " fails left!")


    else:
        guessesW.append(guess)
        print("Incorrect! Please guess again!")
        fails = fails+1
        print("You have " + str(maxfails - fails) + " fails left!")


if('_' not in current_word):
    print("Congratulations, you won! Give yourself a pat on the back and reward yourself with a cookie!  ( ´ ▽ ` )ﾉ")
else:
    print("YOU HAVE LOST!:( The word was " + word_original.upper()+"!\nTRY AGAIN, HUMAN.  (ಠ_ಠ)")
