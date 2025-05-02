import numpy as np
import os
import wave

"""
Audio Module

This module can be used to generate  audio effects.
Author - Trey Custodio
"""

"""Static Variables --------------------------------------"""
SAMPLE_RATE = 44100
CHANNELS = 1
BULK_FOLDER = "bulk-generations"

# Octave 0
A0 = 27.5000
As0 = Bb0 = 29.1352
B0 = 30.8677

# Octave 1
C1 = 32.7032
Cs1 = Db1 = 34.6478
D1 = 36.7081
Ds1 = Eb1 = 38.8909
E1 = 41.2034
F1 = 43.6535
Fs1 = Gb1 = 46.2493
G1 = 48.9994
Gs1 = Ab1 = 51.9131
A1 = 55.0000
As1 = Bb1 = 58.2705
B1 = 61.7354

# Octave 2
C2 = 65.4064
Cs2 = Db2 = 69.2957
D2 = 73.4162
Ds2 = Eb2 = 77.7817
E2 = 82.4069
F2 = 87.3071
Fs2 = Gb2 = 92.4986
G2 = 97.9989
Gs2 = Ab2 = 103.8262
A2 = 110.0000
As2 = Bb2 = 116.5409
B2 = 123.4708

# Octave 3
C3 = 130.8128
Cs3 = Db3 = 138.5913
D3 = 146.8324
Ds3 = Eb3 = 155.5635
E3 = 164.8138
F3 = 174.6141
Fs3 = Gb3 = 184.9972
G3 = 195.9977
Gs3 = Ab3 = 207.6523
A3 = 220.0000
As3 = Bb3 = 233.0819
B3 = 246.9417

# Octave 4 (middle C is C4)
C4 = 261.6256
Cs4 = Db4 = 277.1826
D4 = 293.6648
Ds4 = Eb4 = 311.1270
E4 = 329.6276
F4 = 349.2282
Fs4 = Gb4 = 369.9944
G4 = 391.9954
Gs4 = Ab4 = 415.3047
A4 = 440.0000
As4 = Bb4 = 466.1638
B4 = 493.8833

# Octave 5
C5 = 523.2511
Cs5 = Db5 = 554.3653
D5 = 587.3295
Ds5 = Eb5 = 622.2540
E5 = 659.2551
F5 = 698.4565
Fs5 = Gb5 = 739.9888
G5 = 783.9909
Gs5 = Ab5 = 830.6094
A5 = 880.0000
As5 = Bb5 = 932.3275
B5 = 987.7666

# Octave 6
C6 = 1046.5023
Cs6 = Db6 = 1108.7305
D6 = 1174.6591
Ds6 = Eb6 = 1244.5079
E6 = 1318.5102
F6 = 1396.9129
Fs6 = Gb6 = 1479.9777
G6 = 1567.9817
Gs6 = Ab6 = 1661.2188
A6 = 1760.0000
As6 = Bb6 = 1864.6550
B6 = 1975.5332

# Octave 7
C7 = 2093.0045
Cs7 = Db7 = 2217.4610
D7 = 2349.3181
Ds7 = Eb7 = 2489.0159
E7 = 2637.0205
F7 = 2793.8259
Fs7 = Gb7 = 2959.9554
G7 = 3135.9635
Gs7 = Ab7 = 3322.4376
A7 = 3520.0000
As7 = Bb7 = 3729.3101
B7 = 3951.0664

# Octave 8
C8 = 4186.0090

"""#--------------- Static Dynamics Class -------------#"""
class Dynamics:
    def routine(initial_freq, end_freq, duration, dynamic = False):
        """Set up data to implement a slur effect"""
        #   The number of samples we'll use for the wave
        samples = int(44100 * duration)

        #   Generate time points across the duration; Store rate of change of t
        t = np.linspace(0, duration, samples, endpoint=False)
        dt = duration / samples

        #   Generate the wave with DSG or SSG
        if dynamic:
            return Dynamics.DSG(initial_freq, t, dt, samples)

        else:
            return Dynamics.SSG(initial_freq, end_freq, t, dt, samples)
        

    def SSG(start_freq, end_freq, t, dt, samples):
        """Scripted Sine wave Generation:\n
        Construct the wave based on a start and end frequency.\n
        Generate a frequency array, calculate the phase, and return the final wave"""

        fp = np.linspace(start_freq, end_freq, samples)

        phase_increment = 2 * np.pi * fp * dt
        phase = np.cumsum(phase_increment)
        
        return np.sin(phase)


    def DSG(initial_freq, t, dt, samples):
        """Dynamic Sine wave Generation:\n
        Dynamically construct the wave based on the value obtained from the pitch wheel."""

        """INCOMPLETE"""
        RUNNING = True
        value = 0

        while RUNNING:
            #   Adjust the value on the pitch wheel
            value -= 1

            #   Get the new frequency based on the pitch wheel
            f = initial_freq * 2 **(Dynamics.get_bend(value) / 12)

        return np.sin(f)


    def get_bend(value, bend_range=12):
        """Return the bend value based on the pitch wheel's value,
        Following the Minimoog algorithm."""

        step = 16384 / (2 * bend_range)
        snapped = round((value - 8192) / step) * step + 8192

        bend = ((snapped - 8192) / 8192) * bend_range

        return bend
    


"""Auxillaury Functions ----------------------------------"""
def get_measure(bpm):
    return (1 / (bpm / 60)) * 4

def get_sixteenth(bpm):
    return (1 / (bpm / 60)) / 4

def get_eighth(bpm):
    return (1 / (bpm / 60)) / 2

def get_quarter(bpm):
    return (1 / (bpm / 60))

def get_half(bpm):
    return (1 / (bpm / 60)) * 2

def get_trey(bpm):
    return (1 / (bpm / 60)) * 3

def ensure_1(number):
    """Ensures that an integer or float is at least 1"""
    if number < 1:
        return 1
    else:
        return number

def combine(wave1, wave2):
    """Combine 2 waves together even if they aren't the same length
    by appending 0s to the end of the smaller wave.
    This will work for now, but it will cause mistiming for longer waves."""
    
    #   Copy the waves
    wave1 = wave1.copy()
    wave2 = wave2.copy()
    
    if len(wave1) > len(wave2):
        end = len(wave1) - 1
        num_zeros = end - (len(wave2) - 1)
        zeros = [0 for i in range(num_zeros)]
        wave2 = np.append(wave2, zeros)

        return wave1 + wave2
    
    else:
        end = len(wave2) - 1
        num_zeros = end - (len(wave1) - 1)
        zeros = [0 for i in range(num_zeros)]
        wave1 = np.append(wave1, zeros)

        return wave1 + wave2

def delaycombo(wave1, wave2, rest_time = 0.1):
    """Combines 2 waves but adds the rest time to the beginning of wave2"""
    wave1 = wave1.copy()
    second = add_waves(rest(rest_time), wave2)

    #   Find where Wave 2 begins
    index = 0
    for i in range(len(second)):
        if second[i] != 0:
            index = i
            break

    #   Silence Wave 1 after this index
    wave1[index:] = 0

    return combine(wave1, second)

