from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

        self.instruments = {
            0: [Tangible_Light.Title_Synth, self.keys("v1")],
            1: [Tangible_Light.Title_Bass, self.keys2("v1")],
            2: [KickBass, self.keys2("v1", KickBass2(attack=1))]
            #2: [Bass, self.strings("v1")]
            #2: [DontMind, self.keys2("v1", DontMind(freq_mod = 4))]
        }

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
        

        return v1

    def keys(self, part="") -> list:
        e = self.e
        q = self.q
        s = self.s

        if part == "v1" or part == "v2":
            if part == "v1":
                k = LowSynth(amp=0.6, freq_mod=1/2)

            elif part == "v2":
                k = Tangible_Light.Title_Synth(amp = 1.0)
            
            m1 = [
                delaycombo(k.note(A3, q)(), k.note(F3, q - 0.08)(), 0.08, silence = False),

                delaycombo(k.note(G3, q)(), k.note(B3, q - 0.08)(), 0.08, silence = False),

                delaycombo(k.note(F3, s)(), k.note(A3, s - 0.04)(), 0.04, silence = False), delaycombo(k.note(G3, e)(), k.note(B3, e - 0.06)(), 0.06, False),
                
                delaycombo(k.note(A3, e)(), k.note(C4, e - 0.06)(), 0.06, False),
                delaycombo(k.note(B3, e + s)(), k.note(D4, e + s - 0.07)(), 0.07, False),
            ]

            m2 = [
                k.note(A3, e) + k.note(F3, e), k.note(B3, e) + k.note(G3, e),

                k.note(C4, s) + k.note(A3, s), 

                k.note(D4, e) + k.note(B3, e), k.note(E4, e) + k.note(C4, e),
                
                k.note(D4, e) + k.note(B3, e), k.note(C4, e) + k.note(A3, e), 

                k.note(B3, s) + k.note(G3, s),
                k.note(A3, e) + k.note(F3, e)

            ]

            m3 = [
                k.note(G3, q) + k.note(E3, q),

                k.note(A3, q) + k.note(F3, q),

                k.note(G3, s) + k.note(E3, s), k.note(A3, e) + k.note(F3, e),
                
                k.note(B3, e) + k.note(G3, e), k.note(C4, e + s) + k.note(A3, e + s),

            ]

            m4 = [
                k.note(G3, e) + k.note(E3, e), k.note(A3, e) + k.note(F3, e),

                k.note(B3, s) + k.note(G3, s), 

                k.note(C4, e) + k.note(A3, e), k.note(D4, e) + k.note(B3, e),
                
                k.note(C4, self.h - s) + k.note(A3, self.h - s)

            ]

            v1 = [rest(self.whole*4)]
            v2 = m1 + m2 + m3 + m4
            v3 = v2


            m5 = [
                k.note(F3, e), k.note(G3, e),
                k.note(B3, s), k.note(A3, e),
                k.note(B3, e), k.note(A3, e),
                k.note(B3, e), k.note(A3, s), k.note(G3, e)
            ]

            m6 = [
                k.note(F3, e), k.note(G3, e), # 1
                k.note(B3, s), k.note(A3, e), # 1.75
                k.note(B3, e), k.note(A3, e), # 2.75
                k.note(B3, e + s), # 3.25
                k.note(A3, s), k.note(B3, s) # 3.75
            ]

            m7 = [
                k.note(C4, e), k.note(B3, e), # 1
                k.note(C4, s), k.note(B3, e), # 1.75
                k.note(C4, e), k.note(D4, e), # 2.75
                k.note(D4, e), k.note(C4, s), k.note(B3, e), # 3.75
            ]

            m8 = [
                k.note(C4, e), k.note(B3, e),
                k.note(C4, s), k.note(B3, e),
                k.note(A3, q), rest(self.s),
                k.note(G3, q), 
            ]
            v4 = m5 + m6 + m7 + m8
            

            return v1 +\
                v2 + v3 +\
                v4 + v4

    def keys2(self, part="", instr = Tangible_Light.Title_Bass(amp=1.4)):
        n = instr

        m1 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(E3, self.e), n.note(F3, self.e),
            n.note(D3, self.s),
            n.note(F3, self.e), n.note(E3, self.e),
        ]

        m2 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(C3, self.e), n.note(F3, self.e),
            n.note(D3, self.s),
            n.note(E3, self.e), n.note(F3, self.e),
        ]

        m3 = [
            n.note(F3, self.s), n.note(F3, self.s), n.note(D3, self.e),

            n.note(F3, self.s), n.note(D3, self.s/2), n.note(D3, self.s/2), n.note(D3, self.s), 
            n.note(E3, self.e), n.note(F3, self.e),
            n.note(D3, self.s),
            n.note(F3, self.e), n.note(E3, self.e),
        ]

        m4 = [
            n.note(F3, self.e), n.note(D3, self.e), # 1
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), # 1.75
            n.note(C3, self.e), # 2.25
            
            n.note(D3, self.s / 2), n.note(E3, self.s /2), # 2.5
            n.note(F3, self.e), # 3

            n.note(D3, self.s / 2), n.note(E3, self.s /2), # 3.25
            n.note(F3, self.s), n.note(F3, self.e), # 4
        ]

        m5 = [
            n.note(F3, self.e), n.note(D3, self.e), # 1
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), # 1.75
            n.note(C3, self.e), # 2.25
            
            n.note(D3, self.s / 2), n.note(E3, self.s /2), # 2.5
            n.note(F3, self.e), # 3

            n.note(D3, self.s / 2), n.note(E3, self.s /2), # 3.25
            n.note(F3, self.s), n.note(E3, self.s), n.note(F3, self.s),# 4
        ]

        v1 = m1 + m2 + m3 + m4
        v2 = m1 + m2 + m3 + m5

        return v1 +\
               v2 + v2 +\
               v1 + v2 +\
               v2

    
    def strings(self, part=""):
        n = Bass(freq_mod=8, dist=2.5)

        m1 = [
            n.note(A4, self.q),
            n.note(A4, self.q),
            delaycombo(
            n.note(G4, self.q)(),
            n.note(A4, self.q - 0.10)(),
            0.10
            )
        ]

        m2 = [
            n.note(G4, self.q),
            n.note(G4, self.q),
            n.note(G4, self.q),
            n.note(G4, self.q),

        ]

        return [rest(self.whole * 4)] +\
            m1 + m1 + m2 + m2 +\
            m1 + m1 + m2 + m2

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
   beat = Title(36)
   beat.produce_full()
   beat.save(beat.production, "01_Title")