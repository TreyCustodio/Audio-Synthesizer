from modules.audio import *
from random import random

"""
Drive the synthesizing process here
"""



"""   Modulation Functions    """
def exp(b):
    """Exponential modulation preserves lower harmonics"""
    def exponential(x):
        return x ** b
    
    return exponential

def log(x):
    """Logarithmic modulation preserves mig-high harmonics"""
    return np.log(x + 1)

def stochastic(x):
    """Unpredictable, noisy modulation"""
    return random() * x

def inv(x):
    return 1/x

def lin(b):
    def adjust(x):
        return (x ** b)
    return adjust

def bass_harms(b=2):
    def func(x):
        return x / (b * x)
    return func


"""   Synthesizing Process    """
def synthesize(freq: float = 100.0, duration: float = 0.3, bpm=80, # Data for the fundamental sine wave
               harmonics: int = 2, coeff: float = 1.0, # Data for additive synthesis and frequency adjustments
               freq_func = None, amp_func = None, # Data for Frequency and Amplitude Modulation
               a: float = 0.01, d: float = 0.2, s: float = 0.5, r: float = 0.7
               ):
    
    #   Given the bpm, frequency, and duration ... #


    #   Define the fundamental wave    #
    fundamental = sine_wave(freq, duration)


    #   (1) Add some Harmonics  #
    if harmonics > 0:
        add_harmonics(fundamental, freq, duration,
                    harmonics, coeff,
                    freq_func, amp_func)
    

    #   (2) Add an envelope #
    a = a * duration
    d = d * duration
    s = s
    r = r * duration
    sound = envelope(fundamental, a,d,s,r)

    return sound



"""   Process for Additive Synthesis    """
def add_harmonics(wav: np.ndarray, freq: float = 100.0, duration: float = 0.3,
                    harmonics: int = 2,
                    coeff: float = 1.0,
                    freq_func = None,
                    amp_func = None):
    """Mutator method that adds harmonics to a fundamental wave based on several params.

    harmonics -> number of harmonics to add\n
    freq -> the fundamental frequency\n
    duration -> number of seconds the sample lasts\n
    const -> the constant that the frequency will be multiplied by (1 by default)\n
    coeff -> the coefficient that i (from the for loop) will be multiplied by\n
    freq_func -> a mathematical function that will be applied to i\n
    amp_func -> a mathematical function that will be applied to i, with the output acting as the amplitude.\n

    """

    #   Begin the for loop using the harmonics paramater    #
    for i in range(1, harmonics+1):

        #   Use the frequency function  #
        if freq_func:
            harm = sine_wave(freq * (coeff * freq_func(i)), duration)

            #   Use the amplitude function to modulate the amplitude    #
            if amp_func:
                if amp_func == "hold":
                    pass
                else:
                    a = amp_func(i)
                    harm /= a

            #   Linearly attenuate the amplitude    #
            else:
                harm /= i + 1


        #   Apply no function to i; just multiply by the coefficient   #
        else:
            harm = sine_wave(freq * (coeff * i), duration)

            #   Use the amplitude function to modulate the amplitude    #
            if amp_func:
                a = amp_func(i)
                harm /= a

            #   Linearly attenuate the amplitude    #
            else:
                harm /= i + 1
                pass
    
        wav += harm


    






def main():
    #   Params  #
    freq = G3
    duration = get_quarter(80)
    bpm=80

    harmonics = 5
    const = 2
    coeff = 1
    freq_func = exp(2)
    amp_func = log


    #   Function Call   #
    sound = synthesize(freq, duration, bpm,
                       harmonics, const, coeff,
                       freq_func, amp_func
                       )


    #   Save the sound  #
    write(sound, "tests", "synth")


if __name__ == '__main__':
    main()