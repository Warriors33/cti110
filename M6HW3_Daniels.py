#CTI 110
#M6HW3 Factorial
#Quincetta Daniels
#6 Dec 2017
#

userInteger = int( input("Please enter a Positve number: "))

while userInteger< 1:
    userInteger = int( Input("Please enter a positive number please: "))
factorial = 1

for currentNumber in range( 1, userInteger + 1 ):
    factorial = factorial * currentNumber

print( "The factorial of" , userInteger, "is" , factorial )    
    
