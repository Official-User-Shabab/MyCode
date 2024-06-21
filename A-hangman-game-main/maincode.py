import random
import time

# ERROR//BUG//FIXES LOGS
# 1 I found out that some functions especially at the start is repeated many times. The duplicates should be removed.
# 2 Working on the credits section...
# 3 We really need to agree on using either lower() or higher()...


#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#

#UNIVERSAL FUNCTIONS

## Borders
eternal0 = True
eternal01 = True

def game_started_border():
    print("~~~~~~~~~~~~~~~~~~~~~GAME SESSION STARTED~~~~~~~~~~~~~~~~~~~~~\n")

def border2():
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")

def settings_border():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~SETTINGS PAGE~~~~~~~~~~~~~~~~~~~~~~~~~\n")

##Validate choice from start/home page
def validate_choice(choice):
    while (choice != "play") and (choice != "settings") and (choice != "credits") and (choice != "quit"):
        print("")
        print("Invalid option, please pick an option from the options below")
        print("---------------------------------------------------------------------------")
        print("|PLAY                                                                      |")
        print("|SETTINGS                                                                  |")
        print("|CREDITS                                                                   |")
        print("|QUIT                                                                      |")
        print("---------------------------------------------------------------------------")
        choice = input(": ").lower()
    return choice

##Validates gamemode input
def validate_gm(gm):
        while (gm != "CLASSIC") and (gm != "C") and (gm != "INFINITE") and (gm != "I") and (gm != "HARDCORE") and (gm != "H") and (gm != "QUIT") and (gm != "TRIAL") and (gm != "T"):
            print("")
            print("Invalid gamemode, please choose a gamemode from the ones below:")
            print("---------------------------------------------------------------------------")
            print("|CLASSIC   - (1 word , 7 lives)                                            |")
            print("|INFINITE  - (infinite word , 7 lives , lives reset every word)            |")
            print("|HARDCORE  - (infinite word , 7 lives , lives carry over to the next word) |")
            print("---------------------------------------------------------------------------")
            gm = input("Gamemode: ").upper()
        return gm

##Validate setting input
def validate_setting(setting):
    while (setting != "exit") and (setting != "lives") and (setting != "theme") and (setting != "trial") and (setting != "multi-word") and (setting != "mulit word") and (setting != "mulitword"):
        print("")
        print("Invalid option, pLease choose from the following settings (make sure spelling in correct)")
        print("---------------------------------------------------------------------------")
        print("|Lives       - (settings related to the lives mechanic)                    |")
        print("|Theme       - (settings related to the theme of the words)                |")
        print("|Trial       - (settings related to the 'Trials' gamemode)                 |")
        print("|Multi-word  - (settings related to the 'Multi-word' gamemode)             |")
        print("---------------------------------------------------------------------------")
        print("(If you wish to exit settings page, type 'exit'.)")
        setting = input("Setting: ").lower()
    return setting
import random
import time

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#

#UNIVERSAL FUNCTIONS

## Borders
def game_started_border():
    print("~~~~~~~~~~~~~~~~~~~~~GAME SESSION STARTED~~~~~~~~~~~~~~~~~~~~~\n")

def border2():
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")

def settings_border():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~SETTINGS PAGE~~~~~~~~~~~~~~~~~~~~~~~~~\n")

##Validate choice from start/home page
def validate_choice(choice):
    while (choice != "play") and (choice != "settings") and (choice != "credits") and (choice != "quit"):
        print("")
        print("Invalid option, please pick an option from the options below")
        print("---------------------------------------------------------------------------")
        print("|PLAY                                                                      |")
        print("|SETTINGS                                                                  |")
        print("|CREDITS                                                                   |")
        print("|QUIT                                                                      |")
        print("---------------------------------------------------------------------------")
        choice = input(": ").lower()
    return choice

##Validates gamemode input
def validate_gm(gm):
        while (gm != "CLASSIC") and (gm != "C") and (gm != "INFINITE") and (gm != "I") and (gm != "HARDCORE") and (gm != "H") and (gm != "QUIT") and (gm != "TRIAL") and (gm != "T"):
            print("")
            print("Invalid gamemode, please choose a gamemode from the ones below:")
            print("---------------------------------------------------------------------------")
            print("|CLASSIC   - (1 word , 7 lives)                                            |")
            print("|INFINITE  - (infinite word , 7 lives , lives reset every word)            |")
            print("|HARDCORE  - (infinite word , 7 lives , lives carry over to the next word) |")
            print("---------------------------------------------------------------------------")
            gm = input("Gamemode: ").upper()
        return gm

