from .audio import *
from .instruments import *
from abc import abstractmethod



class Beat:
    """Directory to save beats into"""
    FOLDER = "beats"
    
    """Initializing Instance Variables"""
    def __init__(self, bpm : float = 180.0, name: str = "", path = os.path.join("Tangible_Light", "ost")):
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

        #   Path    #
        self.path = path

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
        return

        
    def produce_full(self, instruments: dict = {}, export = False, stereo = False) -> None:
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
            
            if export:
                self.save(notes, str(key), stereo = True)

            #   Convert the notes into an ndarray   #
            final = self.convert_notes(notes)
            
            #   Add the converted notes to the production  #
            
            prod = mix(
                prod,
                final
            )

        
        if stereo:
            prod = np.column_stack([prod, prod])


        #   Set the production value    #
        self.production = prod

    def add_libs(self, wave):
        return


    def save(self, sound, name = "", norm=True, convert=True, stereo = True, folder=""):
        """Save the sound to the desired folder.
        Set convert to false if *sound* is already an np.ndarray"""
        path = os.path.join(self.path, folder)
        sound = sound.copy()
        
        if convert:
            sound = self.convert_notes(sound)

        if stereo:
            sound = np.column_stack((sound, sound))

        if not os.path.isdir(path):
            os.mkdir(path)

        write(sound, path, name, norm=norm, volume_factor=13_000)

    def get_instruments(self):
        return
    
    def save_instrument(self, key, notes: list = None):
        self.instruments[key][1] = notes
    

    def export_full(self, stereo = True):
        self.get_instruments()
        self.produce_full(export = True, stereo=stereo)
        self.save(self.production, "_prod", convert=False, stereo=False)


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