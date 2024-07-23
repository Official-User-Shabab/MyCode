import random
import time

# A lot of if else statements make it less sustainable long term
# Separate functions/classes for scenarios?
# First map out all options in game first

def credits():
    nok0 = True
    nok1 = True
    while nok0:
        while nok1:
            time.sleep(1)
            border()
            print("CREDITS:")
            time.sleep(1)
            print("  ")
            time.sleep(1)
            print("Shabab: Development and Programming\n"
            "Pingu: Innovation and Creativity\n"
            "Phoenix: Support and Programming\n")
            nok1 = False
    
def border():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def dead():
    print('''
    You lose all your lives, hence ending the game.
          _______     
         /       \    
        | (X) (X) |   
         \   ^   /    
          !|||||!     
         '\_____/'    

    ''')
    print(" ")
    credits()


def life_x():
    if lives == 3:
        print(f"---¥¥¥~~~You have {lives} lives left.~~~¥¥¥---\n")
    if lives == 2:
        print(f"---¥¥~~~You have {lives} lives left.~~~¥¥---\n")
    if lives == 1:
        print(f"---¥~~~You have {lives} lives left.~~~¥---\n")
    if lives == 0:
        print(f"---~~~You have {lives} lives left.~~~---\n")

def win():
    runs0 = True
    runs1 = True
    while runs0:
        while runs1:
            print(" ")
            print(" ")
            print("Well done!!! You have lived through, and won the game!")
            print("Thank you for playing the game")
            border()
            credits()
            runs1 = False
            
def dayR1(l):
    time.sleep(2)
    print("After a few days you go to your grandfather's grave to give a visit.")
    print("It's in Athens, Greece.")
    print("You are in Istanbul, do you fly there or drive there?")
    time.sleep(2)
    ans = input("Type 'y' for flying and 'n' for driving_")
    print(" ")
    border()
    time.sleep(2)
    # 2 lives
    if ans == 'y':
        print("You were killed by anti aircraft guns.")
        print("You then lost another life by being shot by the soldiers.\n")
        l = l - 2
        time.sleep(2)
        print(f"--~~~You have {l} lives left.~~~--")
        return l
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
    elif ans == 'n':
        time.sleep(2)
        print("You arrive and mourn.")
        print("You also realise that you accidentally prayed to the wrong grave, in Ulaanbatar, a very hisotrical city.")
        time.sleep(2)
        print("However, from locals, your pet horse was involved with something paranormal around here, so do you stay?")
        time.sleep(2)
        ans = input("Type 'y' for Istanbul and 'n' for Ulaanbatar_")
        time.sleep(2)
        border()
        if ans == 'y':
            time.sleep(2)
            print("You go back to Istanbul")
            print("As you land in Istanbul and get out of the car,")
            time.sleep(2)
            print("You suddenly see a person in full black running at you with a knife.")
            time.sleep(2)
            print("What do you do?")
            time.sleep(2)
            ans = input("Type 'y' for Taekwondo-Jitsu, 'n' for Hybrid martial arts, or 'p' for running away_")
            time.sleep(2)
            border()
            time.sleep(2)
            if ans == 'y':
                print("He throws the knife at you and you lose a life.")
                l = l - 1
                time.sleep(2)
                print("Suddenly you wake up in a coffee shop and get drowned in coffee by the same man.")
                l = l - 1
                time.sleep(2)
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
            elif ans == 'n':
                time.sleep(2)
                print("You're a bit rusty, but you successfully fend off the man, who runs away, dropping the knife.")
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURN TO MAIN CODE
            elif ans == 'p':
                time.sleep(2)
                print("The man chases you down, and stabs you to death, making you lose a life.")
                print("The bleeding and loss of blood also take away another life, coz why not, I'm outta ideas here.")
                time.sleep(2)
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                l = l - 2
                time.sleep(2)
        elif ans == 'n':
            #1 lives
            print("Your pet horse kills you because it wanted to go back home, and pet food sucks there.")
            time.sleep(2)
            l = l - 1
            print(f"--~~~You have {l} lives left.~~~--\n")
            # coconut number was chosen depending on how many lines there were in code at that time
            print("Suddenly, out of no where, you notice 355 coconuts being thrown at you.")
            print("You have about 100 baskets that can fit 2 coconuts each, and about 140 hungry crabs in your pocket.")
            print("Do you risk your life by trying to fend off from this coconut attack, or retreat and hide?")
            ans = input("Type 'y' for fend off, 'n' for hide_")
            border()
            chance = random.randint(1, 10)
            if chance >= 7 and ans == "y":
                print("Well done! You successfully collect all the coconuts and the crabs eat the rest.")
                print("However, as you're walking back to the city, you see a man, who must've been hurt by coconuts.")
                ans = input("Type 'y' to help him, or 'n' to leave him_")
                border()
                time.sleep(2)
                if ans == "y":
                    print("What a kind heart you have, yet such an unlucky fate...")
                    time.sleep(2)
                    print("The man was dead all along, and you have awoken and disturbed his evil soul.")
                    time.sleep(2)
                    print("You have started the zombie apocalypse in Mongolia, and lose all your lives,")
                    print("because he bites you and turns you into the walking dead as well\n")
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                    l = 0
                if ans == "n":
                    print("The man, named Billy George Jay, nearly died, but survived in the end.")
                    print("He seeks long term revenge on you now. Way to go, making enemies eh?")
                    #MADE ENEMY FOR THE FUTURE
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURN TO MAIN CODE
                    time.sleep(2)
            elif chance < 7 and ans == "y":
                print("Despite your hardest efforts, there were 2 coconuts left, which hit you on the head at light speed.\n")
                time.sleep(2)
                l = l - 1
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                print(f"--~~~You have {l} lives left.~~~--\n")
            elif ans == "n":
                time.sleep(2)
                print("Your coward-like action got you kicked out of Mongolia and shot on the way back.")
                l = l - 1
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                print(f"--~~~You have {l} lives left.~~~--\n")

    return l

