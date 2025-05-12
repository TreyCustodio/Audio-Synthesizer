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
        n = Chime(3, self.whole)

        m1 = build_measure(rest(self.half), 
                           n.q_g, rest(self.eighth), n.q_g,

                           rest(self.whole + self.quarter + self.sixteenth),

                           n.q_g, rest(self.eighth), n.q_g,

                           rest(self.whole + self.quarter + self.sixteenth),
                           n.q_e, rest(self.eighth), n.q_e,

                           rest(self.whole + self.quarter + self.sixteenth),
                           n.q_e, rest(self.eighth), n.q_e, rest(self.quarter)

                            
                           )

        return m1

    def keys(self):
        n4 = Dress(5, self.whole)
        n3 = Dress(4, self.whole)

        #wait = self.quarter - (self.sixteenth / 2)
        
        m1 = build_measure(n4.w_c, rest(self.quarter),
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
        
        return m1
    

    def produce(self):
        k1 = self.keys()
        c1 = self.chimes()
        p1 = self.piano()

        v1 = k1
        v2 = combine(k1, p1)
        v3 = p1

        production = build_measure(v1, v2, v2, v2,
                                   v3, v2)
        
        self.save(production, "dressy")



def main():
    Dressy(90).produce()