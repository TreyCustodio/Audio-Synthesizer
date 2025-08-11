from . import *

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

        #   Keys    #
        self.synth1 = LowSynth(amp=0.2)
        self.synth2 = Tangible_Light.Title_Synth(amp=0.3)


        # self.horn1 = Horn(amp=0.7)
        self.string1 = WhinyString(amp=0.2)

        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=1.0, freq_mod = 2)
        
        #   Percussion  #
        self.kick1 = Tap3(amp=5, attack=25, noise_amount=0.0)
        self.hats1 = HipSkirt(attack=135, amp=0.2, low=0, high=0, dist=8.0, noise_amount=0.6)
        self.crash1 = Tap3(amp=0.1, attack=10, noise_amount=3.0)
        self.crash2 = HipSkirt(attack=20, amp=0.1, low=0, high=0, dist=12.0, noise_amount=1.0)

        #   Adlibs  #
        self.instr8 = Hey()

        self.intro = [rest(self.w*2)]

        self.instruments = {
            #   Keys    #
            0: [self.synth1, self.keys("v1")],
            1: [self.synth2, self.keys("v2")],
            # 2: [self.horn1, self.horns()],
            2: [self.string1, self.strings()],

            #   Bass    #
            3: [self.bass1, self.bass("v1")],
            
            #  Percussion  #
            4: [self.kick1, self.kick()],
            5: [self.hats1, self.drums()],
            6: [self.crash1, self.crash()],




            #  Adlibs  #
            # 8: [self.instr8, self.navi()]
        }

        self.intro_instruments = {
            0: (self.kick1, self.drums_intro()),
            1: (self.string1, self.strings_intro()),

        }


    def save(self, sound, name = "", norm=True, convert=True):
        """Save the sound to the desired folder"""
        super().save(sound, name, norm, convert, os.path.join("Tangible_Light", "ost"))

    def produce_intro(self):
        self.instruments = self.intro_instruments
        self.produce_full()
        self.save(self.production, "01_intro", convert=False)

    
    def drums_intro(self):
        d = self.kick1

        m1 = [
            d.note(C1, self.e), rest(self.e), # 1
            d.note(D1, self.e), rest(self.e), # 2
            rest(self.s), d.note(C1, self.s), rest(self.e), # 3
            d.note(C1, self.e), d.note(D1, self.e) # 4
        ]

        v1 = m1 + m1
        self.save(v1, "01_intro_drum")

        return v1
    
    def strings_intro(self):
        amp = 1.0
        n = self.string1
        s = self.s
        e = self.e
        q = self.q


        #   Verse 1 #
        m2 = [
            n.n(C4, self.w)
        ]

        v1 = m2 + m2

        self.save(v1, "01_intro_string")

        
        
        return v1


    
    

    def strings(self):
        s = self.string1
        amp = 1.0

        m1 = [
            s.n(F3, self.s*3),
            s.n(F3, self.s), # 1

            rest(self.s+self.q),
            s.note(F3, self.s*3),
            s.note(F3, self.e), s.note(F3, self.e)
        ]

        m2 = [
            s.n(F3, self.s*3),
            s.n(F3, self.s), # 1

            rest(self.s+self.q),
            s.note(F3, self.s*3),
            s.note(F3, self.e), s.note(G3, self.e)
        ]


        m3 = [
            s.n(D3, self.w-self.e, amp),
            s.n(C3, self.e, amp)
        ]

        m4 = [
            s.n(D3, self.w, amp),
        ]

        v1 = m1 + m2 + m3 + m4
        

        #   V2  #
        m5 = [
            rest(self.e), s.n(D3, self.e), # 1
            s.n(F3, self.e), s.n(G3, self.s), # 1.75
            s.n(D3, self.e + self.s),# 2.75
            s.n(F3, self.e), s.n(G3, self.q), # 4
        ]

        m5b = [
            s.n(D3, self.e), # 1
            s.n(F3, self.e), s.n(G3, self.s), # 1.75
            s.n(D3, self.e + self.s),# 2.75
            s.n(F3, self.e), s.n(G3, self.q), # 4
        ]
        
        m6 = [
            rest(self.e), s.n(C3, self.e), # 1
            s.n(E3, self.e), s.n(F3, self.s), # 1.75
            s.n(C3, self.e + self.s),# 2.75
            s.n(E3, self.e), s.n(F3, self.q), # 4
        ]

        m6b = [
            s.n(C3, self.e), # 1
            s.n(E3, self.e), s.n(F3, self.s), # 1.75
            s.n(C3, self.e + self.s),# 2.75
            s.n(E3, self.e), s.n(F3, self.q), # 4
        ]
        v2 = m5 + m5 + m6 + m6
        

        #   V3  #
        m7 = [
            rest(self.e), s.n(F3, self.e),
            s.n(F3, self.q),
            s.n(E3, self.e + self.s),
            s.n(E3, self.e + self.s),
            s.n(E3, self.q)
        ]

        m8 = [
            s.n(F3, self.e),
            s.n(F3, self.q),
            s.n(E3, self.e + self.s),
            s.n(E3, self.e + self.s),
            s.n(D3, self.e)
        ]

        m9 = [
            s.n(C3, self.e + self.s), # .75
            s.n(C3, self.s), s.n(A2, self.e), # 1.5

            s.n(C3, self.e + self.s), # 2.25
            s.n(C3, self.s), s.n(A2, self.e), # 3

            s.n(C3, self.e), s.n(B2, self.e) # 4
        ]

        v3 = m7 + m8 + m9 + m9
        off = [rest(self.w*4)]

        #   V4  #
        m10 = [
            rest(self.e), s.n(D3, self.e), # 1
            s.n(F3, self.e), s.n(G3, self.s), # 1.75
            s.n(D3, self.e + self.s),# 2.5
            s.n(F3, self.e), s.n(G3, self.q), # 4
        ]

        m11 = [
            rest(self.e), s.n(D3, self.e), # 1
            s.n(F3, self.e), s.n(G3, self.s), # 1.75
            s.n(A3, self.e),# 2.25
            s.n(G3, self.e + self.q + self.s), # 4
        ]

        m12 = [
            rest(self.e), s.n(C3, self.e), # 1
            s.n(E3, self.e), s.n(F3, self.s), # 1.75
            s.n(C3, self.e + self.s),# 2.75
            s.n(E3, self.e), s.n(F3, self.q), # 4
        ]

        m13 = [
            rest(self.e), s.n(C3, self.e), # 1
            s.n(E3, self.e), s.n(F3, self.s), # 1.75
            s.n(D3, self.q + self.s),# 2.75
            s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.s),# 3.75
        ]
        v4 = m10 + m11 + m12 + m13


        part =  \
        self.intro +\
        v4 +\
        off +\
        off +\
        v3 +\
        v3 +\
        off +\
        v2

        self.save(part, "01_strings")

        return part

    def horns(self):

        s  = self.horn1

        m1 = [s.note(D2, self.s*3), s.note(D2, self.s),  # 1
              rest(self.q + self.s), # 2
              s.note(D2, self.s*3), s.note(D2, self.e),
              s.note(D2, self.e),
              ]
        
        m2 = [s.note(C2, self.s*3), s.note(C2, self.s),  # 1
              rest(self.q + self.s), # 2
              s.note(C2, self.s*3), s.note(C2, self.e),
              s.note(C2, self.e),
              ]
        
        v1 = m1  + m1 + m2 + m2


        m3 = [
            s.n(D2, self.s*3), s.n(D2, self.s), s.n(A1, self.e),
            s.n(D2, self.e + self.s), s.n(D2, self.s), s.n(A1, self.e),
            s.n(D2, self.e), s.n(C2, self.e), # 3
        ]
        
        m4 = [
            s.n(As1, self.s*3), s.n(As1, self.s), s.n(G1, self.e),
            s.n(As1, self.e + self.s), s.n(As1, self.s), s.n(G1, self.e),
            s.n(As1, self.e), s.n(A1, self.e),

        ]
        v2 = m3 + m3 + m4 + m4
        part =  \
        self.intro +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        \
        v2 +\
        \
        v1 +\
        \
        v2 +\
        \
        v1


        self.save(part, "01_horns")
        return part

    def drums(self) -> list:
        
        d = self.hats1
        


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

        part =  \
        self.intro +\
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
    
        self.save(part, "01_drums")
        return part
    
    def kick(self) -> list:
        d = self.kick1

        m1 = [
            d.note(C1, self.e), rest(self.e), # 1
            d.note(D1, self.e), rest(self.e), # 2
            rest(self.s), d.note(C1, self.s), rest(self.e), # 3
            d.note(C1, self.e), d.note(D1, self.e) # 4
        ]
        
        intro = [rest(self.whole * 4)]
        v1 = m1 + m1 + m1 + m1

        refrain = [rest(self.whole * 2)]

        part = \
        self.intro +\
        v1 +\
        \
        v1 +\
        \
        v1 +\
        \
        v1 +\
        \
        v1 +\
        \
        v1 +\
        \
        v1
    
        self.save(part, "01_kick")
        return part

    def crash(self) -> list:
        d = self.crash1
        c = self.crash2

        m1 = [
            rest(self.q), # 1
            rest(self.e), c.note(C2, self.s), d.note(C3, self.e),# 2.25
            rest(self.s), # 2.5
            rest(self.e),# 3.0
            c.note(C2, self.e), d.note(C3, self.s), rest(self.s)# 4
        ]

        off_verse = [rest(self.whole*4)]
        v1 = m1 + m1 + m1 + m1
        
        part =  \
        self.intro +\
        off_verse +\
        \
        off_verse +\
        \
        v1 +\
        \
        off_verse +\
        v1 +\
        \
        off_verse +\
        v1

        self.save(part, "01_crash")
        return part
  

    def keys(self, part="") -> list:
        e = self.e
        q = self.q
        s = self.s

        if part == "v1":
            k = self.synth1

        elif part == "v2":
            k = self.synth2
        

        #   Intro   -- Silent --   #
        intro = [
            # rest(self.whole)
            ]

        #   Bass Solo   -- Silent --  #
        bass_solo = [rest(self.whole*4)]

        #   Verse 1 #
        m1 = [
            delaycombo(k.note(A3, q), k.note(F3, q - 0.08), 0.08, silence = False),

            delaycombo(k.note(G3, q), k.note(B3, q - 0.08), 0.08, silence = False),

            delaycombo(k.note(F3, s), k.note(A3, s - 0.04), 0.04, silence = False), delaycombo(k.note(G3, e), k.note(B3, e - 0.06), 0.06, False),
            
            delaycombo(k.note(A3, e), k.note(C4, e - 0.06), 0.06, False),
            delaycombo(k.note(B3, e + s), k.note(D4, e + s - 0.07), 0.07, False),
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

        part =  \
        self.intro +\
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
        
        self.save(part, "01_keys")
        return part


    def bass(self, part=""):
        n = self.bass1

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



        part = \
            self.intro +\
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
        
        self.save(part, "01_bass")
        return part

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

    # beat.produce_full()
    # beat.save(beat.production, "01_Title", convert=False)