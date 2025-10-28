from modules.beat import *
from modules.instruments import *
from modules.audio import *


class O4(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "04"))
        
        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=0.4)

        #   Plucky, Accoustic Synths   #
        self.acou1 = Acoustic1()
        self.acou2 = Acoustic2(amp=0.4)
        self.acou3 = Acoustic2(amp=0.1)

        # #   Synths  #
        self.synth1 = Plucky()
        self.synth2 = Plucky(amp=0.3)

        # #   Melody Synths   #
        self.synth3 = DontTell2()

        # #   Drums   #
        self.tap1 = Tap3(attack=10, amp=0.5) # clap
        self.tap2 = Tap3(attack=100, amp=0.3)

        self.kick1 = Tap3(amp=2.5, attack=60, noise_amount=0.0)

        self.hat1 = Hi_Hat(amp=2.0)
        self.chime1 = Snare()

        
    def get_instruments(self):
        #   Instrument Dictionary   #
        self.instruments = {

            #   Bass    #
            0: [self.bass1, self.bass()],

            # #   Accoustics  #
            1: [self.acou1, self.acoustic_1()],
            2: [self.acou2, self.acoustic_2()],
            3: [self.acou3, self.acoustic_3()],

            # #   Synths  #
            4: [self.synth1, self.synth_1()],
            8: [self.synth2, self.synth_2()],
            9: [self.synth3, self.melody_1()],
            

            # #   Percussion
            5: [self.tap1, self.claps()],
            6: [self.tap2, self.taps()],
            7: [self.kick1, self.kicks()],
        }
        
    def acoustic_1(self):
        s = self.acou1

        m1 = [
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.e), s.n(D3, self.e), 
        ]

        m2 = [
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.q - self.s),
            s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.e), s.n(D3, self.e), 
        ]
        
        m3 = [
            s.n(C3, self.e + self.s), s.n(C3, self.s), s.n(C3, self.s), # 1
            s.n(C3, self.s), s.n(C3, self.e + self.s), # 2.25
            s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.e), # 3.5
            s.n(C3, self.e), 
        ]


        v1 = m1 + m2 + m3 + m3

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    
    def acoustic_2(self):
        s = self.acou2

        m1 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h),
            rest(self.e)
        ]

        m2 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h),
            rest(self.e)
        ]

        m3 = [
            s.n(A2, self.q),
            rest(self.e),
            s.n(A2, self.h + self.e),

        ]

        m4 = [
            s.n(A2, self.q),
            rest(self.e),
            s.n(A2, self.h + self.e),

        ]
           

        v1 = m1 + m2 + m3 + m4

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    
    def acoustic_3(self):
        s = self.acou3
  
        # m1 = [
        #     s.n(D4, self.e + self.s), s.n(A3, self.s), s.n(A3, self.s), # 1
        #     s.n(A3, self.s), s.n(D4, self.e + self.s), # 2.25
        #     s.n(A3, self.s), s.n(A3, self.s), s.n(A3, self.s), s.n(D4, self.e), # 3.5
        #     s.n(A3, self.e),

        # ]

        # m2 = [
        #     s.n(C4, self.e + self.s), s.n(G3, self.s), s.n(G3, self.s), # 1
        #     s.n(G3, self.s), s.n(C4, self.e + self.s), # 2.25
        #     s.n(G3, self.s), s.n(G3, self.s), s.n(G3, self.s), s.n(C4, self.e), # 3.5
        #     s.n(G3, self.e),
        # ]

        # m1 = [
        #     s.n(D4, self.e), 
        #     rest(self.q),
        #     s.n(D4, self.e), # 2.25
        #     rest(self.q),
        #     s.n(D4, self.e), # 3.5
        #     rest(self.e)
        # ]

        # m2 = [
        #     s.n(C4, self.e),
        #     rest(self.q),
        #     s.n(C4, self.e), # 2.25
        #     rest(self.q),
        #     s.n(C4, self.e), # 3.5
        #     rest(self.e)
        # ]

        m1 = [
            s.n(D4, self.e), 
            s.n(A3, self.e),

            rest(self.e),
            s.n(D4, self.e),

            s.n(A3, self.e),
            rest(self.e),

            s.n(D4, self.e), # 3.5
            s.n(A3, self.e),
        ]

        m2 = [
            s.n(C4, self.e), 
            s.n(G3, self.e),

            rest(self.e),
            s.n(C4, self.e),

            s.n(G3, self.e),
            rest(self.e),

            s.n(C4, self.e), # 3.5
            s.n(G3, self.e),
        ]

        m3 = [
        ]

        m4 = [
        ]
      

        v1 = m1 + m1 + m2 + m2

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1

    def melody_1(self):
        s = self.synth3

        #   Intro 4-bar #
        v0 = [
            rest(self.w*3),
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]

        #   V1  #
        m1 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(E3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m2 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), 
            s.n(G3, self.e + self.s),
        ]

        m3 = [
            s.n(E3, self.w)
        ]

        m4 = [
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]
    
        v1 = m1 + m2 + m3 + m4


        #   V2  #
        m5 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m6 = [
            s.n(F3, self.e), s.n(D3, self.e),
            s.n(F3, self.s), s.n(D3, self.e), # 1.75
            s.n(A3, self.e), s.n(G3, self.e), # 2.75
            s.n(F3, self.e), s.n(G3, self.e +self.s)# 3.25
        ]

        m7 = [
            s.n(E3, self.w),
        ]

        m8 = [
            rest(self.whole - self.s*3),
            s.n(A3, self.s), s.n(A3, self.s), s.n(A3, self.s),
        ]

        v2 = m5 + m6 + m7 + m8


        #   V3  #
        ##  When I'm alone with you
        m9 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e),
            rest(self.t - self.s*2),
            s.n(G3, self.s)
        ]

        ##  My life becomes true--no, no, no body else.
        m10 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e), # 1.25
            s.n(B3, self.q), # 2.25

            ## no, no
            s.n(B3, self.e), s.n(B3, self.e), # 3.25
            s.n(B3, self.e + self.s),
        ]

        m11 = [
            s.n(A3, self.e), s.n(G3, self.s),
            s.n(E3, self.e), # 1.25
            rest(self.t - self.s*2),
            s.n(E3, self.s),
        ]

        m12 = [
            s.n(B3, self.e), s.n(B3, self.s), s.n(A3, self.e), # 1.25
            s.n(G3, self.e), # 1.75
            s.n(E3, self.e), # 2.25
            rest(self.s+ self.e + self.q)
        ]

        v3 = m9 + m10 + m11 + m12

        #   H1 (Hook 1) #
        m13 = [
            s.n(F3, self.e), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m14 = [
            s.n(E3, self.s), s.n(F3, self.s), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m15 = [
            s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h)
        ]

        m16 = [
            s.n(E3, self.s), s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h - self.s)
        ]

        return\
        v0 +\
        v1 +\
        v2 +\
        v3 +\
        \
        \
        v1 +\
        v2
    
    def synth_1(self):
        s = self.synth3

        m1 = [
            s.n(A3, self.e), rest(self.e),
            s.n(D3, self.e), rest(self.e),
            rest(self.e), s.n(D3, self.e), 
            s.n(A3, self.e), rest(self.e)
        ]

        m2 = [
            s.n(D3, self.e), s.n(D3, self.s),
            s.n(A3, self.e), s.n(A3, self.s),
            s.n(D3, self.e), rest(self.e),
            s.n(A3, self.e), s.n(D3, self.e),
            rest(self.e)
        ]

        m3 = [
            s.n(G3, self.e), s.n(C3, self.e),
            rest(self.e), rest(self.e),
             rest(self.e), s.n(C3, self.e),
            s.n(G3, self.e), rest(self.e),
            
        ]

        m4 = [
            s.n(C3, self.e), s.n(C3, self.s), # 0.75
            s.n(G3, self.e), s.n(G3, self.s), # 1.5

            s.n(C3, self.e), rest(self.e), # 2.5
            s.n(G3, self.e), # 3
            s.n(C3, self.e), s.n(F3, self.e), 
        ]


        v1 = m1 + m2 + m3 + m4
        off_verse = [rest(self.whole*4)]

        return \
            off_verse +\
            off_verse +\
            off_verse +\
            off_verse +\
            \
            \
            off_verse +\
            off_verse +\
            \
            v1 +\
            v1
    
    def synth_2(self):
        s = self.synth2

        m1 = [
            rest(self.w)
        ]

        m2 = [
            rest(self.w)

        ]

        m3 = [
            rest(self.w)

            
        ]

        m4 = [
            rest(self.w - self.e*3),
            s.n(F3, self.e) + s.n(C3, self.e), 
            s.n(A3, self.e) + s.n(C3, self.e), rest(self.e)
        ]


        v1 = m1 + m2 + m3 + m4
        off_verse = [rest(self.whole*4)]

        return \
            off_verse +\
            off_verse +\
            off_verse +\
            off_verse +\
            \
            \
            off_verse +\
            off_verse +\
            \
            v1 +\
            v1
       
    def bass(self):
        """Bass melody"""
        b = self.bass1
        m1 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            b.n(D2, self.h + self.e),
        ]

        m2 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            b.n(A1, self.h + self.e),
        ]

        m3 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(D2, self.e), b.n(D2, self.e),
            rest(self.e)
        ]

        m4 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(A1, self.e), b.n(A1, self.e),
            rest(self.e)
        ]
        off_verse = [rest(self.w*4)]
        v1 = m3 + m3 + m4 + m4

        return \
        off_verse +\
        off_verse +\
        off_verse +\
        off_verse +\
        \
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1
    
    def kicks(self):
        b = self.kick1
        m1 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            b.n(D2, self.h + self.e),
        ]

        m2 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            b.n(A1, self.h + self.e),
        ]

        m3 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(D2, self.e), b.n(D2, self.e),
            rest(self.e)
        ]

        m4 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(A1, self.e), b.n(A1, self.e),
            rest(self.e)
        ]

        off_verse = [rest(self.w*4)]
        v1 = m3 + m3 + m4 + m4

        return \
        off_verse +\
        off_verse +\
        off_verse +\
        off_verse +\
        \
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1
    
    def claps(self):
        """Tap melody"""
        d = self.tap1

        intro = [
            rest(self.w*3),
            rest(self.t),
            d.n(C2, self.q)
        ]

        m1 = [
            rest(self.q),
            d.n(C2, self.q),
            rest(self.q),
            d.n(C2, self.q),
        ]

        m4 = [
            rest(self.q),
            d.n(C2, self.q),
            rest(self.q),
            d.n(C2, self.s), d.n(C2, self.s), d.n(C2, self.s), d.n(C2, self.s),
        ]


        v1 = m1 + m1 + m1 + m4
        off_verse = [rest(self.w*4)]

        return \
        off_verse +\
        off_verse +\
        off_verse +\
        off_verse +\
        \
        \
        off_verse +\
        intro +\
        \
        v1 +\
        v1

    def taps(self):
        """Tap melody"""
        d = self.tap2

        

        m1 = [
            d.n(C2, self.q),
            rest(self.q),
            d.n(C1, self.q),
            rest(self.q),


        ]

        m2 = [
            d.n(C2, self.q),
            rest(self.q),
            d.n(C1, self.q),
            rest(self.q),


        ]

        m3 = [
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.e), d.n(C1, self.e), 
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.e), rest(self.e)
        ]

        m4 = [
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.e), d.n(C1, self.e), 
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
            d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s), d.n(C1, self.s),
        ]


        v1 = m1 + m2 + m1 + m2
        v2 = m3 + m4 + m3 + m4

        off_verse = [rest(self.w*4)]
        return \
        off_verse +\
        off_verse +\
        off_verse +\
        off_verse +\
        \
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v2

    
    def hats(self):
        """Hi-hat crashes"""
        d = self.hat1

        return
    
    def chimes(self):
        d = self.chime1

        return

def main():
    beat = O4(40)
    beat.export_full(stereo=False)