# def slur(wave1, wave2, instrument):
#     slur = add_waves(wave1, wave2)
    

#     duration = len(slur) / SAMPLE_RATE
    
#     adsr = instrument.getADSR()
#     a = adsr[0] * duration
#     d = adsr[1] * duration
#     s = adsr[2]
#     r = adsr[3] * duration
    
    
#     slur = envelope(slur, a,d,s,r)
#     return slur               

def slur(note1, note2, duration, dynamic = False):
    """Slur a note"""

    return Dynamics.routine(note1, note2, duration, dynamic)

def synth(frequency, duration):
    #   Define fundamental wave
    sound = sine_wave(frequency, duration)

    #   Apply envelope
    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.7 * duration
    sound = envelope(sound, a,d,s,r)

    return sound

def foo(d):

    sound = slur(F3, A3, d) * 2
 
    for i in range(1, 21):
        a = 1/(4*i)
        sound += slur(F3 * i, A3 * i, d) * a

    sound = envelope(sound,0.2*d,0.1*d,0.5, 0.5*d)
    return sound



def space_synth(frequency, duration):
    #   Define a fundamental wave
    sound = sine_wave(frequency, duration) * 2

    #   Add harmonics
    # for i in range(1,51):
    #     a = np.sqrt(i)
    #     sound += sine_wave(frequency/i, duration) *a#* (1/a)
    
    for i in range(1, 21):
        a = 1/(4*i)
        sound += sine_wave(frequency*i, duration) *a#* (1/a)

    #   Apply envelope
    at = 0.2 * duration
    d = 0.1 * duration
    s = 0.5
    ri = 0.1 * duration
    r = 0.5 * duration

    sound = envelope(sound, at,d,s,r)
   # sound = synth_env(sound, at, d, s, ri, r)

    return sound

def space_synth_bass(frequency, duration):
    #   Define a fundamental wave
    sound = sine_wave(frequency, duration) * 2

    #   Add harmonics
    for i in range(1,21):
        #a = np.sqrt(i)
        a = np.e ** (-2 * i)
        sound += sine_wave(frequency/i, duration) *a#* (1/a)
    
    # for i in range(1, 21):
    #     a = 1/(4*i)
    #     sound += sine_wave(frequency*i, duration) *a#* (1/a)

    #   Apply envelope
    at = 0.01 * duration
    d = 0.1 * duration
    s = 0.5
    ri = 0.1 * duration
    r = 0.5 * duration

    sound = envelope(sound, at,d,s,r)
    
    return sound

def space_synth_percussive(frequency, duration):
    #   Define a fundamental wave
    sound = sine_wave(frequency, duration) * 2

    #   Add harmonics
    for i in range(1,51):
        a = np.sqrt(i)
        sound += sine_wave(frequency/i, duration) *a#* (1/a)
    
    for i in range(1, 21):
        a = 1/i
        sound += sine_wave(frequency*i, duration) *a#* (1/a)

    #   Apply envelope
    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.6 * duration

    sound = envelope(sound, a,d,s,r)
    return sound

def synth_env(audio, a, d, s, ri, r):
    audio = audio.copy()

    sample_rate = SAMPLE_RATE

    attack_samples = int(a * sample_rate)
    decay_samples = int(d * sample_rate)
    rise_samples = int(ri * sample_rate)
    release_samples = int(r * sample_rate)
    sustain_samples = len(audio) - (attack_samples + decay_samples + rise_samples + release_samples)


    #   Attack; rise to max
    audio[:attack_samples] = np.linspace(0, 1, attack_samples)

    #   Decay; decrease to sustain
    audio[attack_samples:attack_samples+decay_samples] *= np.linspace(1, s, decay_samples)
    
    #   Rise: rise back to max
    audio[attack_samples+decay_samples:attack_samples+decay_samples+rise_samples] *= np.linspace(s, 1, rise_samples)

    #   Sustain: hold volume until release
    audio[attack_samples+decay_samples+rise_samples:attack_samples+decay_samples+rise_samples+sustain_samples] *= 1
    
    #   Release: decay to 0
    audio[attack_samples+decay_samples+rise_samples+sustain_samples:] *= np.linspace(1, 0, release_samples)


    return audio


def space_synth_ampedhighs(frequency, duration):
    #   Define a fundamental wave
    sound = sine_wave(frequency, duration) * 2

    #   Add harmonics
    for i in range(1,51):
        a = np.sqrt(i)
        sound += sine_wave(frequency/i, duration) *a#* (1/a)
    
    for i in range(1, 21):
        a = 1/i
        sound += sine_wave(frequency*i, duration) *a#* (1/a)

    #   Apply envelope
    a = 0.2 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.6 * duration

    sound = envelope(sound, a,d,s,r)
    return sound

def slurrysynth_up(frequency, duration):
    sound = slur(ensure_1(frequency - 200), frequency, duration)

    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.7 * duration

    sound = envelope(sound, a,d,s,r)
    return sound

def slurrysynth_down(frequency, duration):
    sound = slur(frequency, ensure_1(frequency - 200), duration)

    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.7 * duration

    sound = envelope(sound, a,d,s,r)
    return sound
    

def write(effect, folder: str = "", name: str = "", stereo=True):
    """Save a sound as a .wav file.
    Final step in the audio generation process.
    (1) Generate and manipulate sine waves in float64 format
    (2) Convert to int16 format and save as .wav
    """

    #   (1) Create a file name
    if name == "":
        name = input("Enter a name for this file: ")
    
    if ".wav" not in name:
        name += ".wav"
        
    #   (2) Decide where to place the .wav file
    if folder != "":
        file = os.path.join(folder, name)
    else:
        file = name

    #   (3) Convert to Stereo?
    # if stereo:
    #     effect = np.column_stack([effect, effect])

    #   (3) Write the file based on the object type
    with wave.open(file, 'w') as wf:
        ## Set the channels and framerate
        wf.setnchannels(2)
        wf.setframerate(SAMPLE_RATE)

        ##  Convert to PCM format and find sample width
        final = (effect / np.max(np.abs(effect)) * 32767).astype(np.int16)
        samp_width = final.dtype.itemsize
        wf.setsampwidth(samp_width)

        ##  Save as .wav
        wf.writeframes(final)

    wf.close()
    

# def play(effect):
#     """Plays the given sound"""
#     if type(effect) is np.ndarray:
#         sd.play(effect)
#         sd.wait()

#     elif type(effect) is Sine:
#         sd.play(effect.wave)
#         sd.wait()

def find_silence(wave):
    """Returns the index of the last silent point
    in a sine wave. Useful for removing chirps."""
    final_index = 0
    for i in range(-1, -len(wave), -1):
        if wave[i] != 0:
            final_index = i
            break
    
    return final_index

def rest(duration = 1.0):
    return sine_wave(0, duration)

def build_measure(*args):
    final = None
    tick = 0
    for wave in args:
        if tick == 0:
            final = wave
            tick += 1
        else:
            final = add_waves(final, wave)

    return final

