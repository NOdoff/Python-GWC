import random
# --- Define your functions below! ---
def intro():
    introduction = '''Hey, I am your personal chatbot! You can call me Chat for short   (*≧▽≦)'''
# OK, let's CHAT, hehe... I hope you do not mind puns (⌯˃̶᷄ ﹏ ˂̶᷄⌯)ﾟ
    print(introduction)


def draw():
    ascii = ['''
────(♥)(♥)(♥)────(♥)(♥)(♥) __ ɪƒ ƴσυ'ʀє αʟσηє,
──(♥)██████(♥)(♥)██████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.
─(♥)████████(♥)████████(♥) ɪƒ ƴσυ ѡαηт тσ cʀƴ,
─(♥)██████████████████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ.
──(♥)████████████████(♥) ɪƒ ƴσυ ѡαηт α ɧυɢ,
────(♥)████████████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ.
──────(♥)████████(♥) ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ,
────────(♥)████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє.
─────────(♥)██(♥) ɓυт αηƴтɪɱє ƴσυ ηєє∂ α ƒʀɪєη∂,
───────────(♥) __ ɪ'ʟʟ ʝυѕт ɓє ɱє.''',
'''
( •̃•̃)
 /█\
 .Π.
''',
'''
│▒│ /▒/
│▒│/▒/
│▒ /▒/─┬─┐
│▒│▒|▒│▒│
┌┴─┴─┐-┘─┘
│▒┌──┘▒▒▒│
└┐▒▒▒▒▒▒┌┘
└┐▒▒▒▒┌┘
''',
'''
ஜ۩۞۩ஜஜ۩۞۩ஜஜ۩۞۩ஜ
█▄█ █ █▀█ █▄█ █▀█ █▀█
█▀█ █ █▀▀ █▀█ █▄█ █▀▀
ஜ۩۞۩ஜஜ۩۞۩ஜஜ۩۞۩ஜ
''',
'''
╔═══╗ ♪
║███║ ♫
║(●)♫
╚═══╝♪♪
''',
'''
╔══╗─╔═════╦══╗
║──║─║──║──║──║
║──║─║──║──║──║
║──╚═╣──║──║──╚═╗
║────║─────║────║
╚════╩═════╩════╝
''',
'''
─────────▀▀▀▀▀▀──────────▀▀▀▀▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀▀▀▀▀▀
────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────▀▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀─────▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
─────▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀───▀▀▀────────▀▀▀
────────▀▀▀▀▀▀▀▀▀──▀▀▀▀▀────▀▀▀▀
───────────▀▀▀▀▀▀───▀▀▀───▀▀▀▀
─────────────▀▀▀▀▀─────▀▀▀▀
────────────────▀▀▀──▀▀▀▀
──────────────────▀▀▀▀
───────────────────▀▀
''',
'''
___________$$$$$$___________
___________$$$$$$___________
____________$$$$____________
____________$$$$____________
____________$$$$____________
____________$$$$____________
____________$$$$____________
____________$$$$____________
___________$$$$$$___________
___________$$$$$$___________
___________$$$$$$___________
__________$$$$$$$$__________
__________$$$$$$$$__________
_____$$$$$$$$$$$$$$$$$$_____
____$_____$$$$$$$$_____$____
___$______$$$$$$$$______$___
___$____________________$___
____$__________________$____
_____$______$$$$______$_____
_____$____$$____$$____$_____
____$_____$$____$$_____$____
___$________$$$$________$___
__$______________________$__
_$________________________$_
_$________________________$_
_$______$$$$$$$$$$$$______$_
__$______________________$__
___$____________________$___
____$$$$____________$$$$____
________$$$$$$$$$$$$________
'''

    ]
    print(random.choice(ascii))
def is_valid_input(user_input, possible):
    # user_input = user_input.lower()
    if(user_input in possible):
        return True
    return False

