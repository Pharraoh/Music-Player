import os
import random
import pygame

def play_random_track(library_path):
    # Set the SDL_AUDIODRIVER environment variable to 'directsound'
    os.environ['SDL_AUDIODRIVER'] = 'directsound'

    # Initialize pygame mixer
    pygame.mixer.init()

    # Get list of music files in the library directory
    music_files = [f for f in os.listdir(library_path) if f.endswith('.mp3')]

    # Select a random track from the library
    if music_files:
        track_path = os.path.join(library_path, random.choice(music_files))
    else:
        print("No music files found in the library directory.")
        return

    # Load and play the selected track
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage:
library_path = "C:/Users/hp/music/Eminem-Kamikaze" #swap C:/Users/hp/music/Eminem-Kamikaze for music file location
play_random_track(library_path)
