from modules.beat import *
from modules.instruments import *
from modules.audio import *

import pygame.sndarray
import pygame.mixer

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

        #   Keys    #
        self.instr0 = LowSynth(amp=0.2, freq_mod=1/2)
        self.instr1 = DontTell(amp=0.6)
        #self.instr2 = Tangible_Light.Title_Synth

        #   Bass    #
        self.instr3 = Tangible_Light.Title_Bass(amp=0.6, freq_mod = 2)
        
        #   Percussion  #
        self.instr4 = KickBass(amp=3.5, attack=85, bass_dist = 0.0, bass_amp = 0.0)
        self.instr5 = HipSkirt(attack=35, amp=0.2, low=0, high=0, dist=8.0, noise_amount=0.6)
        self.instr6 = HipSkirt(attack=75, amp=0.2, low=0, high=0, dist=15.0, noise_amount=1.4)
        self.instr7 = Cymbal(amp=0.3, atk1 = 10, atk2 = 3, dist=0.0)

        self.instr8 = Hey()

        self.instruments = {
            #   Keys    #
            0: [self.instr0, self.keys("v1")],
            1: [self.instr1, self.keys("v2")],
            #2: [self.instr2, self.keys_long("v1")],

            #   Bass    #
            3: [self.instr3, self.bass("v1")],
            
            #   Percussion  #
            4: [self.instr4, self.kick("v1")],
            5: [self.instr5, self.drums("v1")],
            6: [self.instr6, self.crash("v1")],

            #   Adlibs  #
            #8: [self.instr8, self.navi()]
        }


    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=10_000)
    
    def drums(self, part="") -> list:
        
        if part == "v1":
            d = self.instr5

        elif part == "v2":
            c = self.instr6
        
        intro = [

        ]

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
            d.note(Cs1, self.e), d.note(Cs1, self.e), # 1
            d.note(Cs1, self.s), d.note(Cs1, self.s/2), d.note(Cs1, self.s + self.s/2), #1.75
            d.note(Cs1, self.e), rest(self.s), # 2.75
            d.note(Cs1, self.s), d.note(Cs1, self.s), d.note(Cs1, self.s), d.note(Cs1, self.s), d.note(Cs1, self.s), d.note(Cs1, self.s),
        ]

        m4 = [
            d.note(Cs1, self.e), d.note(Cs1, self.e), # 1
            d.note(Cs1, self.s), d.note(Cs1, self.s/2), d.note(Cs1, self.s + self.s/2), #1.5
            d.note(Cs1, self.e), # 2
            
            d.note(Cs1, self.s/2), d.note(Cs1, self.s/2), d.note(Cs1, self.s/2), d.note(Cs1, self.s/2), # 2.5
            rest(self.s), # 2.75

            d.note(Cs1, self.s/2), d.note(Cs1, self.s/2), # 3
            d.note(Cs1, self.s/2), rest(self.s / 2), # 3.25

            d.note(Cs1, self.s/2), d.note(Cs1, self.s/2), # 3.5
            rest(self.s)
        ]

        refrain = m3 + m4

        v1 = m1 + m1 + m1 + m1
        v2 = m2 + m2 + m1 + m1

        return \
        intro +\
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
        v1 +\
        \
        v2 +\
        \
        v2 +\
        \
        v2 +\
        \
        v2 +\
        \
        refrain
    
    def kick(self, part="") -> list:
        d = self.instr4

        m1 = [
            d.note(C1, self.e), rest(self.e),
            d.note(D1, self.e), rest(self.e),
            rest(self.s), d.note(C1, self.s), rest(self.e),
            d.note(C1, self.e), d.note(D1, self.e)
        ]
        
        v1 = m1 + m1 + m1 + m1
        return \
        v1 +\
        \
        v1 +\
        \
        v1


    def crash(self, part="") -> list:
        d = self.instr6
        c = self.instr7

        m1 = [
            rest(self.q),
            rest(self.e), d.note(C1, self.s), c.note(C2, self.e),
            rest(self.s),
            rest(self.s), rest(self.e),
            rest(self.s), c.note(C2, self.e),
        ]

        v1 = m1 + m1 + m1 + m1
        
        return \
        v1 +\
        \
        v1 +\
        \
        v1
    
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
            k = self.instr0

        elif part == "v2":
            k = self.instr1
        

        #   Intro   -- Silent --   #
        intro = [
            # rest(self.whole)
            ]

        #   Bass Solo   -- Silent --  #
        bass_solo = [rest(self.whole*4)]

        #   Verse 1 #
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
        
        v1 = m1 + m2 + m3 + m4

        #   Verse 2 #
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
            k.note(C4, e) + k.note(A3, e), k.note(D4, e) + k.note(B3, e), # 2.75
            k.note(D4, e) + k.note(B3, e), k.note(C4, s) + k.note(A3, s), k.note(B3, e) + k.note(G3, e), # 3.75
        ]

        m7b = [
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

        

        v2 = m5 + m6 + m7 + m8
        v2b = m5 + m6b + m7b + m8

        #   Verse 3    #
        

        m9 = [
            k.note(F3, e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e), # 1
            k.note(B3, s) + k.note(G3, s), k.note(A3, e) + k.note(F3, e), # 1.75

            k.note(F3, e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e), # 2.75
            k.note(F3, s) + k.note(D3, self.s), k.note(B3, e) + k.note(G3, e), # 2.75
            k.note(A3, e) + k.note(F3, e),
        ]

        m10 = [
            k.note(F3, e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e), # 1
            k.note(B3, s) + k.note(G3, s), k.note(A3, e) + k.note(F3, e), # 1.75

            k.note(B3, e) + k.note(G3, self.e), k.note(A3, s) + k.note(F3, s), k.note(G3, s) + k.note(E3, s), # 2.75
            
            k.note(F3, s) + k.note(D3, self.s), k.note(G3, s) + k.note(E3, s), k.note(A3, s) + k.note(F3, s),
            k.note(D3, s) + k.note(B2, self.s), k.note(E3, s) + k.note(C3, self.s),
            
        ]

        m11 = [
            k.note(F3 , e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e), # 1
            k.note(G3, e) + k.note(E3, self.e), # 1.5
            k.note(E3, s) + k.note(C3, self.s), k.note(F3, e) + k.note(D3, self.e), # 2.25
            k.note(G3, e) + k.note(E3, self.e), k.note(G3, e) + k.note(E3, self.e), # 3.25
            rest(self.s * 3)
        ]

        m12 = [
            k.note(F3 , e) + k.note(D3, self.e), k.note(G3, e) + k.note(E3, self.e), # 1
            k.note(G3, e) + k.note(E3, self.e), # 1.5
            k.note(E3, s) + k.note(C3, self.s), k.note(F3, e) + k.note(D3, self.e), # 2.25
            k.note(G3, e) + k.note(E3, self.e), k.note(G3, e) + k.note(E3, self.e), # 3.25
            rest(self.s), 
            k.note(D3, s) + k.note(B2, s), k.note(E3, s) + k.note(C3, s),
        ]

        v3 = m9 + m10 + m11 + m12

        #   Refrain #
        refrain = [rest(self.whole * 2)]

        return \
            intro +\
            \
            bass_solo +\
            \
            v1 +\
            \
            v1 +\
            \
            v2 +\
            \
            v2b+\
            \
            v3 +\
            \
            v3 +\
            \
            refrain
                


    def bass(self, part=""):
        n = self.instr3

        s = self.s
        e = self.e
        q = self.q

        hey = Hey(amp=0.00001).note(C1, e)

        intro = [
            # n.note(F3, self.e), n.note(F3, self.e),
            # n.note(F3, self.e), n.note(F3, self.e),
            # n.note(F3, self.s), rest(self.s),
            # n.note(F3, self.s), rest(self.s),
            # n.note(F3, self.s), rest(self.e + self.s),
        ]

        #   Verse 1 #
        m1 = [
            n.note(D3, self.e), n.note(E3, self.e),
            n.note(F3, self.e), n.note(G3, self.s),

            n.note(D3, self.e), n.note(E3, self.e),
            n.note(F3, self.e), n.note(G3, self.e + self.s),
        ]
        # m1 = [
        #     n.note(F3, self.e), n.note(D3, self.e),
        #     n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
        #     n.note(E3, self.e), n.note(F3, self.e),
        #     #slur_notes(n.note(D3, self.e + self.s), n.note(F3, self.e + self.s), self.s, self.e + self.s, 2000),
        #     n.note(D3, self.e), n.note(F3, self.s),
        #     n.note(E3, self.e),
        # ]

        # m2 = [
        #     n.note(F3, self.e), n.note(D3, self.e),
        #     n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
        #     n.note(C3, self.e), n.note(F3, self.e),
        #     #slur_notes(n.note(D3, self.e + self.s), n.note(C3, self.e + self.s), self.s, self.e+self.s, 2000),
        #     n.note(D3, self.s), n.note(C3, self.e),
        #     n.note(F3, self.e),
        # ]

        m2 = [
            n.note(D3, self.e), n.note(E3, self.e),
            n.note(F3, self.e), n.note(G3, self.s),

            n.note(A3, self.e), n.note(G3, self.e),
            n.note(F3, self.e), n.note(E3, self.s), n.note(D3, self.e)
        ]

        m3 = [
            n.note(C3, self.e), n.note(D3, self.e),
            n.note(E3, self.e), n.note(F3, self.s),

            n.note(C3, self.e + self.s), n.note(D3, self.e),
            n.note(E3, self.e), n.note(F3, self.e),
        ]

        m4 = [
            n.note(C3, self.e), n.note(D3, self.e),
            n.note(E3, self.e), n.note(F3, self.s),

            n.note(C3, self.e + self.s), n.note(D3, self.e),
            n.note(E3, self.s), n.note(E3, self.s), n.note(E3, self.s), n.note(E3, self.s),
        ]

        m4b = [
            n.note(C3, self.e), n.note(D3, self.e),
            n.note(E3, self.e), n.note(F3, self.s),

            n.note(C3, self.e + self.s), n.note(D3, self.e),
            n.note(C3, self.e), n.note(B2, self.e),
        ]

        v1 = m1 + m2 + m3 + m4
        v1b = m1 + m2 + m3 + m4b

        #   Verse 2 #
        m5 = [
            n.note(F3, self.e), n.note(D3, self.e),
            n.note(F3, self.s), n.note(D3, self.s), n.note(D3, self.s), 
            n.note(E3, self.e), rest(self.e), rest(self.s),
            rest(self.q)
        ]

        m6 = [
            n.note(D3, self.e), n.note(F3, self.e),
            n.note(D3, self.s), n.note(D3, self.s), n.note(F3, self.s),
            n.note(E3, self.e), rest(self.e + self.s),
            n.note(D3, self.e), n.note(D3, self.e)
        ]

        m7 = [
            n.note(D3, self.e), n.note(F3, self.e),
            n.note(D3, self.s), n.note(D3, self.s), n.note(F3, self.s),
            n.note(E3, self.e), rest(self.e + self.s),
            n.note(D3, self.q)
        ]
        v2 = m5 + m6 + m5 + m6
        v2b = m5 + m6 + m5 + m7


        #   Verse 3 #
        m9 = [
            n.note(F3, e), n.note(G3, e), # 1
            n.note(B3, s), n.note(A3, e), # 1.75

            n.note(F3, e), n.note(G3, e), # 2.75
            n.note(F3, s), n.note(B3, e), # 2.75
            n.note(A3, e),
        ]

        m10 = [
            n.note(F3, e), n.note(G3, e), # 1
            n.note(B3, s), n.note(A3, e), # 1.75

            n.note(B3, e), n.note(A3, s), n.note(G3, s), # 2.75
            
            n.note(F3, s), n.note(G3, s), n.note(A3, s),
            n.note(D3, s), n.note(E3, s),
            
        ]

        m11 = [
            n.note(F3 , e), n.note(G3, e), # 1
            n.note(G3, e), # 1.5
            n.note(E3, s), n.note(F3, e), # 2.25
            n.note(G3, e), n.note(G3, e), # 3.25
            rest(self.s), hey
        ]

        m12 = [
            n.note(F3 , e), n.note(G3, e), # 1
            n.note(G3, e), # 1.5
            n.note(E3, s), n.note(F3, e), # 2.25
            n.note(G3, e), n.note(G3, e), # 3.25
            rest(self.s),
            n.note(D3, s), n.note(E3, s),
        ]

        v3 = m9 + m10 + m11 + m12

        #   Refrain #
        refrain = [rest(self.whole * 2)]
        return \
            intro +\
            \
            v1 +\
            \
            v1b +\
            \
            v1b +\
            \
            v2 +\
            \
            v2b +\
            \
            v3 +\
            \
            v3 +\
            refrain


    def navi(self, part=""):
        return []
        n = Hey(amp=0.00001)

        m1 = [
            n.note(C1, self.q),
            rest(self.q),
            n.note(C1, self.q),
            rest(self.q)
        ]

        hey = n.note(C1, self.e)

        return \
        




def main():
   beat = Title(38)
   # 42 also works

   beat.produce_full()
   beat.save(beat.production, "01_Title")