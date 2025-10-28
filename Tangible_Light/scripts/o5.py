from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O5(Beat):
    


    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "05"))
        
        #   Bass    #
        self.bass1 = Tangible_Light.Title_Bass(amp=1.0, punchy=True, freq_mod=4)
        # self.bass1 = Bass_1(freq_mod = 1/8)
        self.bass2 = Bass()

        #   Synths  #
        self.synth1 = Tangible_Light.Whine(amp=0.4)
        # self.synth1 = DontTell2()
        self.synth2 = Clean_Key(amp=1.0)
        # self.synth3 = Clean_Key(amp=0.5, freq_mod=1.0,
        #                         attack = 0.01, decay = 0.1, sustain = 0.7, release = 0.01)

        # self.synth3 = Acoustic3(attack=0.01, decay=0.1, sustain=0.7, release=0.01,
        #                         vol_1=0.01, vol_2 =1.0, vol_3 = 0.01, vol_4 = 0.5, vol_5=0.0,vol_6=0.0, vol_7=0.0, vol_8=0.0)
        self.synth3 = WhinyString()
        self.reg = Bass()

        #   Percussion   #
        self.skirt1 = Skirt()
        self.skirt2 = Tap3(1.0, 120, 0.0, 0.5)

        # self.clap1 = PercussiveNoise(4.0, 14, 0.0, 0.1)
        self.clap1 = Rapping.Snare_1()
        # self.clap1 = Rapping.Snare_1()

        self.kick1 = Tap3(3.0, 25, noise_amount=0.01)
        self.cymbal1 = PercussiveNoise(1.0, 7, noise_amount=0.04) 
        self.chime1 = Tap3(attack=25, noise_amount=0.01)
        self.chime2 = Acoustic1()

        #   Instrument Dictionary   #
        self.instruments = {}
    

    def get_instruments(self, save = False):
        """Get each instrument's part. If save, then save each instrument."""
        instruments = {
            #   Bass    #
            # 0: [self.bass1, self.bass(save)],

            #   Middle Synths   #
            
            #   Melodic Synths   #

            #   Stringy Synths  #
            # 5: [self.synth2, self.synth_1(save)],
            # 5.5: [self.synth3, self.synth_3(save)],
            # 6: [self.reg, self.reggae(save)],

            #   Percussion  #
            # 1: [self.kick1, self.kicks(save)],
            2: [self.clap1, self.claps(save)],
            # 3: [self.clap1, self.cymbal(save)],
            # 4: [self.synth1, self.bell(save)],
            # 7: [self.chime1, self.chime(save, "v1")],
            # 8: [self.chime2, self.chime(save, "v2")],


            # 5: [self.chime1, self.],
        }

        return instruments
    
    def set_instruments(self, save = False):
        self.instruments = self.get_instruments(save)


    
    # def cow(self, save = False):
    #     s = self.skirt2

    #     m1 = [
    #         s.n()
    #     ]
    #     return
    def reggae(self, save = False):
        c = self.reg
        m1 = [
            rest(self.q),
            c.n(C2, self.e), rest(self.e),
            rest(self.q),
            c.n(C2, self.e), rest(self.e),
        ]

        m3 = [
            c.n(C2, self.q),
            c.n(C2, self.q),
            c.n(C2, self.q),
            c.n(C2, self.q),
        ]

        m2 = [
            rest(self.q),
            c.n(As1, self.e), rest(self.e),
            rest(self.q), 
            c.n(As1, self.e), rest(self.e),
        ]

        m4 = [
            c.n(D2, self.q),
            c.n(D2, self.q),
            c.n(D2, self.q),
            c.n(D2, self.q),
        ]

        v1 = m1 + m2 + m1 + m2
        off = [rest(self.w*4)]

        part = [rest(self.w*2)] + v1 + off + v1

        if save:
            self.save(part, "reggae")
        return part
    
    def kicks(self, save = False):
        k = self.kick1

        m0 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), rest(self.s), k.n(C1, self.s), rest(self.s),
        ]


        m1 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s), k.n(C1, self.s), rest(self.s),
        ]

        

        m2 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s),rest(self.s), k.n(C1, self.s), # 2
            k.n(C1, self.s), k.n(C1, self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), rest(self.s), k.n(C1, self.s), rest(self.s),
        ]

        m3 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s),rest(self.s), k.n(C1, self.s), # 2
            k.n(C1, self.s), k.n(C1, self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), k.n(C1, self.s), k.n(C1, self.s), k.n(C1, self.s), 
        ]

        
        m4 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s),rest(self.s), k.n(C1, self.s), # 2
            k.n(C1, self.s), k.n(C1, self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), rest(self.e), rest(self.s), 

        ]

        m5 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s), k.n(C1, self.s), rest(self.s),
        ]

        m6 = [
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s),
            k.n(C1, self.s), rest(self.s), rest(self.s), k.n(C1, self.s), 
            k.n(C1, self.s), k.n(C1, self.s), k.n(C1, self.s), k.n(C1, self.s),
        ]

        v1 =  m1 + m2 + m1 + m4
        v2 = m1 + m4 + m1 + m6

        v0 = [rest(self.w)] + m0
        off = [rest(self.w*4)]

        part = v0 + v1 + v1 + off
        if save:
            self.save(part, "kicks")
        return part
    
    def claps(self, save = False):
        c = self.clap1
        m0 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), c.n(C1, self.s),
            c.n(C1, self.s), rest(self.s), c.n(C1, self.e),
        ]
        
        m1 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), c.n(C1, self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
        ]

        m2 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), c.n(C1, self.e),
        ]

        # m2 = [
        #     rest(self.s), rest(self.s), rest(self.s), rest(self.s),
        #     c.n(C1, self.s), rest(self.s), rest(self.s), c.n(C1, self.s), 
        #     rest(self.s), rest(self.s), rest(self.s), c.n(C1, self.s),
        #     c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
        # ]

        m3 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), c.n(C1, self.s), 
        ]

        m4 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), c.n(C1, self.s),
            c.n(C1, self.s), rest(self.s), c.n(C1, self.e),
        ]

        

        v0 = [rest(self.w)] + m0
        v1 = m1 + m2 + m3 + m4


        #   V 2 #
        m7 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            c.n(C1, self.s), rest(self.s), c.n(C1, self.s/2), c.n(C1, self.s/2), c.n(C1, self.s),
        ]

        # v2 = m1 + m2 + m7 + m4
        v2 = [rest(self.w*2)] + m7 + m4


        part = v0 + v1 + v1 + v2
        if save:
            self.save(part, "claps")
        return part 
    

    def cymbal(self, save = False):
        c = self.cymbal1
        m1 = [
            c.n(C1, self.q),
            c.n(C1, self.q),
            c.n(C1, self.q),
            c.n(C1, self.q),
        ]

        v0 = [rest(self.w)] + m1
        v1 =  m1 + m1 + m1 + m1

        part = v0 + v1 + v1 + v1
        if save:
            self.save(part, "cymbal")
        return part
    
    def chime(self, save = False, variant = "v1"):
        if variant == "v1":
            c = self.chime1
        elif variant == "v2":
            c = self.chime2

        note = C3
        m1 = [
            rest(self.w - (self.s*3)),
            c.n(note, self.s), c.n(note, self.s), c.n(note, self.s),
        ]

        m2 = [
            rest(self.w - (self.s*3)), c.n(note, self.s),
            c.n(note, self.s/2), c.n(note, self.s/2), c.n(note, self.s),
        ]

        m4 = [
            rest(self.w - (self.s*2)),
            c.n(note, self.s/2), c.n(note, self.s/2), c.n(note, self.s),
        ]

        v1 =  m1 + m2 + m1 + m4
        
        #   Variant 2   #
        m5 = [
            rest(self.w - (self.s*3)),
            rest(self.s), c.n(note, self.e),
        ]

        m6 = [
            rest(self.w - (self.s*4)), c.n(note, self.s), rest(self.s),
            c.n(note, self.e),
        ]

        m8 = [
            rest(self.w - (self.s*2)),
            c.n(note, self.s/2), c.n(note, self.s/2), c.n(note, self.s),
        ]

        v2 = m5 + m6 + m5 + m6


        v0 = [rest(self.w*2)]
        part = v0 + v1 + v1 + v2

        if save:
            if variant == "v1":
                self.save(part, "chime 1")
            elif variant == "v2":
                self.save(part, "chime 2")

        return part
    
    def bell(self, save = False):
        c = self.synth1
        m1 = [
            rest(self.s), rest(self.s), c.n(G4, self.s), rest(self.s), rest(self.s),
            rest(self.e), rest(self.s),
            rest(self.s), c.n(G4, self.s), rest(self.s), rest(self.s),
            rest(self.e), c.n(G4, self.e)
        ]
        
        m2 = [
            rest(self.e), rest(self.s), c.n(F4, self.e),
            rest(self.q - self.s), 
            rest(self.s), rest(self.e), rest(self.s),
            rest(self.e), c.n(F4, self.e),
        ]

        m3 = [
            rest(self.e), c.n(G4, self.e), 
            rest(self.e), rest(self.e), # 2
            rest(self.s+self.e),
            c.n(G4, self.e), rest(self.s), c.n(G4, self.e),
        ]

        
        m4 = [
            rest(self.s), rest(self.s), rest(self.s), c.n(F4, self.e),
            rest(self.s*3), 
            rest(self.s), rest(self.s), rest(self.s), rest(self.s), 
            rest(self.s), rest(self.s), c.n(F4, self.e),
        ]

        v0 = [rest(self.w*2)]
        v1 =  m1 + m2 + m3 + m4

        #   V2  #
        m5 = [
            rest(self.w)
        ]
        m6 = [
            rest(self.t),
            rest(self.e), c.note(F4, self.e)
        ]

        v2 = m5 + m6 + m6 + m6

        part = v0 + v1 + v1 + v2
        if save:
            self.save(part, "bell")
        return part
    
    def bass(self, save = False):
        s = self.bass1
        
        m1 = [
            s.n(F4, self.e), s.n(F4, self.e), # 1
            s.n(F4, self.e), rest(self.s), # 1.75
            s.n(F4, self.e), s.n(F4, self.e), # 2.75
            s.n(F4, self.e), # 3.5
            s.n(G4, self.e + self.s),# 4
        ]

        m2 = [
            s.n(E4, self.e), s.n(E4, self.e),
            s.n(E4, self.e), rest(self.s),
            s.n(E4, self.e), s.n(E4, self.e),
            s.n(E4, self.s), rest(self.e),
            s.n(E4, self.e),
        ]

        m3 = [
            s.n(F4, self.e), rest(self.s), # 1
            s.n(F4, self.e), rest(self.e), # 1.75

            s.n(F4, self.e), s.n(F4, self.e), # 2.75
            s.n(F4, self.e), rest(self.s), # 3.5
            s.n(F4, self.e)
        ]

        m4 = [
            s.n(E4, self.e),  s.n(E4, self.e), # 1
            s.n(E4, self.e), # 2
            rest(self.s),  rest(self.s), # 2.75
            s.n(E4, self.e),
            rest(self.s), # 3.25
            s.n(G4, self.e),
            rest(self.s), # 3.5
            s.n(E4, self.e),# 4
        ]
        
        m5 = [
            s.n(F4, self.e), rest(self.s), #.75
            s.n(F4, self.e), rest(self.s), #1.5
            s.n(E4, self.e), # 2
            s.n(F4, self.e), rest(self.s), # 2.75
            s.n(F4, self.e), #3.5
            rest(self.s), s.n(F4, self.e)
        ]
        
        m6 = [
            s.n(E4, self.e),  s.n(E4, self.e), # 1
            s.n(E4, self.e), rest(self.e), # 2
            s.n(E4, self.e), rest(self.s),# 2.75
            s.n(E4, self.e), rest(self.s), # 3.5
            s.n(E4, self.e),
        ]

        v0 = [rest(self.w*2)]
        v1 = m3 + m4 + m5 + m6
        v2 = m1 + m2 + m3 + m4

        part = v0 + v1 + v1 + v2

        if save:
            self.save(part, "bass")
        return part
    
    def synth_1(self, save = False):
        s = self.synth2

        m0 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e),
            s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.s) + s.n(F4, self.s),
            rest(self.s),
            rest(self.s),
        ]

        m1 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.e) + s.n(F4, self.e), rest(self.s),# 4
        ]

        m2 = [
            s.n(E4, self.e, 1.5), s.n(E4, self.e, 1.5),
            s.n(E4, self.e, 1.5), s.n(E4, self.s, 1.5),
            s.n(E4, self.e, 1.5), s.n(E4, self.e, 1.5),
            s.n(E4, self.s, 1.5), rest(self.e),
            s.n(E4, self.e, 1.5),
        ]

        m3 = [
            s.n(F4, self.e), s.n(D4, self.e, 1.5), # 1
            s.n(D4, self.e, 1.5), s.n(E4, self.s), # 1.75

            s.n(F4, self.e), s.n(D4, self.e, 1.5), # 2.75
            s.n(D4, self.e, 1.5), s.n(D4, self.s, 1.5), # 3.5
            s.n(F4, self.e)
        ]

        m4 = [
            s.n(E4, self.e, 1.5),  s.n(E4, self.e, 1.5), # 1
            s.n(E4, self.e, 1.5), # 2
            s.n(E4, self.s, 1.5),  s.n(E4, self.e, 1.5), # 2.75
            s.n(E4, self.e, 1.5), # 3.25
            s.n(E4, self.e, 1.5),
            s.n(D4, self.s, 1.5), # 3.5
            s.n(E4, self.e, 1.5),# 4
        ]
        
        m5 = [
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #1.5
            s.n(E4, self.e), # 2
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), # 2.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), #3.5
            s.n(D4, self.s) + s.n(F4, self.s), s.n(D4, self.e) + s.n(F4, self.e)
        ]
        
        m6 = [
            s.n(E4, self.e),  s.n(E4, self.e), # 1
            s.n(E4, self.e), rest(self.e), # 2
            s.n(E4, self.s),  s.n(E4, self.e), # 2.75
            s.n(E4, self.e), s.n(E4, self.s), # 3.5
            s.n(E4, self.e),
        ]

        v0 = m0 + m2
        v1 = m3 + m4 + m5 + m6
        v2 = m1 + m2 + m3 + m4

        part = v0 + v1 + v1 + v2

        if save:
            self.save(part, "synth")
        return part
    
    def synth_3b(self, save = False, note = D4):
        s = self.synth3

        m0 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e),
            s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.s) + s.n(F4, self.s),
            rest(self.s),
            rest(self.s),
        ]

        m1 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.e) + s.n(F4, self.e), rest(self.s),# 4
        ]

        m2 = [
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.e, 1.5) + s.n(C4, self.e),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.s, 1.5) + s.n(C4, self.s),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.e, 1.5) + s.n(C4, self.e),
            s.n(E4, self.s, 1.5) + s.n(C4, self.s), rest(self.e),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e),
        ]

        m3 = [
            s.n(D4, self.q) + s.n(F4, self.q), 
            rest(self.e),
            # s.n(D4, self.e, 1.5), # 1
            # s.n(D4, self.e, 1.5), 

            s.n(C4, self.s, 1.5) + s.n(E4, self.s), # 1.75

            s.n(D4, self.q + self.e, 1.5) + s.n(F4, self.q + self.e), rest(self.e), # 2.75

            s.n(D4, self.s, 1.5), # 3.5
            s.n(D4, self.e, 1.5) + s.n(F4, self.e)
        ]

        m4 = [
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),  s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 1
            s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 2
            s.n(E4, self.s, 1.5),  s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 2.75
            s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 3.25
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),
            s.n(D4, self.s, 1.5), # 3.5
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),# 4
        ]
        
        m5 = [
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #1.5
            s.n(E4, self.e), # 2
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), # 2.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), #3.5
            s.n(D4, self.s) + s.n(F4, self.s), s.n(D4, self.e) + s.n(F4, self.e)
        ]
        
        m6 = [
            s.n(E4, self.e) + s.n(C4, self.e),  s.n(E4, self.e) + s.n(C4, self.e), # 1
            s.n(E4, self.e) + s.n(C4, self.e), rest(self.e), # 2
            s.n(C4, self.s) + s.n(E4, self.s),  s.n(C4, self.e) + s.n(E4, self.e), # 2.75
            s.n(C4, self.e) + s.n(E4, self.e), s.n(E4, self.s), # 3.5
            s.n(C4, self.e) + s.n(E4, self.e),
        ]

        v0 = m0 + m2
        v1 = m3 + m4 + m5 + m6
        v2 = m1 + m2 + m3 + m4

        part = v0 + v1 + v1 + v2

        if save:
            self.save(part, "synth 2")
        return part
    
    def synth_3(self, save = False, note = D4):
        s = self.synth3

        m0 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e),
            s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.s) + s.n(F4, self.s),
            rest(self.s),
            rest(self.s),
        ]

        m1 = [
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 1
            s.n(D4, self.e) + s.n(F4, self.e), s.n(C4, self.s) + s.n(E4, self.s, 1.5), # 1.75
            s.n(D4, self.e) + s.n(F4, self.e), s.n(D4, self.e) + s.n(F4, self.e), # 2.75
            s.n(D4, self.e) + s.n(F4, self.e), # 3.5
            s.n(D4, self.e) + s.n(F4, self.e), rest(self.s),# 4
        ]

        m2 = [
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.e, 1.5) + s.n(C4, self.e),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.s, 1.5) + s.n(C4, self.s),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e), s.n(E4, self.e, 1.5) + s.n(C4, self.e),
            s.n(E4, self.s, 1.5) + s.n(C4, self.s), rest(self.e),
            s.n(E4, self.e, 1.5) + s.n(C4, self.e),
        ]

        m3 = [
            s.n(D4, self.q) + s.n(F4, self.q), # 1
            rest(self.e), s.n(C4, self.s, 1.5) + s.n(E4, self.s), # 2

            s.n(D4, self.q + self.e, 1.5) + s.n(F4, self.q + self.e), # 3.5
            s.n(D4, self.e + self.s, 1.5) + s.n(F4, self.e + self.s)
        ]

        m4 = [
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),  s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 1
            s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 2
            s.n(E4, self.s, 1.5),  s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 2.75
            s.n(C4, self.e) + s.n(E4, self.e, 1.5), # 3.25
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),
            s.n(D4, self.s, 1.5), # 3.5
            s.n(C4, self.e) + s.n(E4, self.e, 1.5),# 4
        ]
        
        m5 = [
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), #1.5
            s.n(E4, self.e), # 2
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), rest(self.s), # 2.75
            s.n(D4, self.e, 1.5) + s.n(F4, self.e), #3.5
            s.n(D4, self.s) + s.n(F4, self.s), s.n(D4, self.e) + s.n(F4, self.e)
        ]
        
        m6 = [
            s.n(E4, self.e) + s.n(C4, self.e),  s.n(E4, self.e) + s.n(C4, self.e), # 1
            s.n(E4, self.e)+ s.n(C4, self.e), rest(self.e), # 2
            s.n(C4, self.s) + s.n(E4, self.s),  s.n(C4, self.e) + s.n(E4, self.e), # 2.75
            s.n(C4, self.e) + s.n(E4, self.e), s.n(E4, self.s), # 3.5
            s.n(C4, self.e) + s.n(E4, self.e),
        ]

        v0 = m0 + m2
        v1 = m3 + m4 + m5 + m6
        v2 = m1 + m2 + m3 + m4

        part = v0 + v1 + v1 + v2

        if save:
            self.save(part, "synth 2")
        return part
    
def main():
    beat = O5(43)

    #   Export each instrument  #
    beat.export_full()

    #   Export the full beat    #
    # beat.set_instruments(save=False)
    # beat.produce_full()
    # beat.save(beat.production, "05", convert=False)

