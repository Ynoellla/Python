#!/usr/bin/env python3
#Levi Noell-Baba, June 5, 2023, CPT-168-W17, Lab 4-1        
##def get_float(prompt, low, high):# "get_float() function with three arguments to the prompt as well as high and low validity values.
##    while True: #Code for while loop that checks the entry into the "get_float()"function to make sure the value is greater than "0" and less than or equal to "1000".
##        number = float(input(prompt))  #Variable prompt for the "get_float() function
##        if number > low and number <= high: #if statement that uses the coded arguments in the function to determine whether the number fits the parameters
##            is_valid = True
##            return number #return statement that returns the number to the calling function if the number adheres to validation checks.
##        else:
##            print("Entry must be greater than", low,
##                  "and less than or equal to", high,
##                  "Please try again.")
##            
##def get_int(prompt, low, high): #a "get_int()" function with three arguments coded into it. High and low validity values coded in.
##    while True: #while loop that codes for a validation check as to whether the value is within the given parameters to continue with the function. if it is valid, the loop holds as true. otherwise it displays the error message.
##        number = int(input(prompt))# #variable connected to the get_int() function
##        if number > low and number <= high: #if statement that uses an AND logical operator to evaluate expressions to determine if TRUE.
##            is_valid = True
##            return number
##        else:
##            print("Entry must be greater than", low,
##                  "and less than or equal to", high,
##                  "Please try again.")

import validation as v #import statement that imports the validation module. 
               
def calculate_future_value(monthly_investment, yearly_interest, years): #calculation the gives value to "future value" when three arguments are called in the code. 
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 #calculation for monthly interest rate
    months = years * 12 #calculation for number of months

    # calculate future value
    future_value = 0.0 # Future_value is a local variable that can be changed by the code without having to alter a global code. most preferred method.
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest #monthly investment is added to the future value which is then added to by the code after it calculates the monthly interest variable to display the return value of future_value

    return future_value # #a return statement that returns the resule of the calculations to the original calling statement of the function

def main(): # definition of the main function that exectures the statements below when the "main() function is called.
    choice = "y" 
    while choice.lower() == "y":
        # get input from the user. the code has been modified to use the functions from the validation.py module. 
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000) #Mothly investment entry in the main(function) has been modified to check the first entry is between 0 and 1000. 
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15) # yearly interest rate entry of the main() function that has been modiefied to check that the second entry is between 0 and 15. 
        years = v.get_int("Enter number of years:\t\t", 0, 50)# Modification of the number of years entry. results in an integer.

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years) #Function that is defined as future_value to call upon monthly investment, yearly interest rate, and number of years
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}") #displays the future value by use of a chain function to round the future value to 2 decimal places and convert to a string value
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ") # loop that continues tohe process if the input is yes or terminates and breaks out of the loop if the user inputs ("n")
        print()

    print("Bye!")
    
if __name__ == "__main__": #an if statement coded to check if program is the main module.
    main()