def dayR2(l):
    ######################### STILL IN CONSTRUCTION
    print("Suddenly, you wake up into an ancient land, and a higher life form appears in front of you...\n")
    print('''
        ::::::::|/''"""'""""-:;:::::::       
        :::::|-`               "-;::::       
        ::::;_       _,,._       ¬;:::       
        ::::_       .::::::,       '::       
        :::::       :::::::;.       |:       
        ::::: ,.      ¬:::::;.       :       
        :::;           ,,:::::;      :       
        ::.  :.:        .::::::, _::,:       
        ::   :|:,      _:::::::::::-;:       
        ::-.;::|:      ¬::::::: |::;.:       
        ::;:_'---'     ;;'"¬--   :::::       
        ::; '|          ;     :  |::::       
        ::| ,:___..`           _; ::::       
        :::..::: '             -" ::::       
        :::;'::                  /::::       
        ::::,''              .__::::::       
        ::::;.            ._::::::::::       
        ::::;           __::::::::::::       
        :::::;_____    '::::::::::::::       
        :::::::::::;,   ::::::::::::::       
        ::::::::::::;   ¬:::::::::::::       
        ::::::::::::/ '  ::: :::::::::       
        ::::::::|-::        ::::::::::       
        ::::#-""- :::      .'::|"---""       
        :|-'  ___,:::,    .|.¬- __,.::       
                  
            - Ernest Khalimov, Gigachad
    ''')
    time.sleep(2)
    return l
    

def dayR3():
    pass
    # still in development...
    # print("You get bored waiting at a gas station,")
    # print("So now you can either play something on your phone,")
    # print("Or listen to some downloaded music on  an mp3")
    # ans = input("Type in 'y' for games, and 'n' for music_")
    # border()
    # lives = 0



#=========VARIABLES=======================================================
eternal = 1
running = True
lives = 3
#=================================================================

