from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    

    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm)
    
    
    def bass(self, part=""):
        q = self.q
        e = self.e
        s = self.s

        if part == "v1":
            k = Tangible_Light.Title_Bass(dist = 2.0)

        elif part == "v2":
            k = Tangible_Light.Title_Bass()

        m1 = build_measure(
                k.note(A3, q),

                k.note(B3, q),

                k.note(A3, s), k.note(B3, e),
                
                k.note(C4, e), k.note(D4, e + s),

            )

        m2 = build_measure(
            k.note(A3, e), k.note(B3, e),

            k.note(C4, s), 

            k.note(D4, e), k.note(E4, e),
            
            k.note(D4, e), k.note(C4, e), 

            k.note(B3, s),
            k.note(A3, e)

        )

        m3 = build_measure(
            k.note(G3, q),

            k.note(A3, q),

            k.note(G3, s), k.note(A3, e),
            
            k.note(B3, e), k.note(C4, e + s),

        )

        m4 = build_measure(
            k.note(G3, e), k.note(A3, e),

            k.note(B3, s), 

            k.note(C4, e), k.note(D4, e),
            
            k.note(C4, e), k.note(B3, e), 
            k.note(A3, s),
            k.note(G3, e)
        )

        v1 = build_measure(m1, m2, m3, m4)
        

        #   For Testing -- Kent Jones type beat #
        # v1 = build_measure(
        #     k.note(A2, e), rest(s),
        #     k.note(F2, e), rest(s),
        #     k.note(G2, e), rest(e),

        #     k.note(G2, e), rest(s), k.note(G2, e), rest(s),
        #     k.note(F2, e), rest(s), k.note(B2, e), rest(s),
        #     k.note(A2, e), rest(e), k.note(A2, e), rest(s), k.note(A2, e)
        # )

        return v1

    def keys(self, part=""):
        e = self.e
        q = self.q
        s = self.s

        if part == "v1" or part == "v2":
            if part == "v1":
                k = Tangible_Light.Title_Synth(amp=1.0)

            elif part == "v2":
                k = Tangible_Light.Title_Synth(amp = 1.0)
            
            m1 = build_measure(
                k.note(A3, q),

                k.note(B3, q),

                k.note(A3, s), k.note(B3, e),
                
                k.note(C4, e), k.note(D4, e + s),
            )

            m2 = build_measure(
                k.note(A3, e), k.note(B3, e),

                k.note(C4, s), 

                k.note(D4, e), k.note(E4, e),
                
                k.note(D4, e), k.note(C4, e), 

                k.note(B3, s),
                k.note(A3, e)

            )

            m3 = build_measure(
                k.note(G3, q),

                k.note(A3, q),

                k.note(G3, s), k.note(A3, e),
                
                k.note(B3, e), k.note(C4, e + s),

            )

            m4 = build_measure(
                k.note(G3, e), k.note(A3, e),

                k.note(B3, s), 

                k.note(C4, e), k.note(D4, e),
                
                k.note(C4, self.h - s)

            )

            v1 = build_measure(m1, m2, m3, m4)

            return v1

    def drums(self, part=""):
        k = HipSkirt(attack=15, amp = 0.2, dist = 32)
        b = KickBass(amp = 2.0, count = 1)

        if part == "v1":
            m1 = build_measure(
                b.note(C2, self.e), b.note(C2, self.e),
                k.note(C2, self.e) + b.note(C2, self.e), b.note(C2, self.e),
                b.note(C2, self.e), b.note(C2, self.e),
                b.note(C2, self.e), b.note(C2, self.e) + k.note(C2, self.e),
            )

            v1 = build_measure(m1, m1, m1, m1)
            return v1

        elif part == "v2":
            m2 = build_measure(
                b.note(C2, self.s), b.note(C2, self.s), b.note(C2, self.s), b.note(C2, self.s),
                b.note(C2, self.s) + k.note(C2, self.s), b.note(C2, self.s) + k.note(C2, self.s), b.note(C2, self.s), b.note(C2, self.s),
                b.note(C2, self.s), b.note(C2, self.s), b.note(C2, self.s), b.note(C2, self.s),
                b.note(C2, self.s), b.note(C2, self.s), 
                combine(k.note(C2, self.e), add_waves(b.note(C2, self.s), b.note(C2, self.s)))
            )

            v2 = build_measure(m2, m2, m2, m2)
            return v2

        elif part == "v3":
            s = HipSkirt(attack=80, amp = 0.1, dist = 15)

            m1 = build_measure(
                s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2),
                s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2),
                s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2),

                s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), 
                rest(self.e)


                #s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2), s.note(C3, self.s / 2),
            
            
            )

            m2 = build_measure(
                s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4),
                s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4),
                s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4),
                s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4), s.note(C3, self.s / 4),
            )

            v3 = build_measure(m1, m1, m1, m1)

            return v3

        elif part == "v4":
            n = Tangible_Light.Title_Snare()

            m1 = build_measure(
                n.note(C1, self.e), n.note(C1, self.e), # 1
                n.note(C1, self.s), n.note(C3, self.e),  # 1.75
                n.note(C1, self.e), n.note(C1, self.e),  # 2.75
                n.note(C1, self.e), rest(self.s), # 3.5
                n.note(C3, self.e),
            )

            v1 = build_measure(m1, m1, m1, m1)
            return v1

        elif part == "v5":
            n = Tangible_Light.Title_Snare(dist=8.0)
            
            m1 = build_measure(
                n.note(C2, self.e), k.note(C1, self.s / 2), k.note(C1, self.s/ 2), k.note(C1, self.s / 2), rest(self.s/2), # 1
                n.note(C2, self.e), k.note(C1, self.s/2), rest(self.s/2), # 1.75
                n.note(C2, self.e), k.note(C1, self.s / 2), rest(self.s/2),# 2.5
                n.note(C2, self.e), k.note(C1, self.s/2), rest(self.s/2),# 3.25
                n.note(C1, self.e), n.note(C1, self.s),
            )

            v1 = build_measure(m1, m1, m1, m1)
            return v1

    def produce(self):      
        #   Gather Each Section of the song    #
        b1 = self.bass('v1')
        
        k1 = self.keys("v1")
        k2 = self.keys("v2")

        d1 = self.drums("v1")
        d2 = self.drums("v5")
        d3 = self.drums("v3")
        d4 = self.drums("v4")

        
        #   Mix Some Sections together  #
        k1 = combine(k1, b1)
        k2 = combine(k1, b1)

        #   Produce the song    #
        v0 = b1

        v1 = k1

        v2 = combine(k2, d1)

        v3 = combine(k1, d2)

        v4 = combine(v3, d3)

        v5 = combine(v3, d4)
    
        prod = build_measure(
            v0, v1, 
            v2, v3,
            v4, v5
        )


        #   Normalize the audio
        prod = (prod / np.max(np.abs(prod)) * 32767).astype(np.int16)

        self.save(prod, "01_Title", norm = False)
        return prod
        

def main():
   Title(36).produce()