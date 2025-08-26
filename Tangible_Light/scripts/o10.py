from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O10(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)

        #   Bass    #
        self.bass1 = Bass_1(freq_mod=2.0, harmonics=20, attack = 0.01, decay=0.05, release = 0.01, sustain=1.0)
        self.bass2 = Bass(freq_mod=1, attack=0.01, sustain=1.0, release=0.01)

        #   Synths  #
        self.synth1 = Acoustic3(amp=0.5, attack=0.1, harmonics=12, sustain=1.0, release=0.01,
                                # vol_1 = 0.000000000001, vol_2 = 0.5,
                                vol_3 = 0.5, vol_4=0.000000000001,
                                )

        self.synth2 = Acoustic3(amp=0.7, attack=0.01, harmonics=12, decay=0.05, sustain=0.3, release=0.05,
                                vol_5 = 0.000000000001, vol_6 = 0.01,
                                vol_7 = 0.000000000001, vol_8 = 0.4)
       
        self.tell1 = DontTell2(freq_mod = 4)
        
        #   Percussion  #
        self.hat1 = Rapping.Hat_1(amp = 0.00001)
        self.hat2 = Rapping.Drill_Hat()

        self.snare1 = Rapping.Snare_2(amp=0.00002)
        self.kick1 = Tap3(3.0, 25, noise_amount=0.0)

        #   Samples #
        self.go = Go(amp=0.001)
        self.surprise = Rapping.Surprise(amp=0.00000002)
        self.viola = Viola_1(amp=0.0002)
        self.viola2 = Viola_2(amp = 0.0005)
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Bass    #
            0: [self.bass1, self.bass_1()],

            #   Synths  #

            #   Percussion  #
            1: [self.bass1, self.snares()],


            #   Samples #


        }
        return
    
    def bass_1(self):
        b = self.bass1

        m1 = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e), b.n(A1, self.s + self.h + self.e),
        ]

        m2 = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e), b.n(A1, self.s + self.h - self.e),
            b.n(F1, self.e), b.n(G1, self.e),
        ]
        m2b = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e), b.n(A1, self.s + self.h - self.e),
            b.n(F1, self.e + self.s), b.n(G1, self.s),
        ]
        
        m3 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(A1, self.e), b.n(G1, self.s + self.h + self.e),
        ]

        m4 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(A1, self.e), b.n(G1, self.s + self.h - self.e),
            b.n(E1, self.e), b.n(F1, self.e),
        ]

        m5 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(B1, self.e), b.n(G1, self.s + self.h - self.e),
            b.n(F1, self.e), b.n(G1, self.e),
        ]

        v1 = m1 + m2 + m1 + m2b
        v2 = m3 + m4 + m3 + m5

        return v1 + v2 + v1 + v2
    
    def snares(self):
        s = self.snare1

        m1 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.q),
            s.n(C1, self.q),
        ]

        m2 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.e),
            s.n(C1, self.q), s.n(C1, self.e),
        ]

        m4 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.e),
            s.n(C1, self.q), rest(self.e),
        ]

        m8 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.e),
            s.n(C1, self.e), s.n(C1, self.e), rest(self.e),
        ]

        v1 = m1 + m2 + m1 + m4

        v2 = m1 + m2 + m1 + m8

        return v1 + v2 + v1 + v2

    def save(self, sound, name = "", convert = True):
        """Save the sound to the desired folder"""
        super().save(sound, name, True, convert, os.path.join("Tangible_Light", "ost", "10"))

    
def main():
    beat = O10(125)

    beat.get_instruments()
    beat.produce_full(export = True, stereo=True)
    beat.save(beat.production, "_prod", convert=False)