##Validate setting input
def validate_setting(setting):
    while (setting != "exit") and (setting != "lives") and (setting != "theme") and (setting != "trial") and (setting != "multi-word") and (setting != "mulit word") and (setting != "mulitword"):
        print("")
        print("Invalid option, pLease choose from the following settings (make sure spelling in correct)")
        print("---------------------------------------------------------------------------")
        print("|Lives       - (settings related to the lives mechanic)                    |")
        print("|Theme       - (settings related to the theme of the words)                |")
        print("|Trial       - (settings related to the 'Trials' gamemode)                 |")
        print("|Multi-word  - (settings related to the 'Multi-word' gamemode)             |")
        print("---------------------------------------------------------------------------")
        print("(If you wish to exit settings page, type 'exit'.)")
        setting = input("Setting: ").lower()
    return setting




## ASCII art + lives system
def f_lives(lives,lost):
    pic = ['''
      +---+
      |  \|
          |
          |
          |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
          |
          |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
      |   |
          |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
     /|   |
          |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
     /|\  |
          |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
     /|\  |
     /    |
          |
    =========''',
    
    '''
      +---+
      |  \|
      O   |
     /|\  |
     / \  |
          |
    =========''']
    print("")
    print(f"You lost a life. You have {lives-int(lost)} lives remaining.\n")
    print(pic[7-lives])
    print("")
    print(found)


##option to end game or start again
def end_repeat():
        print(" ")
        print("Game has ended")
        ans = input("Want to play again? (y/n)_").lower()
        if ans != "y":
            print(" ")
            print("WELP THEN CYA!")
            time.sleep(3)
            quit()
        else:
            return True



#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#


# UNIVERSAL ARRAYS

## game handling arrays
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
used = [" "]

## word arrays
mythical_creatures = ["dragon", "unicorn", "mermaid", "leprechaun", "werewolf", "fairy", "chimera", "sphinx", "griffin", "troll", "centaur", "yeti", "pegasus", "ghoul", "imp", "basilisk", "merman", "phoenix", "manticore", "vampire", "gargoyle", "pixie", "hippocampus", "kelpie", "golem", "goblins", "cyclops", "bigfoot", "sirens", "kraken", "manticore", "salawa", "fenrir", "argos", "hydra", "typhon",]
jobs = ["doctor","nurse","mechanic","engineer","undertaker","miner","teacher","headteacher","police","firefighter","fisherman","accountant","shopkeeper","architect","janitor","scientist","austronaut","footballer"]

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#

eternal = True
running = True

#Default settings
##Lives
start_lives = 7
increment = 1
##Theme
theme = "all"
##Trial
trial_length = 5
##Multi-word
multi_word_number = 2

