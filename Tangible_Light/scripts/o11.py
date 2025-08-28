from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O11(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "11"))

        #   Bass    #
        mod = Ds2 / Gs2
        self.bass1 = Bass_1(amp=1.0, attack=0.005, attack_max = 0.003, freq_mod = mod, sustain=0.3, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)
        self.bass2 = Bass_1(amp=1.0, attack=0.0, attack_max = 0.15, freq_mod = mod, decay = 0.00, sustain=0.3, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

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
        
        self.synth4 = First4()

        self.tell1 = DontTell2(freq_mod = 8, decay = 0.04)
        
        #   Percussion  #
        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000065)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)
        self.hat4 = Rapping.Drill_Hat(amp=0.00005)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)

        ##  Kicks   ##
        self.kick1 = Tap4(6.0, decay = 0.05, sustain=0.0, noise_amount=0.00000)


        #   Samples #
        self.go = Go(amp=0.001)
        self.surprise = Rapping.Surprise(amp=0.00000002)
        self.instruments = {}
        self.violin1 = GlobalSample(os.path.join("samples", "violin", "violin_1.wav"), amp = 0.00002)
        self.violin2 = GlobalSample(os.path.join("samples", "violin", "violin_2.wav"), amp = 0.00003)
        self.violin3 = GlobalSample(os.path.join("samples", "violin", "violin_layered.wav"), amp = 0.00003)



    def get_instruments(self):
        self.instruments = {
            #   Bass    #
            0: [self.bass1, self.bass_a()],
            5: [self.bass1, self.bass_b()],


            #   Percussion  #
            # 1: [None, self.hats_a()],
            # 2: [None, self.snare_a()],
            3: [None, self.kicks_a()],


            #   Synths  #

            #   Samples #
            # 4: [None, self.violin_a()],

        }
        return
    
    
    def violin_a(self):
        vi =  self.violin1
        vi2 =  self.violin2


        m1 = [
            rest(self.w)
        ]

        m2 = [rest(self.w)]

        m3 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            rest(self.e), vi.n(C1, self.q),
            rest(self.e),
        ]

        m4 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            rest(self.e), vi2.n(C1, self.q + self.e),
        ]


        v1 = m1 + m2 + m3 + m4


        v0 = [rest(self.w*4)]
        return v0 + v0 + v0 + v1 + v0 + v1 + v0 + v1 + v0 + v1 + v0 + v1 + v0 + v1


    def bass_a(self):
        """Tough pick here between G2 and Gs2"""
        b = self.bass1
        b2 = self.bass2

        m1 = [
            rest(self.w)
        ]

        m2 = [
            rest(self.w)
        ]

        m3 = [
            rest(self.e), rest(self.e),
            rest(self.e), b2.n(Gs2, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]

        m3b = [
            rest(self.e), rest(self.e),
            rest(self.e), b.n(Gs2, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]


        m4 = [
            rest(self.e), b2.n(Gs2, self.e),
            rest(self.e), b2.n(Gs2, self.e),
            rest(self.e), b2.n(Fs2, self.e + self.q),
        ]

        

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4
        v2 = m1 + m2 + m3b + m4

        return v0 + v0 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2
    
    def bass_b(self):
        b = self.bass1
        b2 = self.bass2

        amp = 1.0

        m0 = [
            b2.n(Gs2, self.w*2, amp),
        ]

        m1 = [rest(self.w)]
        m2 = [
            rest(self.w),
            ]

        m3 = [
            b2.n(Gs2, self.e * 3, amp, fade=True, fade_amount=16),
            rest(self.e), # 2
            rest(self.e),
            b2.n(Gs2, self.e * 3, amp),
        ]

        m4 = [
            rest(self.w)
        ]
        
        m5 = [
            b2.n(Gs2, self.w*2, amp),
        ]
        v0 = [rest(self.w*4)]
        v1 = m0 + m3 + m4
        v2 = m0 + m3 + m4

        return v0 + v0 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2 + v1 + v2
    
    def kicks_a(self):
        k = self.kick1
        #   (1) Set the pitch to the same as the bass
        #   (2) Set the pitch 7 semitones higher

        #   1   #
        m1 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]

        m2 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]

        m3 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), rest(self.e),
            k.n(Gs1, self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e)
        ]
        m4 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e),
            k.n(Fs1, self.e), rest(self.e),

        ]

        m5 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]

        m6 = [
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e),
            k.n(Gs1, self.e), rest(self.e),
        ]

        m7 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            k.n(Gs1, self.e), k.n(Gs1, self.e),
            rest(self.e), rest(self.e)
        ]
        m8 = [
            rest(self.e), rest(self.e),
            k.n(Gs1, self.e), rest(self.e),
            rest(self.e), 
            k.n(Fs1, self.e), rest(self.e),
            rest(self.e),

        ]

        v1 = m1 + m2 + m3 + m4
        v2 = v1

        return v1 + v1 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2

    def hats_a(self):

        h = self.hat3

        m1 = [
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.e), h.n(C1, self.e),
            h.n(C1, self.e), rest(self.e),
            h.n(C1, self.e), rest(self.e),
        ]

        m3 = [
            h.n(C1, self.e), h.n(C1, self.e),
            rest(self.e), h.n(C1, self.e),
            h.n(C1, self.e), rest(self.e),
            h.n(C1, self.e), h.n(C1, self.e),
        ]

        m4 = [
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), rest(self.e),
            rest(self.e), h.n(C1, self.e), 
        ]

        m8 = [
            rest(self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.e), h.n(C1, self.e),
            h.n(C1, self.e), h.n(C1, self.e),
        ]

        m12 = [
            rest(self.e), h.n(C1, self.e),
            rest(self.q),
            h.n(C1, self.e), rest(self.e),
            rest(self.q)
        ]


        v1 = m1 + m1 + m3 + m4
        v2 = m1 + m1 + m3 + m8
        v3 = m1 + m1 + m3 + m12

        return v1 + v1 + v1 + v3 + v1 + v3 + v1 + v3 + v1 + v3 + v1 + v3 + v1 + v3
    
    def snare_a(self):
        s = self.snare4
        s2 = self.snare1

        m1 = [
            rest(self.h),
            s.n(C1, self.q),
            rest(self.q)
        ]

        m4 = [
            rest(self.h),
            s.n(C1, self.q),
            rest(self.e), s.n(C1, self.e),
        ]

        m7 = [
            rest(self.h),
            s.n(C1, self.q),
            rest(self.e), s.n(C1, self.e),
        ]

        m8 = [
            rest(self.q),
            rest(self.q), s.n(C1, self.q),
            s.n(C1, self.q),
        ]

        v1 = m1 + m1 + m1 + m4
        v2 = m1 + m1 + m7 + m8
        return v1 + v1 + v1 + v2 + v1 + v1 + v1 + v2 + v1 + v2 + v1 + v1 + v1 + v2
    

    
def main():
    beat = O11(180)
    beat.export_full()