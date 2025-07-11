from modules.beat import *
from modules.instruments import *
from modules.audio import *

import pygame.sndarray
import pygame.mixer

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

        self.instruments = {
            #   Keys    #
            0: [LowSynth, self.keys("v1")],
            1: [DontTell, self.keys("v3")],
            #2: [Tangible_Light.Title_Synth, self.keys_long("v1")],

            #   Bass    #
            3: [Tangible_Light.Title_Bass, self.bass("v1", Tangible_Light.Title_Bass(amp=2.0, freq_mod = 2))],
            
            #   Percussion  #
            4: [KickBass, self.kick("v1")],
            5: [None, self.drums("v1")]
        }

    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=10_000)
    
    def drums(self, part="") -> list:
        c = HipSkirt(attack=25, amp=0.2, low=0, high=0, dist=15.0, noise_amount=1.4)
        d = HipSkirt(attack=35, amp=0.2, low=0, high=0, dist=8.0, noise_amount=0.6)

        m1 = [
           d.note(Cs1, self.e), d.note(Cs1, self.e), # 1
           d.note(Cs1, self.s), d.note(Cs1, self.s/2), d.note(Cs1, self.s + self.s/2), #1.75
           d.note(Cs1, self.e), rest(self.e), # 2.75
           rest(self.q + self.s)
        ]

        m2 = [
            d.note(Cs1, self.e), d.note(Cs1, self.e), # 1
            d.note(Cs1, self.s), d.note(Cs1, self.s/2), d.note(Cs1, self.s + self.s/2), d.note(Cs1, self.s), # 2
            d.note(Cs1, self.e), d.note(Cs1, self.e),
            d.note(Cs1, self.s), d.note(Cs1, self.s/2), d.note(Cs1, self.s + self.s/2), d.note(Cs1, self.s),
        ]


        m3 = [
            
        ]
        return \
        [rest(self.whole)] +\
        \
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        \
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        [rest(self.whole)] +\
        \
        m1 +\
        m1 +\
        m1 +\
        m1 +\
        \
        m2 +\
        m2 +\
        m1 +\
        m1 +\
        \
        m2 +\
        m2 +\
        m1 +\
        m1

    
    def kick(self, part="") -> list:
        d = KickBass(amp=2.5, attack=85, bass_dist = 0.0, bass_amp = 0.0)
        #d = Tangible_Light.Title_Kick()

        m1 = [
            d.note(C2, self.e), d.note(C2, self.e),
            d.note(C2, self.e), d.note(C2, self.e),
            d.note(C2, self.e), d.note(C2, self.e),
            d.note(C2, self.e), d.note(C2, self.e),
        ]

        return \
        [rest(self.whole)] +\
        m1 +\
        m1 +\
        m1 +\
        m1 +\
        \
        m1 +\
        m1 +\
        m1 +\
        m1 +\
        \
        m1 +\
        m1 +\
        m1 +\
        m1



    def keys_long(self, part="") -> list:
        n = Tangible_Light.Title_Synth(amp=0.65)
        d = DontTell(amp=3.5)
        
        m1 = [
            fade_out(n.note(A4, self.w)(), 12.0),
            #n.note(A4, self.h),
        ]

        m2 = [
            rest(self.h),
            n.note(B4, self.q),
            delaycombo(n.note(A4, self.q)(), n.note(G4, self.e)() * 1.2, self.e, False),
            #n.note(A4, self.e), n.note(G4, self.e),
        ]

        m3 = [
            delaycombo(n.note(G4, self.h)(), n.note(A4, self.q)(), self.q, False),
            delaycombo(n.note(G4, self.h)(), n.note(A4, self.q)(), self.q, False),
        ]

        m4 = [
            delaycombo(n.note(G4, self.h)(), n.note(A4, self.q)(), self.q, False),
            n.note(A4, self.q),
            n.note(G4, self.q)
        ]

        m5 = [
            d.note(F2, self.e), rest(self.e),
            rest(self.e), d.note(F2, self.e), 
            d.note(F2, self.e), rest(self.e),
            rest(self.q)
        ]

        return \
            [rest(self.whole)] +\
            \
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            \
            m1 +\
            m2 +\
            m3 +\
            m4 +\
            \
            m1 +\
            m2 +\
            m3 +\
            m4 +\
            \
            m5 +\
            m5 +\
            m5 +\
            m5 +\
            \
            m5 +\
            m5 +\
            m5 +\
            m5

    def keys(self, part="") -> list:
        e = self.e
        q = self.q
        s = self.s

        if part == "v1":
            k = LowSynth(amp=0.2, freq_mod=1/2)

        elif part == "v2":
            k = Tangible_Light.Title_Synth(amp = 1.0)
        
        elif part == "v3":
            k = DontTell(amp=0.6)
            



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
            k.note(F3, e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e),
            k.note(B3, s) + k.note(G3, s), k.note(A3, e) + k.note(F3, e),
            k.note(B3, e) + k.note(G3, e), k.note(A3, e) + k.note(F3, e),
            k.note(B3, e) + k.note(G3, e), k.note(A3, s) + k.note(F3, s), k.note(G3, e) + k.note(E3, e)
        ]

        m6 = [
            k.note(F3, e), k.note(G3, e), # 1
            k.note(B3, s), k.note(A3, e), # 1.75
            k.note(B3, e), k.note(A3, e), # 2.75
            k.note(B3, e + s) + k.note(G3, e + s), # 3.25
            k.note(A3, s) + k.note(F3, s), k.note(B3, s) + k.note(G3, s) # 3.75
        ]

        m6b = [
            k.note(F3, e), k.note(G3, e) + k.note(E3, e), # 1
            k.note(B3, s) + k.note(G3, s), k.note(A3, e) + k.note(F3, e), # 1.75
            k.note(B3, e) + k.note(G3, e), k.note(A3, e) + k.note(F3, e), # 2.75
            k.note(B3, e + s) + k.note(G3, e + s), # 3.25
            k.note(A3, s) + k.note(F3, s), k.note(B3, s) + k.note(G3, s)
        ]

        m7 = [
            k.note(C4, e) + k.note(A3, e), k.note(B3, e) + k.note(G3, e), # 1
            k.note(C4, s) + k.note(A3, s), k.note(B3, e) + k.note(G3, e), # 1.75
            k.note(C4, e) + k.note(A3, e), k.note(D4, e) + (k.note(B3, e) + k.note(F4, e)), # 2.75
            k.note(D4, e) + (k.note(B3, e) + k.note(F4, e)), k.note(C4, s) + (k.note(A3, s) + k.note(E4, s)), k.note(B3, e) + (k.note(G3, e) + k.note(D4, e)), # 3.75
        ]

        m8 = [
            k.note(C4, e) + k.note(A3, e), k.note(B3, e) + k.note(G3, e),
            k.note(C4, s) + k.note(A3, s), k.note(B3, e) + k.note(G3, e),
            k.note(A3, q) + k.note(F3, q), rest(self.s),
            k.note(G3, q) + k.note(E3, q), 
        ]

        #   Additional solo here    #
        v4 = m5 + m6 + m7 + m8
        
        v0 = [
        rest(self.whole)
        ]

        return \
            [rest(self.whole)] +\
            \
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            [rest(self.whole)] +\
            \
            m1 +\
            m2 +\
            m3 +\
            m4 +\
            \
            m1 +\
            m2 +\
            m3 +\
            m4 +\
            \
            m5 +\
            m6 +\
            m7 +\
            m8 +\
            \
            m5 +\
            m6b +\
            m7 +\
            m8
                


    def bass(self, part="", instr = Tangible_Light.Title_Bass(amp=3.0, freq_mod = 4)):
        n = instr

        ma = [
            n.note(F3, self.q),
            rest(self.e), n.note(F3, self.s),
            n.note(D3, self.q + self.s),
            n.note(F3, self.q)
        ]


        m1 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(E3, self.e), n.note(F3, self.e),
            #slur_notes(n.note(D3, self.e + self.s), n.note(F3, self.e + self.s), self.s, self.e + self.s, 2000),
            n.note(D3, self.e), n.note(F3, self.s),
            n.note(E3, self.e),
        ]

        m2 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(C3, self.e), n.note(F3, self.e),
            #slur_notes(n.note(D3, self.e + self.s), n.note(C3, self.e + self.s), self.s, self.e+self.s, 2000),
            n.note(D3, self.s), n.note(C3, self.e),
            n.note(F3, self.e),
        ]

        m3 = [
            n.note(F3, self.s), n.note(F3, self.s), n.note(D3, self.e),

            n.note(F3, self.s), n.note(D3, self.s/2), n.note(D3, self.s/2), n.note(D3, self.s), 
            n.note(E3, self.e), n.note(F3, self.e),
            #slur_notes(n.note(D3, self.s + self.e), n.note(F3, self.e + self.s), self.s, self.e + self.s),
            n.note(D3, self.s), n.note(F3, self.e),
            n.note(E3, self.e),
        ]

        m4 = [
            #slur_notes(n.note(F3, self.q), n.note(D3, self.q), self.e, self.q), # 1
            n.note(F3, self.e), n.note(D3, self.e),
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


        m6 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(E3, self.e), rest(self.e), rest(self.s),
            rest(self.q)
        ]

        m7 = [
            n.note(D3, self.e), n.note(F3, self.e),
            n.note(D3, self.s), n.note(D3, self.s), n.note(F3, self.s),
            n.note(E3, self.e), rest(self.e + self.s),
            rest(self.q)
        ]

        m8 = [
            n.note(D3, self.e), n.note(F3, self.e),
            n.note(D3, self.s), n.note(D3, self.s), n.note(F3, self.s),
            n.note(E3, self.e), rest(self.e + self.s),
            n.note(D3, self.q)
        ]


        return \
            ma +\
            \
            m1 +\
            m2 +\
            m3 +\
            m4 +\
            \
            m1 +\
            m2 +\
            m3 +\
            m5 +\
            \
            m1 +\
            m2 +\
            m3 +\
            m5 +\
            \
            m6 +\
            m7 +\
            m6 +\
            m7 +\
            \
            m6 +\
            m7 +\
            m6 +\
            m8

    
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



        self.save(prod, "01_Title", norm = False)
        return prod
        

def main():
   beat = Title(36)
   beat.produce_full()
   beat.save(beat.production, "01_Title")