def rock_paper_scissors(positiveAnswers, negativeAnswers):
    playing = True
    plays = ['rock', 'paper', 'scissors']

    print('''
Welcome to Rock-Paper-Scissors Game. Let's start a new game.
    ''')
    while playing:
        throw = input('''What is your throw?

Enter rock for ROCK.
Enter paper for PAPER.
Enter scissors for SCISSORS.
''')
        throw = throw.lower()
        if(throw not in plays):
            print("Sorry. I not understand your input. Try again.")
            continue
        computer_play = random.choice(plays)
        print('I threw %s!'  %(computer_play))
        if(computer_play == throw):
            print("It is a draw!")
        elif(throw == 'rock'):
            if(computer_play == 'scissors'):
                print("The rock crushes the scissors. You won!")
            elif(computer_play == 'paper'):
                print("The paper covers the rock. I won!")
        elif(throw == 'paper'):
            if(computer_play == 'scissors'):
                print("The scissors cut the paper. I won!")
            elif(computer_play == 'rock'):
                print("The paper covers the rock. You won!")
        elif(throw == 'scissors'):
            if(computer_play == 'paper'):
                print("The scissors cut the paper. You won!")
            elif(computer_play == 'rock'):
                print("The rock crushes the scissors. I won!")
        play_again = input("\nDo you want to play again?\n")
        if(play_again in positiveAnswers):
            continue
        else:
            break
def recite_poem():
    poems = [
'''ROBERT FROST “THE ROSE FAMILY”

The rose is a rose,
And was always a rose.
But the theory now goes
That the apple’s a rose,
And the pear is, and so’s
The plum, I suppose.
The dear only knows
What will next prove a rose.
You, of course, are a rose –
But were always a rose.
''',
'''MARGARET ATWOOD “YOU FIT INTO ME”

you fit into me
like a hook into an eye

a fish hook
an open eye
''',
'''MAYA ANGELOU “AWAKENING IN NEW YORK”

Curtains forcing their will
against the wind,
children sleep,
exchanging dreams with
seraphim. The city
drags itself awake on
subway straps; and
I, an alarm, awake as a
rumor of war
lie stretching into dawn
unasked and unheeded.
''',
'''WILLIAM BUTLER YEATS

Had I the heaven’s embroidered cloths,
Enwrought with golden and silver light,
The blue and the dim and the dark cloths
Of night and light and the half-light,
I would spread the cloths under your feet:
But I, being poor, have only my dreams;
I have spread my dreams under your feet;
Tread softly because you tread on my dreams.
''',
'''EMILY DICKINSON

I’m Nobody! Who are you?
Are you — Nobody — Too?
Then there’s a pair of us!
Don’t tell! They’d banish us — you know!

How dreary — to be — Somebody!
How public — like a Frog —
To tell one’s name — the livelong June —]
To an admiring Bog!
''',
'''ROBERT FROST

Nature’s first green is gold,
Her hardest hue to hold.
Her early leaf’s a flower;
But only so an hour.
Then leaf subsides to leaf,
So Eden sank to grief,
So dawn goes down to day
Nothing gold can stay.
'''
    ]
    print(random.choice(poems))
def tell_jokes(yes, no):
    answers = ["who's there?", "whos there?", "who is there?", "who's there", "whos there", "who is there"]
    responces1 = ["Adore", "Annie", "Armageddon", "Boo"]
    responces2 = ["Adore is between us. Open up!", "Annie body home?", "Armageddon a little bored. Let’s go out.", "Gosh, don’t cry it’s just a knock knock joke."]
    while(True):
        check1 = input("Knock, Knock.\n")
        if(check1 in answers):
            index = random.randint(0, len(responces1)-1)
            responce1 = responces1[index]

            input_who = input(responce1+'\n')
            check2 = responce1.lower()+' who'
            print(check2)
            if (check2 in input_who.lower()):
                print(responces2[index])
            else:
                print("Snap! Try again.")
                continue
            play_again = input("Play again?\n")
            if(play_again.lower() in yes):
                continue
            else:
                break
