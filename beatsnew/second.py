from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class Second(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "second"), name)
    
    def bass(self):
        b = Bass()

        m1 = build_measure(
            b.note(C2, self.s + self.s/2), b.note(D2, self.e + self.s/2),
            b.note(E2, self.s + self.s/2), b.note(Gs2, self.e),
            rest(self.q + self.s/2),
            b.note(A2, self.e), rest(self.e)
            )
        
        m2 = build_measure(
            b.note(C2, self.e), b.note(D2, self.e),
            b.note(E2, self.s + self.s/2), b.note(Gs2, self.e),
            rest(self.q + self.s/2),
            b.note(A2, self.e), rest(self.e)
            )

        m3 = build_measure(
            b.note(C2, self.e), b.note(D2, self.e),
            b.note(E2, self.e), b.note(Gs2, self.e),
            rest(self.q),
            b.note(A2, self.e), rest(self.e)
            )
        
        v1 = build_measure(m1, m2, m3, m3)
        return v1

    def keys(self):
        s = Clean_Synth()

        m1 = build_measure(
            s.note(C4, self.s + self.s/2), s.note(D4, self.e + self.s/2),
            s.note(E4, self.s + self.s/2), s.note(Gs4, self.e),
            rest(self.q + self.s/2),
            s.note(A4, self.e), rest(self.e)
            )
        
        m2 = build_measure(
            s.note(C4, self.e), s.note(D4, self.e),
            s.note(E4, self.s + self.s/2), s.note(Gs4, self.e),
            rest(self.q + self.s/2),
            s.note(A4, self.e), rest(self.e)
            )

        m3 = build_measure(
            s.note(C4, self.e), s.note(D4, self.e),
            s.note(E4, self.e), s.note(Gs4, self.e),
            rest(self.q),
            s.note(A4, self.e), rest(self.e)
            )
        
        v1 = build_measure(m1, m2, m3, m3)
        return v1


    def intro(self):
        k1 = self.keys()
        b1 = self.bass()
        b1 *= 25.0

        v1 = combine(k1, b1)

        prod = build_measure(
            k1, combine(k1, b1)
        )
        
        self.save(prod, "intro")
        return prod

    def chorus1(self):
        return

    def hook1(self):
        return

    def verse1(self):
        return

    def refrain1(self):
        return

    def verse2(self):
        return

        

    def produce(self):
        #   Gather Each Section of the song    #
        intro = self.intro()

        #   Save the production #
        prod = build_measure(
            #   Intro   #
            intro
        )

        self.save(prod, "second")

        return
    
def main():
    Second(72).produce()