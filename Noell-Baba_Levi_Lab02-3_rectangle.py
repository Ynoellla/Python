#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
Length = float(input("Please enter the length:  "))
Width = float(input("Please enter the width:  "))

# calculate miles per gallon
Area = (Length * Width)
Perimeter = ((2 * Length) + (2 * Width))
#mpg = miles_driven / gallons_used
#mpg = round(mpg, 2)
            
# format and display the result
print()
print(f"Area = {Area}")
print(f"Perimeter = {Perimeter}")
#print(f"Miles Per Gallon:\t\t{mpg}")
print()
print("Bye!")


