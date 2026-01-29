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


    def save(self, sound, name = "", norm=True, convert=True, stereo = True, folder="", volume = 13_000):
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

        write(sound, path, name, norm=norm, volume_factor=volume)

    def get_instruments(self):
        return
    
    def save_instrument(self, key, notes: list = None):
        self.instruments[key][1] = notes
    

    def set_path(self, path):
        self.path = path
        print("Path changed to \'" + path + "\'")

    def export_full(self, stereo = True):
        self.get_instruments()
        self.produce_full(export = True, stereo=stereo)
        self.save(self.production, "_prod", convert=False, stereo=False)

    def export_selection(self, instruments = {}, name = "_selection", stereo=True, volume = 13_000):
        self.produce_full(instruments, export = False, stereo=stereo)
        self.save(self.production, name, convert=False, stereo=False, volume = volume)
        print(name + " has been exported successfully!")


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


class Project(Beat):
    def __init__(self, bpm, name="project"):
        super().__init__(bpm, path = os.path.join("_Projects", name))
        #   Instruments #


        #   Melody  #
            

        #   Rhythm / Percussion  #
        ##  Bass    ##
        self.bell = AMTR.Bell(amp=0.1, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)

        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)
        
        self.bass1 = LowSynth(1.5, wave_1 = False, wave_2 = True, wave_3 = False, sustain=0.6)
        self.bass2 = LowSynth(1.0, wave_1 = False, wave_2=False, wave_3 = True,
                              sustain=1.0)
        self.bass3 = Bass_1(amp=0.8, 
                            freq_mod = (1.5), 
                            attack=0.01, attack_max = 0.02, decay=0.0, sustain=1.0, release=0.01,
                            amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

        #   Percussion  #
        ##  Chimes
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Kicks
        # self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")
        self.kick1 = Nine_Sample(amp=0.00003, name="kick-classic.wav")
        self.kick2 = E1_Samples(amp=0.00003, name="kick16.wav")
        self.tight_kick = Nine_Sample(amp=0.00004, name="kick-tight.wav")
        self.dry_kick = Nine_Sample(amp=0.00007, name="kick-dry.wav")
        self.kick_electro1 = Nine_Sample(amp=0.00004, name="kick-electro01.wav")
        self.jazz_kick7 = Radar_Jazz(amp=0.00006, path = os.path.join("Drum_Hits", "Kick07.wav"))
        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")
        self.crash2 = Nine_Sample(name="crash-808.wav")


        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav", amp=0.00005)
        self.per_tambo = Nine_Sample(name="perc-tambo.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.closed2 = Nine_Sample(amp = 0.00008, name="hihat-electro.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")
        self.digi1 = Nine_Sample(name="hihat-digital.wav")
        self.perc = Nine_Sample(amp=0.00005, name="perc-808.wav")
        self.jazz_hat2 = Radar_Jazz(amp=0.00001)
        self.jazz_hit2 = Radar_Jazz(amp=0.00001, path = os.path.join("Drum_Hits", "Kit_Hit_02.wav"))

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")
        self.snare5 = Nine_Sample(amp=0.00007, name="snare-analog.wav")
        self.snare8 = Nine_Sample(amp=0.00007, name="snare-808.wav")
        self.cold_snare = GlobalSample(0.00007, os.path.join("samples", "snares", "snare_5.wav"))
        self.jazz_snare5 = Radar_Jazz(amp=0.0001, path = os.path.join("Drum_Hits", "Snare05.wav"))
        self.jazz_snare6 = Radar_Jazz(amp=0.0001, path = os.path.join("Drum_Hits", "Snare06.wav"))


        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")
        self.sumo_snare = Nine_Sample(name="snare-sumo.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")
        self.tom2 = Nine_Sample(name="tom-short.wav")



        #   Samples #
        self.synth1 = Eighties_Synths(amp=0.00005)
        self.synth2 = Eighties_Synths(amp=0.00005, path=os.path.join("Arps and Leads", "105bpm", "80s_FairLead[105]-D.wav"))
        self.synth3 = Eighties_Synths(amp=0.00005, path=os.path.join("Arps and Leads", "105bpm", "80s_FairLead[105]-A2.wav"))
        self.guit1 = Radar_Jazz(amp=0.00001, path = os.path.join("Guitar_Loops", "Guitar_Chords01(160BPM).wav"))
        self.guit2 = Radar_Jazz(amp=0.00001, path = os.path.join("Keys_Loops", "Keys_47(160BPM).wav"))
        
        
        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))
        self.fx9 = E1_Samples(name="fx09.wav")
        self.hey = GlobalSample(0.0001, os.path.join("samples", "hey.wav"))
        self.drop = GlobalSample(0.001, os.path.join("samples", "ambience", "drop_1.wav"))
        self.square = GlobalSample(0.0001, os.path.join("samples", "playful_square_80.wav"))
        self.steel_c = GlobalSample(0.000012, os.path.join("samples", "steel", "steel_pan_c.wav"))
        self.steel_a = GlobalSample(0.000012, os.path.join("samples", "steel", "steel_pan_a.wav"))

        self.instruments = {}

    def get_instruments(self, verse):
        return