def add_waves(wave_1, wave_2, position=-1, buffer = False, rest_time=0.0, times = 1):
    """Insert *wave_2* into *wave_1* at *position*
    
    Default *position* == -1: adds *wave_2* to the *end* of *wave_1*;\n
    *position* == 0: adds *wave_2* to the *0* of *wave_1*;\n
    A *buffer* will add a rest in between the sounds"""

        
    #   (1) Add rest time
    if rest_time > 0.0:
        rest = sine_wave(0, rest_time)
        if position == -1:
            wave_1 = np.concatenate([wave_1, rest])
        else:
            wave_2 = np.concatenate([wave_2, rest])
        

    #   (2) Concatenate the waves
    final = None
    for i in range(times):
        ##  Add wave_2 to the end of wave_1
        if position == -1:
            if i == 0:
                final = np.concatenate([wave_1, wave_2])
            else:
                final = np.concatenate([final, wave_2])

        else:
            ##  Ensure that 0 <= position < len(wave_1)
            position = max(0, min(position, len(wave_1)))
            
            ##  Add wave_2 to wave_1 at position
            final = np.concatenate([wave_1[:position], wave_2, wave_1[position:]])

    return final

def create_measure(duration, waves : list):
    """Produce a measure given a series of waves,
    and the duration of each measure."""
    return

def combine_notes(wave_1, wave_2):
    """Combine notes together"""
    final = wave_1.copy()

    for w in wave_2:
        final.append(w)
    
    return final

def mult(wave_1, wave_2, iterations, rest_time = 0.0):
    """Add *wave_2* to the end of *wave_1* *iterations* times"""
    #   (1) Copy wave_1
    result = wave_1.copy()
    
    #   (2) Add wave_2 to wave_1 iterations times
    for i in range(iterations):
        result = add_waves(result, wave_2, -1, rest_time=rest_time)
    
    #   (3) Return the result
    return result

def fade_out(wave, delta = 1):
    """"""
    w = wave.copy()
    points = len(w) * delta
    decay = 1.0
    factor = (1/points) ** (1/(points-1))

    for i in range(len(wave)):
        w[i] *= decay
        decay *= factor
    
    return w

def fade_in(wave, delta = 1):
    """"""
    w = wave.copy()
    n = len(w) * delta

    for i in range(len(wave)):
        factor = i / n
        w[i] *= factor
    
    return w

def fade_mult(wave_1, wave_2, iterations, rest_time, factor):
    """Add *wave_2* to the end of *wave_1* *iterations* times.
    Each successive addition gets quieter and quieter by *factor*"""
    #   (1) Copy the waves
    result = wave_1.copy()
    other = wave_2.copy() * factor
    
    #   (2) Continuously add the waves up; decrease the volume of wave_2 each time
    for i in range(iterations):
        result = add_waves(result, other, -1, rest_time=rest_time)
        other *= factor
    
    #   (3) Return our final result
    return result

def add_rest(wave_1, duration = 0.0):
    """Attach a rest to the end of a sound"""
    empty = sine_wave(0, duration)
    return add_waves(wave_1, empty, -1)

def join_waves(wave_1, wave_2):
    """Joins two waves together"""

    #   (1) Ensure proper shape size
    if len(wave_1) < len(wave_2):
        for i in range(len(wave_1), len(wave_2)):
            wave_1 = np.insert(wave_1, i, 0)

    elif len(wave_1) > len(wave_2):
        for i in range(len(wave_2), len(wave_1)):
            wave_2 = np.insert(wave_2, i, 0)

    #   (2) Combine the ways
    return wave_1 + wave_2

def create_effect():
    """Generates an audio effect"""
    # (1) Generate a base tone
    base = sine_wave(frequency=220, duration=0.5)
    
    # (2) Add harmonics
    harmonic1 = sine_wave(frequency=440, duration=0.5, amplitude=0.3)
    harmonic2 = sine_wave(frequency=660, duration=0.5, amplitude=0.1)
    
    # (3) Combine waves
    combined = base + harmonic1 + harmonic2
    
    # (4) Apply envelope
    effect = envelope(combined)
    
    return effect
    
def create_triple(wave, wait_time = 0.0):
    buffer = sine_wave(0, wait_time)
    buffered = add_waves(wave, buffer, -1)

    return add_waves(buffered, add_waves(buffered, buffered, -1), -1)

def shift_note(frequency, delta: int):
    """Shift tone based on 12-TET"""
    final = frequency * (2**(delta/12))
    return final

def scale_amplitude(wav):
    peak = np.max(np.abs(wav))
    target = 32767
    factor = target / peak

    return (wav * factor).astype(np.int16)

"""Sound Effect Functions --------------------------------"""
def sine_wave(frequency=444.0, duration=1.0, sampleRate=SAMPLE_RATE, amplitude=0.5, verticalShift=0, stereo = False):
    """Generates a sine wave"""

    #   (1) Create discrete time points over the duration of the sound. Generate (sampleRate * duration) numbers over the duration.
    samples = int(sampleRate * duration)
    t = np.linspace(0, duration, samples, endpoint=False)


    #   (2) Return the sin wave: y = |a|sin(bx - c) + d
    ##  Recall that Amplitude = a, Period = 2pi/b, Phase Shift = c/b, Vertical shift = d
    ##  2*np.pi = period; so period * frequency * t gives us the correct period based on the frequency over time
    wave = amplitude * np.sin(2 * np.pi * frequency * t) + verticalShift

    #   Return a stereo wave    #
    if stereo:
        return np.column_stack([wave, wave])

    #   Return a mono wave  #
    else:
        return wave

def sine_wave_t(frequency=444.0, duration=1.0, sampleRate=SAMPLE_RATE, amplitude=0.5, verticalShift=0, stereo = False):
    """Generates a sine wave by specifying t"""

    #   (1) Create discrete time points over the duration of the sound. Generate (sampleRate * duration) numbers over the duration.
    samples = int(sampleRate * duration)
    t = np.linspace(0, duration, samples, endpoint=False)


    #   (2) Return the sin wave: y = |a|sin(bx - c) + d
    ##  Recall that Amplitude = a, Period = 2pi/b, Phase Shift = c/b, Vertical shift = d
    ##  2*np.pi = period; so period * frequency * t gives us the correct period based on the frequency over time
    wave = amplitude * np.sin(2 * np.pi * frequency * t) + verticalShift

    #   Return a stereo wave    #
    if stereo:
        return np.column_stack([wave, wave])

    #   Return a mono wave  #
    else:
        return wave
def sine_wave16(frequency=444.0, duration=1.0, sampleRate=SAMPLE_RATE, amplitude=0.5, verticalShift=0):
    """Generates a sine wave in Pulse Code Modulation format.
    wav files store raw data along with metadata including sample rate, bit depth, and # channels."""

    #   (1) Create discrete time points over the duration of the sound. Generate (sampleRate * duration) numbers over the duration.
    samples = int(sampleRate * duration)
    t = np.linspace(0, duration, samples, endpoint=False)


    #   (2) Return the sin wave in PCM format
    return (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16) + verticalShift

