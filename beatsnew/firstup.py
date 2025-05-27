from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class First(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "firstup"), name)
    
    
    def bass(self):
        b = Bass()

        #m1 = fade_out(build_measure(b.q_c, b.q_c, b.q_c, b.q_c), 4)
        m1 = build_measure(b.note(C1, self.quarter),
                           rest(self.eighth), b.note(C1, self.s),
                           b.note(C1, self.e), b.note(C1, self.s),
                           rest(self.eighth), b.note(C1, self.e), rest(self.eighth))

        m2 = build_measure(b.note(C1, self.e), rest(self.half + self.sixteenth), # 2.5
                           b.note(C1, self.s), b.note(C1, self.e), b.note(C1, self.s), rest(self.sixteenth)
                           )

        v1 = build_measure(m1, m1, m1, m1)
        v2 = build_measure(m2, m2, m2, m2)

        
        return v1, v2


    def funk(self):
        f = Funk()

        #   Start at a C3
        # C3, B2, A2, C3
        # A2, B2, C3

        m1 = build_measure(
        f.note(C4, self.e), # .5
        f.note(B3, self.s), # .75
        f.note(A3, self.s), # 1
        f.note(C4, self.q), # 2
        rest(self.s), # 2.25
        f.note(A3, self.s), # 2.5
        f.note(B3, self.e), # 3
        f.note(C4, self.q), # 4
        )

        m2 = build_measure( # Tone shift -2 full tones
        f.note(A3, self.e), # .5
        f.note(G3, self.s), # .75
        f.note(F3, self.s), # 1
        f.note(A3, self.q), # 2
        rest(self.s), # 2.25
        f.note(F3, self.s), # 2.5
        f.note(G3, self.e), # 3
        f.note(A3, self.q), # 4
        )


        amp = 0.5
        v1 = build_measure(m1, m1, m2, m2) * amp
        

        v2 = build_measure(m2, m2, m2, m2) * amp
        

        #   V3  #
        m3 = build_measure(f.note(F3, self.e), f.note(A3, self.s),
        f.note(B3, self.e), f.note(C4, self.e),
        f.note(D4, self.e), f.note(C4, self.s),
        f.note(B3, self.e), f.note(A3, self.q)
        )

        m3b = build_measure(f.note(F3, self.e), f.note(A3, self.s),
        f.note(B3, self.e), f.note(C4, self.e),
        f.note(D4, self.e), f.note(C4, self.s),
        f.note(B3, self.e), f.note(A3, self.e), f.note(G3, self.e)
        )

        m4 = build_measure(f.note(E3, self.e), f.note(G3, self.s),
        f.note(A3, self.e), f.note(B3, self.e),
        f.note(C4, self.e), f.note(B3, self.s),
        f.note(A3, self.e), f.note(G3, self.q)
        )

        m4b = build_measure(f.note(E3, self.e), f.note(G3, self.s),
        f.note(A3, self.e), f.note(B3, self.e),
        f.note(C4, self.e), f.note(B3, self.s),
        f.note(A3, self.e), f.note(G3, self.e), f.note(F3, self.e)
        )

        v3 = build_measure(m3, m3b, m4, m4b) * amp

        #   V4  #
        m5 = build_measure(f.note(D3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(D3, self.e), f.note(F3, self.e),
                           rest(self.quarter),)
        
        m6 = build_measure(f.note(D3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e))
                           
        
        m7 = build_measure(f.note(C3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(C3, self.e), f.note(E3, self.e),
                           rest(self.quarter),)
        
        m8 = build_measure(f.note(C3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(D3, self.e), rest(self.e))

        v4 = build_measure(m5, m6, m7, m8)

        return v1, v2, v3, v4
    

    def drums(self):
        d = Skirt()

        m1 = build_measure(
            d.note(C3, self.e),
            d.note(C3, self.s), d.note(C3, self.s), # 1

            d.note(C3, self.e), d.note(C3, self.s), # 1.75
            d.note(C3, self.e), # 2.25
            d.note(C3, self.s), # 2.5

            d.note(C3, self.e), d.note(C3, self.e), #3.5
            d.note(C3, self.s), d.note(C3, self.s) # 4

        )


        v1 = build_measure(m1, m1, m1, m1)

        return v1


    def navi(self):
        n1 = Hey()
        
        m1 = build_measure(n1.note(), n1.note(), n1.note(), n1.note())

        return m1

    def intro(self):

        #   Gather Instruments  #
        b1, b2 = self.bass()
        f1, f2, f3, f4 = self.funk()
        d1 = self.drums()
        n1 = self.navi() * 0.05


        #   Produce each section    #
        v0 = b1

        v1 = combine(b1, d1)

        v2 = combine(b1, f1)
        v2 = combine(v2, d1)

        prod = build_measure(
            v0, v1, v2, v2
        )


        #   Save the production #
        self.save(prod, "intro")
        return prod


    def melody(self):
        #   Gather Instruments  #
        b1, b2 = self.bass()
        f1, f2, f3, f4 = self.funk()
        d1 = self.drums()


        #   Produce each section    #
        v1 = f4
        #v1 = combine(b1, d1)
        #v1 = combine(v1, f2)

        prod = build_measure(
            v1, v1
        )

        # prod = (prod / np.max(np.abs(prod)) * 32767).astype(np.int16)
        # prod = np.column_stack((prod, prod))
        # sound = pygame.sndarray.make_sound(prod)
        # sound.play()
        # while pygame.mixer.get_busy():
        #     pass

        #   Save the production #
        self.save(prod, "melody")
        return prod


    def produce(self):
        #   Gather Each Section of the song    #
        intro = self.intro()
        melody = self.melody()


        #   Save the production #
        prod = build_measure(
            intro, melody
        )

        self.save(prod, "firstup")

        return
    
def main():
    First(62).produce()