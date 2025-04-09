from beat import *

class Rage(Beat):
    def __init__(self):
        super().__init__(170)


    def drumsB(self):
        b = Bass(1, self.whole)
        b1 = Bass(0, self.whole)

        amplifier = 16.0


        m1 = build_measure(b.q_a, b.q_a,
                           b.q_a, b.e_e, b.e_a
                           ) * amplifier

        m2 = build_measure(rest(self.eighth), b.e_e, # 1
                           rest(self.eighth), b.e_e, # 2
                           rest(self.eighth), # 2.5
                           b.e_a, b.e_c, b.e_c) * amplifier
        
        m4 = build_measure(rest(self.eighth), b.e_e, # 1
                           rest(self.eighth), b.e_e, # 2
                           rest(self.quarter),
                           b.e_a, b.e_c) * amplifier

        m6 = build_measure(rest(self.half),
                           b.e_a, b.e_a, b.e_a, b.e_a) * amplifier
        
        v1 = build_measure(m1, m4, m1, m2,
                           m1, m2, m1, m6)
        
        v1 = lowpass(v1, 13435)
        return v1
    

    def drums(self):
        b = Bass(1, self.whole)
        b1 = Bass(0, self.whole)
        s = Skirt(3, self.whole)

        amplifier = 16.0

        m0 = build_measure(rest(self.whole * 20 - (self.quarter)),
                           s.e_a, s.e_d) * amplifier
        
        m1 = build_measure(s.e_a, s.e_g,
                           s.e_f, rest(self.eighth),
                           s.e_c, rest(self.eighth),
                           s.e_c, s.e_c,
                           ) * amplifier
        
        m2 = build_measure(s.e_c, 
                           rest(self.eighth), s.e_c,
                           rest(self.quarter),
                           rest(self.quarter + self.eighth)) * amplifier
        
        m4 = build_measure(rest(self.eighth), s.e_c, 
                           rest(self.eighth), s.e_c,
                           rest(self.quarter),
                           rest(self.quarter)) * amplifier
        #   (V1)


        v1 = build_measure(m1, m4, m1, m2,
                           m1, m2, m1, m4)
        return m0, v1
    
    def pianoB(self):
        n = PianoBass(2, self.whole)
        b1 = PianoBass(1, self.whole)

        amplifier = 12.0


        m1 = build_measure(n.q_c,
                           n.e_d, n.e_d,
                           n.e_d, rest(self.quarter),
                           n.e_d)
        
        m2 = build_measure(n.e_c, n.e_d,
                           n.e_d, n.e_d, 
                           n.e_d, rest(self.eighth),
                           rest(self.quarter))
        
        m3 = build_measure(combine(n.q_f, n.s_e), n.q_d,
                           rest(self.half),
                           )
        
        m4 = build_measure(combine(n.q_g, n.s_f), n.q_d,
                           rest(self.half))
        
        m5 = build_measure(combine(n.q_f, n.s_e), n.q_d,
                           rest(self.quarter + self.eighth),
                           )
        
        m6 = build_measure(n.e_d, n.e_c,
                           n.e_d, n.e_d,
                           rest(self.eighth), n.e_d,
                           rest(self.half - self.eighth))
        
        m7 = build_measure(combine(n.q_f, n.s_e), n.q_d,
                           rest(self.eighth), n.q_d
                           )
        
        m8 = build_measure(n.e_c, n.e_d,
                           n.e_d, n.e_d, 
                           n.e_d, rest(self.eighth),
                           n.q_f)
        
        m9 = build_measure(n.e_c, n.e_d,
                           n.e_d, rest(self.eighth), 
                           n.e_d, rest(self.eighth),
                           rest(self.quarter))
        
        v0 = build_measure(m1, m2, m1, m9,) * amplifier

        v00 = build_measure(m3, m4, m5, m6,) * amplifier

        v1 = build_measure(m3, m4, m5, m6,
                           m3, m4, m7, m6) * amplifier

        v2 = build_measure(m1, m8, m1, m9,
                           m1, m8, m1, m9,) * amplifier

        return v0, v00, v1, v2

    def piano(self):
        n = PianoBass(6, self.whole, "3")
        n1 = PianoBass(7, self.whole, "2")

        amplifier = 4.5

        m1 = build_measure(n.q_c,
                           n.e_d, n.e_d,
                           n.e_d, rest(self.quarter),
                           n.e_d)
        
        m2 = build_measure(n.e_c, n.e_d,
                           n.e_d, n.e_d, 
                           n.e_d, rest(self.eighth),
                           rest(self.quarter))
        
        m3 = build_measure(delaycombo(n.q_f, n.s_e, self.sixteenth * 2), n.q_d,
                           rest(self.half),
                           )
        
        m4 = build_measure(delaycombo(n.q_g, n.s_f, self.sixteenth*2), n.q_d,
                           rest(self.half))
        
        m5 = build_measure(delaycombo(n.q_f, n.s_e, self.sixteenth * 2), n.q_d,
                           rest(self.quarter + self.eighth),
                           )
        
        m6 = build_measure(n.e_d, n.e_c,
                           n.e_d, n.e_d,
                           rest(self.eighth), n.e_d,
                           rest(self.half - self.eighth))
        
        m7 = build_measure(delaycombo(n.q_f, n.s_e, self.sixteenth * 2), n.q_d,
                           rest(self.eighth), n.q_d
                           )
        
        m8 = build_measure(n.e_c, n.e_d,
                           n.e_d, n.e_d, 
                           n.e_d, rest(self.eighth),
                           n.q_f)
        
        m9 = build_measure(n.e_c, n.e_d,
                           n.e_d, rest(self.eighth), 
                           n.e_d, rest(self.eighth),
                           rest(self.quarter))
        
        v0 = build_measure(m1, m2, m1, m9,) * amplifier

        v1 = build_measure(m3, m4, m5, m6,
                           m3, m4, m7, m6) * amplifier

        v2 = build_measure(m1, m8, m1, m9,
                           m1, m8, m1, m9,) * amplifier

        return v0, v1, v2
    

    def produce(self):
        #   Gather Instruments
        db1 = self.drumsB()
        d0, d1 = self.drums()
        pb0, pb00, pb1, pb2 = self.pianoB()
        p0, p1, p2 = self.piano()

        ##  Harmonic Combinations
        p0 += pb0
        p1 += pb1
        p2 += pb2

        d1 = combine(d1, db1)

        #   Combine the Instruments into Verses
        intro = build_measure(pb00, pb0, p0, p1)
        intro = combine(intro, d0)
        
        v1 = combine(p1, d1)
        v2 = combine(p2, d1)
        
        v3 = combine(pb1 * 2.0, d1)
        v4 = combine(pb2 * 2.0, d1)


        #   Build the final production
        production = build_measure(intro,
                                   v1, v2,
                                   v3, v4,
                                
                                #   Switch up drum beat
                                   v1, v2,
                                   v3, v4)

        save(production, "rage", "production")


def main():
    Rage().produce()