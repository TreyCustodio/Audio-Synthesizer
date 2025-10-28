from modules.beat import *
from modules.instruments import *
from modules.audio import *

class First(Beat):
    


    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "03"))
        
        #   Bass    #
        self.bass1 = Bass(amp=0.3)
        self.bass2 = Bass()

        #   Synths  #
        self.synth1 = First4()
        self.synth2 = Church(amp = 0.1)
        self.synth3 = Tangible_Light.Bell()

        #   Drums   #
        self.skirt1 = Skirt()
        self.skirt2 = Skirt()

        self.clap1 = Tap3(1.0, 40, 0.0, 0.7)
        self.kick1 = Tap3(3.0, 25, noise_amount=0.01)

        #   Instrument Dictionary   #
        self.instruments = {}
    

    def get_instruments(self, save = False):
        """Get each instrument's part. If save, then save each instrument."""
        instruments = {
            #   Baseline    #
            0: [self.bass1, self.bass(save)],

            #   Middle Synths   #
            1: [self.bass2, self.high_bass(save)],
            2: [self.bass2, self.high_bass2(save)],
            
            #   Melodic Synths   #
            3: [self.synth1, self.synth_1(save)],
            4: [self.synth2, self.synth_2(save)],
            5: [self.synth3, self.synth_3(save)],


            #   Percussion  #
            6: [self.skirt1, self.skirts(save)],
            7: [self.skirt2, self.bongo(save)],
            8: [self.skirt2, self.chime(save)],
            9: [self.clap1, self.claps(save)],
            10: [self.kick1, self.kicks(save)],

        }

        return instruments
    
    def set_instruments(self, save = False):
        self.instruments = self.get_instruments(save)

    def bass(self, save=False):
        b = self.bass1

        m1 = [
            b.note(C1, self.q),
            rest(self.e), b.note(C1, self.s),
            b.note(C1, self.e), b.note(C1, self.s),
            rest(self.e), b.note(C1, self.e), rest(self.e)
        ]

        m2 = [
            b.note(C1, self.e), rest(self.h + self.s),
            b.note(C1, self.s), b.note(C1, self.e), b.note(C1, self.s), rest(self.s)
        ]
        
        v1 = m1 + m1 + m1 + m1

        part = \
        v1 +\
        m2

        if save:
            self.save(part, "03_bass")
        return part

    def high_bass(self, save = False):
        f = self.bass1

        m1 = [
            delaycombo(f.note(D2, self.e), f.note(F2, self.e), 0.05), rest(self.e - 0.05),
            rest(self.trey - self.e),
            f.note(D2, self.e) + f.note(F2, self.e),
        ]

        m2 = [
            f.note(D2, self.e) + f.note(F2, self.e), 
            rest(self.trey),
            f.note(D2, self.e) + f.note(F2, self.e)
        ]

        m3 = [
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey), # 3
        ]

        m4 = [
            f.note(C2, self.e) + f.note(E2, self.e), f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey - self.e),
            f.note(C2, self.e) + f.note(E2, self.e)
        ]

        m5 = [
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey - self.e), # 3
            f.note(C2, self.e) + f.note(E2, self.e),
        ]

        m6 = [
            f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey),
            f.note(C2, self.e) + f.note(E2, self.e)
        ]

        v1 = m1 + m2 + m3 + m4
        v2 = m1 + m2 + m5 + m6

        part =  \
        [rest(self.whole * 4)] +\
        [rest(self.whole)] +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_highbass_1")
        return part

    def high_bass2(self, save = False):
        f = self.bass1

        m7 = [
            rest(self.q), 
            f.note(D2, self.e), 
            f.note(C2, self.s), f.note(D2, self.e),
            rest(self.s + self.e + self.q)
        ]

        m8 = [
            rest(self.q),
            f.note(E2, self.e), 
            f.note(D2, self.s), f.note(E2, self.e),
            rest(self.s + self.q + self.e)
        ]

        m9 = [
            rest(self.q),
            f.note(E2, self.e), 
            f.note(D2, self.s), f.note(E2, self.e),
            
            rest(self.s), # 2.5
            f.note(D2, self.s), f.note(D2, self.s), # 3
            f.note(D2, self.s), f.note(D2, self.s), #3.5
            f.note(D2, self.s), f.note(D2, self.s), # 4
        ]

        v1 = m7 + m7 + m8 + m8
        v2 = m7 + m7 + m8 + m9

        part =  \
        [rest(self.whole *4)] +\
        [rest(self.whole)] +\
        \
        v1 +\
        v2 +\
        \
        v1 +\
        v2

        if save:
            self.save(part, "03_highbass_2")
        return part

    def intro_drums(self, save=False):
        d = self.skirt1

        intro = rest(self.whole * 5)
        m1 = build_measure(
            d.note(C3, self.e)(), d.note(C3, self.e)(),
            d.note(C5, self.e)(), d.note(C3, self.s)(), d.note(C5, self.s)(),
            d.note(C3, self.s)(), d.note(C5, self.s)(), d.note(C5, self.e)(),
            d.note(B4, self.e),
            rest(self.e)
        )

        v1 = build_measure(
            m1, m1, m1, m1
        )

        v1 = fade_in(v1, 1.0)

        final = add_waves(intro, v1)

        part = final
        if save:
            self.save(part, "03_intro_drums")
        return part
    
    
    
    def skirts(self, save = False):
        d = self.skirt1
        amps = np.geomspace(0.1, 1.0, 16*4)
        intro = [rest(self.whole * 5)]
        m1 = [
            d.note(C3, self.e, amps[0]), d.note(C3, self.e, amps[2]),
            rest(self.e), d.note(C3, self.s, amps[6]), rest(self.s),
            d.note(C3, self.s, amps[8]), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]

        m2 = [
            d.note(C3, self.e, amps[16]), d.note(C3, self.e, amps[18]),
            rest(self.e), d.note(C3, self.s, amps[22]), rest(self.s),
            d.note(C3, self.s, amps[24]), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]

        m3 = [
            d.note(C3, self.e, amps[32]), d.note(C3, self.e, amps[34]),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e), 
        ]

        m4 = [
            d.note(C3, self.e, amps[48]), d.note(C3, self.e, amps[50]),
            rest(self.e), d.note(C3, self.s, amps[54]), rest(self.s),
            d.note(C3, self.s, amps[56]), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]


        v0 = m1 + m2 + m3 + m4

        m5 = [
            d.note(C3, self.e), d.note(C3, self.e),
            rest(self.e), d.note(C3, self.s), rest(self.s),
            d.note(C3, self.s), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]

        m6 = [
            d.note(C3, self.e), d.note(C3, self.e),
            rest(self.e), d.note(C3, self.s), rest(self.s),
            d.note(C3, self.s), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]

        m7 = [
            d.note(C3, self.e), d.note(C3, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e), 
        ]

        m8 = [
            d.note(C3, self.e), d.note(C3, self.e),
            rest(self.e), d.note(C3, self.s), rest(self.s),
            d.note(C3, self.s), rest(self.s), rest(self.e),
            rest(self.e),
            rest(self.e),
        ]

        v1 = m5 + m6 + m7 + m8

        off_verse = [rest(self.whole*4)]

        part =  \
        intro +\
        \
        v0 +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_skirts")
        return part
    
    def bongo(self, save = False):
        d = self.skirt2

        intro = [rest(self.whole * 5)]
        m1 = [
            rest(self.e), rest(self.e),
            d.note(C5, self.e), rest(self.s), d.note(C5, self.s),
            rest(self.s), d.note(C5, self.s), d.note(C5, self.e),
            rest(self.e),
            rest(self.e)
        ]

        m2 = [
            rest(self.e), rest(self.e),
            d.note(C5, self.e), rest(self.s), d.note(C5, self.s),
            rest(self.s), d.note(C5, self.s), d.note(C5, self.e),
            rest(self.e),
            rest(self.e),
        ]

        m3 = [
            rest(self.e), rest(self.e),
            d.note(C5, self.e), rest(self.e),
            rest(self.e), d.note(C5, self.e),
            rest(self.e), rest(self.e), 
        ]

        v1 = m1 + m2 + m3 + m2
        
        off_verse = [rest(self.whole*4)]

        part =  \
        intro +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_bongo")
        return part
    

    def chime(self, save = False):
        d = self.skirt2

        intro = [rest(self.whole * 5)]
        m1 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.e),
            d.note(B4, self.e),
            rest(self.e)
        ]

        m2 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.s), rest(self.s),
            rest(self.s), rest(self.s), rest(self.e),
            d.note(B4, self.e),
            d.note(B4, self.e),
        ]

        m3 = [
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            d.note(B4, self.e), rest(self.e), 
        ]

        v1 = m1 + m2 + m3 + m2
        
        off_verse = [rest(self.whole*4)]

        part =  \
        intro +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_chime")
        return part

    def claps(self, save = False):
        c = self.clap1

        intro = [rest(self.whole*5)]
        off_verse = [rest(self.whole*4)]
        

        m1 = [
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.s),
            rest(self.e), rest(self.s),
            rest(self.e),
            c.note(C2, self.e),
            rest(self.e),
        ]

        m2 = [
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.s),
            rest(self.e), rest(self.s),
            rest(self.e),
            c.note(C2, self.e),
            c.note(C2, self.e),
        ]

        m3 = [
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.s),
            rest(self.e), rest(self.s), # 3.5

            c.note(C2, self.e), c.note(C2, self.e), # 2nd half beat 3
            rest(self.s*2)
        ]

        m4 = [
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.s),
            rest(self.e), rest(self.s),
            c.note(C2, self.e),
            c.note(C2, self.e) + rest(self.e),
            c.note(C2, self.e) + rest(self.e),
        ]

        v1 = m1 + m2 + m3 + m4

        part = \
        intro +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_claps")
        return part
    
    def kicks(self, save = False):
        s = self.kick1

        intro = [rest(self.whole*5)]
        off_verse = [rest(self.whole*4)]

        m1 = [
            s.note(C2, self.e), s.note(C2, self.e),
            rest(self.e), s.note(C2, self.s),
            s.note(C2, self.e), s.note(C2, self.s),
            s.note(C2, self.e),
            rest(self.e),
            rest(self.e),
        ]

        m2 = [
            s.note(C2, self.e), s.note(C2, self.e),
            rest(self.e), s.note(C2, self.s),
            s.note(C2, self.e), s.note(C2, self.s),
            s.note(C2, self.e),
            s.note(C2, self.e),
            s.note(C2, self.e),
        ]

        m3 = [
            s.note(C2, self.e), s.note(C2, self.e),
            rest(self.e), s.note(C2, self.s),
            s.note(C2, self.s),s.note(C2, self.s), s.note(C2, self.s), # 3.5

            rest(self.e), rest(self.e), # 2nd half beat 3
            rest(self.s*2)
        ]


        m4 = [
            s.note(C2, self.e), s.note(C2, self.e),
            rest(self.e), s.note(C2, self.s),
            s.note(C2, self.e), s.note(C2, self.s),
            s.note(C2, self.e),
            s.note(C2, self.e),
            s.note(C2, self.e),
        ]

        v1 = m1 + m2 + m3 + m4

        part =  \
        intro +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_kicks")
        return part


    def synth_1(self, save = False):
        f = self.synth1

        m1 = [
            f.note(F3, self.e), f.note(A3, self.s),
            f.note(B3, self.e), f.note(C4, self.e),
            f.note(D4, self.e), f.note(C4, self.s),
            f.note(B3, self.e), f.note(A3, self.q)
        ]

        m2 = [
            rest(self.e), f.note(A3, self.s),
            f.note(B3, self.e), f.note(C4, self.e),
            f.note(D4, self.e), f.note(C4, self.s),
            f.note(B3, self.e), f.note(A3, self.e), f.note(G3, self.e)
        ]

        m3 = [
            f.note(E3, self.e), f.note(G3, self.s),
            f.note(A3, self.e), f.note(B3, self.e),
            f.note(C4, self.e), f.note(B3, self.s),
            f.note(A3, self.e), f.note(G3, self.q)
        ]

        m4 = [
            rest(self.e), f.note(G3, self.s),
            f.note(A3, self.e), f.note(B3, self.e),
            f.note(C4, self.e), f.note(B3, self.s),
            f.note(A3, self.e), f.note(G3, self.e), f.note(F3, self.e)
        ]

        v1 = m1 + m2 + m3 + m4
        intro = [rest(self.whole * 5)]
        off_verse = [rest(self.whole * 4)]
        
        part =  \
        intro +\
        \
        off_verse +\
        off_verse +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_synth_1")
        return part

    def synth_2(self, save = False):
        f = self.synth2

        m1 = [
            f.note(F3, self.e), f.note(A3, self.s),
            f.note(B3, self.e), f.note(C4, self.e),
            f.note(D4, self.e), f.note(C4, self.s),
            f.note(B3, self.e), f.note(A3, self.q)
        ]

        m2 = [
            rest(self.whole)
        ]

        m3 = [
            f.note(E3, self.e), f.note(G3, self.s),
            f.note(A3, self.e), f.note(B3, self.e),
            f.note(C4, self.e), f.note(B3, self.s),
            f.note(A3, self.e), f.note(G3, self.q)
        ]

        m4 = [
            rest(self.e), f.note(G3, self.s),
            f.note(A3, self.e), f.note(B3, self.e),
            f.note(C4, self.e), f.note(B3, self.s),
            f.note(A3, self.e), f.note(G3, self.e), f.note(F3, self.e)
        ]

        v1 = m1 + m2 + m3 + m4
        intro = [rest(self.whole * 5)]
        off_verse = [rest(self.whole * 4)]
        
        part =  \
        intro +\
        \
        off_verse +\
        off_verse +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_synth_2")
        return part


    def synth_3(self, save = False):
        s = self.synth3

        m1 = [
            s.n(C4, self.e), s.n(D4, self.e),
            s.n(E4, self.e), rest(self.e),
            s.n(C4, self.e), s.n(D4, self.s),
            s.n(E4, self.e), rest(self.e + self.s)
        ]

        m2 = [
            s.n(C4, self.e), s.n(D4, self.e),
            s.n(E4, self.e), s.n(C4, self.e),
            s.n(E4, self.q),
            s.n(D4, self.e + self.s),
            rest(self.s*1)
        ]

        m3 = [
            s.n(B3, self.e), s.n(C4, self.e),
            s.n(D4, self.e), rest(self.e),
            s.n(B3, self.e), s.n(C4, self.s),
            s.n(D4, self.e), rest(self.e + self.s)
        ]

        m4 = [
            s.n(B3, self.e), s.n(C4, self.e),
            s.n(D4, self.e), s.n(B3, self.e),
            s.n(D4, self.q),
            s.n(C4, self.e + self.s), rest(self.s*1)
        ]

        v1 = m1 + m2 + m3 + m4
        intro = [rest(self.whole * 5)]
        off_verse = [rest(self.whole * 4)]
        
        part =  \
        intro +\
        \
        off_verse +\
        off_verse +\
        \
        off_verse +\
        off_verse +\
        \
        v1 +\
        v1

        if save:
            self.save(part, "03_synth_3")
        return part
    

    def whistles_old(self, variation = ""):
        # l, l, s, s, s, l x2 then go down

        p = First2()

        m1 = build_measure(
            p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
            rest(self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
        )
        m2 = build_measure(
            p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
            rest(self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.q)
        )

        m3 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.e), rest(self.e)

        )

        m4 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
        )

        v1 = build_measure(m1, m2, m3, m4) * 0.2

        if variation == "chopped":
            #   Chopped Versions    #
            m5 = build_measure(
                p.note(A4, self.e + self.s), rest(self.q - (self.e + self.s)),
                rest(self.quarter + self.s*2),
                p.note(B4, self.s), p.note(C5, self.s),
                p.note(D5, self.q)
            )

            m6 = build_measure(
                p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
                p.note(D5, self.e), p.note(C5, self.e) *1.5,
                
                rest(self.e), p.note(C5, self.e) * 2.0,
                rest(self.q)
            )

            m7 = build_measure(
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s), p.note(A4, self.e), 
                rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s),
                p.note(A4, self.e), rest(self.e)

            )

            m8 = build_measure(
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s), p.note(A4, self.e), 
                rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s),
                p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
            )

            return build_measure(m5, m6, m7, m8) * 0.2
        
        elif variation == "chopped2":

            m9 = build_measure(
                p.note(A4, self.s), rest(self.s), p.note(A4, self.e),
                rest(self.q + self.e),
                p.note(B4, self.s), p.note(C5, self.s),
                p.note(D5, self.q)
            )

            m10 = build_measure(
                p.note(B4, self.s), p.note(C5, self.s), p.note(D5, self.e),

                p.note(D5, self.s), p.note(C5, self.s), p.note(B4, self.s), p.note(D5, self.e),
                p.note(B4, self.s), p.note(C5, self.e), # 3/4
                
                p.note(D5, self.e), p.note(C5, self.e)
            )

            m11 = build_measure(
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s), p.note(A4, self.e), 
                rest(self.e), rest(self.s), p.note(A4, self.e),
                rest(self.q)
            )

            m12 = build_measure(
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s), p.note(A4, self.e), 
                rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s),
                p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
            )

            return build_measure(m9, m10, m11, m12) * 0.2




        elif variation == "chopped3":

            m13 = build_measure(
                p.note(A4, self.s), rest(self.s), p.note(A4, self.e),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.s), rest(self.s),
            )

            m14 = build_measure(
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                p.note(A4, self.s), rest(self.s), p.note(A4, self.e),
            )

            m15 = build_measure(
                p.note(G4, self.s), rest(self.s), p.note(G4, self.e),
                rest(self.e), p.note(G4, self.s), rest(self.s),
                rest(self.e), p.note(G4, self.s), rest(self.s),
                rest(self.e), p.note(G4, self.e),
            )

            m16 = build_measure(
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s), p.note(A4, self.e), 
                rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
                p.note(B4, self.s),
                p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
            )

            return build_measure(m13, m14, m15, m16) * 0.2


        elif variation == "chopped4":
            m17 = build_measure(
                p.note(A4, self.s), rest(self.s), p.note(A4, self.e),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.e),
                p.note(E5, self.e), p.note(D5, self.s), rest(self.s)
            )

            m18 = build_measure(
                p.note(A4, self.s), rest(self.s), p.note(A4, self.e),
                rest(self.e), p.note(A4, self.s), rest(self.s),
                rest(self.e), p.note(A4, self.e),
                p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s), 
            )

            m19 = build_measure(
                p.note(G4, self.s), rest(self.s), p.note(G4, self.e),
                rest(self.e), p.note(G4, self.s), rest(self.s),
                rest(self.e), p.note(G4, self.e),
                p.note(D5, self.e), p.note(C5, self.s), rest(self.s)
            )

            m20 = build_measure(
                p.note(G4, self.s), rest(self.s), p.note(G4, self.e),
                rest(self.e), p.note(G4, self.s), rest(self.s),
                rest(self.e), p.note(G4, self.e),
                p.note(C5, self.e), p.note(D5, self.s), rest(self.s)
            )

            return build_measure(m17, m18, m19, m20) * 0.2


        elif variation == "faded":
            return build_measure(m1, m2, fade_out(add_waves(m3, m4), 10.0))
        
        elif variation == "intro":
            return build_measure(m1, m2, m3, m4)

        return v1




    def synth_old(self, variation = ""):
        f = Bass()
        #   Notes to be sung    #
        # m1 = build_measure(
        #     f.note(D2, self.q),
        #     f.note(D2, self.e), f.note(E2, self.s),
        #     f.note(F2, self.e), f.note(G2, self.e),
        #     f.note(A2, self.e),
        #     rest(self.s * 3)
        # )

        # m2 = build_measure(
        #     f.note(D2, self.e), f.note(E2, self.s),
        #     f.note(F2, self.e), f.note(G2, self.e),
        #     f.note(A2, self.e),
        #     f.note(G2, self.q + self.s*3)
        # )

        # m3 = build_measure(
        #     rest(self.q),
        #     f.note(C2, self.e), f.note(D2, self.s),
        #     f.note(E2, self.e), f.note(F2, self.e),
        #     f.note(G2, self.e), rest(self.s * 2),
        #     f.note(C2, self.s)
        # )

        # m4 = build_measure(
        #     f.note(C2, self.e), f.note(D2, self.s),
        #     f.note(E2, self.e), f.note(F2, self.e),
        #     f.note(G2, self.e),
        #     f.note(F2, self.q + self.s*3)
        # )


        #   V1 - supporting tenor in Chorus/Verse   #
        m1 = build_measure(
            delaycombo(f.note(D2, self.e), f.note(F2, self.e), 0.05), rest(self.e - 0.05),
            rest(self.trey - self.e),
            f.note(D2, self.e) + f.note(F2, self.e),
        )

        m2 = build_measure(
            f.note(D2, self.e) + f.note(F2, self.e), 
            rest(self.trey),
            f.note(D2, self.e) + f.note(F2, self.e)

        )

        m3 = build_measure(
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey), # 3
           
        )

        m4 = build_measure(
            f.note(C2, self.e) + f.note(E2, self.e), f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey - self.e),
            f.note(C2, self.e) + f.note(E2, self.e)
            
        )

        m5 = build_measure(
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey - self.e), # 3
            f.note(C2, self.e) + f.note(E2, self.e),
        )

        m6 = build_measure(
            f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey),
            f.note(C2, self.e) + f.note(E2, self.e)
        )

        m7 = build_measure(
            rest(self.q), f.note(D2, self.e), 
            f.note(C2, self.s), f.note(D2, self.e),
            rest(self.s + self.q)
        )

        m8 = build_measure(
            rest(self.q), f.note(E2, self.e), 
            f.note(D2, self.s), f.note(E2, self.e),
            rest(self.s + self.q)
        )

        m1 = combine(m1, m7)
        m2 = combine(m2, m7)
        m3 = combine(m3, m8)
        m4 = combine(m4, m8)


        m9 = build_measure(
            rest(self.q + self.q + self.e),
            # leaving self.s + self.q
            f.note(D2, self.s), f.note(D2, self.s), f.note(D2, self.s), f.note(D2, self.s),
            f.note(D2, self.s), f.note(D2, self.s),
        )

        m4 = combine(m4, m9)
        m6 = combine(m6, m8)
        

        v1 = build_measure(m1, m2, m3, m4)

        v1b = build_measure(m1, m2, m5, m6)


        #   V2 - supporting tenor   #
        amp1 = 0.5

        m5 = build_measure(
            f.note(F1, self.q),
            rest(self.h),
            f.note(F1, self.q)
        )

        m6 = build_measure(
            f.note(F1, self.q),
            rest(self.h),
            f.note(F1, self.q)
        )

        m7 = build_measure(
            f.note(E1, self.q),
            rest(self.h),
            f.note(E1, self.q)
        )

        m8 = build_measure(
            f.note(E1, self.q),
            rest(self.h),
            f.note(E1, self.q)
        )

        m5b = build_measure(
            f.note(F2, self.q),
            rest(self.h),
            f.note(F2, self.q)
        ) * amp1

        m6b = build_measure(
            f.note(F2, self.q),
            rest(self.h),
            f.note(F2, self.q)
        ) * amp1

        m7b = build_measure(
            f.note(E2, self.q),
            rest(self.h),
            f.note(E2, self.q)
        ) * amp1

        m8b = build_measure(
            f.note(E2, self.q),
            rest(self.h),
            f.note(E2, self.q)
        ) * amp1

        m5 += m5b
        m6 += m6b
        m7 += m7b
        m8 += m8b

        v2 = build_measure(m5, m6, m7, m8)


        #   Return  #
        if variation == "v1":
            return v1
        
        elif variation == "v1b":
            return v1b

        elif variation == "v2":
            return v2
        
        elif variation == "refrain":
            bar = build_measure(
                rest(self.whole - self.e),
                f.note(D2, self.e) + f.note(F2, self.e),
                
                rest(self.whole - self.q),
                f.note(D2, self.e) + f.note(F2, self.e), f.note(C2, self.e) + f.note(E2, self.e),

                rest(self.whole - self.e),
                f.note(B1, self.e) + f.note(D2, self.e),

                rest(self.whole - self.q - self.s),
                f.note(A1, self.s) + f.note(C2, self.s), 
                f.note(C2, self.s) + f.note(E2, self.s), 
                f.note(C2, self.s)+ f.note(E2, self.s), f.note(C2, self.s) + f.note(E2, self.s), f.note(C2, self.s) + f.note(E2, self.s),
                )


            return bar

        else:
            return v1, v2


    def drums2_old(self, variation=""):
        c = Cymbal()
        s = Snare()
        b = Bass()
        d = Skirt()

        m0 = build_measure(
            s.note(C2, self.e), s.note(C2, self.e),
            c.note(C3, self.e) + s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e),
            c.note(C3, self.e) + s.note(C3, self.e),
            rest(self.e),
        )

        if variation == "refrain":
            return m0 * 3.0

    

        

def main():
    beat = First(62)
    beat.export_full()

