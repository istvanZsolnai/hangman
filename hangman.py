from getpass import getpass
import animations2
import time


def guessing():
    word_to_guess = getpass("What should we guess?")
    list_of_letters = []
    list_of_stipres = []
    for i in word_to_guess:
        list_of_letters.append(i)
        list_of_stipres.append("-")
    
    print(" -"*len(word_to_guess))
    guesses = 0
    used_letters = []
    drawing(guesses)
    while True:

        while True:
            user_input = input("Your guess: ")
            if len(user_input) != 1:
                print("Please guess only one letter.")
            else:
                break

        if user_input in word_to_guess:
            for i, char in enumerate(word_to_guess):
                if char == user_input:
                    list_of_stipres[i] = list_of_letters[i]
            print("Attaboy")
            print (" ".join(map(str,list_of_stipres)))
            print (" ".join(map(str,used_letters)))
            drawing(guesses)

            if "-" not in list_of_stipres:
                print("Congrats, you guessed it!")
                replay = input("Press r if you want to play again: ")
                if replay.lower() == "r":
                    guessing()
                else:
                    print("see ya then")
                    return False
            
        elif user_input not in word_to_guess:
            guesses += 1
            if guesses == 6:
                drawing(guesses)
                replay = input("Press r to play again: ")
                if replay.lower() == "r":
                    guessing()
                else:
                    print("see ya then")
                    return False
            print("Nope")
            used_letters.append(user_input)
            print (" ".join(map(str,list_of_stipres)))
            print (" ".join(map(str,used_letters)))
            drawing(guesses)
        
        



def drawing(guesses):
    if (guesses == 0):
        print ("----------")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("-------------------------")
    elif (guesses == 1):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|")
        print ("|")
        print ("|")
        print ("-------------------------")
    elif (guesses == 2):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	 |")
        print ("|	 |")
        print ("|")
        print ("-------------------------")
    elif (guesses == 3):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|")
        print ("|	 |")
        print ("|")
        print ("-------------------------")
    elif (guesses == 4):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|")
        print ("-------------------------")
    elif (guesses == 5):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ ")
        print ("-------------------------")
    elif (guesses == 6):
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	/|\ ")
        print ("|	 |")
        print ("|	/ \ ")
        print ("-------------------------")
        print("  You have been hanged!")
        print("You died!")
        time.sleep(2)
        animations2.wiggle()
    else:
        return False
 
            

def main():
    guessing()

if __name__ == '__main__':
    main()