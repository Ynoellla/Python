#!/usr/bin/env python3
#Levi Noell-Baba, June 17, 2023, CPT-168-W17, Lab 6-1
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = [] #Modification of the "get_scores() function" in which the test scores are stored in an empty list named scores
    while True:
        score = input("Enter test score: ") #Entry of test scores
        if score == "x":
            return  scores #the list scores being returned by the function when all scores have been entered
        else:
            score = int(score) # converts the "scores" argument into an integer value as its being used as an entry for test scores
            if score >= 0 and score <= 100:#the use of an "if statement" and the "and" logical operator that checks if both statements are true.
                scores.append(score) # "append" is used here to add each test score to the other and acts as a counter.
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores): #"process_scores() fuction" after beiung modified so that the scores list is the only argument call.
    # calculate total score
    total = 0 # the initial assignmnet of the value "0" for the variable total
    for score in scores: #a for statement used to add score to existing score to get the value of score total
         total += score #the += compound assignment operator used to have total equal to the sum of the number of scores from the "scores" list

    #number of scores in the list
    length = len(scores) #the "len()" function is used to call of the scores list to get the number of scores in the list

    # calculate average score
    average = round(total / length) #average calculated by taking the total score and dividing it by the length and then rounded.
    
    # get the high and low score
    low = min(scores)# min function used to get the lowest score from the list
    high = max(scores) #max function used to get the highest score from the list

    # getting the median score
    median_index = len(scores) // 2 #len() function used to call on the "scores" list and take the number of scores and divide it by 2
    if len(scores) % 2 == 1: #an if statment that checks the value of the expression for an off number of scores in the scores list.
        median = scores[median_index] #Executed if the if statement condition holds true for odd numbers in the "scores" list.
    else: #checks the value of the expression for an even number of scores in the scores list
        median1 = scores[median_index] #executed if the if condition holds a false value and calls the test score value at index 2
        median2 = scores[median_index-1] #executed if the if condition holds a false value and calls the test score value at the index 1 position
        median = (median1 + median2)/2 # a statement used to calculate the median test score value which equates to the median 1 test score value plus the median 2 test score value.
    
                
    # format and display the result
    print()
    print("Total:           ", total)
    print("Number of Scores:", length)
    print("Average Score:   ", average)
    print("Low Score:       ", low)
    print("High Score:      ", high)
    print("Median Score:    ", median)

def main():
    display_welcome() #function called after defined that will display "the test scores program"
    scores = get_scores() #list returned by get_scores() is stored in a variable named "scores"
    process_scores(scores) #"process_scores()" modified so that scores list is passed to call statement
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


