from beat import *

class Yank(Beat):
    """
    A minimalist beat with an emphasis on bass and percussion.
    No melody, my voice will provide it.
    """

    def __init__(self, bpm):
        super().__init__(bpm)
    

    def piano(self):
        b = XyloTech(3, self.whole)

        #   This ain't a bad rhythm but I'm changing it #
        m2 = build_measure(b.q_e, # 1
                           b.e_d, b.e_d, # 2
                           b.q_e, rest(self.eighth), #3.5
                           b.e_d, # 4
                           b.q_e, # 5
                           b.e_d, b.e_c, # 6
                            b.e_d, # 7
                            delaycombo(b.q_e, b.e_c, self.eighth), # 8
                            b.e_c
                            )
        
        m1 = build_measure(b.q_e, 
                           b.e_c, b.e_c,
                           b.q_d, 
                           rest(self.eighth), #3.5
                           b.e_c, b.e_e,
                           b.e_c, b.e_c,
                            b.e_c, b.e_c, 
                            b.q_d, rest(self.eighth))


        #   Build Verses    #
        v1 = build_measure(m1, m2, m1, m2,
                           m1, m2, m1, m2)
        
        
        #   Return Verses   #
        return v1
    
    def bass(self):
        #   Generate Instruments    #
        b = PianoBass(1, self.whole, "4")
        b1 = PianoBass(2, self.whole, "4")


        #   Build Measures  #
        m0 = build_measure(b.q_b, b.q_b * 0.5)


        m1 = build_measure(b.q_b, b.q_b, 
                           b1.q_cs, b.e_a, b.q_b,
                           b.e_a, b.q_b,
                           b1.q_cs,
                           )

        m2 = build_measure(b.e_a, b.q_b,
                           b.e_a, b.q_b,
                           b1.q_cs,)

        m3 = build_measure(b.e_a, b.q_b,
                           b.e_a, b.q_b,
                           b1.q_cs, b1.q_cs)
        
        ##  Cut off
        m4 = build_measure(b.e_a, b.q_b,
                           b.e_a, b.q_b,
                           )


        #m4 = build_measure(b.q_b, b.q_b)
        #   Build Verses    #
        v0 = build_measure(m0, rest(self.whole + self.half))
        v1 = build_measure(m1, m2, m3,
                           m1, m2, m3,)
        
        #v2 = build_measure(delaycombo(b.w_b, b.w_b, self.whole)) * 0.5
        v2 = build_measure(fade_out(b.w2_b, 6)) * 0.5

        ##  Quick cutoff for bridge
        v3 = build_measure(m1, m2, m3,
                           m1, m2, m4,)

        #   Return Verses   #
        return v0, v1, v2, v3
    


    def xylos(self):
        x = XyloTech(6, self.whole)

        #   No slur at top  #
        m1 = build_measure(x.q_a, delaycombo(x.q_g, x.q_a, self.eighth), 
                           x.e_g, x.q_a, x.q_a) * 0.1
        
        #   With slur at top    #
        m1a = build_measure(delaycombo(x.q_a, delaycombo(x.q_g, x.q_a, self.eighth), self.eighth), 
                           x.e_g, x.q_a, x.q_a,
                           rest(self.eighth)) * 0.1

        #   No slur at top  #
        m2 = build_measure(x.q_e, delaycombo(x.q_d, x.q_c, self.eighth),
                           delaycombo(x.q_c, x.q_d, self.eighth), x.q_e) * 0.1
        
        #   Slur at top #
        m2a = build_measure(delaycombo(x.q_e, delaycombo(x.q_d, x.q_c, self.eighth), self.eighth),
                           delaycombo(x.q_c, x.q_d, self.eighth), x.q_e) * 0.1
        



        #   1 slurs, 2 slurs
        v1 = build_measure(m1a, rest(self.whole *2 + self.trey), m2a)

        #   1 does not, 2 slurs
        v2 = build_measure(m1, rest(self.whole *2 + self.trey), m2a)

        # 1 Slurs, 2 Does not
        v3 = build_measure(m1a, rest(self.whole *2 + self.trey), m2)

        #   No slurs
        v4 = build_measure(m1, rest(self.whole *2 + self.trey), m2)

        v5 = build_measure(x.e_c, x.e_c, x.e_c, rest(self.eighth)) * 0.3
        
        return v1, v2, v3 ,v4, v5
    
    def drums(self):
        s = Skirt(3, self.whole)
        d = Snare(2, self.whole, "2")
        p = Pluck(3, self.whole, "2")
        c = Symbol(3, self.whole)
        b = Bass(1, self.whole, "h")

        

        m1 = build_measure(d.q_b * 0.5, d.q_b * 0.5, 
                           s.e_b, s.e_e, 
                           d.e_e, d.e_e, 
                           s.e_e, rest(self.half + self.eighth),
                           d.e_b, d.e_b,
                           )
        
        m1a = build_measure(d.q_b * 0.5, d.q_b * 0.5,
                           s.e_b, s.e_e, 
                           d.e_e, d.e_e, 
                           s.e_e, rest(self.half),
                           d.e_b, d.e_b, d.e_b,
                           )
        
        m2 = build_measure(rest(self.half), 
                           s.e_b, s.e_e, 
                           s.e_e, s.s_e, 
                           s.e_e, rest(self.half - self.sixteenth),
                           s.q_b, s.q_b
                           )
        
        #   For Verse 2
        m3 = highpass(build_measure(c.q_c, c.q_c, c.q_c, c.q_c,), 5000)
        m4 = build_measure(c.q_c, c.q_c, c.q_c, c.q_c,)

        #   Bridge
        m5 = m3[:len(m3)//2]
        #m5 = highpass(build_measure(c.q_c, c.q_c,), 5000)
        m6 = build_measure(c.q_c, c.q_c,)


        #   For Intro pt 2
        #m7 = flatten(build_measure(b.q_e, b.q_e, b.q_e, b.q_e), 6.0) * 0.2
        m7 = build_measure(b.q_e, b.q_e, b.q_e, b.q_e) * 0.075


        v2 = build_measure(m3, m3, m3, m3,
                           m3, m3, m3, m3,)
        
        v3 = build_measure(m4, m4, m4, m4,
                           m3, m3, m3, m4)
        
        v4 = build_measure(m3, m3, m3, m3,
                           m3, m3, m3, m5)
        
        i2 = build_measure(m7, m7
                           )
        h1 = m7
        
        return m1, m1a, m2, v2, v3, v4, h1, i2
    
    def intro(self):
        b0, _, b2, _ = self.bass()
        d0, d0a, _, _, _, _, _, d6 = self.drums()


        #   Intro Sections
        v0 = combine(b0, d0)
        v0 = combine(v0, b2)
        v0b = combine(v0, d6) ## Bass added

        v0a = combine(b0, d0a)
        v0a = combine(v0a, b2)
        v0ab = combine(v0a, d6) ##  Bass added


    def produce(self):
        d0, d0a, d1, d2, d3, d4, d5, d6 = self.drums()
        x1, x2, x3, x4, x5 = self.xylos()
        b0, b1, b2, b3 = self.bass()
        p = self.piano()


        #   Intro Sections
        v0 = combine(b0, d0)
        v0 = combine(v0, b2)
        v0b = combine(v0, d6) ## Bass added

        v0a = combine(b0, d0a)
        v0a = combine(v0a, b2)
        v0ab = combine(v0a, d6) ##  Bass added

        v1 = combine(b1, x1)

        v2 = combine(b1, x2)


        ##  Drums kick in
        v3 = combine(b1, x1) ## Drums are quiet
        v4 = combine(v3, d3) ## Drums are loud
        v3 = combine(v3, d2)

        ##  Bridge = abrupt cutoff leading into xylo solo
        bridge1 = combine(b3, d4)



        intro1 = build_measure(v0,v0,v0a,v0)
        intro2 = build_measure(v0b,v0b,v0ab,v0b,v0ab, rest(self.whole*2 + self.half))

        hook1 = build_measure(v0, v0, v0a, v0)
        hook1 = combine(hook1, d5)


        production = build_measure(
                        intro1,
                        intro2,

                        hook1,

                        v1, v2, # She a vengeful girl
                        bridge1, x5, v4, v4, v4  # Main 
                        )

        save(production, "yank", "yank-that")


def main():
    #b = Bass(1, get_measure(165), "h")
    #save(shrink((build_measure(b.q_e, b.q_e, b.q_e, b.q_e)), 7.0, 0.0), "yank", "bass")

    Yank(165).produce()