# GAME LINE
while eternal:
    while running:

        #Start page
        print("Welcome to 'Scuffed Hangman', a game created by programmer noobs all about hanging a person (or multiple people)")
        print("What u wanna select?")
        print("---------------------------------------------------------------------------")
        print("|PLAY                                                                      |")
        print("|SETTINGS                                                                  |")
        print("|CREDITS                                                                   |")
        print("|QUIT                                                                      |")
        print("---------------------------------------------------------------------------")
        choice = input(": ").lower()
        choice = validate_choice(choice)

        ##############################################

        #the game
        if choice == "play":
            #gamemode selection
            print("Please choose a gamemode from the ones below:\n")
            print("---------------------------------------------------------------------------")
            print("|CLASSIC   - (1 word , 7 lives)                                            |")
            print("|INFINITE  - (infinite word , 7 lives , lives reset every word)            |")
            print("|HARDCORE  - (infinite word , 7 lives , lives carry over to the next word) |")
            print("---------------------------------------------------------------------------")
            gm = input("Gamemode: ").upper()
            print("         ")

            #gamemode input validation
            gm = validate_gm(gm)

            #option there if you want to quit
        #quitting
        if gm == "QUIT":
            quit()

            #used for input validation in game
            choice_check = True
            
            # puts user into correct gamemode
            game_started_border()
            
            
            #MAINLINES OF GAMEPLAY:
            
            # CLASSIC GM
            if (gm == "CLASSIC") or (gm == "C"):
                lives = int(start_lives)
                word = random.choice(mythical_creatures)
                found = "_ " * len(word)
                word2 = " ".join(list(word)) + " "
                print(found)
                print("")
                while (found != word2) and (lives > 0):
                    lose_life = True
                    choice = input("Enter your guess: ").lower()
                    while choice_check:
                        if (choice in alphabet)== False:
                            choice = input("Invalid choice. Please choose a single letter from the english alphabet: ")
                        else:
                            choice_check = False
                    for x in range(len(word2)):
                        if choice == word2[x]:
                            found = found[:x] + choice + found[x + 1:]
                            lose_life = False
                    if lose_life:
                        f_lives(lives,increment)
                        lives -= increment
                    else:
                        print(" ")
                        print("Correct guess!\n")
                        print(found)
                if lives <= 0:
                    print(f"You lost all your lives, the word was {word}")
                else:
                    print(f"Well done! You guessed the word ({word})")

                #below is so the user can end or start again
                running = end_repeat()


            # INFINITE GM
            elif (gm == "INFINITE") or (gm == "I"):
                correct = 0
                lives = int(start_lives)
                while lives > 0:
                    lives = 7
                    word = random.choice(mythical_creatures)
                    found = "_ " * len(word)
                    word2 = " ".join(list(word)) + " "
                    print("")
                    print(found)
                    while (found != word2) and (lives > 0):
                        lose_life = True
                        choice = input("Enter your guess: ").lower()
                        while choice_check:
                            if (choice in alphabet) == False:
                                choice = input("Invalid choice. Please choose a single letter from the english alphabet: ").lower()
                            else:
                                choice_check = False
                        for x in range(len(word2)):
                            if choice == word2[x]:
                                found = found[:x] + choice + found[x + 1:]
                                lose_life = False
                        if lose_life:
                            f_lives(lives,increment)
                            lives -= increment
                        else:
                            print(" ")
                            print("Correct guess!\n")
                            print(found)
                    if found == word2:
                        correct += 1
                    if lives <= 0:
                        print(f"You lost all your lives, you got {correct} words correct.\n")

                        #below is so the user can end or start again
                        running = end_repeat()
                        
                    else:
                        print(f"Well done! You guessed the word ({word})\n")
                        print("NEXT WORD:")


            # HARDCORE GM
            elif (gm == "HARDCORE") or (gm == "H"):
                correct = 0
                lives = int(start_lives)
                while lives > 0:
                    word = random.choice(mythical_creatures)
                    found = "_ " * len(word)
                    word2 = " ".join(list(word)) + " "
                    print(found)
                    print("")
                    while (found != word2) and (lives > 0):
                        lose_life = True
                        choice = input("Enter your guess: ").lower()
                        while choice_check:
                            if (choice in alphabet) == False:
                                choice = input("Invalid choice. Please choose a single letter from the english alphabet: ").lower()
                            else:
                                choice_check = False
                        for x in range(len(word2)):
                            if choice == word2[x]:
                                found = found[:x] + choice + found[x + 1:]
                                lose_life = False
                        if lose_life:
                            f_lives(lives,increment)
                            lives -= increment
                        else:
                            print(" ")
                            print("Correct guess!\n")
                            print(found)
                    if found == word2:
                        correct += 1
                    if lives <= 0:
                        print(f"You lost all your lives, you got {correct} words correct.\n")
                        #below is so the user can end or start again
                        running = end_repeat()
                        
                    else:
                        print(f"Well done! You guessed the word ({word})\n")
                        print("NEXT WORD:")


            #TRIAL GM
            elif (gm == "TRIAL") or (gm == "T"):
                score = 0
                for i in range(trial_length):
                    lives = int(start_lives)
                    word = random.choice(mythical_creatures)
                    found = "_ " * len(word)
                    word2 = " ".join(list(word)) + " "
                    print(found)
                    print("")
                    while (found != word2) and (lives > 0):
                        lose_life = True
                        choice = input("Enter your guess: ").lower()
                        while choice_check:
                            if (choice in alphabet) == False:
                                choice = input("Invalid choice. Please choose a single letter from the english alphabet: ").lower()
                            else:
                                choice_check = False
                        for x in range(len(word2)):
                            if choice == word2[x]:
                                found = found[:x] + choice + found[x + 1:]
                                lose_life = False
                        if lose_life:
                            f_lives(lives,increment)
                            lives -= increment
                        else:
                            print(" ")
                            print("Correct guess!\n")
                            print(found)
                    if found == word2:
                        score += 1
                        print("New word:")
                    #elif
                print("")
                print("The trial has ended.")
                print(f"You got {score} out of the {trail_lengh} words correct.")
                #below is so the user can end or start again
                running = end_repeat()
        #settings
        elif choice == "settings":
            #settings page 1
                settings_border()
                print("Below are the following settings groups that can be changed:")
                print("---------------------------------------------------------------------------")
                print("|Lives       - (settings related to the lives mechanic)                    |")
                print("|Theme       - (settings related to the theme of the words)                |")
                print("|Trial       - (settings related to the 'Trials' gamemode)                 |")
                print("|Multi-word  - (settings related to the 'Multi-word' gamemode)             |")
                print("---------------------------------------------------------------------------")
                print("(If you wish to exit settings page, type 'exit')")
                setting = input("Setting: ").lower()

                #input validation
                setting = validate_setting(setting)
                print("")
                #puts user into specific settings page
                #Lives
                if setting == "lives":
                    print("Below are the following settings related to lives:")
                    print("---------------------------------------------------------------------------")
                    print("|Start        - (lives you start with)                                     |")
                    print("|Increment   - (amount of lives lost per incorrect guess)                  |")
                    print("---------------------------------------------------------------------------")
                    print("(If you wish to go back, type 'back')")
                    setting = input("Setting: ").lower()
                    #setting input validation
                    while (setting != "start") and (setting != "increment") and (setting != "back"):
                        print("")
                        print("Invalid option, please choose from the options below:")
                        print("---------------------------------------------------------------------------")
                        print("|Start        - (lives you start with)                                     |")
                        print("|Increment   - (amount of lives lost per incorrect guess)                  |")
                        print("---------------------------------------------------------------------------")
                        print("(If you wish to go back, type 'back')")
                        setting = input("Setting: ").lower()
                    if setting == "start":
                        print("Please enter the number of lives you wish to start with, input must be over 0 and below 8, invalid inputs will be defaulted to 7.")
                        start_lives = input("Start lives: ")
                        #input validation, not repeated instead defaulted
                        if (start_lives != "1") and (start_lives != "2") and (start_lives != "3") and (start_lives != "4") and (start_lives != "5") and (start_lives != "6") and (start_lives != "7"):
                            start_lives = 7
                    elif setting == "increment":
                        print("Pick an increment of either 1 or 2, invalid inputs will be defaulted to 1")
                        increment = input("Increment: ")
                        #input validation, not repeated instead defaulted
                        if (increment != "1") and (increment != "2"):
                            increment = 1
                #Theme
                if setting == "theme":
                    print("Please pick a theme from the ones below:")
                    print("---------------------------------------------------------------------------")
                    print("|All                                                                       |")
                    print("|Mythical Creatures ('mc' for shot)                                        |")
                    print("|Jobs                                                                      |")
                    print("---------------------------------------------------------------------------")
                    print("(If you wish to go back, type 'back')")
                    theme = input("Theme: ").lower()
                    #input validation
                    while (theme != "all") and (theme != "mythical creatures") and (theme != "mc") and (theme != "jobs") and (theme != "back"):
                        print("Invalid input, please pick a theme from the ones below:")
                        print("---------------------------------------------------------------------------")
                        print("|All                                                                       |")
                        print("|Mythical Creatures ('mc' for shot)                                        |")
                        print("|Jobs                                                                      |")
                        print("---------------------------------------------------------------------------")
                        print("(If you wish to go back, type 'back')")
                        theme = input("Theme: ").lower()
        #credits
        elif choice == "credits":
            while eternal0:
                while eternal01:
                    border2()
                    print("Phoenix  |   Main developer and innovator")
                    print("Ming     |   Secondary developer and designs")
                    print(" ")
                    border2()
                    exiting = input("Enter y to go back_").lower()
                    eternal01 = False
                    if exiting == "y":
                        pass


