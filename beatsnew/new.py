from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class New(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "new"), name)
    
    def drums(self, part=""):
        if part == "v1":
            #kb = KickBass2(dist=15.0, attack=20, amp=5)
            kb = Snare(amp=20)
            k = HipSkirt(attack = 30)


            m1 = build_measure(
                kb.note(C1, self.q),
                kb.note(C1, self.q),
                kb.note(C1, self.q),
                kb.note(C1, self.q),
            )

            s1 = build_measure(
                rest(self.h),
                k.note(C2, self.s), k.note(C2, self.e), rest(self.s),
                rest(self.q)
            )

            s2 = build_measure(
                rest(self.h),
                k.note(C2, self.s), k.note(C2, self.s), k.note(C2, self.s), rest(self.s),
                rest(self.q)
            )

            s4 = build_measure(
                rest(self.h),
                k.note(C2, self.e), k.note(C2, self.e), 
                k.note(C2, self.e), rest(self.e)
            )


            m1 = combine(m1, s1)
            m2 = combine(m1, s2)
            m4 = combine(m1, s4)

            v1 = build_measure(m1, m2, m1, m4)
            return v1
        
        elif part == "v2":
            s = Snare(amp=20)

            m1 = build_measure(
                s.note(C1, self.q),
                s.note(C1, self.q),
                s.note(C1, self.q),
                s.note(C1, self.q),
            )

            v1 = build_measure(m1, m1, m1, m1)
            return v1

        elif part == "r1":
            k = HipSkirt(attack = 30)

            m1 = build_measure(
                k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), rest(self.s),
            )

            return m1


    def bass(self, part=""):
        if part == "v1":
            b = Bass()

            m1 = build_measure(
                b.note(A0, self.whole  * 4)
            )


            return m1

    def keys(self, part= ""):
        if part == "v1":
            k = DontMind()

            m1 = build_measure(
                k.note(E4, self.e), k.note(F4, self.e),
                k.note(D4, self.e), rest(self.e),
                k.note(D4, self.e), rest(self.e),
                rest(self.e), k.note(D4, self.e),
            )

            m4 = build_measure(
                k.note(E4, self.e), k.note(C4, self.e),
                rest(self.q),
                k.note(D4, self.e), k.note(D4, self.e),
                k.note(D4, self.e), k.note(D4, self.e),
            )

            v1 = build_measure(m1, m1, m1, m4)

            return v1
        
        elif part == "v2" or part == "v2q":
            if part == "v2":
                k = DontMind(amp=2.0)
            elif part == "v2q":
                k = DontMind()

            m1 = build_measure(
                k.note(E3, self.e) + k.note(G3, self.e), k.note(F3, self.e) + k.note(A3, self.e),
                k.note(D3, self.e) + k.note(F3, self.e), rest(self.e),
                k.note(D3, self.e) + k.note(F3, self.e), rest(self.e),
                rest(self.e), k.note(D3, self.e) + k.note(F3, self.e),
            )

            m4 = build_measure(
                k.note(E3, self.e) + k.note(G3, self.e), k.note(C3, self.e) + k.note(E3, self.e),
                rest(self.q),

                k.note(D3, self.s) + k.note(F3, self.s), k.note(D3, self.s) + k.note(F3, self.s), k.note(D3, self.e) + k.note(F3, self.e),
                k.note(D3, self.e) + k.note(F3, self.e), k.note(D3, self.e) + k.note(F3, self.e),
            )

            v1 = build_measure(m1, m1, m1, m4)

            return v1

        elif part == "r1":
            k = DontMind()

            m1 = build_measure(
                k.note(F4, self.s), k.note(F4, self.s), k.note(F4, self.e),
            )
            return m1
        
        elif part == "r2":
            k = DontMind()

            m1 = build_measure(
                k.note(F5, self.e), k.note(F5, self.e),
            )
            return m1


    def produce(self):
        #   Gather Each Section of the song    #
        k1 = self.keys("v1")
        k2 = self.keys("v2")
        k2q = self.keys("v2q")
        kr = self.keys("r1")
        kr2 = self.keys("r2")

        d1 = self.drums("v1")
        d2 = self.drums("v2")
        dr = self.drums("r1")
        
        b1 = self.bass("v1")


        v1 = k1

        v2 = combine(k1, d1)

        v3 = combine(v2, d2)

        v4 = combine(k2, d1)
        
        v5 = mix(k2q, k1)

        v6 = mix(v5, d1, d2)


        refrain1 = dr
        refrain2 = combine(kr, dr)
        refrain3 = combine(refrain2, kr2)

        #   Save the production #
        prod = build_measure(
            v1, v1,

            refrain1,

            v2, v2,

            refrain2,
            
            v3, v3,

            refrain2,

            v4, v4,

            refrain3,

            v5, v5,

            v6, v6



        )

        self.save(prod, "new")

        return
    
def main():
    New(72).produce()