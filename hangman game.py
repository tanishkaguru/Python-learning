#hangman game

import random

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

words = ["aardvark", "baboon", "camel","oranges","toffee",'quizzes','talking','laughing','astonish','elucidate','scratch','sphinx']

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

guess=list(random.choice(words))
no_blanks=len(guess)
word=[]
for i in range(no_blanks):
    word+='_'

def disp(w):
    for i in w:
        print(i,end=' ')
    print("\n")

lives=6

while(no_blanks!=0 and lives!=0):
    let=input("Guess a letter: ").lower()

    for i in range(len(guess)):
        if guess[i]==let:
            word[i]=let
            no_blanks-=1
        
    if let not in guess:
        print(f"You guessed {let}. That's not in the word. You lose a life!")
        lives-=1
    disp(word)
    print(stages[lives])

if '_' not in word:
    print("YOU WIN\nGAME OVER!")
else:
    guess=list(guess)
    print("YOU LOSE.\nGAME OVER!")
    print("The word was ",end='')
    disp(guess)
