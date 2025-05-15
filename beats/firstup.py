from modules.beat import *
from modules.instruments import *
from modules.audio import *

class First(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beats", "firstup"), name)


    
    
    
    def synth(self):
        s = First2(3, self.whole)
        s2 = First2(4, self.whole)
        

        f = First1(3, self.whole)
        #f2 = First1(3, self.whole)

        m1 = build_measure(f.q_a, rest(self.quarter), f.e_gs, f.q_a, rest(self.eighth))

        m1b = build_measure(f.q_f, rest(self.quarter), f.e_ds, f.q_f, rest(self.eighth))
        m1 = combine(m1, m1b)

        m2 = build_measure(rest(self.eighth), s.e_a,
                           s.e_a, s.s_a, s.s_a,
                           s2.s_d, s2.s_c, s.s_b, s.s_b,
                           rest(self.quarter))

        m3 = build_measure(rest(self.eighth), s.e_a,
                           s.e_a, s.s_a, s.s_a,
                           s.s_g, s.s_g, s.s_a, s.s_a,
                           rest(self.quarter))
        


        v1 = build_measure(rest(self.whole), rest(self.whole), rest(self.whole), m2)
        v2 = build_measure(m3, m2, m3) # Last verse of the intro !

        v3 = build_measure(m1, m1, m1, m1)

        return v1, v2, v3
    

    def bass(self):
        b = DressDB(1, self.whole)

        #m1 = fade_out(build_measure(b.q_c, b.q_c, b.q_c, b.q_c), 4)
        m1 = build_measure(b.q_c,
                           rest(self.eighth), b.s_c,
                           b.e_c, b.s_c,
                           rest(self.eighth), b.e_c, rest(self.eighth))

        m2 = build_measure(b.e_c, rest(self.half + self.sixteenth), # 2.5
                           b.s_c, b.e_c, b.s_c, rest(self.sixteenth)
                           )

        v1 = build_measure(m1, m1, m1, m1)
        v2 = build_measure(m1, m1, m1, m2)
        v3 = build_measure(m2, m2, m2)
        
        return v1, v2, v3
    

    def funk(self):
        return rest(self.whole * 4)
    
    def drums(self):
        v1 = rest(self.whole * 3) # Lead into the melody
        v2 = rest(self.whole * 4) # Main beat

        return v1, v2
    
    def produce(self):
        #   Get ya instruments !    #
        m1 = self.metronome()
        m1 = build_measure(m1, m1, m1, m1)

        b1, b2, b3 = self.bass()

        s1, s2, s3 = self.synth()

        d0, d1 = self.drums()

        f1 = self.funk()

        #   Get ya verses!  #
        #   Intro
        v1 = combine(m1, b1)

        v2 = combine(m1, b2) # end of intro
        v2 = combine(v2, s1)

        v3 = combine(b3, s2) # ONLY 3 MEASURES LONG! SETS UP THE MELODY
        v3 = combine(v3, d0) # add the drum intro to v3

        #   Melody Kicks in
        v4 = combine(v1, d1) # make d4 out of v3
        

        #   Produce ya beat !!  #
        p = build_measure(
            #   Intro   #
            v1, v2, v3,

            #   Melody  #
                          )


        #   Save ya beat.    #
        self.save(p, "First Up")

    def test(self):
        a, b, c = self.synth()

        p = build_measure(a, b, c, c, a, a, b, a, b, a, b)

        self.save(p, "Test")

def main():
    #First(60).test()
    First(60).produce()