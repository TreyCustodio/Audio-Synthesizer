from modules.beat import *
from modules.instruments import *
from modules.audio import *

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
        f.note(C3, self.e), # .5
        f.note(B2, self.s), # .75
        f.note(A2, self.s), # 1
        f.note(C3, self.q), # 2
        rest(self.s), # 2.25
        f.note(A2, self.s), # 2.5
        f.note(B2, self.e), # 3
        f.note(C3, self.q), # 4
        )

        m2 = build_measure( # Tone shift -2 full tones
        f.note(A2, self.e), # .5
        f.note(G2, self.s), # .75
        f.note(F2, self.s), # 1
        f.note(A2, self.q), # 2
        rest(self.s), # 2.25
        f.note(F2, self.s), # 2.5
        f.note(G2, self.e), # 3
        f.note(A2, self.q), # 4
        )



        v1 = build_measure(m1, m1, m2, m2)
        v2 = build_measure(m2, m2, m2, m2)

        return v1, v2
    

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

    def intro(self):

        #   Gather Instruments  #
        #m1 = self.metronome()
        #m1 = build_measure(m1, m1, m1, m1)

        b1, b2 = self.bass()
        f1, f2 = self.funk()
        d1 = self.drums()

        #s1, s2, s3 = self.synth()

        #d0, d1 = self.drums()


        #   Produce each section    #
        v1 = combine(b1, d1)

        v2 = combine(b1, f1)
        v2 = combine(v2, d1)

        prod = build_measure(
            v1, v2
        )

        prod = d1

        #   Save the production #
        self.save(prod, "intro")


    def produce(self):
        #   Gather Each Section of the song    #

        #   Save the production #
        return
    
def main():
    First(62).intro()