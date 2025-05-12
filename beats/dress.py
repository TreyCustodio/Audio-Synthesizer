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
        n4 = Dress(5, self.whole)
        n3 = Dress(4, self.whole)

        #wait = self.quarter - (self.sixteenth / 2)
        
        m1 = build_measure(n4.w_c, rest(self.quarter + self.eighth),
                           n3.e_g, n3.e_a, rest(self.eighth),
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
        
        return m1

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

        m1 = build_measure(rest(self.half),
                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.quarter + self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.q_c, rest(self.eighth), n1.q_c, rest(self.half - self.eighth),
                           n1.create_note(B0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), rest(self.trey),

                           n1.create_note(B0, self.quarter), rest(self.eighth), n1.create_note(B0, self.quarter), rest(self.half - self.eighth),
                           n1.create_note(A0, self.quarter), n1.create_note(B0, self.quarter), n1.q_c

                           ) * 3.0  
        
        m2 = m1 * 0.75
        
        return m1, m2

    def produce(self):
        #   Instruments #
        k1 = self.keys()
        c1, c2 = self.chimes() # c1 -> singled out chimes; c2 -> bass tones for k1
        p1, p2 = self.piano() # p1 -> bass tones / keeping beat; p2 -> bass tones for k1
        b1, b2 = self.bass() # b1 -> bass; b2 -> quieter bass

        #   Adjustments to instruments / Combinations   #
        ##  Exoeriment with c2 vs p2 here
        #p2 = combine(p2, b2)
        #k1 = combine(k1, p2)

        # #   Sections    #
        v1 = combine(k1, b2)
        v2 = combine(v1, c1 * 0.65)
        v3 = combine(b1, c1)

        # #   Final Product   #
        production = build_measure(b1,
                                   v1, v2, v2, v2,
                                   v3, v2)
        
        self.save(production, "dressy")





    def test(self):
        k1 = self.keys()
        b1, b2 = self.bass() # b1 -> introductory bass; b2 -> bass with less rest
        
        v1 = combine(k1, b1)
        v2 = combine(k1, b2)
        
        test = build_measure(v1, v2)

        self.save(test, "dressy")
        


def main():
    Dressy(90).produce()
    #Dressy(90).test()