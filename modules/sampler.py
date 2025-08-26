from .audio import *
import pygame
import wave
import scipy.io.wavfile as wav
from scipy.signal import resample

SAMPLE_FOLDER = "samples"

class Sampler:
    def sample(sound, dur = 1.0, sample_rate=44100):
        """Convert a sound file to a numpy array using pygame's mixer.
        Returns a stereo audio file.
        """
    
        #   Initialize pygame mixer #
        pygame.mixer.init()

        #   Load the sound file #
        sound = pygame.mixer.Sound(sound)

        #   Convert the sound to a numpy array  #
        sound_data = pygame.sndarray.array(sound)
        write(sound_data, "", "surprise", volume_factor = 1, sample_rate=44100)

        #   Ensure the sound is monotone    #
        if len(sound_data.shape) > 1:  # Stereo audio
            # Convert to mono by averaging the two channels
            sound_data = sound_data.mean(axis=1).astype(sound_data.dtype)

        #   Cut off or add padding to the sample to achieve the desired duration   #
        target_length = int(dur * sample_rate)  # Calculate the target number of samples
        current_length = len(sound_data)

        ##  Cut the array   #
        if current_length > target_length:
            sound_data = sound_data[:target_length]

        ##  Extend the array    #
        elif current_length < target_length:
            padding = np.zeros(target_length - current_length, dtype=sound_data.dtype)
            sound_data = np.concatenate((sound_data, padding))
        
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
    pygame.mixer.init()

    #   Load the sound file
    sound = os.path.join(SAMPLE_FOLDER, "Navi", "hey.wav")

    #   Convert the sound to a numpy array
    sampled_sound = Sampler.sample(sound)
    write(sampled_sound[0], "", "Hey!", volume_factor = 1, sample_rate=8000)




    #   Manipulate the numpy array

    ##  Apply an envelope to the sounds
    #sampled_sound = Sampler.sample_env(sampled_sound)
    
    ##  Adjust the pitch and speed of the sound
    #sampled_sound = Sampler.shift_pitch_and_speed(sampled_sound, -6)  # Shift pitch up by 2 semitones

    ##  Adjust the length of the sound based on a bpm


    #   Convert the numpy array back to a pygame sound object
    # sampled_sound = pygame.sndarray.make_sound(sampled_sound)

    # #   Play the sound
    # sampled_sound.play()

    # #   Wait until the sound finishes playing
    # while pygame.mixer.get_busy():
    #     pass