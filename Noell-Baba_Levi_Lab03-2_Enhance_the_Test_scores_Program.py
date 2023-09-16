#!/usr/bin/env python3
#Levi Noell-Baba, June 4, 2023, CPT-168-W17, Lab 3-2
# display a welcome message
print("The Test Scores application")
print()
another_set = "y"

while another_set == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0
#    while True:
#        test_score = input("Enter Test Score:  ")
#        if test_score == "end":
#            break
#        elif (int(test_score) >=0) and (int(test_score) <= 100):
#            score_total += int(test_score)
#            counter += 1
#        else:
#            print("Test score must be from 0 through 100. Try again.")
#While loop to control input of scores and breaking out    
    while (test_score := input("Enter test score: ").lower()) != "end":
        test_score = int(test_score)
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print("Test score must be from 0 through 100. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()
    another_set = input("Enter another set of test scores (y/n)?")
    print()
print("Bye!")


