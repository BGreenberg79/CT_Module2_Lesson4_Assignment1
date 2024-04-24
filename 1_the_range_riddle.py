# Task 1 Your Mood Today

# before  I start writing out the code that assigns random moods to days of week I will import the random package
import random

# I will write out the python lists that list the different days of the week and various moods that can be selected
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["excited", "peaceful", "joyous", "accomplished", "frustrated"]

for day_index in range(7):
    day = days_of_week[day_index]
    print(f"Today is {day} and I feel " + str(random.choice(moods)) + "!")

'''
The program I wrote for this assignment was a for loop in a range of 7
as there are 7 days in the week (a constant that will never change). The variable prior to in was
identified as day index as I knew that the day variable I was trying to define for my print statement
would be the 0-6 that would then call each index in my days_of_week list.
The for loop, and the range being appropriately assigned, would allow for each value to be referenced.
I would also argue that if the prompt did not specifically call for the use of the range function
there is a simpler way to write this program. That simpler way is as follows:
for day in days_of_week:
    print(f"Today is {day} and I feel " + str(random.choice(moods)))
This function produces the same results as the one I wrote for the assignment 
in a more efficient and graceful way (i.e. more in accordance with PEP), however I do 
understand that this assignment needs to test our understanding of the range function!
'''