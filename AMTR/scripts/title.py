from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "01"))
        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Bass    ##5
        mod = 0.5
        self.bass1 = Bass_1(amp=1.0,
                            attack=0.01, attack_max = 0.02, freq_mod = mod,
                            decay=0.0, sustain=1.0, release= 0.1, amp_final = 0.00000000001,
                            top_freq = 1, harmonics=1
                            )

        self.bass1 = LowSynth(1.0)
        
        self.bass2 = Bass_1(amp=1.0, attack=0.0, attack_max = 0.15, freq_mod = mod, decay = 0.00, sustain=0.3, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        ##  Whistle ##
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = False, wave_3=True,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 1.0)

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
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        self.punchy_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "punchy_snare.wav"))
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       
       
        ##  Kicks   ##
        self.kick1 = Tap4(3.0, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)

        #   Samples #
        self.go = Go(amp=0.00001)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Rhythm and Bass #
            'bass1':[None, self.bass_1()],
            'snares':[None, self.snare_1()],
            'snare_echo':[None, self.snare_2()],
            # # 'whistle':[None, self.whistle_1()]
            'kicks':[None, self.kick_1()],
            'hats':[None, self.hats_1()],


            #   Melody  #

            #   Samples / Libs  #
        }

    def whistle_1(self):
        w = self.whistle1

        m1 = [
            rest(self.q*3),
            w.n(C2, self.q)
        ]

        v1 = m1 + m1 + m1 + m1 +\
             m1 + m1 + m1 + m1
        
        v2 = m1 + m1 + m1 + m1

        return \
        v1 +\
        \
        v2 + v2 +\
        v2 + v2
    
    def hats_1(self):
        h1 = self.hat4
        v0 = [rest(self.w*4)]

        m1 = [
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            rest(self.q),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
        ]
        
        m3 = [
            h1.n(self.e), h1.n(self.e),
            h1.n(self.e), h1.n(self.e),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
        ]

        m4 = [
            h1.n(self.e), h1.n(self.e),
            h1.n(self.e), h1.n(self.e),
            rest(self.e), h1.n(self.e),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
        ]

        v1 = m1 + m1 + m3 + m4

        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        v1 + v1
    
    def kick_1(self):
        k = self.kick1
        # n1 = F3
        n1 = F2
        n2 = F2
        v0 = [rest(self.w*4)]
        m1 = [
            k.n(n1, self.q, 0.5),
            rest(self.q),
            rest(self.e), k.n(n2, self.e),
            rest(self.s), k.n(n2, self.e), rest(self.s)
        ]

        m3 = [
            k.n(n1, self.q, 0.5),
            k.n(n2, self.q),
            rest(self.e), k.n(n2, self.e),
            rest(self.s), k.n(n2, self.e), rest(self.s)
        ]

        v1 = m1 + m1 + m3 + m1
        v2 = m1 + m1 + m3 + m3


        return \
        v0 + v1 +\
        \
        v2 + v2 +\
        v2 + v2
    
    def bass_1(self):
        b1 = self.bass1
        b2 = self.bass2

        m1 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q),
            rest(self.e),
            rest(self.q)
        ]

        m2 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q), rest(self.e),
            b1.n(D2, self.q),
        ]

        m3 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q),
            rest(self.e),
            rest(self.q)
        ]


        m4 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q), rest(self.e),
            b1.n(D2, self.q),
        ]
        


        m5 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q + self.e + self.q),
        ]

        m6 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q + self.e),
            b1.n(D2, self.q),
        ]

        m7 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e + self.q),
        ]

        m8 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e),
            b1.n(D2, self.e), b1.n(E2, self.e),
        ]

        
        m9 = m5
        m10 = m6
        m11 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e + self.q),
        ]
        v1 = m1 + m2 + m3 + m4
        v1b = m5 + m6 + m7 + m8
        
        v2 = m5 + m6 + m7 + m8

        v3 = m5 + m6 + m7 + m8

        return \
        v1 + v1b +\
        \
        v2 + v2 +\
        v2 + v2
    
    def snare_1(self):
        s = self.punchy_snare

        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
        ]

        m2 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.e), s.n(self.e),
        ]

        m4 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.s/2), s.n(self.s/2), s.n(self.s), s.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m4

        return \
        v0 +\
        \
        v1 + v1 +\
        v1 + v1

    def snare_2(self):
        s = self.clicky_snare
        s1 = self.afro_snare

        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            rest(self.e), s.n(self.e),
            rest(self.q),
            rest(self.q),
        ]

        m2 = [
            rest(self.w)
        ]

        m6 = [
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
            s.n(self.q),
        ]

        v1 = m1 + m1 + m2 + m2
        v2 = m1 + m6 + m1 + m6
        v3 = m1 + m1 + m6 + m6

        return \
        v0 +\
        \
        v1 + v2 +\
        v3 + v2


def main():
    beat = Title(78)
    beat.export_full()