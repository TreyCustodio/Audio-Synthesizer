from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O8(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)

        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=1.0, punchy=True)
        self.bass2 = Bass()

        self.synth1 = Acoustic3(amp=0.5, attack=0.1, harmonics=12, sustain=1.0, release=0.01,
                                vol_1 = 0.000000000001, vol_2 = 0.5,
                                vol_3 = 0.5, vol_4=0.000000000001,
                                )

        self.synth2 = Acoustic3(amp=0.7, attack=0.01, harmonics=12, decay=0.05, sustain=0.3, release=0.05,
                                vol_5 = 0.000000000001, vol_6 = 0.01,
                                vol_7 = 0.000000000001, vol_8 = 0.4)
        
        self.hat1 = PercussiveNoise(1.0, 190, noise_amount=0.4)
        self.snare1 = PercussiveNoise(1.0, 13, noise_amount=0.7)
        
        
        # self.synth2 
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Bass    #
            # 0: [self.bass1, self.bass_1()],

            #   Synths  #
            1: [self.synth1, self.synth_1()],
            2: [self.synth2, self.synth_2("v2")],
            3: [self.hat1, self.hats()],
            4: [self.hat1, self.snare()],

        }
        return
    
    def hats(self):
        s = self.hat1
        m1 = [rest(self.w)]
        m2 = [rest(self.w)]
        m3 = [
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            ]
        
        v1 = m3 + m3 + m3 + m3
        v0 = m1 + m2 + m3 + m3

        return v0 + v1
    
    def snare(self):
        s = self.snare1
        m1 = [rest(self.w)]
        m3 = [
            rest(self.q),
            s.n(C1, self.s), rest(self.s*3),
            rest(self.q),
            s.n(C1, self.s), rest(self.s*3),
            ]
        
        v0 = m1 + m1 + m3 + m3
        v1 = m3 + m3 + m3 + m3

        return v0 + v1
    
    def bass_1(self):
        b = self.bass1
        return
    

    def synth_1(self, variation = "v1"):
        if variation == "v1":
            s = self.synth1
        elif variation == "v2":
            s = self.synth2
        
        m1 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
        ]

        m2 = [
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
        ]

        m3 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.e),
            s.n(G1, self.e), s.n(F1, self.e),
            s.n(G1, self.e), s.n(E1, self.e),
        ]

        m4 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.e),
            s.n(G1, self.e), s.n(F1, self.e),
            s.n(E1, self.e), s.n(G1, self.e), 
        ]
        v1 = m1 + m2 + m3 + m4

        return v1 + v1
    
    def synth_2(self, variation = "v2"):
        if variation == "v1":
            s = self.synth1
        elif variation == "v2":
            s = self.synth2
        
        m1 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(D1, self.e),
        ]

        m2 = [
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
            s.n(E1, self.e), s.n(C1, self.e),
        ]

        m3 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.e),
            s.n(G1, self.e), s.n(F1, self.e),
            s.n(G1, self.e), s.n(E1, self.e),
        ]

        m4 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.e),
            s.n(G1, self.e), s.n(F1, self.e),
            s.n(E1, self.e), s.n(G1, self.e), 
        ]
        v0 = [rest(self.w*2)] + m3 + m4

        return v0 + v0
    
    def save(self, sound, name = "", convert = True):
        """Save the sound to the desired folder"""
        super().save(sound, name, True, convert, os.path.join("Tangible_Light", "ost", "08"))


def main():
    beat = O8(44)

    beat.get_instruments()
    beat.produce_full()
    beat.save(beat.production, "_prod", convert=False)