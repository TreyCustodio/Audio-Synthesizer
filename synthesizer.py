from modules.audio import *

"""
Drive the synthesizing process here
"""

def synthesize():
    #   Given the bpm, frequency, and duration ... #
    bpm = 80
    freq = C3
    duration = get_quarter(bpm)


    #   Define the fundamental wave    #
    fundamental = sine_wave(freq, duration)


    #   (1) Add some Harmonics  #
    add_harmonics(fundamental, freq, duration)
    

    #   (2) Add an envelope #
    a = 0.01 * duration
    d = 0.2 * duration
    s = 0.5
    r = 0.7 * duration
    sound = envelope(fundamental, a,d,s,r)

    return sound


def add_harmonics(wav: np.ndarray, freq: float = 100.0, duration: float = 0.3,
                    harmonics: int = 2,
                    const: int = 1,
                    coeff: float = 1.0,
                    freq_func = None):
    """Mutator method that adds harmonics to a fundamental wave based on several params.

    harmonics -> number of harmonics to add\n
    freq -> the fundamental frequency\n
    duration -> number of seconds the sample lasts\n
    const -> the constant that the frequency will be multiplied by (1 by default)\n
    coeff -> the coefficient that i (from the for loop) will be multiplied by\n
    freq_func -> a mathematical function that will be applied to i\n
    """

    #   Begin the for loop using the harmonics paramater    #
    for i in range(1, harmonics+1):
        #   Use the frequency function  #
        if freq_func:
            wav += sine_wave(freq * const * (coeff * freq_func(i)), duration)
        
        #   Apply no function to i; just multiply by the coefficient   #
        else:
            wav += sine_wave(freq * const * (coeff * i), duration)
            wav /= i



    






def main():
    sound = synthesize()
    write(sound, "tests", "synth")

if __name__ == '__main__':
    main()