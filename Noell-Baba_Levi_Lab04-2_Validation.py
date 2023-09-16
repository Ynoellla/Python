#!/usr/bin/env python3
#Levi Noell-Baba, June 5, 2023, CPT-168-W17, Lab 4-2        
def get_float(prompt, low, high): #modified get_float() function that has three arguments to prompt a validity high/low check of parameters.
    while True: # an infinite while loop that checks for entry into the modified get_float() function until the value is greater than 0 and less than 1000.
        number = float(input(prompt)) #variable "number" that is assigned to the get_float() function that is assigned an argument for a prompt that assigns the variable a value.
        if number > low and number <= high: #if statement that uses the "AND" logical operator to evalute the expressions on the left and right of the operator to determine if the value is within the set parameters before continuing.
            return number #return function that returns the value of the variable "number" to the calling statement to be used. 
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)
            
def get_int(prompt, low, high): #a modified "get_int()" function that has three arguments for a prompt and high/low validity checks.
    while True: #an infinite while loop that checks for entry into the modified get_int() function until the value is greater than 0 and less than 1000.
        number = int(input(prompt)) #Variable "number" that is assigned to the get_int() function that is assigned an argument for a prompt that assigns the variable a value.
        if number > low and number <= high: #if statement that uses the "AND" logical operator to evaluate the expressions of the left and right of the operator to determine if the value is within the set parameters before continuing.
            return number # return function that returns the value of the variable "number" to the calling statement to be used.
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)

def main(): # definition fo the "main" function that calls on the statements below
    choice = "y"
    while choice.lower() == "y":
        # get input from user through the modified "get_float()" and "get_int()" functions.
        valid_number = get_float("Enter number: ", 0, 1000) #function called to test the "get_float() function definition. checks whether the value is higher than 0 and less than 1000
        print("Valid number = ", valid_number) #display of the value after it is validated by the "get_float()" function
        print()
        valid_integer = get_int("Enter integer: ", 0, 50) #function whos purpose is to test the validation of the conditions of the get_int() function.     
        print("Valid integer = ", valid_integer) #display of the value assignted to valid_integer if it passes the validation.
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ") #the input that decides whether the loop continues or ends based on the user input.
        print()

    print("Bye!")
    
if __name__ == "__main__": #an if statement that checks if this program is the main module.
    main()
