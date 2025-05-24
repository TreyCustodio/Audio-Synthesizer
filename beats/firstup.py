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
        #f = First1(3, self.whole)

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
        


        #   Chord Progression during section 2 of the melody   #
        m9 = build_measure(s.e_f, s.s_a,
                           s.e_b, s2.e_c,
                           s2.e_d, s2.s_c,
                           s.e_b, s.q_a,
                           )
        
        m10 = build_measure(s.e_e, s.s_g,
                           s.e_a, s.e_b,
                           s2.e_c, s.s_b,
                           s.e_a, s.q_g,
                           )
        
        v1 = build_measure(m2, m3, m2, m3) # Last verse of the intro !

        v2 = build_measure(m1, m1, m1, m1)

        v3 = build_measure(m9, m9, m10, m10)

        return v1, v2, v3
    
    def synth2(self):
        s = First2(3, self.whole)
        s2 = First2(4, self.whole)

        #   Chord Progression during section 2 of the melody   #
        m9 = build_measure(s.e_f, s.s_a,
                           s.e_b, s2.e_c,
                           s2.e_d, s2.s_c,
                           s.e_b, s.q_a,
                           )
        
        m10 = build_measure(s.e_e, s.s_g,
                           s.e_a, s.e_b,
                           s2.e_c, s.s_b,
                           s.e_a, s.q_g,
                           )
        

        v1 = build_measure(m9, m9, m10, m10) * 1.4

        return v1
    

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
        v2 = build_measure(m2, m2, m2, m2)

        
        return v1, v2
    
    def bass2(self):
        b = DressDB(1, self.whole)

        #m1 = fade_out(build_measure(b.q_c, b.q_c, b.q_c, b.q_c), 4)
        notew = b.create_note(B0, self.whole)
        noteh = b.create_note(B0, self.half)

        m1 = build_measure(b.w_c)
        m2 = build_measure(notew)
        m3 = build_measure(noteh, b.create_note(B0, self.quarter), b.q_c)

        

        v1 = build_measure(m1, m1, m2)
        v2 = build_measure(m2, m2, m3, m3)
        
        return v1, v2
    

    def funk(self):
        #f = FirstF(2, self.whole)
        f = First3(2, self.whole)
        #f2 = First3(3, self.whole)


        m1 = build_measure(f.q_d, # 1
                           f.e_d, f.s_e, # 1.75
                           f.e_f, f.e_g, # 2.75
                           f.e_a, # 3.25
                           rest(self.sixteenth * 3),
                           )
        
        m2 = build_measure(f.e_d, f.s_e, # .75
                           f.e_f, f.e_g, # 1.75
                           f.e_a, # 2.25
                           f.create_note(G2, self.quarter + self.sixteenth*3)
                           #f.q_g, # 3.25
                           #rest(self.sixteenth *3)
                           )
        
        m2b = build_measure(f.e_d, f.s_e,
                           f.e_f, f.e_g,
                           f.q_a,
                           f.q_g, rest(self.sixteenth)
                           )
        
        m3 = build_measure(rest(self.quarter),
                           f.e_c, f.s_d,
                           f.e_e, f.e_f,
                           f.e_g, rest(self.sixteenth * 2), f.s_c
                           )
        
        m4 = build_measure(f.e_c, f.s_d,
                           f.e_e, f.e_f,
                           f.e_g,
                           f.create_note(F2, self.quarter + self.sixteenth*3)
                           )
        

        #   V 2 #
        m5 = build_measure(rest(self.sixteenth * 3), f.s_d, # 1
                            f.e_d, f.s_e, # 2
                            f.e_f, f.e_g, # 3
                            f.e_a, 
                            rest(self.sixteenth * 2),
                            )

        m6 = build_measure(f.s_d, f.e_d, f.s_e, # 1
                           f.e_f, f.e_g,  #2
                           f.q_a, # 3
                           f.create_note(G2, self.quarter + self.sixteenth*3) # 3 sixteenth notes carry into the second measure
                           # 4.75
                           )
        
        m7 = build_measure(rest(self.sixteenth * 1), # 5 / 8
                           f.s_c,
                            f.e_c, f.s_d, # 6/ 8
                            f.e_e, f.e_f, # 7 / 8
                            f.e_g,
                            rest(self.sixteenth * 2), # 8 / 8
                            )

        m8 = build_measure(rest(self.sixteenth), f.e_c, f.s_d,
                           f.e_e, f.e_f,
                           f.q_g,
                           f.q_f)
       
       

        #   Considering making this section just Synth2 #
        #   Leave the bass tones to Synth3  #
        # m9 = build_measure(f.e_f, f.s_a,
        #                    f.e_b, f2.e_c,
        #                    f2.e_d, f2.s_c,
        #                    f.e_b, f.q_a,
        #                    )
        
        # m10 = build_measure(f.e_e, f.s_g,
        #                    f.e_a, f.e_b,
        #                    f2.e_c, f.s_b,
        #                    f.e_a, f.q_g,
        #                    )
        
        m11 = build_measure(f.q_f, rest(self.half),
                            f.q_f)
        
        m12 = build_measure(f.q_f, rest(self.half), f.q_f)

        m13 = build_measure(f.q_e, rest(self.half), f.q_e)

        
        m14 = build_measure(f.q_e, rest(self.half),
                            f.q_e)





        v1 = build_measure(m1, m2, m3, m4)

        v2 = build_measure(m5, m6, m7, m8)

       # v3 = build_measure(m9, m9, m10, m10)
        v3 = build_measure(m11, m12, m13, m14)

        return v1, v2, v3
    

    def drums(self):
        v1 = rest(self.whole * 3) # Lead into the melody
        v2 = rest(self.whole * 4) # Main beat

        return v1, v2
    
    def produce(self):
        #   Produce ya beat !!  #
        p = build_measure(
            #   Intro   #
            self.intro(),

            #   Melody  #
            self.melody()

                          )


        #   Save ya beat.    #
        self.save(p, "First Up")


    def intro(self):
        #   Get ya instruments !    #
        m1 = self.metronome()
        m1 = build_measure(m1, m1, m1, m1)

        b1, b2 = self.bass()

        s1, s2, s3 = self.synth()

        d0, d1 = self.drums()


        #   Get ya verses!  #
        #   Intro
        v1 = combine(m1, b1)

        v2 = combine(m1, b2) # end of intro
        v2 = combine(v2, s1)
        v2 = combine(v2, d0) # add the drums

        #   Produce ya beat !!  #
        p = build_measure(
            v1, v2,

                          )


        #   Save ya beat.    #
        self.save(p, "intro")

        return p

    def intro(self):
        """Using this function to test runtime efficiency"""
        #   Get ya instruments !    #
        # m1 = self.metronome()
        # m1 = build_measure(m1, m1, m1, m1)

        b1, b2 = self.bass()

        # s1, s2, s3 = self.synth()

        # d0, d1 = self.drums()


        #   Get ya verses!  #
        #   Intro
        # v1 = combine(m1, b1)

        # v2 = combine(m1, b2) # end of intro
        # v2 = combine(v2, s1)
        # v2 = combine(v2, d0) # add the drums
        v1 = b1
        v2 = b2

        #   Produce ya beat !!  #
        p = build_measure(
            v1, v2,

                          )


        #   Save ya beat.    #
        self.save(p, "intro")

        return p


    def melody(self):
        """
        It's the first one up!
        Plenty more to gooooo!
        Bless the first one up!
        Ya got to feel the groooove!

        I write to sing along
        To catchy beats I maaaaaaake!
        I sing to get you out
        That nasty mood you haaaaaate!



        Man I said goodbye to my tv,
        I can't make money watching kids be dreary,
        The rich get richer so the poor keep dreaming,
        The man with the money doesn't hear you screaming.

        Please let me just make art alone,



        """

        #   Instras #
        f1, f2, f3 = self.funk()
        s1 = self.synth2()

        
        #   Verses  #
        v1 = combine(f1, self.metronome(4))

        v2 = combine(f2, self.metronome(4))

        v3 = combine(f3, self.metronome(4))
        v3 = combine(v3, s1) # Add synth2

        v4 = None   # V4 is V3 1 or 2 pitches lower

        #   Prod    #
        p = build_measure(v1, v2,
                          v3, v3,
                          v1, v2,
                          v3, v3,
                          # Here, go down 1 or 2 pitches on V3   #
                          )


        #   Sav #
        self.save(p, "melody")

        return p

    def test(self):
        a, b, c = self.synth()

        p = build_measure(a, b, c, c, a, a, b, a, b, a, b)

        self.save(p, "Test")

def main():
    First(62).intro()
    #First(62).produce()
    #First(62).melody()