from beat import *

class Unknown(Beat):
    def __init__(self):
        super().__init__(155)

    def drums(self):
        n = Snare(3, self.whole)
        s = Skirt(3, self.whole)
        sa = Skirt(4, self.whole)
        b = Bass(1, self.whole)

        amplifier = 1.5
        skamplifier = 1.5

        #   (V1)    #
        m0 = build_measure(s.q_c, # 1
                           s.e_c, rest(self.eighth), # 2
                           s.e_c, # 2.5
                           s.q_c, # 3.5
                           s.e_c, # 4
                           rest(self.eighth),
                           ) * skamplifier
        
        m00 = build_measure(s.q_c, # 1
                           s.e_c, rest(self.eighth), # 2
                           s.e_c, # 2.5
                           s.e_c, s.e_c,# 3.5
                           s.e_c, # 4
                           rest(self.eighth),
                           ) * skamplifier

        m000 = build_measure(s.q_c, # 1
                           s.e_c, # 2
                           s.s_c, s.s_c, s.e_c,# 3.5
                           s.s_c, s.s_c, s.e_c, # 4
                           rest(self.eighth),
                           s.e_c,
                           ) * skamplifier
        
        m1 = build_measure(s.q_c, # 1
                           s.e_c, rest(self.eighth), # 2
                           s.e_c, # 2.5
                           s.q_c, # 3.5
                           s.e_c, # 4
                           #rest(self.eighth),
                           ) * skamplifier
        
        m2 = build_measure(s.q_c, # 1
                           s.e_c, rest(self.eighth), # 2
                           s.e_c, # 2.5
                           s.q_c, # 3.5
                           s.e_c, # 4
                           #rest(self.eighth),
                           ) * skamplifier
        

        m1q = build_measure(s.q_c, # 1
                           s.e_c, rest(self.eighth), # 2
                           s.e_c, # 2.5
                           s.q_c, # 3.5
                           s.e_c, # 4
                           #rest(self.eighth),
                           )
        
        
        #   Verses  #
        v0 = build_measure(m0, m00, m0, m000,
                           m1, m1, m1, m1)
        
        v1 = build_measure(m1, m1, m1, m1,
                           m1, m1, m1, m1)

        v1q = build_measure(m1q, m1q, m1q, m1q,
                           m1q, m1q, m1q, m1q)
        
        
        return v0, v1, v1q
    

    def piano(self):
        p = PianoTreble(4, self.whole)
        p1 = PianoTreble(5, self.whole)

        b = PianoBass(5, self.whole)

        amplifier = 4.0


        #   Intro   #
        m1 = build_measure(
                           p.s_a, p.s_g, p.s_f, # 1.75
                           p.e_a, rest(self.eighth), # 2.75
                           p.e_b, p1.e_c, # 3.75
                           rest(self.sixteenth), # 4
                           ) * amplifier
        
        m2 = build_measure(rest(self.sixteenth),
                           p.e_d, rest(self.eighth), # 1.25
                           p.e_a, p.e_b, # 2.25
                           p.e_c, p.e_a, # 3.25
                           rest(self.sixteenth * 3)
                           ) * amplifier
        
        m3 = build_measure( rest(self.sixteenth), 
                            p.e_g, rest(self.eighth), # 1.25
                           p.e_g, rest(self.eighth), # 2.25
                           p.e_a, p.e_b, # 3.25
                           p1.e_c, # 3.75
                           ) * amplifier
        
        m4 = build_measure(
                           p.e_d, rest(self.eighth), # 1
                           p.e_a, p.e_b, # 2
                           p.e_c, p.e_a, rest(self.eighth), # 3
                           p.e_a, # 3.5
                           rest(self.eighth)
                           ) * amplifier
        
        #   (V1)    #
        ##  (V1) - Top Half ##
        m5 = build_measure(
                           p.e_g, rest(self.eighth),
                           p.e_g, rest(self.eighth),
                           p.e_a, p.e_b,
                           p1.e_c, p.e_d,
                           ) * amplifier
        
        m6 = build_measure(
                           rest(self.eighth), p.e_a, 
                           p.e_b, p.e_c,
                           p.e_a, rest(self.eighth), 
                           p.e_a, rest(self.eighth)
                           ) * amplifier

        m7 = build_measure(
                            p.e_g, rest(self.eighth), # 1
                           p.e_g, rest(self.eighth), # 2
                           p.e_a, p.e_b, # 3
                           p1.e_c, p.e_d,
                           ) * amplifier
        
        m8 = build_measure(
                           rest(self.eighth), p.e_a,
                           p.e_b, p.e_c,
                           p.e_a, rest(self.eighth),
                           p.e_a, rest(self.eighth)
                           ) * amplifier
        
        ##  (V1) - Bottom Half  ##
        m9 = build_measure(
                           p.e_g, p.e_f,
                           p.e_g, rest(self.eighth),
                           p.e_a, p.e_b,
                           p1.e_c, p.e_d,
                           ) * amplifier

        m11 = build_measure(
                            p.e_f, p.e_g, # 1
                           p.e_a, rest(self.eighth), # 2
                           p.e_a, p.e_b, # 3
                           p1.e_c, p.e_d,
                           ) * amplifier


        #   (V2) - The Bass #
        m13 = build_measure(b.e_g, rest(self.eighth),
                            b.e_g, rest(self.eighth),
                            b.e_g, rest(self.eighth),
                            b.e_g, b.e_a)
        
        m14 = build_measure(
                            rest(self.eighth), b.e_a,
                            b.e_g, rest(self.eighth),
                            b.e_a, b.e_g,
                            rest(self.quarter))

        m15 = build_measure(b.e_g, rest(self.eighth),
                            b.e_g, rest(self.eighth),
                            b.e_g, rest(self.eighth),
                            b.e_g, b.e_f)
        
        m16 = build_measure(
                            rest(self.eighth), b.e_g,
                            b.e_f, rest(self.eighth),
                            b.e_f, rest(self.eighth),
                            b.e_a, rest(self.eighth))
        
        m17 = build_measure(
                            rest(self.eighth), b.e_a,
                            b.e_g, rest(self.eighth),
                            rest(self.half))
        
        m18 = build_measure( rest(self.half),
                            b.e_g, b.e_f,
                            b.e_f, b.e_a)

        #   Verse Construction  #
        v0 = build_measure(m1, m2, m3, m4)
        v00 = build_measure(m5, m6, m7, m8)

        v1 = build_measure(m5, m6, m7, m8,
                           m9, m6, m11, m8)

        v2 = build_measure(rest(self.whole*4),
                           m13, m14, m15, m16,
                           )
        
        v3 = build_measure(rest(self.whole), m18, m15, m16,
                           m13, m17, rest(self.whole), m18,)
        
        v4 = add_waves(v3, b.q_g)
        return v0, v00, v1, v2, v3, v4
    
    def plucks(self):
        p = Piano(4, self.whole,)
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
        x0 = XyloBass(4, self.whole)
        x = XyloBass(3, self.whole,)
        x1 = XyloBass(2, self.whole,)
        x2 = XyloBass(1, self.whole,)

        x3 = XyloBass(5, self.whole,)

        p = PianoTreble(3, self.whole)
        p1 = PianoTreble(2, self.whole)

        amplifier = 3.3
        amplifier2 = 3.9
        amplifier3 = 4.3


        #   Intro   #
        m0 = build_measure(
                           rest(self.quarter + self.eighth),
                           x1.q_e + p.q_e,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier
        
        m00 = build_measure(rest(self.quarter),
                           x2.e_b + p1.e_b,  x1.q_c + p.q_c,
                           rest(self.whole - (self.quarter + self.quarter + self.eighth))) * amplifier
        
        
        #   (V1)    #
        ##  Top Half
        m1 = build_measure(
                           x.e_g, rest(self.eighth),
                           x.e_g, rest(self.eighth),
                           x.e_a, x.e_b,
                           x0.e_c, x.e_d,
                           ) * amplifier
        
        m2 = build_measure(
                           rest(self.eighth), x.e_a, 
                           x.e_b, x.e_c,
                           x.e_a, rest(self.eighth), 
                           x.e_a, rest(self.eighth)
                           ) * amplifier

        m3 = build_measure(
                            x.e_g, x.e_f, # 1
                           x.e_g, rest(self.eighth), # 2
                           x.e_a, x.e_b, # 3
                           x1.e_c, x.e_d,
                           ) * amplifier
        
        m4 = build_measure(
                           rest(self.eighth), x.e_a,
                           x.e_b, x.e_c,
                           x.e_a, rest(self.eighth),
                           x.e_a, rest(self.eighth)
                           ) * amplifier

        ##  Bottom Half
        m5 = build_measure(
                           x.e_g, x.e_f,
                           x.e_g, rest(self.eighth),
                           x.e_a, x.e_b,
                           x0.e_c, x.e_d,
                           ) * amplifier
        
        m6 = build_measure(
                           rest(self.eighth), x.e_a, 
                           x.e_b, x.e_c,
                           x.e_a, rest(self.eighth), 
                           x.e_a, rest(self.eighth)
                           ) * amplifier
        
        m11 = build_measure(
                            x.e_f, x.e_g, # 1
                           x.e_a, rest(self.eighth), # 2
                           x.e_a, x.e_b, # 3
                           x1.e_c, x.e_d,
                           ) * amplifier



        #   Verse Construction  #
        v0 = build_measure(m0, m0, m0, m0,
                           m00, m00, m00, m00, rest(self.whole))
        
        v00 = build_measure(m1, m2, m3, m4)

        v1 = build_measure(m1, m2, m3, m4,
                           m5, m6, m11, m4,)
        
        v2 = build_measure(m0, m0, m0, m0,
                           m00, m00, m00, m00)
        
        return v0, v00, v1, v2

    
    def produce(self, amplitude=1.0, noIntro=False):
        #   Gather the instruments
        d0, d1, d1q = self.drums()
        x0, x00, x1, x2 = self.xylos()
        k0, k00, k1, k2, k3, k4 = self.piano()


        #   Create the Verses
        ##  Intro
        i0 = x0 # Solo bass at beginning
        i1 = k0 # Solo piano at beginning
        intro = add_waves(i0, i1)
        intro = add_waves(intro, combine(x00, k00))
        #intro = lowpass(intro, 1275)


        ##  Section 1
        v1 = combine(x1, k1)
        v1 = combine(v1, d0)

        v2 = combine(x1, d1)
        v2 = combine(v2, k2)
        
        v3 = combine(x1, k1)
        v3 = combine(v3, d1)
        v3 = combine(v3, x2) # 

        v4 = combine(x1, d1)
        v4 = combine(v4, k3)

        v5 = combine(x2, d1)

        v6 = combine(v5, k2)

        v7 = combine(d1,k3)#= combine(v5, k3)

        v8 = combine(v3, k2 * 4.0)

        v9 = combine(v3, k3 * 4.0)

        v10 = combine(v3, k4 * 4.0)

        ##  Section 2


        #   Create the final production
        if noIntro:
            production = build_measure(
                                
                                #   Section 1
                                v1, v1,

                                v2, v4,

                                v3, v3,

                                v5, v6, v7,

                                v2, v4,

                                v3,
                                v8, v9, v10
                                #   Section 2
                                   )
        else:
            production = build_measure(
                                    #   Intro
                                    intro,
                                    
                                    #   Section 1
                                    v1, v1,

                                    v2, v4,

                                    v3, v3,

                                    v5, v6, v7,

                                    v2, v4,

                                    v3,
                                    v8, v9, v10
                                    #   Section 2
                                    )

        production *= amplitude
        #production = lowpass(production, 13230)
        #   Save the production
        save(production, "unknown", "unknown")


def main(amplitude, noIntro=False):
    Unknown().produce(amplitude, noIntro)