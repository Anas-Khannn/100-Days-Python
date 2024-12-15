"""
This program manages a music playlist using OOP concepts.
It demonstrates:
- Creating a Song class to represent a song with attributes like title, artist, and duration
- Adding songs to a playlist
- Displaying all songs in the playlist
- Removing a song from the playlist
"""

# Define a class to represent a Song
class Song:
    # Constructor to initialize song attributes
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in minutes
        print(f"Song '{self.title}' by {self.artist} ({self.duration} min) has been added to the playlist.")

    # Method to display song details
    def display_details(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} min")

    # Destructor to indicate removal of a song
    def __del__(self):
        print(f"Song '{self.title}' by {self.artist} has been removed from the playlist.")

# Main program to interact with the user
print("Welcome to the Music Playlist Manager!")
playlist = []

# Add songs to the playlist
num_songs = int(input("How many songs would you like to add to your playlist? "))
for i in range(num_songs):
    print(f"\nEnter details for Song {i + 1}:")
    title = input("Song Title: ")
    artist = input("Artist: ")
    duration = float(input("Duration (in minutes): "))
    playlist.append(Song(title, artist, duration))

# Display all songs in the playlist
print("\nYour Music Playlist:")
for i, song in enumerate(playlist, 1):
    print(f"\nSong {i}:")
    song.display_details()

# Remove a song from the playlist
print("\nWould you like to remove a song from the playlist?")
choice = input("Enter 'yes' to remove, or 'no' to keep the playlist as is: ").strip().lower()

if choice == 'yes':
    song_to_remove = int(input(f"Enter the song number (1 to {len(playlist)}) to remove: "))
    if 1 <= song_to_remove <= len(playlist):
        del playlist[song_to_remove - 1]
    else:
        print("Invalid choice! No song was removed.")

# Display final playlist
print("\nFinal Playlist:")
if playlist:
    for i, song in enumerate(playlist, 1):
        print(f"\nSong {i}:")
        song.display_details()
else:
    print("The playlist is empty!")