# WHENEVER TAKING A LIFE AWAY, USE THIS WHOLE SNIPPET IN MAIN CODE:~~~~~~~~~~~~~~~~~~~~~~~~~~~
#lives = lives - 1
#life_x()
#if lives == 0:
#    break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def intro():
    #####################INTRODUCTION######################################-------------------
    time.sleep(2)
    print(" ________________________________________________________________________________________\n"
    "/This game is played by making choices. After each paragraph of plot, you'll be         |\n"
    "|given choices relevant to the that segment - both nice and not so nice. Remember       |\n"
    f"|that you are only given {lives} lives to live through, making the wrong choice in the        |\n"
    "|wrong situation costs you a life of each. Lose them all, and it's game over.           |\n"
    "`--------------------------------------------------------------------------------------¬ \\\n"
    "                                                                                        \ \\\n"
    "                                                                                         \ \\\n"
    "                                                                                          \/\n")
    time.sleep(9)
    print(" ")
    print(" ________________________________________________________________________________________\n"
    "/However don't be silly enough to play it too safe by being nicer than you'd like       |\n"
    "|to be. In some segments making the right type of wrong choice can actually make        |\n"
    "|more interesting events take place, thus you get to experience more content and        |\n"
    "|scenarios in the game that a pacifist would miss.                                      |\n"
    "`--------------------------------------------------------------------------------------¬ \\\n"
    "                                                                                        \ \\\n"
    "                                                                                         \ \\\n"
    "                                                                                          \/\n")
    time.sleep(8)
    print(" ")
    print(" ________________________________________________________________________________________\n"
    "/So, consider the time, place and person you're dealing with. Make right choice         |\n"
    "|in the wrong times and don't hesitate to make a wrong choice at just the right time!   |\n"
    "|                                                                                       |\n"
    "|(PS: This program is still in its Alpha phase)                                         |\n"
    "`--------------------------------------------------------------------------------------¬ \\\n"
    "                                                                                        \ \\\n"
    "                                                                                         \ \\\n"
    "                                                                                          \/")
    time.sleep(4)
    print(" ")
    print(" __________________________________________________________________________________________\n"
    "|Enjoy...                                                                                  |\n"
    "`---------------------------------------------------------------------------------------¬  |\n"
    "                                                                                         \ \\\n"
    "                                                                                          \ \\\n"
    "                                                                                           \/")
    time.sleep(3)
    print(" ")
    print(" ")
    ans = input("Type in 'y' to start_")
    return ans
    border()
    ##################################################################################



##############################################################################

ans = intro()

