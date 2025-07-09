from .audio import *
from .instruments import *
from abc import abstractmethod



class Beat:
    """Directory to save beats into"""
    FOLDER = "beats"
    
    """Initializing Instance Variables"""
    def __init__(self, bpm : float = 180.0, name: str = ""):
        #   Bpm
        self.bpm = bpm
        beat = 1 / (bpm / 60)

        #   Note Lengths
        self.sixteenth = beat / 4
        self.eighth = beat / 2
        self.quarter = beat
        self.half = self.quarter * 2
        self.trey = self.quarter * 3
        self.whole = self.quarter * 4

        #   Note Lengths ver 2
        self.s = beat / 4
        self.e = beat / 2
        self.q = beat
        self.h = self.quarter * 2
        self.t = self.quarter * 3
        self.w = self.quarter * 4

        #   Instrument Dictionary
        self.instruments = {
            0 : None
        }

        #   File Name
        self.fileName = name

        #   Production
        #self.production = np.zeros((1,1), dtype=np.int16)
        self.production = sine_wave(0, 0.1)

    """ Getting Metadata"""
    
    def get_production(self):
        """Return the production of the beat"""
        return self.production




    """ Production"""
    def produce(self, key):
        """
        Add an instrument's section to the final production.

        Sample Input:
        current_instrument = 0 -> used to reference self.instruments[0] -> (Instrument(), sound wave)

        Sample Output:
        prod = mix(prod, m1) -> np.ndarray
        """

        self.production = mix(
            self.production,
            self.instruments[key][1]
        )
    
    def produce_full(self):
        #   Initialize the prod with 1 millisecond of silence   #
        prod = sine_wave(0, 0.001)

        #   Loop through each instrument    #
        for key in self.instruments:

            #   Calculate the instrument's waveform #
            notes = self.instruments[key][1] # A list of lists

            ##  Set the final waveform to the first note    #
            if issubclass(Note, type(notes[0])):
                final = notes[0]()
            else:
                final = notes[0]

            ##  Add the rest of the notes into the wave #
            for i in range(1, len(notes)):
                if issubclass(Note, type(notes[i])):
                    final = add_waves(final, notes[i]())
                else:
                    final = add_waves(final, notes[i])

                #final = add_waves(final, notes[i]())

            #   Mix the waveform with the prod  #
            prod = mix(
                prod,
                final
            )
        
        self.production = prod

    def save(self):
        write(self.fileName)


    def save_instrument(self, key, notes: list = None):
        self.instruments[key][1] = notes
        
    def metronome(self, bars=1):
        """Return a measure of a metronome"""
        n = Skirt(4, self.whole)

        m1 = build_measure(n.q_c, n.q_c, n.q_c, n.q_c)
        v1 = m1

        for i in range(bars-1):
            v1 = add_waves(v1, m1)
            
        return v1
    
    def tempo(self, sound):
        """Return 4 measures of an instrument keeping tempo"""
        m1 = build_measure(sound, sound, sound, sound,)
        v1 = build_measure(m1, m1, m1, m1)

        return v1

    def add_instrument(self, instrument: Instrument):
        #   Append the Instrument to the dictionary #
        self.instruments[list(self.instruments.keys())[-1] + 1] = instrument
    
    def del_instrument(self, key):
        #   Delete the instrument from the dictionary   #
        del self.instruments[key]