def silence(duration=1.0, sampleRate=SAMPLE_RATE):
    return sine_wave(0, duration)
    samples = int(sampleRate * duration)
    t = np.linspace(0, duration, samples, endpoint=False)

    return np.sin(0 * t)

def envelope(audio, attack=0.5, decay=0.2, sustain=0.6, release=0.5, sample_rate=SAMPLE_RATE):
    """Creates an envelope for a sound.
    Envelopes shape a sine wave's amplitude over time 
    by multiplying the amplitude at each point in time.

    -----------------------------------------------------------------------------
    [ADSR]

    Attack: seconds (s)
    - how quickly the sound will reach its full volume upon being triggered

    Decay: seconds (s)
    - how quickly the sound will reach sustain

    Sustain: percentage (0.0 - 1.0)
    - the volume the sound will be held out to
    - at 100%, decay doesn't matter

    Release: seconds (s)
    - how quickly the sound reaches 0 volume after the note is finished
    - you can trigger the note to end, which will skip attack, decay, and sustain,
    and immediately enter the release stage, inching towards 0 db

    --------------------------------------------------------------------------------------
    [Presets]

    Low ASD, high R -> plucky sounds
    """
    #   (0.1) Create a copy of the audio; define the sample rate based on the length of the sine wave
    audio = audio.copy()
    sample_rate = sample_rate#len(audio)

    #   (0.2) Calculate the number of samples for each stage
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = len(audio) - (attack_samples + decay_samples + release_samples)
    
    #   (0.3) Calculate the indices for each stage of the envelope
    stage_1 = attack_samples
    stage_2 = stage_1 + decay_samples
    stage_3 = stage_2 + sustain_samples
    stage_4 = stage_3 + release_samples

    #   (0.4) Print statements for debugging
    # print("length:",len(audio))
    # print("stage_1:", attack_samples)
    # print("stage_2:", stage_2)
    # print("stage_3:", stage_3)
    # print("stage_4:", stage_4, end="\n\n")


    #   (1) Attack: Scale volume of the audio from 0 to 1, with 1 being max volume
    audio[:stage_1] *= np.linspace(0, 1, attack_samples)
    

    #   (2) Decay: Decrease the volume to the sustain value
    audio[attack_samples:attack_samples+decay_samples] *= np.linspace(1, sustain, decay_samples)
    

    #   (3) Sustain: Draw the sound out until release
    audio[stage_2:stage_3] *= sustain


    #   (4) Release: Fade the sound to 0 upon triggering the release
    audio[stage_3:] *= np.linspace(sustain, 0, release_samples)
    

    return audio

def envelope16(audio, attack, decay, sustain, release, sample_rate = SAMPLE_RATE):
    #   (0.1) Create a copy of the audio; define the sample rate based on the length of the sine wave
    audio = audio.copy()
    sample_rate = sample_rate#len(audio)

    #   (0.2) Calculate the number of samples for each stage
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = len(audio) - (attack_samples + decay_samples + release_samples)
    
    #   (0.3) Calculate the indices for each stage of the envelope
    stage_1 = attack_samples
    stage_2 = stage_1 + decay_samples
    stage_3 = stage_2 + sustain_samples
    stage_4 = stage_3 + release_samples

    #   (0.4) Print statements for debugging
    # print("length:",len(audio))
    # print("stage_1:", attack_samples)
    # print("stage_2:", stage_2)
    # print("stage_3:", stage_3)
    # print("stage_4:", stage_4, end="\n\n")


    #   (0) Cast the wave as float64
    audio = audio.astype(np.float64)

    #   (1) Attack: Scale volume of the audio from 0 to 1, with 1 being max volume
    audio[:stage_1] *= np.linspace(0, 1, attack_samples)
    

    #   (2) Decay: Decrease the volume to the sustain value
    audio[attack_samples:attack_samples+decay_samples] *= np.linspace(1, sustain, decay_samples)
    

    #   (3) Sustain: Draw the sound out until release
    audio[stage_2:stage_3] *= sustain


    #   (4) Release: Fade the sound to 0 upon triggering the release
    audio[stage_3:] *= np.linspace(sustain, 0, release_samples)
    

    return audio.astype(np.int16)

def warp(wave, factor, wrap_around):
    tick = 0
    for i in range(len(wave)):
        if tick == 0:
            wave[i] *= factor
        tick += 1
        tick %= wrap_around
    
    return wave


def lowpass(wave, cutoff):
    """Expects a wave and a cutoff; returns the filtered wave"""
    # frequency = 20 + 20000
    # x = np.tan()
    
    
    
    fft_wave = np.fft.fft(wave) # Converts time signal to frequency-domain representation
    frequencies = np.fft.fftfreq(len(wave), 1/SAMPLE_RATE)
    fft_wave[np.abs(frequencies) > cutoff] = 0
    final = np.fft.ifft(fft_wave)

    return np.real(final)

def highpass(wave, cutoff):
    """Expects a wave and a cutoff; returns the filtered wave"""
    fft_wave = np.fft.fft(wave) # Converts time signal to frequency-domain representation
    frequencies = np.fft.fftfreq(len(wave), 1/SAMPLE_RATE)
    fft_wave[np.abs(frequencies) < cutoff] = 0
    final = np.fft.ifft(fft_wave)

    return np.real(final)

def dream(frequency, duration):
    """Add an envelope to the wave that makes it sound dreamy"""
    #   (1) Define the harmonics
    base = sine_wave(frequency, duration)
    under = sine_wave(frequency / 2, duration)
    base += under
    base = distort(base, 3)

    #   (2) Define A,S,D,R
    a = duration * 0.05
    d = duration * (1.0 - (0.05 + 0.39 ))
    s = 1.0
    r = duration * 0.39

    #   (3) Apply the effects to the wave
    return envelope(base, a, d, s, r) * 0.8

def pitch_envelope(start_frequency : int = 330, end_frequency : int = 150, duration : float = 0.3, sample_rate : int =SAMPLE_RATE) -> np.ndarray:
    """Create a wave with a rapid downward frequency to simulate a striking sound"""
    #   Determine the number of points
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    #   Create the frequency
    frequency = np.logspace(np.log10(start_frequency), np.log10(end_frequency), len(t))

    #   Build the phase
    phase = 2 * np.pi * np.cumsum(frequency) / sample_rate
    
    #   Return the wave
    return np.sin(phase)


def snare_envelope(wave):
    """Add a snare envelope to the wave"""
    return envelope(wave, 0, 0.5, 0.0, 0.0, sample_rate=len(wave))


def white_noise(wave : np.ndarray, noise_amount : float = 0.1, cutoff = 0.0):
    """Add a sizzle/static effect to a sound by adding white noise"""
    noise = np.random.normal(0, noise_amount, len(wave))
    index = 0
    for w in wave:
        if abs(w) < cutoff:
            pass
        else:
            wave[index] += noise[index]
        index += 1

    return wave #+ noise