def play_hangman():
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

    answer1 = input('''Hey! Welcome to the hangman game! Are you ready for the fun stuff?
''')
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
def play_text_adventure():
    intro = '''
    You were just opening the door to relax after long and tiring day of work,
    when you noticed that you were not in your house anymore.
    The room that you were in was blindingly white as if it was in the hospital.
    Looking around, you noticed a black device in the middle of the room.
        '''
    print(intro)
    goodwill = 0
    while True:
        touchDevice = input('''
Are you brave and curious enough to check it out?
ENTER YES or NO.
        ''')
        if(touchDevice.lower() == 'yes'):

            nResponce = "[You decided to touch it]"
            print(nResponce)
            startAI = True
            goodwill +=1
            break
        elif(touchDevice.lower() == 'no'):
            yResponce = "[You decided to leave it alone]"
            print(yResponce)
            startAI = False
            break
        else:
            continue
    # max is 1
    if(startAI):
        choice = '''
    While you were contemplating whether you were right to do that, '''


    else:
        choice = '''
    As you were wondering about how you could leave the room, '''
    greeting = '''
    you were suddenly called out by the voice that came from your head,
        'Hey, you must be the new tester!
        Do not be scared!
        My name is Sammy.
        I will be your AI helper today.
        I was designed to help you to go through this test.
        I am just a beta version, so please forgive me if I make any mistakes.
        Well, enough about me, I would like to learn about you too!'
        '''
    print(choice + greeting)

    name = input("First and foremost tell me your name =>\n")

    print('''
    As you said your name, the voice cheerfully responded,
        'Ohoho!
        %s is a unique name. My software does not have records anyone with that name before.
        It would be a pleasure to work with you, %s.'
    ''' %(name, name))
    print('''
    Then Sammy continued to excitedly talk,
        'OK, lets jump into it!
        I will guide you through this, so listen carefully'
    Only after his words, you noticed that you were not in the white room anyone,
    but instead were in what looked like a control panel.
        'First you need to tell me what you see. Tell the truth, because we will check it later.'
    Suddenly, you noticed that a very strange fog appeared in front of you that shaped as panther.
        'So, what are you seeing?', urged Sammy.
    As you were to answer him, you heard a faint whisper.
        'Wait... it is a trap...'
    ''')

    while True:
        command1 = input('''
    ENTER A to answer panther.
    ENTER W to answer 'nothing'.
    ENTER D do not say anything.
        ''')
        if(command1.lower() == 'a'):
            responce1 = '''
[You chose to answer panther.]
        'WHAAAAAAAAAAAAAAAAT! HOLY SMOKES! I AM NOT DEALING WITH THIS AGAIN...
    I AM TOO OLD FOR THIS...', shrieked the AI in an panicked voice.
        'I am sorry for this but I have no choice', it stated seemingly sad.
    Then you felt yourself fainting.
    As you were losing your consciousness, you heard the same whisper in your head sighing,
        'I warned you...'
        It must have said something else, but you heard no more.

'''
            branch1 = 0
            break
        elif(command1.lower() == 'w'):
            responce1 = '''
[You chose to answer 'nothing'.]
    The voice sounded very dejected,
        'Really? Aww, that sucks...'
        '''
            branch1 = 1
            break
        elif(command1.lower() == 'd'):
            responce1 = '''
[You chose not to say anything.]
    You decided to continue to listen to the voice within you,
    ignoring the poor Sammy and pretending to look further into the black fog.
    As if hearing your wishes, the whisper emerges again...
            '''
            branch1 = 2
            break
        else:
            continue
    print(responce1)
    if(branch1 == 0):
        exit(0)
    elif(branch1 == 1):

        conseq1 = '''
    You unconsiously felt bad for lying to AI, but then you remembered that
    it was probably simulating those feelings and that you had a right to be suspicious
    since you still did not know where you were and if AI was your ally or foe.
    You finally decided to ask Sammy about the reasons for your abrupt arrival.
        '''

    elif(branch1 == 2):
        conseq1 = '''
        'Say that you see the number 42, believe me I know what I am doing',
    whispered the voice so convincingly that you unconsiously complied.
        'Really?! Okay, that is certainly encouraging',
    exclaimed Sammy happily when he heard your answer.
        While he said that, you remembered that you still did not ask him as to why you were here.
            '''
        goodwill +=2
    print(conseq1)
    print('''
        'Ummmm, I would love to answer your questions, but can we do it after testing?
        We are kind of in the rush...',
    said AI in a nervous voice.
    You were unsure if it was because of time limit or because of something else, but you ...
    ''')
    command2 = input('''
ENTER A to agree to continue the test.
ENTER D to refuse to cooperate.
    ''')
    # max 3
    while True:
        if(command2.lower() == 'a'):
            '''
[You chose to cooperate]
    'Thanks, I appreciate it!'
            '''
            goodwill+=1
            break
        elif(command2.lower() == 'd'):
            '''
[You chose to ignore the suggestion]
    'I did not want to do it, but looks like I will need to forcefully move on'
            '''
            goodwill-=1
            break
        else:
            continue
    print('''
    'Okay, lets move on to next test. This one is phychological', said Sammy.
    'If you saw your leader and your family member in the lake who would you save...'
    'Save first?', you inquired.
    'Sure', said the AI, 'let it be that way.'
    ''')
    # max 4; min -1
    command3 = input('''
ENTER A for your boss.
ENTER D for your family member.
ENTER S to refuse to answer.
    ''')
    while True:
        if(command3.lower() == 'a'):
            print('''
[You chose to save your boss]
        'I want to save my boss, because he always helped me throughout my hard times.
        He was technically my family, and he does not know how to swim, unlike my swimmer family'
            ''')
            goodwill+=1
            break
        elif(command3.lower() == 'd'):
            print('''
[You chose to save your family member]
        'My poor Annabelle. I will not be able to live without you!', you sighed sa you thought about your cat.
        'It could count as a revenge for Mr. Collins for eating my cookies without permission'
        ''')
            break
        elif(command3.lower() == 's'):
            print('''
[You chose to abstain from answering]
        'I cannot choose to abandon anyone...'
        ''')
            if(goodwill>2):
                goodwill+=2
                print(
        '''
        'I see so you feel like all lives matter? Good, good, Sammy responded'
        ''')
            else:
                goodwill-=2
                print('''
        'I understand your hesitation, but it might be dangerous to do that in dire situations, noted Sammy'
        ''')
            break
        else:
            continue
    print('''
        'OK, thank you for your cooperation, the results of your survey will soon emerge.''

    ''')
    if(goodwill>=3):
        print(
        '''
        'Congratulations, WE are proud to announce that you will be the new employee of the Intergalactic Inc.
        YOU were chosen out of millions of participants across the universe.
        That is why YOU should be proud!', the loud announcement rang throughout the control room.
        You were covered in confetti, but you were happy for some unknown reason.
        You did not know what would await you in future, but you were sure it would not be boring!


        ''')
    else:
        print(
        '''
        'Sorry, you are uncompatible. Please cooperate with the procedure of erasing your memory',
         sounded the announcement.
         When you woke up in your room, you were stifled. I did not know why but you were not as happy
         as you thought about the vacation.
         YOU FELT LIKE YOU LOST SOMETHING, SOMETHING IMPORTANT...


        ''')

