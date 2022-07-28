import random
import string
words=['India','Universe','Programming','Language','Laptop','Python','Github']
def getvalid_word(words):
    word=random.choice(words)
    return word.upper()

def Hangman():
    word=getvalid_word(words)
    alphabet=set(string.ascii_uppercase)
    guesses=''
    lives=10
    while len(word)>0:
        your_word=''
        for cha in word:
            if cha in guesses:
                your_word = your_word + cha
            else:
                your_word = your_word +'_ '
        if your_word == word:
            print("You won !Yay !.... the word was :"+ word )
            break
        
        print("Guess the word", your_word)
        guess=input().upper()
        if guess in alphabet:
            guesses=guesses + guess
        else:
            print("Please Enter a valid character")
            guess=input(" Guess a valid letter ").upper()
        if guess not in word:
            lives -= 1
            if lives== 9:
                print("9 lives left")
                print("----------------")
            if lives== 8:
                print("8 lives left ")
                print("----------------")
                print("       O        ")
            if lives== 7:
                print("7 lives left")
                print("----------------")
                print("       O        ")
                print("       |         ")
            if lives== 6:
                print("6 lives left")
                print("----------------")
                print("        O        ")
                print("        |         ")
                print("       /          ")
            if lives== 5:
                print("5 lives left")
                print("----------------")
                print("        O        ")
                print("        |         ")
                print("       / \       ")
            if lives== 4:
                print("4 lives left")
                print("----------------")
                print("        O /       ")
                print("        |         ")
                print("       / \        ")
            if lives== 3:
                print("3 lives left")
                print("----------------")
                print("      \ O /       ")
                print("        |         ")
                print("       / \        ")
            if lives== 2:
                print("2 lives left")
                print("----------------")
                print("       \O/  |     ")
                print("        |         ")
                print("       / \        ")
            if lives== 1:
                print(" only 1 turn left !!!")
                print("----------------")
                print("       \O/___|     ")
                print("        |         ")
                print("       / \        ")
            if lives==0:
                print(" You have no more turn  !!!")
                print("----------------")
                print("        O___|     ")
                print("       /|\        ")
                print("       / \        ")
                print("You died!! Sorry, the word was: " ,word)
                break
name=input("Enter Your name  ")
print(f'Welcome to Hangman game {name}')
print("You have 10 attempts to guess")
Hangman()
            
            
            
            
            
            

        