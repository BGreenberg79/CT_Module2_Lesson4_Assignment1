# Task 1 The Selective DJ

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres[1:4]:
    print(f"This sublist of genres includes {genre}")

#This for loop lists the three genres included in the sublist, Rock, Hip-hop, and classical from tracks 2 to 4 by using python's slice feature

# Task 2 One liner band with list comprehensions
genre_music = [genre + " Music" for genre in genres]
print(genre_music)
'''
This list comprehension is using the ability of python to merge string to concisely create a new 
list appending each existing genre into the new list and adding the music addendum to each item.
'''

# Task 3 Numerical beat with range

print("Let's start the count down!")
for beat in range(10, 0, -1):
    print(beat)
print("The beat drops now!")

'''
The range function is used here withboth optional parameters - start and increment the first and last digits.
In doing so the starting point is set at 10, the ending point is set at index 0 (which is 1), and the 
increment is negative 1. To clarify the intent and purpose of this program a print statement starts the countdown
and a print statement dropping the beat follows it.
'''