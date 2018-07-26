import time
import os
def wiggle():
    for i in range(5):
        os.system('clear')
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	/|\ ")
        print ("|	 |")
        print ("|	/ \ ")
        print ("-------------------------")
        print("  You have been hanged!")
        time.sleep(0.3)
        os.system('clear')

        print ("----------")
        print ("|	 \ ")
        print ("|	  O")
        print ("|         /|\ ")
        print ("|	   )")
        print ("|         / \ ")
        print ("-------------------------")
        print("  You have been hanged!")
        time.sleep(0.2)
        os.system('clear')
        print ("----------")
        print ("|	 |")
        print ("|	 O")
        print ("|	/|\ ")
        print ("|	 |")
        print ("|	/ \ ")
        print ("-------------------------")
        print("  You have been hanged!")
        time.sleep(0.3)
        os.system('clear')

        print ("----------")
        print ("|	 / ")
        print ("|	O")
        print ("|     /|\ ")
        print ("|      (")
        print ("|     / \ ")
        print ("-------------------------")
        print("  You have been hanged!")        
        time.sleep(0.2)

def main():
    wiggle()

if __name__ == '__main__':
    main()