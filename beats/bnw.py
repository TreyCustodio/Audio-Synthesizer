from beat import *

class BNW(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    

    def drums(self):
        """8 Beats per measure"""

        d = Snare(1, self.whole, "2")

        #   Variant 1 (V1)  #
        m1 = build_measure(d.q_a, d.q_f, d.q_a, d.e_f, d.q_g,
                           d.q_a, d.e_f, d.e_a, d.e_a, d.q_g,)
        
        m2 = build_measure(d.q_a, d.q_f, d.q_a, d.e_f, d.q_e,
                           d.q_a, d.e_f, d.e_a, d.e_a, d.q_g,)
        
        v1 = build_measure(m1, m2) * 1.2



        #   Variant 2 (V2)  #
        m2 = build_measure(d.q_a, d.q_f, d.q_a, d.e_f, d.q_e,
                           d.q_a, d.e_f, d.e_g, d.e_g, d.q_a,)
        
        v2 = build_measure(m1, m2) * 1.2
        
        return v1, v2
    
    def skirts(self):
        """8 Beats per measure"""
        
        s = Skirt(3, self.whole)

        #   Variant 1   (V1)    #
        m1 = build_measure(s.e_e, s.e_e, s.q_b,
                           s.e_e, s.q_b,
                           s.e_e, s.q_b,
                           s.q_e)

        return m1

    def keys_bass(self):
        """8 Beats per measure"""

        k1 = SpaceSynth(1, self.whole)
        k2 = SpaceSynth(1, self.whole, "bass")
        k3 = SpaceSynth(2, self.whole)

        # D, E, F, G, A

        #   Variant 1 (V1)    #
        m1_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_g,
                             k1.q_a, k1.e_f, k1.q_a, k1.q_g)
        
        m1_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_d,
                             k1.q_d, k1.e_d, k1.q_d, k1.q_d)
        
        
        
        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, k1.q_g, k1.q_a)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.q_d, k1.q_d)
        
        
        m1 = m1_t + m1_b

        m2 = m2_t + m2_b

        v1 = build_measure(m1, m2)
        v1 = fade_in(v1, 6)



        #   Variant 2 (V2)    #
        m1_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_g,
                             k1.q_a, 
                             k1.e_f, k1.e_a,#foo(self.quarter),#k1.create_slur(F3, A3, self.quarter),
                             #k1.e_f, k1.e_a, 
                             k1.e_a, 
                             k1.q_g)
        
        m1_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_d,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)

        
        
        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, 
                             k1.e_g, k1.e_g, k1.q_a)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)
        
        m1 = m1_t + m1_b

        m2 = m2_t + m2_b

        v2 = build_measure(m1, m2)


        #   Variant 3   (V3)    #
        ##  Slight change on measure 2,
        ##  high pitch for "thattaway"


        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, k1.e_a, k1.e_a, k1.q_g)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)
        

        m2 = m2_t + m2_b

        v3 = build_measure(m1, m2)
        
        
        #   Variant 4   (V4)    #
        # A, G, F, E, D, F, G
        # A, G, F, E, D, F, E, D


        m1  = build_measure(k1.q_a, k1.q_g, k1.q_f, k1.q_e, k1.q_d, k1.e_f, k1.h_g, rest(self.eighth),
                            k1.q_a, k1.q_g, k1.q_f, k1.q_e, k1.q_d, k1.e_f, k1.h_d, rest(self.eighth))
        
        #m1 = build_measure(k1.create_slur(A3, G3, self.half)
#)



        m2 = build_measure(k3.w2_d, k3.w2_d)
        
        v4 = m1 + m2


        #   Variant 5 (V5)    #
        m1 = build_measure(k1.q_a, k1.q_f, k1.create_note(E3, self.quarter+self.eighth), #3.5  #rest(self.eighth),
                          k1.q_a, k1.q_f, k1.e_f, k1.h_e) # 4.5 + 3.5 = 8
        
        m2  =build_measure(k1.q_a, k1.q_f, k1.create_note(E3, self.quarter+self.eighth), #rest(self.eighth),
                           k1.q_a, k1.q_g, k1.e_f, k1.h_a)
        
        m1d = build_measure(k1.q_d, k1.q_d, k1.create_note(C3, self.quarter+self.eighth), #rest(self.eighth),
                            k1.q_d, k1.q_d, k1.e_d, k1.h_c)
        
        m2d = build_measure(k1.q_d, k1.q_d, k1.create_note(C3, self.quarter+self.eighth), #rest(self.eighth),
                            k1.q_d, k1.q_d, k1.e_d, k1.h_e)
        
        m1 += m1d
        m2 += m2d
        v5 = build_measure(m1, m2)


        #   Amplification   #
        amp = 0.25
        #v1 *= amp
        v2 *= amp
        v3 *= amp
        v4 *= amp
        v5 *= amp

        return v1, v2, v3, v4, v5
    

    def keys(self):
        """8 Beats per measure"""

        k1 = SpaceSynth(3, self.whole)
        k2 = SpaceSynth(2, self.whole)
        k3 = SpaceSynth(4, self.whole)

        # D, E, F, G, A

        #   Variant 1 (V1)    #
        m1_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_g,
                             k1.q_a, k1.e_f, k1.q_a, k1.q_g)
        
        m1_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_d,
                             k1.q_d, k1.e_d, k1.q_d, k1.q_d)
        
        
        
        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, k1.q_g, k1.q_a)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.q_d, k1.q_d)
        
        
        m1 = m1_t + m1_b

        m2 = m2_t + m2_b

        v1 = build_measure(m1, m2)
        v1 = fade_in(v1, 6)



        #   Variant 2 (V2)    #
        m1_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_g,
                             k1.q_a, 
                             k1.e_f, k1.e_a,#foo(self.quarter),#k1.create_slur(F3, A3, self.quarter),
                             #k1.e_f, k1.e_a, 
                             k1.e_a, 
                             k1.q_g)
        
        m1_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_d,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)

        
        
        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, 
                             k1.e_g, k1.e_g, k1.q_a)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)
        
        m1 = m1_t + m1_b

        m2 = m2_t + m2_b

        v2 = build_measure(m1, m2)


        #   Variant 3   (V3)    #
        ##  Slight change on measure 2,
        ##  high pitch for "thattaway"


        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, k1.e_a, k1.e_a, k1.q_g)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)
        

        m2 = m2_t + m2_b

        v3 = build_measure(m1, m2)
        
        
        #   Variant 4   (V4)    #
        # A, G, F, E, D, F, G
        # A, G, F, E, D, F, E, D


        m1  = build_measure(k1.q_a, k1.q_g, k1.q_f, k1.q_e, k1.q_d, k1.e_f, k1.h_g, rest(self.eighth),
                            k1.q_a, k1.q_g, k1.q_f, k1.q_e, k1.q_d, k1.e_f, k1.h_d, rest(self.eighth))
        
        #m1 = build_measure(k1.create_slur(A3, G3, self.half)
