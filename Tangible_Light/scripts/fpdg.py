from modules.beat import *
from modules.instruments import *
from modules.audio import *


class FPDG(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)
        
        #   Bass    #
        self.bass1 = RapBass(amp=6)
        # self.bass2 = RapBass(freq_mod=2)



        #   Plucky, Accoustic Synths   #
        self.acou1 = Acoustic2(amp=2)

        #   Synths  #
        self.synth1 = DontMind2(freq_mod=0.25)

        #   Melody Synths   #

        #   Drums   #
        self.kick1 = Tap(5.0, 30)

        self.clap1 = Tap3(0.3, 15, noise_amount=4.0)
        self.clap2 = Hi_Hat(noise_amount=0.05)
        self.hat1 = Tap3(0.1, 120, 2.0, 2.0)
        self.hat2 = Tap3(1.0, 50, noise_amount=0.7)

        #   Instrument Dictionary   #
        self.instruments = {
            
            #   Bass    #
            0: [self.bass1, self.bass()],

            #   Accoustics  #
            3: [self.acou1, self.acoustic1()],
            
            #   Synths  #
            6: [self.synth1, self.piano()],

            #   Percussion  #
            1: [self.kick1, self.kicks()],
            2: [self.clap1, self.claps()],
            4: [self.hat1, self.hats()],
            5: [self.clap1, self.claps2()],
            7: [self.hat2, self.hats_2()],

            #   Libs    #
            # 8: [None, self.navi()]
        }


    def piano(self):
        s = self.synth1

        # m1 = [
        #     s.n(A3, self.s), s.n(B3, self.s), s.n(A3, self.s), s.n(B3, self.s),
        #     s.n(B3, self.s), s.n(C4, self.s), s.n(B3, self.s), s.n(C4, self.s),
        #     s.n(C4, self.s), s.n(D4, self.s), s.n(C4, self.s), s.n(D4, self.s),
        #     s.n(D4, self.s), s.n(C4, self.s), s.n(B3, self.s), s.n(A3, self.s),
        # ]

        # m2 = [
        #     s.n(F3, self.s), s.n(F3, self.s), s.n(F3, self.s), s.n(A3, self.e), # 1.25
        #     s.n(F3, self.s), s.n(F3, self.s), s.n(A3, self.e), # 2.25
        #     s.n(F3, self.s), s.n(F3, self.s), s.n(F3, self.s), # 3
        #     s.n(A3, self.e), s.n(As3, self.e),
        # ] 

        v0 = [
            rest(self.w * 3),
            s.n(A3, self.e, 0.1), s.n(A3, self.e, 0.3),
            s.n(A3, self.e, 0.5), s.n(A3, self.e, 0.7),
            s.n(A3, self.e, 0.9), s.n(A3, self.e),
            s.n(A3, self.e), rest(self.e)
        ]


        m1 = [
            s.n(A3, self.e, 0.5), s.n(A3, self.s), delaycombo(s.n(C4, self.e + self.s), s.n(B3, self.q), self.e + self.s),
            delaycombo(s.n(D4, self.e), s.n(C4, self.e + self.s), self.s),
             s.n(A3, self.e),
        ]   

        m4 = [
            s.n(A3, self.e), s.n(A3, self.s), s.n(B3, self.e), # 1.25
            rest(self.s * 3),
            s.n(D4, self.q + self.e),
            s.n(D4, self.e),
        ]
        m2 = m1

        v1 = m1 + m1 + m2 + m2
        v2 = m1 + m1 + m2 + m4

        return \
        [rest(self.w*4)] +\
        \
        v0 +\
        v1 +\
        v2 +\
        \
        [rest(self.w*4)] +\
        \
        v1 +\
        v1 +\
        v2 +\
        \
        [rest(self.w*4)] +\
        \
        v1
    
    def acoustic1(self):
        s = self.acou1

        m1 = [
            s.n(C4, self.e), s.n(C4, self.e),
            rest(self.q),
            rest(self.e), s.n(C4, self.e),
            rest(self.s), delaycombo(s.n(C4, self.s), s.n(C4, self.e + self.s - 0.1), 0.1)
        ]

        m2 = [
            s.n(C4, self.e), s.n(C4, self.e),
            rest(self.q),
            rest(self.e), s.n(C4, self.e),
            rest(self.s), s.n(C4, self.e), rest(self.s)
        ]

        m3 = [
            delaycombo(s.n(C4, self.s), s.n(C4, self.e - 0.1), 0.1), s.n(C4, self.e),
            rest(self.q),
            rest(self.e), s.n(C4, self.e),
            rest(self.s), s.n(C4, self.e), rest(self.s)
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1

    def bass(self):
        b = self.bass1

        
        m1 = [
            b.n(C2, self.w),
        ]

        m2 = [
            b.n(C2, self.e), b.n(C2, self.e),
            rest(self.e), b.n(C2, self.e),
            rest(self.e), b.n(C2, self.e),
            b.n(C2, self.e), rest(self.e)
        ]

        m4 = [
            b.n(C2, self.e), b.n(C2, self.e),
            rest(self.e), b.n(C2, self.e),
            rest(self.e), b.n(C2, self.q),
            rest(self.e)
        ]
        # m1 = [
        #     b.n(C2, self.e), b.n(C2, self.e),
        #     rest(self.q),
        #     rest(self.e), b.n(C2, self.e),
        #     rest(self.s), b.n(C2, self.e), rest(self.s),
        # ]

        # m2 = [
        #     b.n(C2, self.e), b.n(C2, self.e),
        #     rest(self.q),
        #     rest(self.e), b.n(C2, self.q),
        #     b.n(C2, self.e),
        # ]

        v1  = m1 + m2 + m1 + m4

        return\
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1
    
    def kicks(self):
        b = self.kick1

        m1 = [
            b.n(C2, self.e), b.n(C2, self.e),
            b.n(C3, self.e), rest(self.s),
            b.n(C2, self.e), rest(self.s),
            b.n(C2, self.e), b.n(C3, self.e),
            rest(self.e)
        ]

        m2 = [
            b.n(C3, self.e), b.n(C3, self.e),
            b.n(C3, self.e), rest(self.s),
            b.n(C3, self.e), rest(self.s),
            b.n(C3, self.e), b.n(C3, self.e),
            rest(self.e)
        ]

        v1  = m1 + m1 + m1 + m1

        return\
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1
    
    def claps(self):
        c = self.clap1

        v0 = [
            rest(self.w*3),

            rest(self.q),

            c.n(C1, self.e), rest(self.s),
            c.n(C1, self.e), rest(self.s),
            c.n(C1, self.e), c.n(C1, self.e),
            
            #2.5 
            rest(self.e),

        ]

        m1 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.q),
            c.n(C1, self.q),
        ]

        m2 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.q),
            c.n(C1, self.e), c.n(C1, self.e),
        ]

        m4 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.e),
            c.n(C1, self.q), c.n(C1, self.e),

        ]

        v1  = m1 + m2 + m1 + m4

       
        return\
        [rest(self.w*4)] +\
        \
        v0 +\
        v1 +\
        v1 +\
        \
        [rest(self.w*4)] +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        [rest(self.w*4)] +\
        \
        v1
    
    def claps2(self):
        c = self.clap2

        m1 = [
            rest(self.q),
            c.n(C2, self.e), rest(self.e),
            rest(self.q),
            c.n(C2, self.e), rest(self.e)
        ]

        m2 = [
            rest(self.q),
            c.n(C2, self.e), rest(self.e),
            rest(self.q),
            c.n(C2, self.e), c.n(C2, self.e),
        ]

        m4 = [
            rest(self.q),
            c.n(C2, self.e), rest(self.e),
            rest(self.e),
            c.n(C2, self.e), rest(self.e), c.n(C2, self.e),

        ]

        v1  = m1 + m2 + m1 + m4

        m5 = [
            c.n(C1, self.q),
            c.n(C1, self.q),
            c.n(C1, self.q),
            c.n(C1, self.q),

        ]

        v2 = m5 + m5 + m5 + m5
       
        return\
        [rest(self.w*4)] +\
        \
        [rest(self.w*4)] +\
        v1 +\
        v1 +\
        \
        v2 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v2 +\
        \
        v1
    
    def hats(self):
        d = self.hat1

        m1 = [
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
        ]

        m4 = [
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            rest(self.h)
        ]
        v1 = m1 + m1 + m1 + m4
        
        m5 = [
            d.n(C1, self.e), d.n(C1, self.e),
            d.n(C1, self.e), d.n(C1, self.e),
            d.n(C1, self.e), d.n(C1, self.e),
            d.n(C1, self.e), d.n(C1, self.e),
        ]

        v2 = m5 + m5 + m5 + m5

        return\
        [rest(self.w*4)] +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v2 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v2 +\
        \
        v1
    
    def hats_2(self):
        d = self.hat2

        m1 = [
            d.n(C4, self.e), d.n(C4, self.e), 
            d.n(C4, self.e), d.n(C5, self.e),
            d.n(C4, self.e), d.n(C4, self.e),
            d.n(C4, self.e), d.n(C5, self.e),
        ]

        v1 = m1 + m1 + m1 + m1
        

        return\
        [rest(self.w*4)] +\
        \
        [rest(self.w*4)] +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1
    
    def navi(self):
        n = Hey()
        m1 = [
            rest(self.e*3), n.n(C1, self.e),
            rest(self.e*3), n.n(C1, self.e),
        ]

        v1 = m1 + m1 + m1 + m1

        return\
        [rest(self.w*4)] +\
        \
        [rest(self.w*4)] +\
        v1 +\
        v1 +\
        \
        v1 +\
        \
        v1
    
    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=11_000)


def main():
    beat = FPDG(45)
    beat.produce_full()
    beat.save(beat.production, "Fake Plants Don't Grow")

