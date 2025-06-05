from .audio import *
import pygame

SAMPLE_FOLDER = "samples"

class Sampler:
    def sample(sound):
        """Convert a sound file to a numpy array using pygame's mixer.
        Returns a stereo audio file.
        """

        #   Initialize pygame mixer
        pygame.mixer.init()

        #   Load the sound file
        sound = pygame.mixer.Sound(sound)

        #   Convert the sound to a numpy array
        sound_data = pygame.sndarray.array(sound)

        #   Convert to mono -- Not used
        sound = pygame.sndarray.make_sound(sound_data)

        mono = [arr[0] for arr in sound_data]
        mono = np.column_stack((mono, mono))

        return sound_data

    def sample_env(sampled_sound, attack=0.0, decay=0.0, sustain=1.0, release=0.0):
        """Convert a sound file to a numpy array and apply an envelope"""

        #   Manipulate the numpy array (e.g., apply an envelope)
        duration = len(sampled_sound) / 44100
        mono = sampled_sound.mean(axis=1)
        mono = mono.astype(np.float64)
        mono = envelope(mono, attack=attack * duration, decay=decay * duration, sustain=sustain, release=release * duration)
        
        return stereo

    def shift_pitch(sampled_sound, semitones):
        factor = 2 ** (semitones / 12.0)
        duration = len(sampled_sound) / 44100
        # Requires a complicted algorithm to change pitch without changing speed

    def shift_pitch_and_speed(sampled_sound, semitones):
        """Shift the pitch and speed of a sound sample"""
        
        #   Convert to Mono
        sampled_sound = sampled_sound.mean(axis=1)

        #   Shift the pitch
        factor = 2 ** (semitones / 12.0)
        new_length = int(len(sampled_sound) / factor)

        #   Adjust the speed
        old = np.linspace(0, len(sampled_sound), num=len(sampled_sound))
        new = np.linspace(0, len(sampled_sound), num=new_length)
        sound = np.interp(new, old, sampled_sound)

        #   Back to stereo
        sound = np.column_stack((sound, sound))
        return sound


def main():
    """Main function to test sample()"""

    #   Load the sound file
    sound = os.path.join(SAMPLE_FOLDER, "Navi", "hey.wav")

    #   Convert the sound to a numpy array
    sampled_sound = Sampler.sample(sound)


    #   Manipulate the numpy array

    ##  Apply an envelope to the sounds
    sampled_sound = Sampler.sample_env(sampled_sound)
    
    ##  Adjust the pitch and speed of the sound
    sampled_sound = Sampler.shift_pitch_and_speed(sampled_sound, -6)  # Shift pitch up by 2 semitones

    ##  Adjust the length of the sound based on a bpm


    #   Convert the numpy array back to a pygame sound object
    sampled_sound = pygame.sndarray.make_sound(sampled_sound.astype(np.int16))

    #   Play the sound
    sampled_sound.play()

    #   Wait until the sound finishes playing
    while pygame.mixer.get_busy():
        pass