def makeSilent(wave):
    w = wave.copy()
    for i in range(len(w) // 2):
        w[i] = 0
    
    for i in range(len(w) // 2, len(w)):
        w[i] *= 2.0
    
    return w


def distort(wave : np.ndarray, distortion_amount : float =0.1):
    """Add a gritty effect to a sound"""
    return np.tanh(distortion_amount * wave) / np.tanh(distortion_amount)

"""The values for t (time) are as follows,
Immediate: t < 0.01
Very fast: 0.01 < t < 0.1
Fast: 0.1 < t < 0.5
Medium: 0.5 < t < 1.0
Slow: t > 1.0
"""

def pluck(frequency: int = 250, duration: float = 0.3, attack = 0.02, decay=0.1, sustain=0.3, release=0.1) -> np.ndarray:
    """String Instruments
    Attack: very fast
    Decay: short
    Sustain: low
    Release: medium
    """
    # (1) Generate a base tone
    base = sine_wave(frequency, duration)
    base = distort(base, 4)
    low = sine_wave(frequency / 2, duration)
    base += low
    

    # (2) Modify the A, D, and R values to fit the duration
    attack = duration * (0.02 / 0.3)
    decay = duration * (0.1 / 0.3)
    release = duration * (0.1 / 0.3)

    # (3) Apply the envelope
    return fade_out(envelope(base, attack, decay, sustain, release), 5) * 0.6

def pluck2(frequency: int = 250, duration: float = 0.3, attack = 0.02, decay=0.1, sustain=0.3, release=0.1) -> np.ndarray:
    """String Instruments
    Attack: very fast
    Decay: short
    Sustain: low
    Release: medium
    """
    # (1) Generate a base tone
    base = sine_wave(frequency, duration)
    a = sine_wave(shift_note(frequency, -6), duration)

    low = sine_wave(frequency / 2, duration)
    lowa = sine_wave(shift_note(frequency, -6) / 2, duration)

    base = distort(base, 4)
    a = distort(a, 2)

    base += low
    a += lowa
    #a = distort(a, 4)

    

    # (2) Modify the A, D, and R values to fit the duration
    attack = duration * (0.02 / 0.3)
    decay = duration * (0.1 / 0.3)
    release = duration * (0.1 / 0.3)

    # (3) Apply the envelope
    base = fade_out(envelope(base, attack, decay, sustain, release), 5)
    a = fade_out(envelope(a, attack, decay, sustain, release), 5)
    
    return base + a

def pluck3(frequency: int = 250, duration: float = 0.3, attack = 0.02, decay=0.1, sustain=0.3, release=0.1) -> np.ndarray:
    """String Instruments
    Attack: very fast
    Decay: short
    Sustain: low
    Release: medium
    """
    # (1) Generate a base tone
    base = sine_wave(frequency, duration)
    a = sine_wave(shift_note(frequency, -6), duration)

    base = distort(base, 4)
    a = distort(a, 4)

    #low = sine_wave(frequency / 2, duration)
    #base += low
    

    # (2) Modify the A, D, and R values to fit the duration
    attack = duration * (0.02 / 0.3)
    decay = duration * (0.1 / 0.3)
    release = duration * (0.1 / 0.3)

    # (3) Apply the envelope
    base = fade_out(envelope(base, attack, decay, sustain, release), 5) * 0.6
    a = fade_out(envelope(a, attack, decay, sustain, release), 5) * 0.6
    
    return base + a

def pluck4(frequency: int = 250, duration: float = 0.3, attack = 0.02, decay=0.1, sustain=0.3, release=0.1) -> np.ndarray:
    """String Instruments
    Attack: very fast
    Decay: short
    Sustain: low
    Release: medium
    """
    # (1) Generate a base tone
    base = sine_wave(frequency, duration)
    base = distort(base, 12)

    low = sine_wave(frequency / 2, duration)
    base += low
    

    # (2) Modify the A, D, and R values to fit the duration
    attack = duration * (0.02 / 0.3)
    decay = duration * (0.1 / 0.3)
    release = duration * (0.1 / 0.3)

    # (3) Apply the envelope
    return fade_out(envelope(base, attack, decay, sustain, release), 5) * 0.6



def xylo(frequency, duration):
    volume_reduction = 0.4

    base = sine_wave(frequency, duration)
    a = sine_wave(frequency * 4, duration) * (volume_reduction)
    b = sine_wave(frequency * 9, duration) * (volume_reduction / 2)

    base += (a + b)

    a = 0.1 * duration
    d = 0.2 * duration
    s = 1.0
    r = 0.4 * duration

    base = envelope(base, a, d, s, r)

    return base

def xylotech(frequency, duration):
    volume_reduction = 0.4

    base = sine_wave(frequency, duration)
    a = sine_wave(frequency * 3, duration) #* (volume_reduction / 2)
    b = sine_wave(frequency / 4, duration) #* (volume_reduction)

    base += (a + b)

    a = 0.001 * duration
    d = 0.2 * duration
    s = 1.0
    r = 0.3 * duration

    base = envelope(base, a, d, s, r)
    return fade_out(base, 2)

def xylotech2(frequency, duration):
    volume_reduction = 0.4

    #   First Harmonic
    base = sine_wave(frequency, duration)
    a = sine_wave(frequency * 3, duration)
    b = sine_wave(frequency / 2, duration)
    base += (a + b)

    #   Second Harmonic
    freq_2 = shift_note(frequency, -5)
    base2 = sine_wave(freq_2, duration)
    a2 = sine_wave(freq_2 * 3, duration)
    b2 = sine_wave(freq_2 / 2, duration)
    base2 += (a2 + b2)
    
    #   Combine the harmonics
    base += base2

    #   Apply the envelope
    a = 0.001 * duration
    d = 0.2 * duration
    s = 1.0
    r = 0.3 * duration
    base = envelope(base, a, d, s, r)

    #   Fade and return
    return fade_out(base, 2)


def xylohorn2(frequency, duration):
    volume_reduction = 0.4

    #   First Harmonic
    base = sine_wave(frequency, duration)
    a = sine_wave(frequency * 2, duration)
    b = sine_wave(frequency / 4, duration)
    base += (a + b)

    #   Second Harmonic
    freq_2 = shift_note(frequency, -5)
    base2 = sine_wave(freq_2, duration)
    a2 = sine_wave(freq_2 * 6, duration)
    b2 = sine_wave(freq_2 / 4, duration)
    base2 += (a2 + b2)
    
    #   Combine the harmonics
    #base += base2

    #   Apply the envelope
    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.6
    r = 0.01 * duration
    base = envelope(base, a, d, s, r)

    #   Fade and return
    #base = lowpass(base, 11250)
    return base #fade_out(base, 2)

def xylobass(frequency, duration):

    #   First Harmonic
    base = sine_wave(frequency, duration)
    a = sine_wave(frequency * 2, duration)
    b = sine_wave(frequency / 4, duration)
    c = sine_wave(frequency / 2, duration)
    base += (a + b + c)

    
    
    #   Combine the harmonics
    #base += base2

    #   Apply the envelope
    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.6
    r = 0.01 * duration
    base = envelope(base, a, d, s, r)

    #   Fade and return
    #base = lowpass(base, 11250)
    return base #fade_out(base, 2)

def snare(frequency = 140, duration = 0.17):
    """Generate a snare sound, following the percussion framework
    Larger decrements create more of a bass effect"""
    #   (1) Create the initial swoop
    swoop = pitch_envelope(start_frequency=frequency, end_frequency=1, duration=duration)
    swoop_2 = pitch_envelope(start_frequency=frequency / 2, end_frequency=1, duration=duration)
    swoop += swoop_2

    #   (2) Add some effects
    swoop = distort(swoop, 2.0)
    swoop = white_noise(swoop, 0.007, 0.1)
    swoop = snare_envelope(swoop)
    
    return swoop

def snare2(frequency, duration):
    #   (1) Create the initial swoop
    swoop = sine_wave(frequency, duration)

    amp = 1.0
    for i in range(1, 100):
        amp *= i
        s = sine_wave(frequency / i, duration) / amp
        swoop += s

    #   (2) Add some effects
    swoop = distort(swoop, 1.0)
    swoop = white_noise(swoop, 0.007, 0.1)
    swoop = snare_envelope(swoop)
    
    return swoop

def bass(frequency=330, duration=0.1):
    """A bass drum sound"""
    frequency_end = 30
    decay_rate = 2
    
    # Time array
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))

    # 1. Frequency envelope (exponential decay)
    env = frequency * np.exp(-5 * t) + frequency_end

    # 1a. Add some harmonics
    enva = (frequency * 2) * np.exp(-5 * t) + (frequency_end)

    # 2. Amplitude envelope (sharp attack, quick decay)
    amp = np.exp(-decay_rate * 5 * t)

    # 3. Generate modulated sine wave
    kick_wave = amp * np.sin(2 * np.pi * np.cumsum(env) / SAMPLE_RATE)
    kick_wavea = amp * np.sin(2 * np.pi * np.cumsum(enva) / SAMPLE_RATE)

    # 4. Add subtle distortion
    kick_wave = np.tanh(kick_wave * 1.5)  # Soft clipping
    kick_wavea = np.tanh(kick_wavea * 1.5)  # Soft clipping
    
    # 5. Add a click sound
    click = np.random.randn(int(0.005 * SAMPLE_RATE)) * 0.1  # 5ms noise burst
    kick_wave[:len(click)] += click * np.linspace(1, 0, len(click))
    kick_wavea[:len(click)] += click * np.linspace(1, 0, len(click))
    

    #pattern = [1, 0, 0.7, 0, 0.5, 0, 0.3]  # Beat accents
    #kick_wave = np.concatenate([kick_wave * p for p in pattern])

    kick_wave = np.arctan(kick_wave * 2) * 0.8
    kick_wavea = np.arctan(kick_wavea * 2) * 0.8
    
    # Normalize and play
    kick_wave /= np.max(np.abs(kick_wave))
    kick_wavea /= np.max(np.abs(kick_wavea))


    #   Add Harmonics
    return kick_wave + kick_wavea

