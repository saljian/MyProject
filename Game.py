import random
def welcome():
    '''This function will creates a welcome page for our gaming applicaton'''
    for i in range (0,24): #first line
        print("\033[1;33m* \t",end="") # \033[1;33m - unicode for yellow color
    print()
    for i in range(0,24):  #Second line
        print("* \t", end="")
    print()
    print("*\t*",end="")   #third line
    for i in range(0,21):
        print("\t", end="")
    print("*\t*")
    print("*\t*", end="")  #Forth line
    for i in range(0, 21):
        print("\t", end="")
    print("*\t*")
    print("*\t*",end="")   #Fifth line
    for i in range(0,10):
        print("\t\033[0m",end="") # \033[0m- end
    print("\033[1m WELCOME \U0001f600 \033[0m",end="") # \U0001f600- emoji , \033[1m- bold
    for i in range(0,9):
        print("\033[0;36m\033[1m\t",end="") # \033[0;36m- cyan
    print("*\t*")
    print("*\t*", end="")  # sixth line
    for i in range(0, 21):
        print("\t", end="")
    print("*\t*")
    print("*\t*", end="")  # seventh line
    for i in range(0, 21):
        print("\t", end="")
    print("*\t*")
    for i in range (0,24): # eigth line
        print("* \t",end="")
    print()
    for i in range(0,24):  # nineth line
        print("* \t", end="")
    print("\033[0m\n")
    for i in range(0,9):
        print("\t",end="")
    input("Press any key to start \U0001F929")


def mainmenu():
    '''This function will creates a menu page for our gaming applicaton'''
    print("\n\033[1mWHICH GAME YOU WANTS TO PLAY? \033[0m\n") #\033[4m-underline , \033[0m-end
    print("1. Rock Paper Scissors\n2. Cows And Bulls\n3. Exit\n")
    ch=int(input("ENTER YOUR CHOICE: "))
    print("\n")
    if ch==1:
        rockpaperscissormenu()
    elif ch==2:
        cowsandbullsmenu()
    elif ch==3:
        print("Do you really wants to exit?")
        print("Press 1 for YES\nPress 2 for NO")
        ech=int(input("\nEnter your choice here: "))
        if(ech==1):
            print("\nTHANK YOU FOR PLAYING!")
            exit()
        elif(ech==2):
            mainmenu()
    else:
        print("Invalid choice \U0001F61E")
        mainmenu()


def rockpaperscissormenu():
    '''This function will creates a rock paper scissor menu page for our gaming applicaton'''
    print("\033[4m\033[1m ROCK PAPER SCISSORS \033[0m")
    print("1. Play\n2. Rules\n3. Return to main menu\n")
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        rockpaperscissor()
    elif ch == 2:
        rockpaperscissorrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice\U0001F61E")
        rockpaperscissormenu()

def rockpaperscissor():
    '''This function will creates a rock paper scissor game for our gaming applicaton'''
    print("\n\033[1m\033[94m*************************\033[4m\033[1m WELCOME TO ROCK PAPER SCISSORS\033[0m\033[94m\033[1m *************************\033[0m")
    print("\nYou will be competing against the computer. The player that scores 5 points first will be declared as the winner.\n")
    print("If you choice is ROCK. Please enter 0 ")
    print("If you choice is PAPER. Please enter 1 ")
    print("If you choice is SCISSORS. Please enter 2 ")
    print("If you wish to exit. Please enter -1 ")
    user_score=0
    comp_score=0
    count=0 #to prevent loop for infinite iteration
    chc=["ROCK","PAPER","SCISSORS"]
    while(user_score<5 and comp_score<5 and count<25):
        count+=1
        user_choice=int(input("\nEnter your choice: "))
        if(user_choice==-1):
            print("Thank You!")
            break
        comp_choice=random.choice([0,1,2])
        if(user_choice==0 and comp_choice==1):
            print("\nPaper covers rock!")
            comp_score+=1
        elif(user_choice==0 and comp_choice==2):
            print("\nRock smashes scissor!")
            user_score+=1
        elif (user_choice == 1 and comp_choice == 0):
            print("\nPaper covers stone!")
            user_score += 1
        elif (user_choice == 1 and comp_choice == 2):
            print("\nScissors cut paper!")
            comp_score += 1
        elif (user_choice == 2 and comp_choice == 0):
            print("\nRock smashes scissor!")
            comp_score += 1
        elif (user_choice == 2 and comp_choice == 1):
            print("\nScissors cut paper!")
            user_score += 1
        elif(user_choice>2):
            print("\nInvalid choice! Please enter your choice again")
            continue
        print("\033[1mYou: \033[0m",chc[user_choice],"\t\t\t\033[1mComputer: \033[0m",chc[comp_choice]) #\033[1m-bold \033[1m-end
        print("\033[1mYour score: \033[0m",user_score,"\t\t\t\033[1mcomputer score: \033[0m",comp_score)
    if(user_score>comp_score):
        print("\n\033[1m\033[94m@@@@@@@@@@@@@@@@@@@@ \U0001F604 Congratulations! You Win @@@@@@@@@@@@@@@@@@@@\033[0m\n")
    elif(comp_score>user_score):
        print("\n\033[1m\033[94m @@@@@@@@@@@@@@@@@@@@ \U0001F610 Oops! Sorry, You lose. Better luck next time.@@@@@@@@@@@@@@@@@@@@\033[0m\n")
    else:
        print("\n\t\t\t\t\t\t\t\t\033[1m\033[94m@@@@@@@@@@@@@@@@@@@@ \U0001F611 Match Draw!@@@@@@@@@@@@@@@@@@@@\033[0m\n")
    rockpaperscissormenu()

