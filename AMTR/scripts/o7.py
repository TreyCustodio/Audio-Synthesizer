from modules import *

"""
Project Frozen FLame
"""

class O7(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path=os.path.join("AMTR", "ost", "07"))

        #   Instruments #

        #   Melody  #
        self.key1 = Tangible_Light.Bell(amp=0.05, freq_mod=(1.5), wave_2 = False, wave_3=False,
                                        sustain=1.0)
        
        self.key2 = Tangible_Light.Bell(amp=0.1, freq_mod=3, wave_2 = False, wave_3=False,
                                        attack=0.001, decay=0.1, sustain=0.0, release=0.0)

        #   Rhythm / Percussion  #
        self.bass1 = Bass_1(amp=0.3, attack=0.01, attack_max = 0.02, freq_mod = 1, sustain=1.0, release= 0.01, amp_final = 0.00000000001, harmonics=3)

        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)
        self.hat4 = Hat_4(amp=0.00004)
        self.hatd = Rapping.Drill_Hat(amp=0.00005)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.mp3"))

        ##  Kicks   ##
        self.kick1 = Tap4(6.0, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)
        self.kick2 = GlobalSample(amp=0.00001, file_path=os.path.join("samples", "kick", "new-kick.wav"))

        #   Samples #
        self.go = Go(amp=0.00001)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.flame = GlobalSample(0.00003, os.path.join("samples", "video-games", "ff.mp3"))
        
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Main Melody #
            'bass1': [self.bass1, self.key_1(self.bass1)],
            # 'key1': [self.key1, self.key_2(self.key1)],
            'key2': [self.key1, self.key_2(self.key2)],



            
            #   Rhythm and Bass #
            'snares':[None, self.snare_1()],
            'kick':[None, self.kick_1()],


            #   Melody  #

            #   Samples / Libs  #
            # 'flame':[None, self.flame_1()],
        }


    """
    """
   
    def kick_1(self):
        k = self.kick2

        m1 = [
            k.n(self.e), k.n(self.e),
            rest(self.s*3), k.n(self.s),# 2
            k.n(self.e), rest(self.s), # 2.75
            k.n(self.e), k.n(self.s),
            rest(self.e), # 3.25
        ]

        m1b = [
            k.n(self.e), k.n(self.e),
            rest(self.s*3), k.n(self.s),# 2
            k.n(self.e), rest(self.s), # 2.75
            k.n(self.e), k.n(self.s),
            rest(self.e), # 3.25
        ]

        m2 = [
            k.n(self.e), k.n(self.e),
            rest(self.s*3), k.n(self.s),# 2
            k.n(self.e), rest(self.s), # 2.75
            rest(self.e), # 3.25
            k.n(self.e), rest(self.s),
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v1


    def snare_1(self):
        """Begin at M13"""

        s = self.snare1
        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.e), rest(self.s), s.n(self.s),
        ]

        v1 = m1 + m1 + m1 + m1

        return v1
    

    def key_1(self, k):

        m1 = [
            k.n(D2, self.s*3),
            k.n(B1, self.s*3), # 1.5
            k.n(C2, self.e), rest(self.e), # 2.5
            k.n(D2, self.s*3), # 3.25
            k.n(B1, self.s*3), # 4
        ]


        return \
        m1 + m1 + m1 + m1 +\
        m1 + m1 + m1 + m1
        
    
    def key_2(self, k):

        m1 = [
            k.n(D5, self.s*2), k.n(D5, self.s),
            k.n(B4, self.s*2), k.n(B4, self.s), # 1.5
            k.n(C5, self.e), rest(self.e), # 2.5
            k.n(D5, self.s*2), k.n(D5, self.s), # 3.25
            k.n(B4, self.s*2), k.n(B4, self.s),# 4
        ]


        return \
        m1 + m1 + m1 + m1
    
    def flame_1(self):
        return [self.flame.n(self.w*50)]
    
    



def main():
    beat = O7(61)
    beat.get_instruments()
    beat.export_selection(name="07_main")