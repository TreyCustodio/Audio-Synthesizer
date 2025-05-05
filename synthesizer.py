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
    add_harmonics(fundamental, 9)

    #   (2) Add an envelope #





    #   Helper Methods  -> Because we want to be able to use freq   #
    def add_harmonics(wav: np.ndarray, 
                      harmonics: int = 1,
                      const: int = 1,
                      coeff: float = 1.0,
                      freq_func: function = None):
        """Mutator method that adds harmonics to a fundamental wave based on several params.

        harmonics -> number of harmonics to add\n
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






def main():
    sound = synthesize()
    write(sound, "tests", "synth")

if __name__ == '__main__':
    main()