#!/usr/bin/env python3
#Levi Noell-Baba, July 18, 2023, CPT-168-W17, Lab 11-2
from datetime import datetime, time #import datetime and time classes from the datetime module

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now() #waits for the enter key to be pressed then begins the timer
    print(f"Start time: {start_time:%X.%f}") #prints the start time in hours, minutes, and seconds as X and microseconds as f
    print()
    
    # stop timer
    input("Press Enter to stop...")    #input letting the user know to press enter to stop the timer
    stop_time = datetime.now() # gets the stop_time variable and assigns the current date and time
    print(f"Stop time: {stop_time:%X.%f}") #prints the stop time in the same format as the start time was formatted
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time #calculates the elapsed time by subtracting the start_time from the stop_time
    minutes = elapsed_time.seconds // 60 #calculates the total number of minutes in the elapsed time
    seconds = elapsed_time.seconds % 60 #calculates the remaining seconds in the elapsed time after calculating minutes
    microseconds = elapsed_time.microseconds #gets the microseconds of the elapsed time

    # calculate hours and minutes
    hours = minutes // 60 #calculates the total number of hours in elapsed time
    minutes = minutes % 60 #calculates the number of minutes after the hours have been calculated and updates the minutes

    # create time object
    time_object = time(hours, minutes, seconds, microseconds) #time object created to store the hours, minutes, seconds, and microseconds

    # display results
    print("ELAPSED TIME")
    if hours > 0 or minutes > 0: #if statement that checks if the hours are greater than 0 and if the minutes are greater than 0
        print(f"Hours/minutes: {time_object:%H:%M}") #prints amount of hours and minutes that have passed
    print(f"Seconds: {time_object:%S.%f}") #prints the amount of seconds that have passed

if __name__ == "__main__":
    main()
