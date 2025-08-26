from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O9(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)

        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=1.0, punchy=True)
        self.bass2 = Bass(freq_mod=1, attack=0.01, sustain=1.0, release=0.01)

        #   Synths  #
        self.synth1 = Acoustic3(amp=0.5, attack=0.1, harmonics=12, sustain=1.0, release=0.01,
                                # vol_1 = 0.000000000001, vol_2 = 0.5,
                                vol_3 = 0.5, vol_4=0.000000000001,
                                )

        self.synth2 = Acoustic3(amp=0.7, attack=0.01, harmonics=12, decay=0.05, sustain=0.3, release=0.05,
                                vol_5 = 0.000000000001, vol_6 = 0.01,
                                vol_7 = 0.000000000001, vol_8 = 0.4)
       
        # self.tell1 = DontMind(freq_mod = 4)
        self.tell1 = DontTell2(freq_mod = 4)

        
        #   Percussion  #
        self.hat1 = Rapping.Hat_1(amp = 0.00001)
        self.hat2 = Rapping.Drill_Hat()

        self.snare1 = Rapping.Snare_1(amp=0.00015)
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
            5: [self.bass1, self.bass_1()],
            6: [self.tell1, self.synth_1()],

            #   Synths  #

            #   Percussion  #
            1: [self.snare1, self.snare()],
            2: [self.hat1, self.hats()],
            # 3: [self.hat1, self.hats_2()],


            #   Samples #
            0: [self.surprise, self.surp()],
            4: [self.viola, self.violas()]


        }
        return
    
    def violas(self):
        v = self.viola

        m0 = [rest(self.h - self.s/2)]
        off = [rest(self.w)]
        m1 = [rest(self.t), v.n(C1, self.q)]

        v1 = off + off + off + m1
        v0 = [rest(self.w*4)]

        return m0 + v1 + v1 + v1 + v1 + v0 + v1
    
    def surp(self):
        s = self.surprise

        m1 = [
            s.n(C1, self.h  - self.s/2),
        ]

        return m1
    
    def hats(self):
        h = self.hat2
        m0 = [
            rest(self.h- self.s/2)
        ]

        m1 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.e), h.n(C1, self.e),
        ]
        
        m4 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
        ]
        v1 = m1 + m1 + m1 + m4
        return m0 + v1 + v1 + v1 + v1 + v1 + v1
    
    def hats_2(self):
        h = self.hat1
        m0 = [
            rest(self.h- self.s/2)
        ]

        m1 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.e), h.n(C1, self.e),
        ]
        
        m4 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.s), h.n(C1, self.s), h.n(C1, self.e),
        ]
        v1 = m1 + m1 + m1 + m4
        return m0 + v1 + v1 + v1 + v1
    
    def snare(self):
        s = self.snare1
        m0 = [
            rest(self.h- self.s/2)
        ]
        m1 = [
            rest(self.h),
            s.n(C1, self.q),
            rest(self.q),
            ]
        
        m4 = [
            rest(self.h),
            s.n(C1, self.q),
            rest(self.e), s.n(C1, self.e),
            ]
        
        v1 = m1 + m1 + m1 + m4
        return m0 + v1 + v1 + v1 + v1 + v1 + v1
    
    def kicks(self):
        k = self.kick1

        m1 = [
        ]

        m2 = [
        ]

        m3 = [
        ]

        m4 = [
        ]

        v1 = m1 + m2 + m3 + m3

        return [rest(self.w)]
    
    def bass_1(self):
        b = self.bass2
        
        m0 = [rest(self.h - self.s/2)]

        v0 = [rest(self.w*4)]
        v1 = [
            b.n(E2, self.w * 2),
            b.n(E2, self.q),
            b.n(F2, self.h),
            b.n(E2, self.q),
            b.n(G2, self.h),
            b.n(F2, self.h),
        ]

        v2 = [
            b.n(E2, self.w * 2),
            b.n(E2, self.q),
            b.n(F2, self.h),
            b.n(E2, self.q),
            b.n(G2, self.h),
            b.n(A2, self.h),
        ]

        
        
        return m0 + v0 + v0 + v1 + v2 + v1 + v2
        
    def synth_1(self, variation = "v1"):
        s = self.tell1

        m1 = [
            s.n(E2, self.q),
            s.n(E2, self.q),
            s.n(E2, self.e),
            s.n(E2, self.q + self.e),
        ]

        m2 = [
        ]

        m3 = [
            rest(self.q),
            s.n(E2, self.h),
            rest(self.q),
        ]

        m4 = [
            s.n(E2, self.h),
            rest(self.q),
            s.n(E2, self.q),
        ]
        v1 = m1 + m1 + m3 + m4

        v0 = [rest(self.h - self.s/2)]
        off = [rest(self.w*4)]

        return v0 + off + off + v1 + v1 + v1 + v1
    
    def synth_2(self):
        b = self.bass2
        
        m0 = [rest(self.h - self.s/2)]

        v0 = [rest(self.w*4)]
        v1 = [
            b.n(E2, self.w * 2),
            b.n(E2, self.q),
            b.n(F2, self.h),
            b.n(E2, self.q),
            b.n(G2, self.h),
            b.n(F2, self.h),
        ]

        v2 = [
            b.n(E2, self.w * 2),
            b.n(E2, self.q),
            b.n(F2, self.h),
            b.n(E2, self.q),
            b.n(G2, self.h),
            b.n(A2, self.h),
        ]

        
        
        return m0 + v0 + v0 + v1 + v2 + v1 + v2
        
    def save(self, sound, name = "", convert = True):
        """Save the sound to the desired folder"""
        super().save(sound, name, True, convert, os.path.join("Tangible_Light", "ost", "09"))

    
def main():
    beat = O9(180)

    beat.get_instruments()
    beat.produce_full(export = True, stereo=True)
    beat.save(beat.production, "_prod", convert=False)