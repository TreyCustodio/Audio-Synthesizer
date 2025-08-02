from modules.beat import *
from modules.instruments import *
from modules.audio import *


class O4(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)
        
        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=0.7)

        #   Plucky Synths   #
        self.acou1 = Acoustic(amp=0.7)
        self.acou2 = Acoustic()

        #   Synths  #
        self.synth1 = First4()
        self.synth2 = Church(amp = 0.5)

        #   Drums   #
        self.tap1 = Tap3(attack=10, amp=0.5) # clap
        self.tap2 = Tap3(attack=90, amp=0.3)


        self.kick1 = Tap3(attack=90, noise_amount=0.0)
        self.hat1 = Hi_Hat(amp=2.0)
        self.chime1 = Snare()

        #   Instrument Dictionary   #
        self.instruments = {
            # 0: [self.bass1, self.bass()],
            1: [self.acou1, self.acoustic1()],
            2: [self.acou1, self.acoustic2()],
            3: [self.acou2, self.acoustic3()],


            4: [self.tap1, self.claps()],
            5: [self.tap2, self.taps()],

            6:  [self.bass1, self.bass()],
            7:  [self.kick1, self.kicks()],


        }

    def acoustic1(self):
        s = self.acou1

        m1 = [
            s.n(D3, self.e + self.s), s.n(D3, self.s), s.n(D3, self.s), # 1
            s.n(D3, self.s), s.n(D3, self.e + self.s), # 2.25
            s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.e), # 3.5
            s.n(D3, self.e), 
        ]
        
        m2 = [
            s.n(D3, self.e + self.s), s.n(D3, self.s), s.n(D3, self.s), # 1
            s.n(D3, self.s), s.n(D3, self.e + self.s), # 2.25
            s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.e), # 3.5
            s.n(D3, self.e), 
        ]


        v1 = m1 + m2 + m1 + m2

        return \
            v1 +\
            v1 +\
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    
    def acoustic2(self):
        s = self.acou2

        m1 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h + self.e),
        ]

        m2 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h + self.e),

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
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    

    def acoustic3(self):
        s = Plucky()

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
            v1 +\
            \
            v1 +\
            v1 +\
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

        off_verse = [rest(self.w*4)]
        v1 = m1 + m1 + m2 + m2

        return \
        off_verse +\
        v1 +\
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

        off_verse = [rest(self.w*4)]
        v1 = m1 + m1 + m2 + m2

        return \
        off_verse +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1
    
    def claps(self):
        """Tap melody"""
        d = self.tap1

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
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1

    def taps(self):
        """Tap melody"""
        d = self.tap2

        

        m1 = [
            d.n(C6, self.q),
            d.n(C6, self.q),
            d.n(C5, self.q),
            d.n(C5, self.q),

        ]

        m2 = [
            d.n(C6, self.q),
            d.n(C6, self.q),
            d.n(C5, self.q),
            d.n(C5, self.q),

        ]

        m3 = [
            d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s),
            d.n(C5, self.e), d.n(C5, self.e), 
            d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s),
            d.n(C5, self.e), rest(self.e)
        ]

        m4 = [
            d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s),
            d.n(C5, self.e), d.n(C5, self.e), 
            d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s),
            d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s), d.n(C5, self.s),
        ]


        v1 = m1 + m2 + m1 + m2
        v2 = m3 + m4 + m3 + m4

        off_verse = [rest(self.w*4)]
        return \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v2 +\
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

    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=10_000)


def main():
    beat = O4(41)
    beat.produce_full()
    beat.save(beat.production, "04")

