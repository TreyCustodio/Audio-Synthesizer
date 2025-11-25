from modules import *

"""
Project Frozen FLame
"""

class FF(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path=os.path.join("AMTR", "ost", "03"))

        #   Instruments #

        #   Melody  #
        self.key1 = Tangible_Light.Bell(amp=0.5, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        sustain=1.0)


        #   Rhythm / Percussion  #
        ##  Whistle ##
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = True, wave_3=False,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 1.0)

        self.string1 = WhinyString(amp=0.2, freq_mod=2.0, harmonics=4,
                                   sustain=1.0)

        self.saw1 = SawDefinition(amp=0.01)

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
        self.quick_hat = GlobalSample(0.000005, os.path.join("samples", "hats", "quicky.wav"))

        ##  Kicks   ##
        self.kick1 = Tap4(6.0, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)

        #   Samples #
        self.go = Go(amp=0.00001)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.flame = GlobalSample(0.00003, os.path.join("samples", "video-games", "ff.mp3"))
        
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Main Melody #
            # 'string1': [self.string1, self.string_1()],
            # 'saw1': [self.string1, self.saw_1()],
            # 'key1': [self.key1, self.key_1()],

            
            #   Rhythm and Bass #
            # 'snares':[None, self.snare_1()],
            # 'hat1': [0, self.hats_1()],

            #   Melody  #

            #   Samples / Libs  #
            'flame':[None, self.flame_1()],
        }


    """
    Each measure = 3 eigth notes
    Each verse = 12 eigth notes
    """
    def string_1(self):
        s = self.string1


        m1 = [
            s.n(B2, self.e),
            s.n(E3, self.e),
            s.n(D3, self.e),
        ]

        m2 = [
            s.n(E3, self.e * 6),
        ]

        m3 = [
            s.n(C3, self.e * 5),
            s.n(D3, self.e),
        ]
        

        m4 = [
            s.n(B2, self.e * 6),
        ]


        return m1 +\
        m2 + m3 + m4
        
        
    def saw_1(self):
        s = self.saw1


        m1 = [
            rest(self.e*3)
        ]

        m2 = [
            rest(self.s*3), # 1.5
            s.n(E4, self.e),  # 2.5
            s.n(E4, self.s), # 3
        ]

        m3 = [
            s.n(C4, self.e),
            rest(self.e*2)
        ]
        

        m4 = [
            s.n(C4, self.e),
            rest(self.e * 2 - self.s),
            s.n(D4, self.s),
        ]
        
        m5 = [
            s.n(B3, self.e * 3),
        ]


        return m1 +\
        m2 + m3 +\
        m2 + m4 +\
        m5
    
    def key_1(self):
        k = self.key1

        m0 = [rest(self.e*3)]

        m1 = [
            k.n(C4, self.s), k.n(D4, self.s),
            k.n(E4, self.s), k.n(F4, self.s),
            k.n(G4, self.s), k.n(A4, self.s),
        ]

        m2 = [
            k.n(B3, self.s), k.n(C4, self.s),
            k.n(D4, self.s), k.n(E4, self.s),
            k.n(F4, self.s), k.n(G4, self.s),
        ]

        return m0 +\
        m1 + m1 + m1 + m1 +\
        m2 + m2 + m2 + m2 +\
        m1 + m1 + m1 + m1 +\
        m2 + m2 + m2 + m2
        
        
    
    def flame_1(self):
        return [self.flame.n(self.w*50)]
    
    def snare_1(self):
        """Begin at M13"""

        s = self.snare1

        m0 = [
            rest(self.e*3)
        ]
        m1 = [
            s.n(self.e * 3),
        ]

        v1 = m1 + m1 + m1 + m1

        return m0 + v1
    
    def hats_1(self):
        h = self.quick_hat

        m1 = [
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        v1 = m1 + m1 + m1 + m1

        return v1 + v1



def main():
    beat = FF(122)
    beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    beat.get_instruments()
    beat.export_selection(name="03_main", volume = 16_000)
