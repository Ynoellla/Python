#!/usr/bin/env python3
#Levi Noell-Baba, June 17, 2023, CPT-168-W17, Lab 5-1 
# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0 # initial value of the counter variable
score_total = 0 # initial value of the score_total variable
test_score = 0 #initial value of the test_score variable

while True:
    test_score = int(input("Enter test score (or 'x' to quit): "))
    if test_score != "x": #if statement that detects if an 'x' was entered as an input to break out of the loop
        test_score = int(test_score) # allows an integer value to be entered as the test_score value as long as 'x' is not entered
    else:
        break # us of the break statment ends the loop
    if test_score >= 0 and test_score <= 100: # the use of the and logical operator and an if statement checks if both conditions are true.
        score_total += test_score # the test_score variable is added to the score_total variable
        counter += 1 # counter variable that adds one to the counter
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.") #display of an error message when an invalid input is entered

# calculate average score
average_score = round(score_total / counter) # the round function is used to diplay the average_score variable to the nearest whole integer.
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print("Bye")


