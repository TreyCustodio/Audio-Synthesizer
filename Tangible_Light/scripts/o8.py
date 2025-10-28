from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O8(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "08"))

        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=1.0, punchy=True)
        self.bass2 = Bass()

        self.synth1 = Acoustic3(amp=0.5, attack=0.1, harmonics=12, sustain=1.0, release=0.01,
                                # vol_1 = 0.000000000001, vol_2 = 0.5,
                                vol_3 = 0.5, vol_4=0.000000000001,
                                )

        self.synth2 = Acoustic3(amp=0.7, attack=0.01, harmonics=12, decay=0.05, sustain=0.3, release=0.05,
                                vol_5 = 0.000000000001, vol_6 = 0.01,
                                vol_7 = 0.000000000001, vol_8 = 0.4)
        
        # self.hat1 = PercussiveNoise(1.0, 70, noise_amount=0.6)
        self.hat1 = Rapping.Hat_1(amp=0.01)
        self.snare1 = Rapping.Snare_1()
        # self.snare1 = Hey(amp=0.0001)
        self.go = Go(amp=0.001)
        self.kick1 = Tap3(3.0, 25, noise_amount=0.0)
        self.tell1 = DontTell2()
        
        # self.synth2 
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Bass    #
            0: [self.bass1, self.bass_1()],
            1: [self.tell1, self.bass_2()],

            #   Synths  #
            2: [self.synth1, self.synth_1()],
            3: [self.synth2, self.synth_2("v2")],
            4: [self.hat1, self.hats()],
            5: [self.hat1, self.hats("v2")],
            6: [self.hat1, self.snare()],
            7: [self.go, self.goes()],
            8: [self.kick1, self.kicks()],




        }
        return
    
    def kicks(self):
        k = self.kick1

        m1 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
        ]

        m2 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), k.n(C1, self.s), rest(self.s), rest(self.s)
        ]

        m3 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), k.n(C1, self.s), k.n(C1, self.s),
            rest(self.s), k.n(C1, self.s), k.n(C1, self.s), rest(self.s),
            rest(self.q)
        ]

        v1 = m1 + m2 + m3 + m3

        
        amp = 0.5
        m5 = [
            k.n(C1, self.s, amp), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), k.n(C1, self.s), rest(self.s), rest(self.s),
            rest(self.s), k.n(C1, self.s), rest(self.s), rest(self.s),
        ]

        v2 = m5 + m5 + m3 + m3
        return v1 + v1 + v2 + v2
    
    def bass_1(self):
        b = self.bass1
        v0 = [rest(self.w*4)]
        
        m1 = [
            b.n(E1, self.e), rest(self.s),
            b.n(E1, self.e), rest(self.s),
            b.n(E1, self.e), rest(self.q),
            rest(self.e + self.s), b.n(E1, self.s),
        ]
        
        m2 = [
            b.n(D1, self.e), rest(self.s),
            b.n(D1, self.e), rest(self.s),
            b.n(D1, self.e), rest(self.q),
            rest(self.e), b.n(C1, self.e),
        ]

        m4 = [
            b.n(D1, self.e), rest(self.s),
            b.n(D1, self.e), rest(self.s),
            b.n(D1, self.e), rest(self.q),
            rest(self.e + self.s), b.n(C1, self.s),
        ]
        v1 = m1 + m2 + m2 + m4
        return v0 + v0 + v1 + v1
    
    def bass_2(self):
        d = self.tell1
        v0 = [rest(self.w*4)]
        
        m1 = [
            rest(self.q),
            rest(self.q),
            rest(self.q),
            d.n(E2, self.s), d.n(F2, self.s), d.n(G2, self.s), d.n(F2, self.s),
        ]
        
        m2 = [
            rest(self.q),
            rest(self.q),
            rest(self.q),
            d.n(D2, self.s), d.n(E2, self.s), d.n(F2, self.s), d.n(E2, self.s),
        ]

        m3 = [
            rest(self.q),
            rest(self.q),
            rest(self.q),
            d.n(D2, self.s), d.n(C2, self.e), d.n(E2, self.s),
        ]

        v1 = m1 + m2 + m3 + m3
        return v0 + v0 + v1 + v1
    
    def goes(self):
        g = self.go

        m4 = [
            rest(self.t + self.s),
            g.n(C1, self.e + self.s)
        ]
        m8 = [
            rest(self.t),
            g.n(C1, self.e),
            g.n(C1, self.e)
        ]
        v1 = [rest(self.w*3)] + m4

        v2 = [rest(self.w*3)] + m8

        return v1 + v1 + v2 + v1
    
    def hats(self, variant = "v1"):
        s = self.hat1
        m1 = [rest(self.w)]
        m2 = [rest(self.w)]
        m3 = [
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), rest(self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            ]
        
        m4 = [
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
        ]

        v1 = m4 + m4 + m3 + m3
        v0 = m1 + m2 + m3 + m3
        if variant == "v2":
            m3 = [
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), rest(self.s), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), rest(self.s),
            s.n(C1, self.s), s.n(C1, self.s), s.n(C1, self.s), rest(self.s),
        ]

            vb0 = [rest(self.w*4)]
            v1 = [rest(self.w*2)] + m3 + m3
            return vb0 + v1 + v1 + v1
        
        return v0 + v1 + v1 + v1
    
    def snare(self):
        s = self.snare1
        m1 = [
            rest(self.q),
            s.n(C1, self.e), rest(self.s*2),
            rest(self.q),
            s.n(C1, self.e), rest(self.s*2),
            ]
        
        m2 = [
            rest(self.q),
            s.n(C1, self.e), rest(self.s*2),
            rest(self.q),
            s.n(C1, self.s), rest(self.s), s.n(C1, self.e),
        ]

        m3 = [
            rest(self.q),
            s.n(C1, self.e), rest(self.s*2),
            rest(self.q),
            s.n(C1, self.e), s.n(C1, self.s), s.n(C1, self.s),
        ]
        v0 = [rest(self.w*2)] + m1 + m1
        v1 = m1 + m2 + m1 + m3

        return v0 + v1 + v1 + v1
    

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
            s.n(F1, self.e), s.n(A1, self.s),
            s.n(G1, self.e + self.s), s.n(F1, self.e),
            s.n(G1, self.e), s.n(E1, self.e),
        ]

        m4 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.e),
            rest(self.e), s.n(A1, self.e),
            s.n(E1, self.e), s.n(G1, self.e), 
        ]
        v1 = m1 + m2 + m3 + m4
        off = [rest(self.w)]

        return v1 + v1 + v1 + v1
    
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


        m5 = [
            s.n(F1, self.e), s.n(D1, self.e),
            s.n(F1, self.e), s.n(A1, self.s),
            s.n(G1, self.e + self.s), s.n(F1, self.e),
            s.n(G1, self.e), s.n(E1, self.e),
        ]
        
        off = [rest(self.w)]
        v0 = [rest(self.w*2)] + m3 + m4

        v1 = [rest(self.w*2)] + m5 + m4

        return v0 + v0 + v1 + v1
    

    def get_first(self):
        return
    
    def get_second(self):
        return
    
def main():
    beat = O8(44)
    beat.export_full()