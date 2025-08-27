from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O11(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "11"))

        #   Bass    #
        self.bass1 = Bass_1(amp=1.5, freq_mod=1.0, harmonics=10, attack = 0.05, decay=0.00, release = 0.1, sustain=1.0)
        self.bass2 = Bass(freq_mod=2, attack=0.01, sustain=1.0, release=0.01)

        #   Synths  #
        self.synth1 = Acoustic3(amp=0.5, harmonics=12, attack=0.05, decay=0.0, sustain=1.0, release=0.01,
                                # vol_1 = 4.0, vol_2 = 0.3,
                                vol_3 = 1.0, vol_4=0.000000000001,
                                )

        self.synth2 = Acoustic3(amp=0.4, attack=0.01, attack_max=0.01, harmonics=12, decay=0.05, sustain=0.7, release=0.05,
                                vol_3 = 0.000000000001, vol_4 = 1.0,
                                # vol_5 = 0.000000000001, vol_6 = 1.0,
                                vol_7 = 0.000000000001, vol_8 = 0.4
                                )
       
        self.synth3 = Tangible_Light.Bell(amp = 0.6, freq_mod=3)


        self.tell1 = DontTell2(freq_mod = 8, decay = 0.04)
        
        #   Percussion  #
        # self.hat1 = Rapping.Drill_Hat(amp=0.00005)
        # self.hat1 = Rapping.Crackle_Snare(amp=0.00001)
        self.hat1 = Rapping.Hat_1(amp=0.000065)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00003)


        self.snare1 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare2 = Rapping.Snare_3(amp=0.00004)
        self.snare3 = Rapping.Crackle_Snare(amp=0.00004)

        self.kick1 = Tap3(3.0, 25, noise_amount=0.0)

        #   Samples #
        self.go = Go(amp=0.001)
        self.surprise = Rapping.Surprise(amp=0.00000002)
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Bass    #

            #   Percussion  #

            #   Synths  #

            #   Samples #


        }
        return
    

def main():
    beat = O11(80)
    beat.export_full()