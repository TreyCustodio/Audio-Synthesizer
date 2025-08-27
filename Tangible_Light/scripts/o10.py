from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O10(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "10"))

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
        self.hat1 = Rapping.Hat_3(amp=0.000065)
        self.hat2 = Rapping.Hat_2(amp=0.00003)

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
            0: [self.bass1, self.bass_1()],

            #   Percussion  #
            1: [self.snare1, self.snares()],
            2: [self.snare2, self.snares_2()],
            3: [self.snare3, self.snares_3()],
            4: [self.hat1, self.hats()],
            5: [self.hat2, self.hats_2()],
            
            #   Synths  #
            6: [self.synth2, self.synth_1()]



            #   Samples #


        }
        return
    
    def bass_1(self):
        b = self.bass1

        m0 = [rest(self.e)]

        m1 = [
            b.n(D1, self.q), rest(self.e),
            b.n(D1, self.e),
            rest(self.h)
        ]

        m2 = [
            b.n(D1, self.q), rest(self.e),
            b.n(D1, self.e), 
            rest(self.e),
            b.n(E1, self.q), rest(self.e)
        ]

        m3 = [
            b.n(C1, self.q), rest(self.e),
            b.n(C1, self.e),
            rest(self.h)
        ]

        m4 = [
            b.n(C1, self.q), rest(self.e),
            b.n(C1, self.e), 
            rest(self.e),
            b.n(D1, self.q), rest(self.e)
        ]
        v1 = m1 + m2 + m1 + m2
        v2 = m3 + m4 + m3 + m4

        return m0 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2 
    
    def synth_1(self):
        b = self.synth3

        amp = 0.6
        m1 = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e + self.s, amp), b.n(A1, self.e),
            rest(self.h)
        ]

        m2 = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e + self.s, amp), b.n(A1, self.e),
            rest(self.q),
            b.n(F1, self.e), b.n(G1, self.e),
        ]
        m2b = [
            b.n(A1, self.e), b.n(A1, self.s),
            b.n(C2, self.e + self.s, amp), b.n(A1, self.e),
            rest(self.q),
            b.n(F1, self.e + self.s), b.n(G1, self.s),
        ]
        
        m3 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(A1, self.e + self.s), b.n(G1, self.q, fade = True, fade_amount=20),
            rest(self.h - self.e)
        ]

        m4 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(A1, self.e + self.s), b.n(G1, self.h - self.e, fade=True, fade_amount = 16),
            b.n(E1, self.e), b.n(F1, self.e),
        ]

        m5 = [
            b.n(G1, self.e), b.n(G1, self.s),
            b.n(B1, self.e + self.s), b.n(G1, self.q, fade=True, fade_amount=20),
            rest(self.e),
            b.n(F1, self.e), b.n(G1, self.e),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m2b
        v2 = m3 + m4 + m3 + m5
        m0 = [rest(self.e)]
        return m0 + v0 + v0 + v1 + v2 + v1 + v2 + v0 + v0
    
    def hats(self):
        h = self.hat1

        m1 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
        ]

        m2 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
        ]

        m3 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
        ]

        m4 =[
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.s), h.n(C1, self.s),
        ]

        v1 = m1 + m2 + m3 + m4
        m0 = [rest(self.e)]
        return m0 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1
    
    def hats_2(self):
        h = self.hat2

        m1 = [
            rest(self.w),
        ]

        m2 = [
            rest(self.t - self.e),
            h.n(C1, self.e), h.n(C1, self.q),
        ]

        m3 = [
            rest(self.t - self.e),
            h.n(C1, self.q + self.e)
        ]

        m3b = [
            rest(self.t),
            h.n(C1, self.q)
        ]

        m4 = [
            rest(self.t - self.e),
            h.n(C1, self.s*4), h.n(C1, self.s*2)
        ]

        v1 = m1 + m2 + m1 + m3
        v2 = m3b + m1 + m1 + m4
        m0 = [rest(self.e)]

        return m0 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2
    
    
    
    def snares(self):
        s = self.snare2

        
        m0 = [rest(self.e)]
        
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

        m3 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.e),
            s.n(C1, self.q + self.e),
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

        m12 = [
            rest(self.q),
            s.n(C1, self.q),
            rest(self.e),
            s.n(C1, self.q), s.n(C1, self.s), s.n(C1, self.s),
        ]

        v1 = m3 + m2 + m1 + m4

        v2 = m1 + m2 + m3 + m8

        v3 = m1 + m2 + m3 + m12

        return m0 + v1 + v2 + v3 + v2 + v1 + v2 + v3 + v2

    def snares_2(self):
        s = self.snare1
        amp_0 = 0.4
        # m0 = [
        #     s.n(C1, self.s, amp_0), s.n(C1, self.s, amp_0),
        #     s.n(C1, self.s, amp_0),
        # ]
        m0 = [rest(self.e)]


        m1 = [
            rest(self.q*4),
        ]


        m4 = [
            rest(self.h),
            rest(self.e), s.n(C1, self.s), s.n(C1, self.s),
            s.n(C1, self.q),
        ]


        v1 = [rest(self.w*4)]

        v2 = m1 + m1 + m1 + m4

        return m0 + v2 + v1 + v2 + v1 + v2 + v1 + v2 + v1
    
    def snares_3(self):
        s = self.snare3
        m0 = [
            s.n(C1, self.e),
        ]

        m2 = [
            rest(self.q),
            rest(self.q),
            s.n(C1, self.e),
            rest(self.q + self.e)
        ]

        v1 = [rest(self.w)] + m2 + [rest(self.w*2)]
        v2 = [rest(self.w*2)] + m2 + [rest(self.w)]
        v0 = [rest(self.w*4)]
        return m0 + v0 + v1 + v0 + v1 + v0 + v1 + v0 + v1

    
def main():
    beat = O10(140)
    beat.export_full()