def rockpaperscissorrules():
    print("\n\033[1m\033[4mRULES:\033[0m")
    print("1.Game should be played between two players. Here you will be competing against the computer\n2.Each player have to select one shape between the Rock, paper and scissore.")
    print("3.If rock and paper comes the paper covers the rock and get one point.\n4.If rock and scissors come then rock smashes the scissor and get one point.\n5.If paper and scissors comes the scissors cut the paper and get one point. \nThe player that scores 5 points first will be declared as the winner.")
    print("\n*****BEST OF LUCK*****")
    input("\nPress any key to go back\n")
    rockpaperscissormenu()

def cowsandbullsmenu():
    '''This function will creates cows and bulls menu page for our gaming applicaton'''
    print("\n\033[4m\033[1m COWS AND BULLS\033[0m")
    print("1. Play\n2. Rules\n3. Return to main menu")
    ch = int(input("\nENTER YOUR CHOICE: "))
    if ch == 1:
        cowsandbulls()
    elif ch == 2:
        cowsandbullsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice")
        cowsandbullsmenu()


def cowsandbulls():
    '''This function will creates cows and bulls game for our gaming applicaton'''
    print("\n\033[1m\033[94m*************************\033[4m\033[1m WELCOME TO COWS AND BULLS\033[0m\033[94m\033[1m *************************\033[0m")
    numbers=["1243","7483","8649","3562","7823","6378","5374","6789","1245","7641"]
    rand=random.randrange(0,10)
    number=numbers[rand]
    count=0
    while(count<15):
        num=input("\nEnter your number: ")
        if(num==-1):
            print("Thank You!")
            return
        elif(len(num)>4 or len(num)<4):
            print("Invalid choice! ")
            continue
        cows=0
        bulls=0
        chars=0
        for c in num:
            if c in number:
                chars+=1
        for i in range(0,4):
            if num[i]==number[i]:
                bulls+=1
        cows=chars-bulls
        print("COWS: ",cows,"\tBULLS: ",bulls)
        if(bulls==4):
            print("\n\033[1m\033[94m@@@@@@@@@@@@@@@@@@@@ \U0001F604 Congratulations! You Win @@@@@@@@@@@@@@@@@@@@\033[0m\n")
            print("The number is: ", number)
            cowsandbullsmenu()
        count+=1
    print("\n\033[1m\033[94m @@@@@@@@@@@@@@@@@@@@ \U0001F610 Oops! Sorry, You reached maximum limit.@@@@@@@@@@@@@@@@@@@@\033[0m\n")
    print("The number is: ", number)
    cowsandbullsmenu()

def cowsandbullsrules():
    print("\n\033[1m\033[4mRULES:\033[0m")
    print("1.Game should be played between two players. Here you will be competing against the computer.\n2.The computer take one 4 digit number.\n3.You should have to guess that number.\n3.The digits in the number should not be repeated.\n4.Before exceding the maximum number of limits you should have to guess that number.")
    print("5.The number of digits you guess in correct place then that number of bulls you will get.\n6.If if you guess the digit but now in correct place the You will get cows")
    print("7.To win the game you should have to score 4 Bulls")
    print("\n*****BEST OF LUCK*****")
    input("\nPress any key to go back\n")
    cowsandbullsmenu()
welcome()
print("\n"*100)
mainmenu()
