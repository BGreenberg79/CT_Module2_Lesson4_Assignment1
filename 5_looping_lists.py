# Task 1 The for Loop DJ Set

genres = ["Jazz", "Rock", "Hip-hop", "Classical"]

for genre in genres:
    print(f"This song can be categorized as being part of the {genre} genre")
# Each genre with a customized message
for track_number, genre in enumerate(genres, 1):
    print(f"This song, Track {track_number}, can be categorized as being part of the {genre} genre")
'''
For this part of the prompt I used the enumerate function to add a count that could be associated with 
each individual genre starting at 1 and increasing in increments of 1. I then expanded the original f-string
print statement to now include the track number in the message.
'''

# Task 2 The Remix Artist With While
track_number = 0
genres = ["Jazz", "Rock", "Hip-hop", "Classical"]
while track_number < 4:
    genre = genres[track_number]
    track_number += 1
    print(f"This song, Track {track_number}, can be categorized as being part of the {genre} genre")

'''
This while loop is the identical function as the for loop that used the enumnerate feature in Task 1.
Here we define a variable as track_number and set it to zero before we start the function. This will be our
counter. I also copied the genres list to keep it accesible and prevent any index errors here in Task 2.
Going into the while loop I set it's condition to run until the  track number is no longer less than 4.
Inside the loop I defined genre to be the value in the genres list at the index of the current track number.
Then I increased that track_number by one each time the loop runs. Lastly I reiterated the same f-string print
statement I ran earlier.
'''

# Task 3 Light Show Technician Loop
genres = ["Jazz", "Rock", "Hip-hop", "Classical"]
for genre_index in range(len(genres)):
    genre = genres[genre_index]
    if genre == "Classical":
        continue
    else:
        print(f"The light show is ready for the {genre} song, Track Number {genre_index+1}")
print("Classical music is too elegant and graceful to be tarnished with a light show")

'''
This for loop creates the genre_index variable and runs through it for each number in the range of the length of the list genres.
in that range of numbers (4) it assigns to the variable genre each genre that can be called from the genres list by index number
Once that index number hits the number that would call "Classical" and it is assigned to the variable genre, we run an if
conditionall where if it is the same as the string "Classical" we use the continue statement to skip through and run the rest of 
the list where we print that the light show is ready for that genre song and it's track number. I finally add
one more print statement explaining why Classical had no light show.  
'''