def flatten(wave, cutoff=0.5):
    
    #   np.where can do this in 1 line  #
    # np.where(np.abs(sine_wave) > cutoff, 
    #                np.sign(sine_wave) * cutoff, 
    #                sine_wave)
    
    #   Begin with a wave of the same length that contains all 0s   #
    flat = np.zeros_like(wave)

    for i in range(len(wave)):
        
        #   Cap the positive values to the cutoff   #
        if wave[i] > cutoff:
            flat[i] = cutoff

        #   Cap the negative values to the cutoff   #
        elif wave[i] < -cutoff:
            flat[i] = -cutoff
        
        #   Otherwise just keep the same value  #
        else:
            flat[i] = wave[i]

    return flat


def shrink(wave, cutoff=0.5, factor=0.5):
    """Shrink parts of the wave that are greater than the cutoff"""
    #   Begin with a wave of the same length that contains all 0s   #
    flat = np.zeros_like(wave)

    for i in range(len(wave)):
        
        #   Cap the positive values to the cutoff   #
        if wave[i] > cutoff:
            flat[i] = wave[i] * factor

        #   Cap the negative values to the cutoff   #
        elif wave[i] < -cutoff:
            flat[i] = wave[i] * factor
        
        #   Otherwise just keep the same value  #
        else:
            flat[i] = wave[i]

    return flat



def bassh(frequency=330, duration=0.1):
    """Bass with some sexy harmonics"""
    base = bass(frequency, duration)

    for i in range(1, 11):
        base += bass(frequency / i, duration)
    
    return base

def percussify(frequency, duration, noise_factor):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    # wave = np.sin(2 * np.pi * frequency * t)

    wave = pitch_envelope(frequency, 1, duration)

    noise = noise_factor * wave**2 #* np.random.randn(len(t))
    # noise = np.random.normal(loc=0, 
    #                          scale=noise_factor * np.abs(wave)
    #                          )
    
    return wave + noise


def symbol(frequency=330, duration=0.1):
    """A symbol; best used to keep tempo"""

    # Time array
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    
    # Generate multiple high-frequency sine waves
    frequencies = np.random.uniform(frequency, frequency / 2, 20)  # 20 random frequencies between 3kHz and 7kHz
    cymbal = np.zeros_like(t)
    for freq in frequencies:
        cymbal += np.sin(2 * np.pi * freq * t)
    
    # Add noise for the characteristic "sizzle"
    cymbal = white_noise(cymbal, 0.5)
    #cymbal += noise

    
    # Envelope shaping (fast attack, slow decay)
    envelope = np.exp(-t * 5)  # Adjust the 5 for different decay rates
    cymbal *= envelope
    
    # Normalize
    cymbal = cymbal / np.max(np.abs(cymbal))
    
    return cymbal

    #   (1) Generate the base tone using a pitch envelope
    #base = pitch_envelope(start_frequency=frequency, end_frequency=1, duration=duration)
    #base = percussify(frequency, duration, 0.01)

    #   (2) Find A,D,S,R
    a = 0.00 * duration
    d = 0.1 * duration
    s = 1.0
    r = 0.1 * duration

    #   (3) Apply the envelope and return the sound
    base = envelope(base, a, d, s, r)

    #base = distort(base, 2.0)
    #base = percussify(base, 0.05)
    return base * 0.7

def pad(frequency: int = 300, duration: float = 1.0, attack = 1.0, decay = 0.5, sustain = 0.9, release = 1.0) -> np.ndarray:
    base = sine_wave(frequency, duration)

    return envelope(base, attack, decay, sustain, release)

def bell(frequency: int = 300, duration: float = 1.0) -> np.ndarray:
    base = sine_wave(frequency, duration)

    return envelope(base, 0.05, 1.0, 0.5, 1.4)

def percussion(frequency = 400, duration = 0.2, sample_rate = SAMPLE_RATE) -> np.ndarray:
    """Percussion Instruments
    Attack: immediate
    Decay: very fast
    Sustain: barely any
    Release: fast
    """
    # (1) Generate a base tone
    base = slur(frequency,frequency- 200, duration / 2)
    a=0.005 * duration
    d=0.05 * duration
    s=0.1
    r=0.5 * duration

    # (2) Apply the envelope
    return envelope(base, a,d,s,r)

