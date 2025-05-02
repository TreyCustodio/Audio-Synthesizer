from beat import *

class Jiggy(Beat):
    def __init__(self):
        super().__init__(180)

    def xylos(self):
        x = XyloHorn(7, self.whole, "2")

        m1 = build_measure(x.q_e, x.q_c, x.e_e, rest(self.eighth),
                           x.e_c, x.e_e, rest(self.eighth),
                           x.e_e, x.e_c, rest(self.eighth),
                           x.e_e, x.q_d, rest(self.eighth))

        m2 = build_measure(x.e_e, x.e_e, x.q_c, x.e_e, rest(self.eighth),
                           x.e_e, x.e_c, rest(self.eighth),
                           x.e_c, x.e_f, rest(self.eighth),
                           x.e_f, x.q_d, rest(self.eighth))
        return build_measure(m1, m2)
    
    def produce(self):
        x1 = self.xylos()

        save (x1, "jiggy", "production")


def main():
    Jiggy().produce()
    
