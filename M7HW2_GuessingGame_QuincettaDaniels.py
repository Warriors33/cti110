# Write a program asking user to guess the nummber
#14 Dec 2017
#CTI 110 M7HW2- Guessing Game
#Quincetta Daniels
#

import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100 )
    return randomNumber

randomNumber = 55

def askUserForNumber():
        userNumber = int( input( "Guess the number: " ))
        return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
            randomNumber = generateRandomNumber()
            userNumber = askUserForNumber()
            message = checkUserNumber( userNumber, randomNumber )

    while message != "Congratulations":
            print( message )
            userNumber = askUserForNumber( "Try again:" )
            message = checkNumber( userNumber, randomNumber )

    print( message )
    userCongratulated = True

main()       



