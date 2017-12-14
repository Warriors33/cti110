#CTI 110
#M6HW Running Total
#Quincetta Daniels
#6 Dec 2017
#

total = 0
userNumber = float( input("Please enter the first number of a negative  " + \
                          "number to quit:"))

while userNumber > -1:
    total = total + userNumber
    userNumber = float( input( "Please enter the next number or a " + \
                               "negative number to quit:"))
    print( "\nThe sum of all the numbers you entered is" ,total )
