from beat import *

class BlessUp(Song):
    def __init__(self):
        super().__init__(160)

    def drums(self):
        n = Snare(3, self.whole)
        s = Skirt(3, self.whole)
        sa = Skirt(4, self.whole)
        b = Bass(1, self.whole)

        amplifier = 1.5
        skamplifier = 1.0

        #   Section 1   #
        ##   Measure 1
        m1 = build_measure(n.e_a, n.e_a,
                           n.q_a,
                           s.q_b * skamplifier,
                           n.e_a, n.e_a,
                           )
        
        m1b = build_measure(b.e_a, b.e_a,
                           b.q_a,
                           b.q_b,
                           b.e_a, b.e_a
                           )
        
        m1 = combine(m1, m1b)


        ##   Measure 2
        m2 = build_measure(rest(self.eighth),
                           n.e_a, n.e_a,
                           rest(self.eighth),
                           combine(n.q_b, s.q_c * skamplifier), # 3
                           s.q_b * skamplifier,
                           )

        m2b = build_measure(rest(self.eighth),
                           b.e_a, b.e_a,
                           rest(self.eighth),
                           b.q_b, # 3
                           rest(self.quarter)
                           )
        
        m2 = combine(m2, m2b)

        
        ##   Measure 3
        m3 = build_measure(rest(self.eighth),
                           n.e_a, n.e_a,
                           rest(self.eighth),
                           combine(combine(n.q_b, s.q_c * skamplifier), add_waves(rest(self.eighth),s.e_b)), # 3
                           s.e_b * skamplifier, s.e_b * skamplifier,
                           )
        
        m3 = combine(m3, m2)


        #   Section 2   #

        ##  Skirts
        s1 = build_measure(s.e_c, s.e_c,
                           s.e_c, s.e_c,
                           s.e_c, s.e_c,
                           s.e_c, s.e_c,)
        
        s2 = build_measure(rest(self.eighth), s.e_b, 
                           s.e_c, s.e_c,
                           s.e_b, rest(self.eighth),
                           sa.e_b + s.e_b, rest(self.eighth))
        
        s3 = build_measure(rest(self.eighth), s.e_b, 
                           s.e_c, s.e_c,
                           s.e_b, rest(self.eighth),
                           s.s_b, s.s_a, sa.e_b + s.e_b)
        
        ##  Measure 4
        m4 = build_measure(n.q_a, rest(self.eighth),
                           n.e_a, n.q_a, # 3
                           n.e_a, rest(self.eighth))
        
        m4b = build_measure(b.q_a, rest(self.eighth),
                           b.e_a, b.q_a, # 3
                           b.e_a, rest(self.eighth))
        m4 = combine(m4, m4b)
        m4 = combine(m4, s1)

        ##  Measure 5
        m5 = build_measure(rest(self.eighth), n.q_a, n.e_a,
                           n.e_a, n.e_a,
                           n.e_a, n.e_a,
                           )
        m5b = build_measure(rest(self.eighth), b.q_a, b.e_a,
                           b.e_a, b.e_a,
                           b.e_a, b.e_a,
                           )
        m5 = combine(m5, m5b)
        m5 = combine(m5, s2)


        ##  Measure 6
        m6 = build_measure(rest(self.eighth), n.q_a, n.e_a,
                           n.e_a, n.e_a,
                           n.e_a, n.e_a,
                           )
        
        m6b = build_measure(rest(self.eighth), b.q_a, b.e_a,
                           b.e_a, b.e_a,
                           b.e_a, rest(self.eighth),
                           )
        m6 = combine(m6, m6b)
        m6 = combine(m6, s3)



        
        #   Verses  #
        v1 = build_measure(m1, m2, m1, m3,
                           m1, m2, m1, m3) * amplifier

        v2 = build_measure(m4, m5, m4, m6,
                           m4, m5, m4, m6,
                           ) * amplifier

        return v1, v2
    

    def plucks(self):
        p = Pluck(2, self.whole, "2")
        b = Bass(1, self.whole)

        amplifier = 4.0

        #   Measure 0
        m0 = build_measure(p.q_a, p.e_g, rest(self.eighth),) * amplifier
        m0b = build_measure(b.q_a, b.e_g, rest(self.eighth))
        m0 += m0b

        #   Measure 1
        m1 = build_measure(p.q_a, p.e_g, rest(self.eighth), # 2
                           p.e_b, p.e_b, # 3
                           p.e_b, p.e_b, # 4
                           ) * amplifier
        
        m1b = build_measure(
                           b.q_b, b.e_a, rest(self.eighth), # 2
                           b.e_b, b.e_b,
                           b.e_b, b.e_b,
                           )
        m1 += m1b


        #   Measure 2
        m2 = build_measure(p.q_a, p.e_g,
                           rest(self.eighth),
                           p.e_b, p.e_b,
                           p.e_b, p.e_b,
                           ) * amplifier
        
        m2b = build_measure(b.q_a, b.e_g,
                            rest(self.eighth),
                            b.e_b, b.e_b,
                            b.e_b, b.e_b,
                        )
        m2 += m2b
        
        m3 = build_measure(p.q_a, p.e_g, rest(self.eighth), # 2
                           p.q_a, p.e_g, rest(self.eighth),# 4
                           p.h_f, p.h_g, # 7
                           ) * amplifier
        
        m4 = build_measure(p.h_f, p.h_g,) * amplifier

        #   Verse 1
        v1 = build_measure(m1, m2, m1, m3,
                           rest(self.whole), m4, rest(self.whole)
                           )
                           
        
        return m0, v1
    

    def xylos(self):
        x = XyloTech(4, self.whole, "2")
        x1 = XyloTech(3, self.whole, "2")
        x2 = XyloTech(2, self.whole, "2")

        x3 = XyloHorn(5, self.whole, "2")

        amplifier = 1.3
        amplifier2 = 1.9
        amplifier3 = 2.3

        m0 = build_measure(
                           rest(self.quarter + self.eighth),
                           x.q_e,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier
        
        #   (V1)    #
        ##  More Sounds
        m1 = build_measure(x.q_a, x.e_g,
                           x.q_e,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier

        ##  End Bar
        m3 = build_measure(x.q_a, x.e_g, rest(self.eighth),
                           x.q_a, x.e_g, # 3
                           rest(self.eighth))
        m3b = build_measure(x1.q_a, x1.e_g, rest(self.eighth),
                           x1.q_a, x1.e_g, # 3
                           rest(self.eighth))
        m3 += m3b
        

        ##  Cleaner for chorus
        m5 = build_measure(x.q_a, x.e_g,
                           rest(self.quarter),
                           rest(self.whole - (self.quarter + self.quarter + self.eighth)))
        m5b = build_measure(x1.q_a, x1.e_g,
                           rest(self.quarter),
                           rest(self.whole - (self.quarter + self.quarter + self.eighth)))
        m5 += m5b
        
        ##  More Sounds; Deep
        m7 = build_measure(x1.q_a, x1.e_g,
                           x1.q_e,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier2

        ##  End Bar; Deep
        m9 = build_measure(x1.q_a, x1.e_g, rest(self.eighth),
                           x1.q_a, x1.e_g, # 3
                           rest(self.eighth)) * amplifier2
        
        #   (V2)    #
        ##  More Sounds
        m2 = build_measure(rest(self.quarter),
                           x1.s_b, rest(self.sixteenth), x.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier
        
        ##  More Sounds
        m4 = build_measure(rest(self.quarter),
                           x1.e_b,  x.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier
        
        ##  Cleaner for chorus
        m6 = build_measure(rest(self.quarter + self.eighth),
                           x.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier

        ##  More Sounds; Deep
        m8 = build_measure(rest(self.quarter),
                           x2.s_b, rest(self.sixteenth), x1.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier3
        
        ##  More Sounds; Deep
        m10 = build_measure(rest(self.quarter),
                           x2.e_b,  x1.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier3


        #   SECTION 2   #
        m11 = build_measure(x3.q_a, 
                            x3.e_g, rest(self.eighth),
                            x3.e_g, rest(self.eighth),
                            x3.e_f, rest(self.eighth)
                            )
        
        m12 = build_measure(x3.e_a,
                            x3.e_g, rest(self.eighth),
                            x3.e_g, rest(self.eighth),
                            x3.e_f, x3.e_g
                            ) # Lacking an eigth note; make up for it in v4

        m13 = build_measure(x3.q_a,
                            x3.e_g, rest(self.eighth),
                            x3.e_g, rest(self.eighth),
                            x3.e_b, x3.e_a)

        #   Verses
        v0 = build_measure(m0, m0, m0, m0,
                           m4, m2, m4, m2, rest(self.whole * 5))
        
        v00 = build_measure(x.q_a, x.e_g, rest(self.eighth)) + build_measure(x1.q_a, x1.e_g, rest(self.eighth))

        v1 = build_measure(m5, m5, m5, m3,
                           m6, m2, m6, m2)
        
        v2 = build_measure(m7, m7, m7, m9,
                           m10, m8, m10, m8)
        
        v3 = build_measure(m1, m1, m1, m3,
                           m4, m2, m4, m2)
        
        v4 = build_measure(m11, m12, m13, rest(self.whole+ self.eighth),
                           m11, m12, m13, rest(self.whole+ self.eighth),)
        
        v5 = combine(v2, v3) * 0.7
        return v0, v00, v1, v2, v3, v4, v5

    def produce(self):
        #   Gather the instruments
        d1, d2 = self.drums()
        p0, p1 = self.plucks()
        x0, x00, x1, x2, x3, x4, x5 = self.xylos()


        #   Create the Verses
        ##  Intro
        i0 = x0
        i1 = combine(p0, x00)
        intro = add_waves(i0, i1)
        intro = lowpass(intro, 1275)

        ##  Section 1
        v1 = combine(d1, p1)
        v1 = combine(v1, x1)

        v2 = combine(d1, x2)

        v3 = combine(d1, p1)
        v3 = combine(v3, x5)

        ##  Section 2
        v4 = combine(d2, x4)


        #   Create the final production
        production = build_measure(
                                #   Intro
                                   intro,
                                
                                #   Section 1
                                   v1,v1,

                                   v2, v2,

                                   v1, v1,

                                   v2, v2,

                                   v3, v3,
                                
                                #   Section 2
                                   v4
                                   )

        production = lowpass(production, 13230)
        #   Save the production
        save(production, "blessup", "production")


def main():
    BlessUp().produce()