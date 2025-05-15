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

        m1 = build_measure(f.q_d, # 1
                           f.e_d, f.s_e, # 1.75
                           f.e_f, f.e_g, # 2.75
                           f.e_a, # 3.25
                           rest(self.sixteenth * 3),
                           )
        
        m2 = build_measure(f.e_d, f.s_e, # .75
                           f.e_f, f.e_g, # 1.75
                           f.e_a, # 2.25
                           f.q_g, # 3.25
                           rest(self.sixteenth *3)
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
                           f.q_f, rest(self.sixteenth * 3)
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
                           f.q_g, #4
                           )
        
        m7 = build_measure(rest(self.sixteenth * 4), f.s_c, # 1
                            f.e_c, f.s_d, # 2
                            f.e_e, f.e_f, # 3
                            f.e_g, 
                            rest(self.sixteenth * 2),
                            )

        m8 = build_measure(rest(self.sixteenth), f.e_c, f.s_d,
                           f.e_e, f.e_f,
                           f.q_g,
                           f.q_f)
       
       
        
        v1 = build_measure(m1, m2, m3, m4)

        v2 = build_measure(m5, m6, m7, m8)

        return v1, v2
    

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

        b1, b2, b3 = self.bass()

        s1, s2, s3 = self.synth()

        d0, d1 = self.drums()


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
        f1, f2 = self.funk()
        b1, b2 = self.bass2()

        
        #   Verses  #
        v1 = combine(f1, b1)
        v1 = combine(v1, self.metronome(4))

        v2 = combine(f2, self.metronome(4))
        v2 = combine(v2, b1)

        #   Prod    #
        p = build_measure(v1, v2, v1, v2)


        #   Sav #
        self.save(p, "melody")

        return p

    def test(self):
        a, b, c = self.synth()

        p = build_measure(a, b, c, c, a, a, b, a, b, a, b)

        self.save(p, "Test")

def main():
    #First(60).test()
    #First(62).produce()
    First(62).melody()