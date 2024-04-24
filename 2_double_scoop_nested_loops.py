# Task 1 Mood Tracker

import random

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
moods = ["calm", "envious", "frightened", "happy", "hopeful", "celebratory"]

for day_index in range(7):
    for time_index in range(3):
        day = days_of_week[day_index]
        time = time_of_day[time_index]
        print(f"This {day} {time} I felt very " + str(random.choice(moods)) + ".")

'''
This nested for statement uses a very similar set up to my program from Question 1.
I set up the random import, days of week list, and moods list nearly identically.
The original for statement setting the index number as the item to loop through a range was also
identical. This time the only real change i made was adding a time of day list, and then running
the index number of that list as the item to loop through. By nesting the time of day loop inside 
the day of week loop all 21 days and times of the week were covered by the f string print statement 
that identifies the time and day before randomly choosing a mood off of my moods list.  
'''