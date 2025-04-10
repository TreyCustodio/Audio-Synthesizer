from beat import *

class Rage(Beat):
    def __init__(self):
        super().__init__(170)


    def drumsB(self):
        b = Bass(1, self.whole)
        #b1 = Bass(0, self.whole)

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
        

        m7 = build_measure(b.s_e, rest(self.sixteenth), b.e_e,
                           rest(self.eighth), b.e_e,
                           b.q_a,
                           rest(self.eighth), b.e_e) * amplifier
        
        v1 = build_measure(m1, m4, m1, m2,
                           m1, m2, m1, m6)
        
        v2 = build_measure(m7, m7, m7, m7,
                           m7, m7, m7, m7)
        
        v1 = lowpass(v1, 15435)
        return v1, v2
    

    def drums(self):
        b = Bass(1, self.whole)
        b1 = Bass(0, self.whole)
        s = Skirt(3, self.whole)

        amplifier = 16.0

        m0 = build_measure(rest(self.whole * 20 - (self.quarter)),
                           s.e_a, s.e_d) * amplifier
        
        m1 = build_measure(s.e_a, s.e_g,
                           s.e_f, rest(self.eighth),
                           s.e_a, rest(self.eighth),
                           s.e_g, s.e_a,
                           ) * amplifier
        
        m2 = build_measure(s.e_c, 
                           rest(self.eighth), s.e_c,
                           rest(self.quarter),
                           rest(self.quarter + self.eighth)) * amplifier
        
        m3 = build_measure(rest(self.eighth), s.e_c, 
                           rest(self.eighth), s.e_c,
                           s.e_c, s.e_c,
                           s.e_c, s.e_c,) * amplifier
        
        m4 = build_measure(rest(self.eighth), s.e_c, 
                           rest(self.eighth), s.e_c,
                           rest(self.quarter),
                           rest(self.quarter)) * amplifier
        #   (V1)


        v1 = build_measure(m1, m3, m1, m4,
                           m1, m2, m1, m3)
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
        
        ##
        m3 = build_measure(combine(n.q_e, n.s_d), n.q_d,
                           rest(self.half),
                           )
        
        m4 = build_measure(combine(n.q_fs, n.s_e), n.q_d,
                           rest(self.half))
        
        m5 = build_measure(combine(n.q_f, n.s_ds), n.q_d,
                           rest(self.quarter + self.eighth),
                           )
        
        m6 = build_measure(n.e_d, n.e_c,
                           n.e_d, n.e_d,
                           
                           rest(self.eighth), n.e_d,
                           rest(self.half - self.eighth))
        
        m7 = build_measure(combine(n.q_f, n.s_ds), n.q_d,
                           rest(self.eighth), n.q_d
                           )
        ##

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
        
        ##
        m3 = build_measure(n.q_d,
                            #delaycombo(n.q_d, n.s_d, self.sixteenth),
                            n.q_d,
                           rest(self.half),
                           )
        
        m4 = build_measure(n.q_e,
            #delaycombo(n.q_e, n.s_ds, self.sixteenth), 
                           n.q_d,
                           rest(self.half))
        
        m5 = build_measure(n.q_f,
            #delaycombo(n.q_f, n.s_c, self.sixteenth),
                           n.q_d,
                           rest(self.eighth + self.quarter)
                           )
        
        m6 = build_measure(slur(n.e_d, n.e_c, n),#combine(makeSilent(n.q_c), n.e_d),
            #n.e_d, n.e_c,
                           n.e_d, n.e_d,
                           rest(self.eighth), n.e_d,
                           rest(self.half - self.eighth))
        
        m7 = build_measure(n.q_f,
            #delaycombo(n.q_e, n.s_d, self.sixteenth),
                           n.q_d,
                           rest(self.eighth), n.q_d
                           )
        ##
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
    
    def xylos(self):
        n = XyloHorn(5, self.whole, "2")
        amplifier = 19.0


        m1 = build_measure(n.e_a, n.e_f,
                           n.e_d,
                           n.q_g,
                           n.q_a, rest(self.eighth)) * amplifier
        
        m2 = build_measure(n.e_d, n.e_c,
                           n.e_d,
                           n.q_f,
                           n.q_d,
                           rest(self.eighth)) * amplifier
        
        ##  Half a measure!
        m3 = build_measure(n.e_d, n.e_c,
                           n.e_d,
                           n.q_f,
                           n.q_d,
                           n.e_d, n.e_d,
                           n.e_d, n.e_d,
                           n.e_d,
                           ) * amplifier
        
        v1 = build_measure(rest(self.half), m1, rest(self.whole), m2, rest(self.half),
                           rest(self.half), m1, rest(self.whole), m2, rest(self.half))

        v2 = build_measure(rest(self.half), m1, rest(self.whole), m2, rest(self.half),
                           rest(self.half), m1, rest(self.whole), m3)
        return v1, v2

    def produce(self):
        #   Gather Instruments
        db1, db2 = self.drumsB()
        d0, d1 = self.drums()
        pb0, pb00, pb1, pb2 = self.pianoB()
        p0, p1, p2 = self.piano()
        x1, x2 = self.xylos()

        ##  Harmonic Combinations
        ##  Initial saving of piano before adding bass
        save(p0, "rage", "piano0")
        save(p1, "rage", "piano1")
        save(p2, "rage", "piano2")

        p0 += pb0
        p1 = combine(p1, pb1)#p1 += pb1
        p2 += pb2

        d1 = combine(d1, db1)#combine(d1, db1)

        #   Combine the Instruments into Verses
        intro = build_measure(pb00, pb0, p0, p1)
        intro = combine(intro, d0)
        
        v1 = combine(p1, d1)
        v2 = combine(p2, d1)
        
        v3 = combine(pb1 * 3.0, d1)
        v3 = combine(v3, x1)
        v4 = combine(pb2 * 3.0, d1)
        v4 = combine(v4, x2)


        #   Build the final production
        production = build_measure(intro,
                                   v1, v2,
                                   v3, v4,
                                
                                #   Switch up drum beat
                                   v1, v2,
                                   v3, v4,

                                #   Quota
                                   v1, v2,
                                   d1 * 1.5)

        save(production, "rage", "production")

        #   Save all the instruments seperately
        save(d0, "rage", "drums0")
        save(d1, "rage", "drums1")

        # save(p0, "rage", "piano0")
        # save(p1, "rage", "piano1")
        # save(p2, "rage", "piano2")

        save(pb0, "rage", "bassPiano0")
        save(pb00, "rage", "bassPiano00")
        save(pb1, "rage", "bassPiano1")
        save(pb2, "rage", "bassPiano2")

        save(x1, "rage", "xylos1")
        save(x2, "rage", "xylos2")
        




def main():
    Rage().produce()