def process_input():

    positiveAnswers = ['yes', 'y']
    negativeAnswers = ['no', 'n']
    greetings = ['hi', 'hello', 'yo', 'hey']
    poem = ['tell me a poem', 'poem']
    rock = ['rps', 'rock paper scissors', 'play rock paper scissors', 'i want play rock paper scissors',
    "let's play rock paper scissors", "lets play rock paper scissors"]
    picture = ['picture', 'draw']
    bye = ['bye', 'out', 'done', 'exit', 'quit']
    suggestions = ['suggestions', 's']
    jokes = ['knockknock', 'knock-knock', 'knock']
    hangman = ['hangman']
    adventure = ['text adventure']
    all = greetings + poem + rock + picture + suggestions + bye+jokes+hangman+adventure
    while True:
        answer = input("Do you have anything you want to share or do? Type s or suggestions for suggestions. \n")
        answer = answer.lower()
        check = is_valid_input(answer, all)
        if(check):
            if(answer in suggestions):
                print('You can access all of the following!')
                print('For greetings enter the following in upper or lower case:')
                for i in greetings:
                    print(i)
                print('For pictures enter the following in upper or lower case:')
                for i in picture:
                    print(i)
                print('For Rock-Paper-Scissors Game enter the following in upper or lower case:')
                for i in rock:
                    print(i)
                print('For exiting enter the following in upper or lower case:')
                for i in bye:
                    print(i)
                print('For poem enter the following in upper or lower case:')
                for i in poem:
                    print(i)
                print('For knock-knock jokes enter the following in upper or lower case:')
                for i in jokes:
                    print(i)
                print('For hangman enter the following in upper or lower case:')
                for i in hangman:
                    print(i)
                print('For text adventure enter the following in upper or lower case:')
                for i in adventure:
                    print(i)
            elif(answer in greetings):
                print("Hello to you too! I hope you are having fun chatting with me! (*^▽^*)")
            elif(answer in poem):#cont poem creating
                print("Of course! I will gladly demonstrate you my artistic skills...\n")
                recite_poem()
            elif(answer in rock):
                rock_paper_scissors(positiveAnswers, negativeAnswers)
            elif(answer in bye):
                print('OK, bye. It nice chatting with you!')
                exit(0)
            elif(answer in picture):
                print("Of course! I will gladly show off my drawings... \n")
                draw()
            elif(answer in jokes):
                tell_jokes(positiveAnswers, negativeAnswers)
            elif(answer in hangman):
                play_hangman()
            elif(answer in adventure):
                play_text_adventure()




        else:
            print("\nThat's cool!")

# --- Put your main program below! ---
def main():
    intro()
    process_input()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
