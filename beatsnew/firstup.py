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

    def intro(self):

        #   Gather Instruments  #
        #m1 = self.metronome()
        #m1 = build_measure(m1, m1, m1, m1)

        b1, b2 = self.bass()
        
        #s1, s2, s3 = self.synth()

        #d0, d1 = self.drums()


        #   Produce each section    #
        v1 = b1
        v2 = b2

        prod = build_measure(
            v1, v2
        )


        #   Save the production #
        self.save(prod, "intro")


    def produce(self):
        #   Gather Each Section of the song    #

        #   Save the production #
        return
    
def main():
    First(62).intro()