#)



        m2 = build_measure(k3.w2_d, k3.w2_d)
        
        v4 = m1 + m2


        #   Variant 5 (V5)    #
        m1 = build_measure(k1.q_a, k1.q_f, k1.create_note(E3, self.quarter+self.eighth), #3.5  #rest(self.eighth),
                          k1.q_a, k1.q_f, k1.e_f, k1.h_e) # 4.5 + 3.5 = 8
        
        m2  =build_measure(k1.q_a, k1.q_f, k1.create_note(E3, self.quarter+self.eighth), #rest(self.eighth),
                           k1.q_a, k1.q_g, k1.e_f, k1.h_a)
        
        m1d = build_measure(k1.q_d, k1.q_d, k1.create_note(C3, self.quarter+self.eighth), #rest(self.eighth),
                            k1.q_d, k1.q_d, k1.e_d, k1.h_c)
        
        m2d = build_measure(k1.q_d, k1.q_d, k1.create_note(C3, self.quarter+self.eighth), #rest(self.eighth),
                            k1.q_d, k1.q_d, k1.e_d, k1.h_e)
        
        m1 += m1d
        m2 += m2d
        v5 = build_measure(m1, m2)


        #   Amplification   #
        amp = 0.25
        #v1 *= amp
        v2 *= amp
        v3 *= amp
        v4 *= amp
        v5 *= amp

        return v1, v2, v3, v4, v5
    

    def synth(self):
        k1 = SpaceSynth(3, self.whole, "bass")
        k2 = SpaceSynth(4, self.whole, "bass")

        

        #   Variant 1   (V1)    #
        m1_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_g,
                             k1.q_a, k1.e_f, k1.e_a, k1.e_a, k1.q_g)
        
        m1_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_d,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)

        
        
        m2_t = build_measure(k1.q_a, k1.q_f, k1.q_a, k1.e_f, k1.q_e,
                             k1.q_a, k1.e_f, k1.e_g, k1.e_g, k1.q_a)
        
        m2_b = build_measure(k1.q_d, k1.q_d, k1.q_d, k1.e_d, k1.q_c,
                             k1.q_d, k1.e_d, k1.e_d, k1.e_d, k1.q_d)
        
        m1 = m1_t + m1_b

        m2 = m2_t + m2_b

        v1 = build_measure(m1, m2)
        v1 = fade_out(v1, 4)


        #   Variant 2 (V2)  #
        note  = delaycombo(k1.h_a, k1.w_f, self.quarter)
        note2  = delaycombo(k1.h_e, k1.w_c, self.quarter)

        m1 = build_measure(k1.t_g, k1.e_a, rest(self.sixteenth), #k1.h_a, k1.w_f,
                           note
                           )
        m1d = build_measure(k1.t_d, k1.e_e,  rest(self.sixteenth), #k1.h_e, k1.w_c
                            note2
                            )
        
        
        v2 = m1 + m1d
        return v1, v2


    def percussion(self):
        p = Percussion(3, self.whole)

        return build_measure(p.q_a, p.q_g, p.q_f)
    

    def produce(self):
        k1, k2, k3, k4, k5 = self.keys()
        kb1, kb2, kb3, kb4, kb5 = self.keys_bass()

        k1 += kb1
        k2 += kb2
        k3 += kb3
        k4 += kb4
        k5 += kb5

        d1, d2 = self.drums()
        sk1 = self.skirts()
        s1, s2 = self.synth()
        # save(s2, "bnw", "synth")
        # return
        

        k2b = combine(k2, s1)

        v1 = combine(k3, d1)
        v1b = combine(k2b, d1)

        v2 = combine(k2, d2)

        v3 = s2

        production = build_measure(
                                   #    Intro; no Drums #
                                   k1, k2,

                                   #    Main Melody
                                   v1, v2,
                                   v1, v2,

                                   #    Hook
                                   #v3, v3, v3, v3,

                                   #   Bridge  #
                                   k5, k5,
                                   #k4, k4,

                                   v1, v1
                                    )

        save(production, "bnw", "Black and White")



def main():
    BNW(70).produce()