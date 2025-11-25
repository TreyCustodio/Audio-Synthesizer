from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Silent(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "10"))
        mod = 0.5
        
        #   ----- Melody -----  #
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)



        #   ----- Rhythm / Percussion -----  #
        #   Bass    #
        self.bass1 = LowSynth(2.0)
        
        self.bass2 = Bass_1(amp=0.6, attack=0.05, attack_max = 0.15, freq_mod = mod, decay = 0.0, sustain=1.0, release= 0.05, amp_final = 0.00000000001, top_freq = 2, harmonics=2)
        

        #   Hats    #
        self.hat1 = Rapping.Hat_1(amp=0.000025)

        self.hat2 = Rapping.Hat_2(amp=0.00003)

        self.hat3 = Rapping.Hat_3(amp=0.00012)

        self.hat4 = Hat_4(amp=0.00005)

        self.quick_hat = GlobalSample(0.000005, os.path.join("samples", "hats", "quicky.wav"))

        self.hatd = Rapping.Drill_Hat(amp=0.00004)


        #   Snares  #
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)
        
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        
        self.punchy_snare = GlobalSample(0.00008, os.path.join("samples", "snares", "punchy_snare.wav"))
        
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       

       #    Kicks   #
        self.kick1 = Tap4(1.0, attack=0.001, decay = 0.03, sustain=0.0, noise_amount=0.0)
        
        self.kick2 = GlobalSample(amp=0.00002, file_path=os.path.join("samples", "kick", "new-kick.wav"))
        
        self.kick3 = GlobalSample(amp=0.00002, file_path=os.path.join("samples", "kick", "new-kick_2.wav"))


        #   Chimes  #
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)
        

        #   Whistles    #
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = False, wave_3=True,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 0.3)
        


        #   ----- MIDIs -----   #
        self.bass_mid = GlobalSample(0.00001, os.path.join("samples", "AMTR", "10_Bass_MIDI.wav"))



        #   ----- Samples ----- #
        self.go = GlobalSample(0.00001, os.path.join("samples", "go_low.wav"))
        
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))



        #   ----- Dictionary of Instruments -----   #
        self.instruments = {}


    def get_instruments(self, verse = "main"):
        self.instruments = {
            #   Rhythm and Bass #
            "bass1" : [0, self.bass_1(verse)]

            #   Melody  #



            #   Samples / Libs  #

        }

    def bass_1(self, verse = "full"):
        v1 = [self.bass_mid.n(self.w*4)]

        return \
        v1 + v1
    

def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Silent(73)
    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    beat.get_instruments()
    beat.export_selection(name="10_main", volume=14_500)

    # beat.get_instruments("intro")
    # beat.export_selection(name = "10_intro", volume=14_500)
    # beat.get_instruments("main")
    # beat.export_selection(name = "10_main", volume=14_500)