while eternal == 1:
    while running == True:
        while lives > 0:
            if ans == "y":
                # 3 lives
                border()
                time.sleep(2)
                print("You're talking to your mother on the phone, but only 2% battery is left.The charging rate of")
                time.sleep(1)
                print("your phone is 1% per minute and usage is -0.5% per minute.Do you charge your phone whilst on the phone")
                time.sleep(1)
                print("with your mother? Remember, she's your mother and she'll think hanging up means ignorance.\n")
                time.sleep(3)
                ans = input("Type 'y' for charging phone whilst talking but 'n' for waiting to run out, then charge_")
                time.sleep(2)
                border()
                if ans == 'y':
                    print("The phone explodes internally.\n")
                    lives = lives - 1
                    life_x()
                    time.sleep(2)
                    if lives == 0:
                        break
                    print("Since your mother thought you hung up on her, she decides for one day, you have to\n"
                    "COOK your OWN food.\n"
                    "So you do.\n")
                    time.sleep(2)
                    print("You are given the option to cook a salad.\n"
                    "However you use a knife\n"
                    "But you can cook carrot-cake flavoured tea.\n"
                    "By using the boiling water in the kettle, you have little experience doing this.\n")
                    time.sleep(3)
                    print("Which recipe do you cook?\n")
                    ans = input("Type 'y' for carrot-cake flavoured tea or 'n' for a salad_")
                    border()
                    time.sleep(2)
                    if ans == 'y':
                        print("You make your meal successfully.")
                        time.sleep(1)
                        print("After a few days you go to your grandfather's grave to give a visit.")
                        time.sleep(1)
                        print("It's in Amsterdam, Netherlands.")
                        time.sleep(2)
                        print("You are currently in Istanbul, do you fly there or drive there?")
                        time.sleep(1)
                        ans = input("Type 'y' for flying and 'n' for driving_")
                        border()
                        time.sleep(2)
                        if ans == 'y':
                            print("You lost a life from being shot down by anti aircraft guns.")
                            time.sleep(2)
                            print("You then lost your other life by being shot by the soldiers.")
                            time.sleep(2)
                            lives = lives - 2
                            life_x()
                            time.sleep(2)
                            if lives == 0:
                                break
                                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                        elif ans == 'n':
                            print("You arrive and mourn successfully.")
                            time.sleep(1)
                            print("You realise that you are in Fukushima, a very radioactive city due to its history.")
                            time.sleep(1)
                            print("However, your cousins were involved with something around here, as said by monks,")
                            time.sleep(1)
                            print("so do you stay to find out or do you leave and go back to Istanbul?")
                            time.sleep(1)
                            ans = input("Type 'y' for Istanbul and 'n' for Fukushima_")
                            print(" ")
                            time.sleep(1)
                            border()
                            if ans == 'y':
                                print("You go back to Istanbul")
                                time.sleep(1)
                                print("As you get out of the car and land on Istanbul,")
                                time.sleep(1)
                                print("You suddenly see a person in black running at you with a knife.")
                                time.sleep(1)
                                print("What do you do?")
                                print(" ")
                                # 2 lives
                            elif ans == 'n':
                                print("You lost a life from radiation")
                                lives = lives - 1
                                life_x()
                                if lives == 0:
                                    break
                                #1 life
                                # make at least one route winning from here
                                print("From reading ancient scripts, you realise that your cousins are guardians for the city,\n"
                                "Now you are another guardian, and your job is to protect the city from ghouls...\n"
                                "...perfect timing,\n")
                                print("  ")
                                time.sleep(4)
                                print("Suddenly, some weak ghouls appear before you, to defeat you and destroy the city,\n"
                                "Do you defend the city and eliminate the ghouls?")
                                time.sleep(1)
                                ans = input("Type 'y' for defend city, or 'n' make friends with the ghouls_")
                                time.sleep(1)
                                border()
                                if ans == 'y':
                                    print("You successfully fend off the ghouls, burning them alive with your powers.")
                                    time.sleep(1)
                                    win()
                                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WIN
                                else:
                                    time.sleep(1)
                                    print("The other guardians kill you and the ghouls...")
                                    time.sleep(1)
                                    lives = lives - 1
                                    life_x()
                                    if lives == 0:
                                        break
                                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                    elif ans == 'n':
                        print("The using of a knife,")
                        print("cut your hand.")
                        lives = lives - 1
                        #1 Life
                        life_x()
                        time.sleep(2)
                        border()
                        if lives == 0:
                            break
                        print("As you swim 50 miles and climb 3 mountains to go to the hospital, you suddenly fall into a\n"
                        "vortex in the sky, and it sucks you into another universe...\n")
                        #new universe
                        lives = dayR2(lives)
                        if lives == 0:
                            break
                        
                elif ans == 'n':
                    time.sleep(2)
                    print("Because your mother thought you hang up on her,")
                    print("you now have to go to...your cousin's house")
                    print("Since she can't stand you anymore.")
                    print("And so you go there, but the first meal he gives you at dinner is")
                    time.sleep(2)
                    print("Nuts")
                    time.sleep(2)
                    print("Would you eat that or eat nothing but drink a cup of slightly blue milkshake?\n")
                    # Here doomed - when left on one life the 'almondy feel' kills them from cyanide in this drink
                    ans = input("Type 'y' to eat nuts but 'n' to drink slightly blue milkshake_")
                    border()
                    time.sleep(2)
                    if ans == 'y':
                        print(" ")
                        print("You choke on the nuts.\n")
                        time.sleep(2)
                        print("You lose a life.")
                        lives = lives - 1
                        life_x()
                        if lives == 0:
                            break
                        breakoff = dayR1(lives)
                        if breakoff == 0:
                            break
                        lives = breakoff
                        border()
                        time.sleep(1)
                        
                        print("What animal is like a jellyfish, can be extremely big, is underwater, and is technically\n"
                        "a lot of souls or bodies but organised in one body, and starts with 's', ends with 'e', and is the\n"
                        "favourite animal of the developer of this game you're playing right now?\n")
                        ans = input("Type in which animal you think it is (it's one word)_")
                        print(" ")
                        border()
                        time.sleep(1)
                        if ans.lower() == "siphonophore":
                            print("Well, correct!")
                        else:
                            print("Incorrect answer. You've probably never heard of this creature...anyway that's one life gone.")
                            lives = lives - 1
                            life_x()
                            if lives == 0:
                                break
                            border()
                            time.sleep(1)
                            print("You may have lived through, but remember your enemy from 10 years ago, Billy George Jay?")
                            time.sleep(3)
                            print("He spawns in and throws a coconut towards you at the speed of light, wiping off the face of the Solar system.")
                            time.sleep(2)
                            border()
                            lives = lives - 1
                            life_x()
                            if lives == 0:
                                break
                                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                    elif ans == 'n':
                        print("An almondy-feel rushes through your system once you consume it.\n")
                        time.sleep(1)
                        print("But never mind that, you have bigger problems to face!\n")
                        time.sleep(2)
                        border()
                        print("As you're walking to the public library at 0430 am to read ")
                        time.sleep(1)
                        print("a nice extract from Shakespeare's Macbeth, a BIG spider with a")
                        time.sleep(1)
                        print("machette flies toward you! Your instincts give the option to ")
                        time.sleep(1)
                        print("either shoot the big spider with a cube-shaped nerf gun, or morph")
                        time.sleep(1)
                        print("into a power ranger.\n")
                        time.sleep(3)
                        ans = input("Type 'y' for cube-shaped nerf gun, or 'n' for morphing_")
                        border()
                        time.sleep(2)
                        if ans == "y":
                            print("You hastily pull out your cube-shaped nerf gun from your pocket")
                            print("and shoot the crazy flying big spider with high firepower...")
                            time.sleep(2)
                            print("But oh no! The big spider evades all the plasma bullets by doing an ancient")
                            print("shuffle dance from Tik Tok, and it seems like it hates you now...\n")
                            time.sleep(2)
                            print("With extreme rage, the big spider swims rapidly mid-air straight at you")
                            print("and does a triple-spinning flying kick to your face and plucks your ")
                            print("eyebrows out one by one while putting you in an un-moveable headlock ")
                            print("position and making you listen to Rick Astley's 'Never gonna give you up'.\n")
                            time.sleep(2)
                            print("Will a weakling like you plead for mercy?\n")
                            time.sleep(2)
                            ans = input("Type 'y' for begging for mercy or 'n' to use Judo_")
                            border()
                            if ans == 'y':
                                print("You fool! You fell victim to one of the classic blunders!\n")
                                time.sleep(2)
                                print("The big spider, however, being so kind and benevolent decides to kidnap")
                                print("you on a hovering roller coaster and send you off to the Bubble Tea world.")
                                time.sleep(2)
                                print("...")
                                time.sleep(2)
                                print("The next thing you know once you awaken from a deep sleep is that a ")
                                print("large mickey mouse holds you hostage in a Boba restuarant, and gives you")
                                time.sleep(2)
                                print("a chance to buy your freedom. You have to answer all the questions correctly,")
                                print("and let's just say getting a question wrong...shall have reprocussions.\n")
                                time.sleep(2)
                                print('''

                                         .-"""-.      
                                        /       \     
                                        \       /     
                                 .-"""-.-`.-.-.<_     
                                /           \  /| _   
                                |      _,-\ ()()_/:)  
                                \     / ,  `     `|   
                                 '-..-| \-.,___,  /   
                                       \ `-.__/  /    
                                        `-.__.-'`     

                                ''')
                                time.sleep(2)
                                print("Mick:Well, another customer! How lucky I am on this fine day...")
                                time.sleep(2)
                                border()
                                ans = int(input("1) What is the result of 10853983 + 7825931?_"))
                                ansRight = 10853983 + 7825931
                                if ans == ansRight:
                                    print("Mick:WELL DONE, but that was an easy one...\n")
                                    ans = int(input("2) What year did Vincent Van Gogh die?_"))
                                    border()
                                    if ans == 1890:
                                        print("Mick:Well, correct you are!")
                                        print("Mick:You must be thinking these are easy, eh, smarty pants?")
                                        print("Mick:Well guess what??? YOU CAN'T FOOL ME.")
                                        print("Mick:I KNOW THAT YOU USED SOME SORT OF HELP TO ANSWER THESE...")
                                        print("Mick:WHETHER IT BE A CALCULATOR OR THE INTERNET...OR EVEN THAT BRAIN OF YOURS")
                                        print("Mick:Speaking of which...yes...that is the PERFECT punishment...\n")
                                        print("Suddenly, Mickey rips your brains out, and so you lose a life...\n")
                                        lives = lives - 1
                                        life_x()
                                        if lives == 0:
                                            break
                                        print("...but the excess bleeding takes away another life!\n")
                                        lives = lives - 1
                                        life_x()
                                        if lives == 0:
                                            break
                                        print("...and suddenly, the nightmare you've always feared is coming true...")
                                        print("You are trapped in a small cave in the desert...but with DORA THE EXPLORER!")
                                        print("You lose a life because you couldn't help Dora find the exit of the cave.\n")
                                        lives = lives - 1
                                        life_x()
                                        if lives == 0:
                                            break
                                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                                else:
                                    print("Mick:Seems like you slipped up...on a SIMPLE math question")
                                    print("Mick:Clearly...things didn't add up, eh?")
                                    print("Mick:Sadly, you'll be punished now.")
                                    print("Mick:Remember that slightly blue milkshake you drank?")
                                    print("Mick:Well, it had cyanide mixed into it, (And guess who mixed it in?)")
                                    print("Mick:That 'almondy' feel will now take its effects, stealing a life...")
                                    lives = lives - 1
                                    life_x()
                                    if lives == 0:
                                        break
                                    print("Mick:...but that's not all!")
                                    print("Mick:Now I shall take another life, by drowning you in BOBA.  >:)\n")
                                    lives = lives - 1
                                    life_x()
                                    if lives == 0:
                                        break
                                    print("\n")
                                    print("Mick:Ahem, so continuing on...give them an easy one please.\n")
                                    time.sleep(2)
                                    border()
                                    ans = input("2)Which continent, did the developer of this game come from? (Europe/Africa etc)_")
                                    if ans.lower() == "asia":
                                        time.sleep(2)
                                        print("Mick:WELL, WELL, WELL! CORRECT!")
                                        time.sleep(2)
                                        print("Mick:But that was easy of course...hahaha.\n")
                                        time.sleep(2)
                                        print("Mick:Time for another question...\n")
                                        time.sleep(2)
                                        print("3) Five birds are on a tree, and you just shot one of those birds")
                                        print("down, dead, with a rifle, about 13m from the tree. So how many")
                                        print("birds left on the tree now?")
                                        time.sleep(2)
                                        ans = int(input("Type in the number_"))
                                        border()
                                        print(" ")
                                        if ans == 0:
                                            time.sleep(2)
                                            print("Mick:Well, correct you are!")
                                            print("Mick:You must be thinking these are easy, eh, smarty pants?")
                                            print("Mick:Well...final question, for your freedom...\n")
                                            time.sleep(2)
                                            print("(Type in one word only, most likely the keyword)")
                                            ans = input("Cause of Steve Job's death_")
                                            if ans.lower() == "cancer":
                                                print("Mick:Awww...seems like you've escaped from my clutches lucky duck...\n")
                                                time.sleep(2)
                                            else:
                                                time.sleep(2)
                                                print("CORRECT!!!                               ,not\n")
                                                time.sleep(2)
                                                print("Mickey drowns you in bubble tea.")
                                                time.sleep(2)
                                                lives = lives - 1
                                                life_x()
                                                if lives == 0:
                                                    break
                                        else:
                                            print("Mick:Well, correct you are...NOT!\n")
                                            lives = lives - 1
                                            life_x()
                                            if lives == 0:
                                                break
                                            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD

                                    else:
                                        print("Mick:WELL, WELL, WELL...correct........NOT!\n")
                                        print("You get stabbed multiple times while being burnt, losing 2 lives")
                                        lives = lives - 2
                                        life_x()
                                        if lives == 0:
                                            break

                                break
                            elif ans == 'n':
                                break
                            print("Frantically, you take out your morph gadget from")
                            break
                        break
            elif ans.lower() == "wu ming":
                border()
                print('''
                Wait, why didn't you follow the options? What have you done???
                Oh no, you've entered: the PATH OF DARKNESS!

                This hidden section of the game is still being developed...but it shall open soon.

                ''')
                special = True
                while eternal == 1:
                    while special:
                        print('''

                               .,ad00000000baa,                  
                            ,d0P"""        ""9000ba.             
                         .a0"          ,ad00000000000a           
                        aP'          ,00000000000000000a         
                      ,0"           ,00000000000000000000,       
                     ,0'            (000000000( )000000000,      
                    ,0'             `0000000000000000000000      
                    0)               `000000000000000000000,     
                    0                  "0000000000000000000)     
                    0                   `000000000000000000)     
                    0)                    "0000000000000000      
                    (b                     "00000000000000'      
                    `0,        (0)          0000000000000)       
                     "0a                   ,000000000000)        
                       V0,                 d00000000000"         
                        `0b,             ,d0000000000P'          
                          `V0a,       ,ad0000000000P'            
                             ""00000000000000000P"               
                                  """"""""""""                   

                        ''')
                        special = False
                        break
                    #ascii art pls
            else:
                border()
                runs0 = True
                runs1 = True
                while runs0:
                    while runs1:
                        print("You were supposed to type 'y', just restart the program to play.")
                        runs1 = False
                
        time.sleep(2)
        dead()
        running = False
