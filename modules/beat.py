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
    
    def convert_notes(self, notes: list):
        """Take a python list of audio signals and combines them into one signal"""
        #   Initialize the array to be returned #
        ##  If the data types are Notes, just call them to convert them to ndarrays ##
        if issubclass(Note, type(notes[0])):
            final = notes[0]()
        else:
            final = notes[0]

        #  Add the rest of the notes to the wave #
        for i in range(1, len(notes)):
            ##  Call the Note objects to get their arrays    ##
            if issubclass(Note, type(notes[i])):
                final = add_waves(final, notes[i]())
            else:
                final = add_waves(final, notes[i])
        
        return final
    
    def produce_one(self, key):
        """Produce one instrument"""
        self.produce_full(self.instruments[key])

        
    def produce_full(self, instruments: dict = {}) -> None:
        """Combine each part of the song and produce the full beat"""

        #   Initialize the prod with 1 millisecond of silence   #
        prod = sine_wave(0, 0.001)

        #   Get the instruments to combine  #
        if instruments == {}:
            instruments = self.instruments

        #   Loop through each instrument    #
        for key in instruments:
            #   Get the instrument's notes from the dict    #
            notes = instruments[key][1]

            #   Convert the notes into an ndarray   #
            final = self.convert_notes(notes)
            
            #   Add the converted notes to the production  #
            prod = mix(
                prod,
                final
            )
        
        #   Set the production value    #
        self.production = prod

    def add_lib(self, wave):
        print("prod", self.production)
        print("adlib", wave)

        self.production = mix(
            self.production, wave
        )


    def save(self, sound, name = "", norm=True, convert=True, path=""):
        """Save the sound to the desired folder"""
        if convert:
            sound = self.convert_notes(sound)
        write(sound, path, name, norm=norm, volume_factor=10_000)

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