def bandpass(wave, lowcut, highcut, filter_length = 101):
    """Basic FIR bandpass filter using windowed sinc method"""
    nyq = 0.5 * SAMPLE_RATE
    low = lowcut / nyq
    high = highcut / nyq
    n = np.arange(filter_length)
    
    # Ideal bandpass impulse response
    sinc = np.sinc(2 * high * (n - (filter_length-1)/2)) - np.sinc(2 * low * (n - (filter_length-1)/2))
    
    # Apply Hamming window
    window = np.hamming(filter_length)
    kernel = sinc * window
    
    # Normalize kernel
    kernel /= np.sum(kernel)
    
    # Apply filter via convolution
    return np.convolve(wave, kernel, mode='same')

def piano(frequency, duration):
    #   (1) Get the wave
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 26):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i
    
    #bass = sine_wave(frequency * 2, duration)
    #base += (a)

    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return base

def piano2(frequency, duration):
    #   First Key
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 11):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i

    #   Second Key
    freq_2 = frequency / 2
    a = sine_wave(freq_2, duration)
    amplitude = 1.0
    for i in range(1, 51):
        a += sine_wave(freq_2 * i, duration) * amplitude
        amplitude /= i

    
    #   Combine the keys
    base += a


    #   Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)

    #   Return the wave
    return base

def pianobass(frequency, duration):
    #   (1) Get the wave
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 51):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i
    
    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return base

def pianobass(frequency, duration):
    #   First Key
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 51):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i

    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return base

def pianobass2(frequency, duration):
    #   First Key
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 51):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i
    
    #   Second Key
    freq_a = frequency / 2
    a = sine_wave(freq_a, duration)
    amplitude = 1.0
    for i in range(1, 51):
        a += sine_wave(freq_a * i, duration) * amplitude
        amplitude /= i

    base += a
    
    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return base

def pianobass3(frequency, duration):
    #   First Key
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 51):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i
    
    #   Second Key
    freq_a = frequency / 2
    a = sine_wave(freq_a, duration)
    amplitude = 1.0
    for i in range(1, 51):
        a += sine_wave(freq_a * i, duration) * amplitude
        amplitude /= i

    #   Third Key
    freq_b = frequency / 4
    b = sine_wave(freq_b, duration)
    amplitude = 1.0
    for i in range(1, 51):
        b += sine_wave(freq_b * i, duration) * amplitude
        amplitude /= i

    #   Metallic Key
    freq_m = frequency / 8
    m = sine_wave(freq_m, duration)
    amplitude = 1.0
    for i in range(1, 51):
        m += sine_wave(freq_m * i, duration) * amplitude
        amplitude /= i


    base += (a + b + m)
    
    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.8 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return lowpass(fade_out(base, 8), 5000)

def pianobass4(frequency, duration):
    """pianobass2 but distorted"""

    base = pianobass2(frequency, duration)
    base = distort(base, 2.0)

    # #   First Key
    # base = sine_wave(frequency, duration)
    # amplitude = 1.0
    # for i in range(1, 51):
    #     base += sine_wave(frequency * i, duration) * amplitude
    #     amplitude /= i
    # base = distort(base, 8.0)
    

    # #   Second Key
    # freq_a = frequency / 2
    # a = sine_wave(freq_a, duration)
    # amplitude = 1.0
    # for i in range(1, 51):
    #     a += sine_wave(freq_a * i, duration) * amplitude
    #     amplitude /= i
    # a = distort(a, 4.0)
    # base += a
    
    # #   (2) Apply the Envelope
    # a = 0.005 * duration
    # d = 0.3 * duration
    # s = 0.1
    # r = 0.05 * duration

    # base = envelope(base, a, d, s, r)


    #   Return the wave
    return base

def pianotreble(frequency, duration):
    #   (1) Get the wave
    base = sine_wave(frequency, duration)
    amplitude = 1.0
    for i in range(1, 16):
        base += sine_wave(frequency * i, duration) * amplitude
        amplitude /= i

    #   (2) Apply the Envelope
    a = 0.005 * duration
    d = 0.3 * duration
    s = 0.1
    r = 0.05 * duration

    base = envelope(base, a, d, s, r)
    #   Return the wave
    return base
