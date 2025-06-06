from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class TrapPop(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "trappop"), name)
    
    """
    Instrumental Sections
    """
    def bass(self):
        b = Bass()
        d = Snare()
        
        amp = 2.0

        m1 = build_measure(
            b.note(C1, self.q),
            rest(self.trey - self.e),
            b.note(C1, self.e)
        )

        m2 = build_measure(
            b.note(C1, self.q),
            rest(self.trey)
        )

        m1b = build_measure(
            d.note(C2, self.q),
            rest(self.trey - self.e),
            d.note(C2, self.e)
        ) * amp

        m2b = build_measure(
            d.note(C2, self.q),
            rest(self.trey)
        ) * amp

        m1 += m1b
        m2 += m2b

        v1 = build_measure(m1, m2, m1, m2)
        return v1

    def drums(self):
        k = Skirt()
        s = Snare()
        c = HipSkirt()

        m1 = build_measure(
            k.note(C3, self.e), k.note(C3, self.e), 
            k.note(C3, self.e), k.note(C3, self.e),
            k.note(C3, self.e) + c.note(C3, self.e), k.note(C3, self.e),
            k.note(C3, self.e), k.note(C3, self.e) + c.note(C3, self.e),
        )

        m2 = build_measure(
            k.note(C3, self.e), k.note(C3, self.e) + c.note(B2, self.e),
            k.note(C3, self.e), k.note(C3, self.e) + c.note(B2, self.e),
            k.note(C3, self.e) + c.note(C3, self.e), k.note(C3, self.e), 
            k.note(C3, self.e), k.note(C3, self.e),
        )

        v1 = build_measure(m1, m2, m1, m2)

        return v1

    def drums2(self):
        k = Skirt()
        s = Snare()
        c = Cymbal()

        m1 = build_measure(
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
        )

        m1b = build_measure(
            s.note(C3, self.e), rest(self.e),
            rest(self.trey),
        ) * 5.0

        m1 = combine(m1, m1b)

        v1 = build_measure(m1, m1, m1, m1)

        return v1

    def synth(self):
        s = Clean_Synth()

        m1 = build_measure(
            s.note(A3, self.e), s.note(F3, self.e),
            s.note(E3, self.e), s.note(D3, self.e),
            s.note(G3, self.e), s.note(F3, self.e),
            s.note(E3, self.e), s.note(D3, self.e)
        ) * 0.2

        m2 = m1 = build_measure(
            s.note(A4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e),
            s.note(G4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e)
        ) * 0.01

        m3 = build_measure(
            s.note(A2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e),
            s.note(G2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e)
        ) * 0.1

        v1_bar = m1 + m2 + m3
        v1 = build_measure(v1_bar, v1_bar, v1_bar, v1_bar)

        return v1

    def synth2(self):
        s = Clean_Synth()

        m2 = m1 = build_measure(
            s.note(A4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e),
            s.note(G4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e)
        ) * 0.01

        m3 = build_measure(
            s.note(A2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e),
            s.note(G2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e)
        ) * 0.1

        v1_bar = m2 + m3
        v1 = build_measure(v1_bar, v1_bar, v1_bar, v1_bar)

        return v1

    def keys(self):
        return

    def klinks(self):
        k = Skirt()
        s = Snare()

        m0 = build_measure(
            rest(self.whole*3),
            rest(self.trey),
            k.note(A2, self.s), k.note(F2, self.s), k.note(A2, self.e)
        ) * 3.0

        m0b = build_measure(
            rest(self.whole*3),
            rest(self.trey),
            s.note(A2, self.s), s.note(F2, self.s), s.note(A2, self.e)
        ) * 2.0

        m0 += m0b

        


        return m0


    """
    Sections of the Song
    """
    def intro(self):
        b1 = self.bass()
        d1= self.drums()
        d2 = self.drums2()
        s1 = self.synth()
        k = self.klinks()

        v1 = combine(b1, d1)

        v2 = combine(v1, s1)

        v3 = combine(v2, k)

        v4 = combine(v2, d2)

        v5 = combine(v4, k)

        prod = build_measure(
            v1, v1, 
            v2, v3,
            v4, v5
        )

        return prod

    def chorus1(self):
        return

    def hook1(self):
        return

    def loop(self):
        b1 = self.bass()
        d1= self.drums()
        d2 = self.drums2()
        s1 = self.synth()

        v1 = combine(b1, d1)

        v2 = combine(v1, s1)

        v4 = combine(v2, d2)


        prod = build_measure(
            v4, v4,
            v4, v4,
            v4, v4,
            v4, v4
        )

        return prod

    def verse1(self):
        b1 = self.bass()
        d1= self.drums()
        d2 = self.drums2()
        s1 = self.synth2()
        s2 = self.synth()

        base = combine(b1, d1)
        base = combine(base, d2)

        v1 = combine(base, s1)
        v2 = combine(base, fade_in(s2, 1.0))
        v3 = combine(base, s2)

        prod = build_measure(
            v1, v1,
            v2, v3
        )

        return prod

    def refrain1(self):
        return

    def verse2(self):
        return

        

    def produce(self):
        #   Gather Each Section of the song    #
        intro = self.intro()
        loop = self.loop()
        verse1 = self.verse1()

        #   Save the production #
        prod = build_measure(
            #   Intro   #
            intro,

            #   Verse 1 #
            loop
        )

        self.save(prod, "Trap Pop")

    
def main():
    TrapPop(82).produce()