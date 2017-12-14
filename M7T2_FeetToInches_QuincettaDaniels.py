# You will Convert Feet To Inches
#14 Dec 2017
#CTI 110 M7T2_FeetToInches
#Quincetta Daniels
#

def feetToInches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

def main():
    userFeet = float( input( "Please enter the number of feet: " ))
    inches = feetToInches( userFeet )
    print( userFeet, "feet converted to inches is" , format( inches, ".2f"), "inches" )

main()

