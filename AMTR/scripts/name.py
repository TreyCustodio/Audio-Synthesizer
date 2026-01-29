from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Name(Project):
    def __init__(self, bpm, name="Name Him"):
        super().__init__(bpm, name)

    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],

            #   Melody  #


            #   Samples / Libs  #
            'guitar': [0, self.synth(verse)]


        }

    def synth(self, verse):
        s = self.guit1
        s2 = self.guit2

        v0 = [rest(self.w*4)]
        
        v1 = [s.n(self.w*4)]

        return \
        v0 + v1 +\
        v1 + v1 +\
        v0 + v1 +\
        v1 + v1
    
    def hats(self, verse):
        h = self.jazz_hat2
        h2 = self.jazz_hit2

        m0 = [rest(self.w)]
        mi = [
            h.n(self.q),
            rest(self.q),
            h.n(self.s), h.n(self.e + self.s),
            rest(self.q),
        ]

        mi2 = [
            h.n(self.q),
            rest(self.q),
            h.n(self.e), h.n(self.e),
            rest(self.q),
        ]
        
        me1 = [
            h.n(self.e) + h2.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        me2 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        mq = [
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        ms = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        v1 = mi + mi2 + me1 + me1

        v2 = me1 + me1 + me1 + me2
        

        return \
        v1 + v2 +\
        v2 + v2 +\
        v2 + v2 +\
        v2 + v2
    
    def drums(self, verse):
        k = self.jazz_kick7
        k2 = self.kick_electro1
        s = self.jazz_snare6

        m1 = [
            k.n(self.q - self.s),
            s.n(self.e), rest(self.s), s.n(self.e),
            k.n(self.s), k.n(self.s + self.e), 
            s.n(self.e), rest(self.s), s.n(self.s),
        ]

        m2 = [
            k.n(self.q - self.s),
            s.n(self.e), rest(self.s), s.n(self.e),
            k.n(self.e), k.n(self.e), 
            s.n(self.e), rest(self.e)
        ]

        m4 = [
            k.n(self.q - self.s),
            s.n(self.e), rest(self.s), s.n(self.e),
            k.n(self.e), rest(self.s), k.n(self.s), 
            s.n(self.e), s.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m4
        return \
        v1 + v1 +\
        v1 + v1 +\
        v1 + v1 +\
        v1 + v1


def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Name(80)



    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="production", volume=30_500)
    # beat.export_selection(name="03_prod", volume=30_500)