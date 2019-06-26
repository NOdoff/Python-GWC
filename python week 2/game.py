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
        'First?', you inquired.
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
