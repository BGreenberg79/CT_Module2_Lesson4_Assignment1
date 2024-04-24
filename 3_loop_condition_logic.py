# Task 1 Loop Condition Exploration

GROUNDHOG_DAY = "February 2nd"
phil_selfish = True

while GROUNDHOG_DAY == "February 2nd":
    for days_elapsed in range(1000):
        if phil_selfish == True:
            print(f"Phil is still selfish, the time loop continues and another day passes. So far {days_elapsed+1} days have passed.")
            if days_elapsed >= 4:
                phil_selfish = False
                print("Phil learns he can change, time is precious, and falls for Rita") 
        else:
            print("Phil is no longer selfish.")
            break
    break
print("Today is February 3rd. The time loop has broken and it is no longer Groundhog day")

'''
This program demonstrates an infinite while loop as Feb. 2nd is Groundhog Day a holiday that 
doesn't change, a constant. Inside this while loop I tell the story of a movie about (time) loops, 
Groundhog Day. The program will indefinitely run a for loop with a range to 1,000 infinite times until
it's logic is  changed and a break statement forces both the for statement and while loops to stop. 
Inside of this for loop an if conditional states that if weatherman Phil Connor is still selfish he 
will be trapped in a time loop as days continue to pass but time stays still. This statement is printed 
as an f string lists how many days he's perceived to have elapsed (which has a +1 inside of it to account 
forpython indexing from 0). This will continue to return as true and the for loop will continue to count 
untildays elapsed is greater than or equal to 4 (once again python starts as 0, if we wanted to use 5 the 
nested if could have read days_elapsed+1 >= 5). Once we reach the 5th day (or the index hits 4) we break 
the loop by followiing the story of the movie, Phil is no longer selfish, and a print statement states his 
newfound understanding of time, love, and relationships. Now that phil_selfish has been assigned false the 
if statement goes to else, where his selflessness is restated and the for loop ends with a break statement. 
After I break the for loop I also break the while loop. After both loops have ended I print that today has 
finally become February 3rd and the time loop has broken.
'''

#Task 2 Conditional exit

GROUNDHOG_DAY = "February 2nd"
phil_selfish = True

while phil_selfish == True:
    for days_elapsed in range(6):
        if phil_selfish == True:
            print(f"Phil is still selfish, the time loop continues and another day passes. So far {days_elapsed+1} days have passed.")
            if days_elapsed >= 4:
                phil_selfish = False
                print("Phil learns he can change, time is precious, and falls for Rita") 
        else:
            print("Phil is no longer selfish.")
print("Today is February 3rd. The time loop has broken and it is no longer Groundhog day")

'''
To turn the program from task 1 that was infinitely looping until a break statement, into one with a 
conditional exit, two changes had to be made. the first change is that the while loop had to be 
disassociated from the Groundhog Day constant so I just related it to Phil's selfishness which as we know
can and will be changed by movie's/program's end. The second change I made was to bring the nested for loop 
to an end by bringing down the range to exactly 6, instead of the original 1000. I chose 6 as it allowed
for the 5 selfish days to be counted in the first if statement and one more day for the else statement to run,
once the nested conditional if assigns Phil's selfishness a False boolean. Other than the change in range and 
changing how the while evaluates, the only other changes was deleting both breaks.
'''