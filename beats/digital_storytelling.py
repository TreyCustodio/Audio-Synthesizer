from modules.beat import *
from modules.instruments import *
from modules.audio import *

class DST(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beats", "dst"), name)


    def drums(self):
        return 
    
    def keys(self):
        n4 = Weeknd(4, self.whole)
        n3 = Weeknd(3, self.whole)

        m1 = build_measure(n4.q_c, n3.e_g, n3.q_a,
                           n4.e_c, n3.e_g, n3.e_a,

                           n4.q_c, n4.e_d, n4.q_e,
                           n4.e_c, n3.e_g, n3.e_a,

                           #n4.q_c, n3.e_g, n3.q_a, # shift this 2 tones down
                           n4.q_c, n3.e_f, n3.q_g,
                           )
        return m1

    def produce(self):
        k1 = self.keys()
        
        self.save(k1, "test")



def main():
    DST(70).produce()