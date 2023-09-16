#!/usr/bin/env python3
#Levi Noell-Baba, June 17, 2023, CPT-168-W17, Lab 5-2        
def get_float(prompt, low, high): #definition fo the get_number function that calls 3 arguments of a prompt
    while True: #code for an infinite while loop that checks for entry into the get_number() function until the value is greater than 0 and less than or equal to 1000
        number = float(input(prompt)) #variable "number" that connects to the get_float function that accepts an argument
        if number > low and number <= high: #an if statement that uses the and logical operator to check if the value is within the specified conditions.
            is_valid = True #if conditions are met, the argument equates to True and returns the number variable.
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.") #error message that displays if a number outside of acceptable conditions is entered.
            
def get_integer(prompt, low, high): #definition of get_integer function that calls 3 arguments for prompts
    while True: #check for entry into the get_integer() gunction that the value is greater than 0 and less than of equal to 50
        number = int(input(prompt)) # the number variable thats connected to the get_integer function that accepts an argument
        if number > low and number <= high: #if statement that uses the and logical operator that checks if the value is within both conditions
            is_valid = True #value is set to true if the conditions are met and the number variable is returned.
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.") #error message displayed if input is outside of conditions
            
def calculate_future_value(monthly_investment, yearly_interest, years):
    #print("Entering calculate_future_value()")
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 #Logic Error - An additional division by 100 needed to be added here
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months +1): #Logic Error - Python starts at 1 and stopped at months + 1. now, instead of stopping at "months" which the argument states, it now includes the additional month with the help of the +1 calling argument.
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        #print("i =", i, "future value =", future_value) #print function that displays the values of the variables as it changes each time it passes through.
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
