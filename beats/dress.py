from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Dressy(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beats", "dressy"), name)


    def drums(self):
        return 

    def chimes(self):
        n4 = Chime(3, self.whole)
        n3 = Chime(2, self.whole)
        n2 = Chime(1, self.whole)



        m1 = build_measure(rest(self.half),
                           n4.q_c, rest(self.eighth), n4.q_c, rest(self.quarter + self.eighth),
                           rest(self.trey + self.quarter),

                           n4.q_c, rest(self.eighth), n4.q_c, rest(self.quarter + self.eighth),
                           rest(self.trey + self.quarter),

                           n3.q_b, rest(self.eighth), n3.q_b, rest(self.quarter + self.eighth),
                           rest(self.trey + self.quarter),

                           n3.q_b, rest(self.eighth), n3.q_b, rest(self.quarter + self.eighth),
                           rest(self.quarter), n3.q_b, n4.q_c
                           )
        
        m2 = build_measure(n3.w_c, rest(self.quarter),
                           n2.e_g, n2.e_a, rest(self.eighth),
                           n2.q_b,
                           #delaycombo(delaycombo(n2.q_g, n2.q_a, wait), n2.q_b, self.half - self.sixteenth / 2),
                           n3.w_c, rest(self.quarter),

                           n2.e_g, n2.e_a, rest(self.eighth),
                           #delaycombo(n2.q_g, n2.q_a, wait),
                           n3.q_d,
                           n2.w_b, rest(self.quarter),

                           n2.e_g, n2.e_a, rest(self.eighth),
                           n2.q_f,
                           #delaycombo(delaycombo(n2.q_g, n2.q_a, wait), n2.q_f, self.half - self.sixteenth / 2),
                           n2.w_e,
                           n2.w_d,
                           )
        
        return m1, m2



    def keys(self):
        n4 = DressP(4, self.whole)
        n3 = DressP(3, self.whole)

        #wait = self.quarter - (self.sixteenth / 2)
        
        m1 = build_measure(n4.w_c, rest(self.quarter + self.eighth),
                           n3.e_g, n3.e_a, rest(self.quarter),
                           n3.q_b,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_b, self.half - self.sixteenth / 2),
                           n4.w_c, rest(self.quarter + self.eighth),

                           n3.e_g, n3.e_a, rest(self.eighth),
                           #delaycombo(n3.q_g, n3.q_a, wait),
                           n4.q_d,
                           n3.w_b, rest(self.quarter + self.eighth),

                           n3.e_g, n3.e_a, rest(self.eighth),
                           n3.q_f,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_f, self.half - self.sixteenth / 2),
                           n3.w_e,
                           n3.w_d,
                           )

        m2 = build_measure(n3.w_g, rest(self.quarter + self.eighth),
                           n3.e_d, n3.e_e, rest(self.quarter),
                           n3.q_fs,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_b, self.half - self.sixteenth / 2),
                           n3.w_g, rest(self.quarter + self.eighth),

                           n3.e_d, n3.e_e, rest(self.eighth),
                           #delaycombo(n3.q_g, n3.q_a, wait),
                           n3.q_a,
                           n3.w_fs, rest(self.quarter + self.eighth),

                           n3.e_d, n3.e_e, rest(self.eighth),
                           n3.q_c,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_f, self.half - self.sixteenth / 2),
                           n3.create_note(B2, self.whole),
                           n3.create_note(A2, self.whole)
                           )
        
        return combine(m1, m2)

    def piano(self):
        n4 = DressP(2, self.whole)
        n3 = DressP(1, self.whole)

        wait = self.quarter - (self.sixteenth / 2)
        
        m1 = build_measure(rest(self.half),
                           n4.q_c, rest(self.eighth), n4.q_c,
                           rest(self.whole + self.quarter),
                           n4.q_c, rest(self.eighth), n4.q_c,
                           rest(self.whole + self.quarter),
                           n3.q_b, rest(self.eighth), n3.q_b,
                           rest(self.whole + self.quarter),
                           n3.q_b, rest(self.eighth), n3.q_b,
                           rest(self.half), n3.q_b, n4.q_c
                           )
        
        m2 = build_measure(n4.w_c, rest(self.quarter),
                           n3.e_g, n3.e_a, rest(self.eighth),
                           n3.q_b,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_b, self.half - self.sixteenth / 2),
                           n4.w_c, rest(self.quarter),

                           n3.e_g, n3.e_a, rest(self.eighth),
                           #delaycombo(n3.q_g, n3.q_a, wait),
                           n4.q_d,
                           n3.w_b, rest(self.quarter),

                           n3.e_g, n3.e_a, rest(self.eighth),
                           n3.q_f,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_f, self.half - self.sixteenth / 2),
                           n3.w_e,
                           n3.w_d,
                           )

        
        return m1, m2
    
    def bass(self):
        n1 = DressB(1, self.whole)
        
        d1 = DressD(3, self.whole)
        d2 = DressD(2, self.whole)


        m1 = build_measure(rest(self.half),
                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.quarter + self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.half - self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), n1.create_note(B0, self.quarter), n1.q_c, rest(self.quarter)

                           ) * 3.0  
        
        m2 = build_measure(rest(self.half),
                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.quarter + self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.half - self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), n1.create_note(B0, self.quarter), n1.q_c

                           ) * 3.0
        
        m3 = m2
        m2 *= 0.85


        m4 = build_measure(rest(self.half),
                           d1.q_c, rest(self.eighth), d1.q_c, rest(self.quarter + self.eighth),
                           d2.q_b, rest(self.trey),

                           d1.q_c, rest(self.eighth), d1.q_c, rest(self.half - self.eighth),
                           d2.q_b, rest(self.trey),

                           d2.q_b, rest(self.eighth), d2.q_b, rest(self.half - self.eighth),
                           d2.q_a, rest(self.trey),

                           d2.q_b, rest(self.eighth), d2.q_b, rest(self.half - self.eighth),
                           d2.q_a, d2.q_b, d1.q_c, rest(self.quarter)

                           )
        
        m5 = build_measure(rest(self.half),
                           d1.q_c, rest(self.eighth), d1.q_c, rest(self.quarter + self.eighth),
                           d2.q_b, rest(self.trey),

                           d1.q_c, rest(self.eighth), d1.q_c, rest(self.half - self.eighth),
                           d2.q_b, rest(self.trey),

                           d2.q_b, rest(self.eighth), d2.q_b, rest(self.half - self.eighth),
                           d2.q_a, rest(self.trey),

                           d2.q_b, rest(self.eighth), d2.q_b, rest(self.half - self.eighth),
                           d2.q_a, d2.q_b, d1.q_c,

                           )
        
        m1 = combine(m1, m4)
        m2 = combine(m2, m5)

        return m1, m2, m3



    def drums(self):
        pass







    def produce(self):
        #   Instruments #
        k1 = self.keys()
        c1, c2 = self.chimes() # c1 -> singled out chimes; c2 -> bass tones for k1
        p1, p2 = self.piano() # p1 -> bass tones / keeping beat; p2 -> bass tones for k1
        b1, b2, b3 = self.bass() # b1 -> bass; b2 -> quieter bass
        #d1 = self.drums()

        #   Adjustments to instruments / Combinations   #
        ##  Exoeriment with c2 vs p2 here
        #p2 = combine(p2, b2)
        #k1 = combine(k1, p2)

        # #   Sections    #
        v1 = combine(k1, b2) # Keys and bass
        v2 = combine(v1, c1 * 0.65) # Keys, Bass, and Chimes
        #v3 = combine(v2, d1) # Keys, Bass, Chimes, and Drums
        v4 = combine(b3, c1) # Bass and Chimes

        # #   Final Product   #
        production = build_measure(b1, v1, v2, # Intro / Build-up
                                   
                                   v2, v2, # Add Drums (V3)

                                   v4, # Refrain

                                   v2, v2, # Back to melody
                                   )
        
        self.save(production, "dressy")





    def test(self):
        k1 = self.keys()
        # b1, b2 = self.bass() # b1 -> introductory bass; b2 -> bass with less rest
        
        # v1 = combine(k1, b1)
        # v2 = combine(k1, b2)
        
        # test = build_measure(v1, v2)

        # d1 = self.drums()

        self.save(k1, "dressy")
        


def main():
    Dressy(90).produce()
    #Dressy(90).test()