def skirt(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    
    # 1. Core metallic resonance (FM synthesis)
    carrier_freq = frequency * 112 # Base frequency (Hz)
    mod_freq = 120       # Modulation frequency (Hz)
    mod_index = 8        # Modulation intensity
    fm_wave = np.sin(2 * np.pi * carrier_freq * t + 
                    mod_index * np.sin(2 * np.pi * mod_freq * t))
    
    # 2. Noise transient layer (attack)
    noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
    fm_wave += noise

    # 3. Bandpass filtering for tonal shaping
    fm_wave = bandpass(fm_wave, 2000, 6000)
    
    # 4. Amplitude envelope (sharp attack/decay)
    env = np.exp(-t * 25) * (1 - np.exp(-t * 200))
    processed = fm_wave * env
    
    # 5. Add lo-fi texture (bit-crush effect)
    bit_depth = 10
    processed = np.round(processed * (2**bit_depth)) / (2**bit_depth)
    
    # # Add comb filtering for "springy" resonance
    # delay_time = 1/8000  # 8kHz delay line
    # comb = signal.lfilter([1], [1] + [0]*(int(delay_time*SAMPLE_RATE)-1) + [-0.7], processed)

    # # Apply tape saturation
    # saturated = np.arctan(comb * 3) * 0.8

    # # Add stereo widening
    # left = saturated * np.exp(-t * 5)
    # right = saturated * np.exp(-t * 4.8)
    # stereo_skirt = np.vstack([left, right]).T
    
    # Normalize and return
    return processed / np.max(np.abs(processed))
    
def skirt2(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    
    # 1. Core metallic resonance (FM synthesis)
    carrier_freq = frequency # Base frequency (Hz)
    mod_freq = 220   # Modulation frequency (Hz)
    mod_index = 20        # Modulation intensity
    fm_wave = np.sin(2 * np.pi * carrier_freq * t + 
                    mod_index * np.sin(2 * np.pi * mod_freq * t))
    
    # 2. Noise transient layer (attack)
    noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
    fm_wave += noise

    # 3. Bandpass filtering for tonal shaping
    fm_wave = bandpass(fm_wave, 2000, 6000)
    
    # 4. Amplitude envelope (sharp attack/decay)
    env = np.exp(-t * 25) * (1 - np.exp(-t * 200))
    processed = fm_wave * env
    
    # 5. Add lo-fi texture (bit-crush effect)
    bit_depth = 10
    processed = np.round(processed * (2**bit_depth)) / (2**bit_depth)
    
    # # Add comb filtering for "springy" resonance
    # delay_time = 1/8000  # 8kHz delay line
    # comb = signal.lfilter([1], [1] + [0]*(int(delay_time*SAMPLE_RATE)-1) + [-0.7], processed)

    # # Apply tape saturation
    # saturated = np.arctan(comb * 3) * 0.8

    # # Add stereo widening
    # left = saturated * np.exp(-t * 5)
    # right = saturated * np.exp(-t * 4.8)
    # stereo_skirt = np.vstack([left, right]).T
    
    # Normalize and return
    return processed / np.max(np.abs(processed))

"""Video Game Sound Effects ------------------------------------------------------------------------"""
def interact(frequency = 400, duration = 0.3, sample_rate = SAMPLE_RATE):
    wave = percussion(frequency, duration, sample_rate)
    wave_2 = percussion(frequency=frequency-100, duration=duration, sample_rate=sample_rate + 1000)
    return distort(join_waves(wave, wave_2), 2.0)

def text_next():
    return envelope(interact(400), 0.3 * 0.01, 0.3 * 0.2, 0.4, 0.3 * 0.1)


def text_close():
    duration = 0.3

    #   Wave 1 - High
    wave_1 = interact(400)

    #   Wave 2 - Low
    wave_2 = interact(350)

    #   Wave 3 - Mid
    wave_3 = interact(300)
    wave_3a = interact(500)
    
    #   Shorten Wave 2 and 3
    wave_4 = wave_2[:-8000]
    wave_5 = wave_3[:-9000]

    #   Combine Wave 4 and 5
    wave_6 = add_waves(wave_4, wave_5, position=0)

    #   Combine Wave 1 and 3; Combine Wave 6 with the new wave
    final = add_waves(wave_6, (wave_3a + wave_1) * 0.5)
    
    return envelope(final, 0.01 * duration, 0.1 * duration, 1.0, 0.8 * duration)

def text_done():
    duration = 0.3
    #   Wave 1 - High
    wave_1 = interact(300)

    #   Wave 2 - Low
    wave_2 = interact(300)

    #   Wave 3 - Mid
    wave_3 = interact(400 / 2)
    
    #   Shorten Wave 2 and 3
    wave_4 = wave_2[:-8000]
    wave_5 = wave_3[:-9000]

    #   Combine Wave 4 and 5
    wave_6 = add_waves(wave_5, wave_4, position=0)

    #   Combine Wave 1 and 3; Combine Wave 6 with the new wave
    final = add_waves(wave_6, (wave_1  + wave_3) * 0.5, -1)
    
    return envelope(final, 0.01 * duration, 0.1 * duration, 1.0, 0.1 * duration)


def text(frequency = 400, duration = 0.25, decrement = 200, amp_factor = 0.8):
    """Create a text sound inspired by Twilight Princess"""

    #   (1) Create a string tone
    base = pluck(frequency, 0.25)
    #base = distort(base, 4.0)


    #   (2) Create a lower string tone
    base_2 = pluck(ensure_1(frequency-decrement), 0.25)
    #base_2 = distort(base_2, 4.0)


    #   (3) Combine the tones and wrap them in a snare envelope
    final = base + base_2
    final = envelope(final, 0.01 * 0.25, 0.2 * 0.25, 0.5, 0.01 * 0.25) * amp_factor

    return final

def text_sad(frequency = 300, decrement = 200, amp_factor = 1.2):
    #   (1) Create a string tone
    base = pluck(frequency, 0.25)
    #base = distort(base, 4.0)


    #   (2) Create a lower string tone
    base_2 = pluck(ensure_1(frequency-decrement), 0.25)
    #base_2 = distort(base_2, 4.0)


    #   (3) Combine the tones and wrap them in a snare envelope
    final = base + base_2
    final = envelope(final, 0.01 * 0.25, 0.2 * 0.25, 0.5, 0.01 * 0.25) * amp_factor

    return final

def text_angry(frequency = 400, decrement = 200, amp_factor = 1.2):
    #   (1) Create a string tone
    base = pluck(frequency, 0.25)
    #base = distort(base, 4.0)


    #   (2) Create a lower string tone
    base_2 = pluck(ensure_1(600-decrement), 0.25) * 1.3
    #base_2 = distort(base_2, 4.0)


    #   (3) Combine the tones and wrap them in a snare envelope
    final = base + base_2
    final = envelope(final, 0.01 * 0.25, 0.2 * 0.25, 0.5, 0.01 * 0.25) * amp_factor

    return distort(final, 1.0)

def sound_generator(base_frequency: int = 100, max_frequency: int = 900, increment : int = 50, envelope : any = pluck, folder : str ="", play_sounds : bool = False) -> None:
    """Writes a series of .wav files to a directory. Produce sounds in bulk.
    
    base_frequency -> the starting frequency\n
    max_freuquency -> the top frequency\n
    increment -> the value to increment the frequency by for each .wav file\n
    envelope -> the envelope that will be applied to each sine wav\n
    folder -> the directory where the outputted files will be written"""
    
    #   Initialize the vars we increment each round
    current_frequency = base_frequency
    name = 0

    while current_frequency <= max_frequency:
        #   Get the sound + envelope
        sound = envelope(current_frequency)

        #   Play the sound
        if play_sounds:
            pass
           ## play(sound)

        #   Save the sound
        write(sound, folder, str(name))

        #   Prepare to generate and play the next sound
        current_frequency += increment
        name += 1

def full_generation(base_frequency: int = 100, max_frequency: int = 900, increment : int = 50, play_sounds : bool = False):
    """Generates a series of .wav files for each instrument/ADSR preset"""
    
    #   Strings
    sound_generator(base_frequency, max_frequency, increment, pluck, BULK_FOLDER + "\\strings", play_sounds)
    
    #   Percussion
    sound_generator(base_frequency, max_frequency, increment, percussion, BULK_FOLDER + "\\percussion", play_sounds)

    #   Pad

    #   Brass

    #   Snares
    sound_generator(base_frequency, max_frequency, increment, percussion, BULK_FOLDER + "\\snares", play_sounds)
    
    #   Bass

class Sine(object):
    """A class used to generate sine waves and harmonics"""
    
    def __init__(self, frequency: int, duration: float):
        """Initialize with a frequency and duration"""
        self.wave = sine_wave(frequency, duration)
        self.frequency = frequency
        self.duration = duration

    def __add__(self, other):
        """Add two waves to create a longer sound.
        This function calls audio.add_waves to combine the two arrays.
        This is different than vector addition on two sine waves."""
        
        self.wave = add_waves(self.wave, other.wave, -1)
        self.duration = self.duration + other.duration

    def __call__(self, *args, **kwds):
        return self.wave

    def __repr__(self):
        return self.wave

    def __str__(self):
        """__str__"""
        return str(self.wave)
    
    def get_wave(frequency: int = 300, duration: float = 0.3) -> np.ndarray:
        """Generates a sine wave lickety split"""
        return sine_wave(frequency, duration)
    
    def add_harmonics(self, *frequencies):
        """Takes in an audio sample; adds each wave passed into the function to the sample"""
        for f in frequencies:
            if type(f) is Sine:
                pass
            else:
                self.wave += sine_wave(f, self.duration)

# class Note(object):

#     def __add__(self, other: float = 0.5 | 1.0):
#         return Note()