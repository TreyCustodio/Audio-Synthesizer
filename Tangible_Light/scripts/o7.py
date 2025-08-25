from modules.beat import *
from modules.instruments import *
from modules.audio import *

class O7(Beat):

    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)
        
        #   Bass    #
        self.bass1 = Key_Harms(amp=0.4, freq_mod=0.25, harmonics = 1, attack=0.001, decay=0.00, sustain=1.0, release = 0.01, metal = False)

        #   Synths  #
        self.acou1 = Acoustic3(amp=0.3, freq_mod=1.0, sustain=1.0,
                               vol_3 = 1.0, vol_4 = 1.0)
        self.whistle1 = First4(amp=0.1, wave_1=False, wave_2=False)
        self.whistle2 = First4(amp=0.1, freq_mod=4, wave_1=False, wave_2=False)
        self.whistle3 = First4(amp=0.1, freq_mod=0.75, wave_1=False, wave_2=False)


        self.punch1 = First3(amp=0.1)
        self.synth1 = First4(amp=0.5, wave_2 = False, wave_3 = False)

        self.bell1 = Tangible_Light.Bell(amp=0.1, freq_mod=2)


        #   Percussion   #
        self.tap1 = Tap3(1.0, 120, 0.0, 0.5)
        self.clap1 = Rapping.Snare_1()

        self.kick1 = Tap3(3.0, 25, noise_amount=0.01)
        self.cymbal1 = PercussiveNoise(1.0, 7, noise_amount=0.04) 
        self.chime1 = Tap3(attack=25, noise_amount=0.01)
        self.chime2 = Acoustic1()

        #   Instrument Dictionary   #
        self.instruments = {}

        self.v0 = [rest(self.w*2)]
    

    def get_instruments(self, save = False):
        """Get each instrument's part. If save, then save each instrument."""
        instruments = {
            #   Bass    #
            1: [self.bass1, self.bass(save)],

            #   Middle Synths   #
            2: [self.acou1, self.acou_1(save)],
            22: [self.acou1, self.acou_1(save, "v2")],

            3: [self.whistle1, self.punch_1(save)],
            4: [self.punch1, self.whistles(save)],
            5: [self.synth1, self.synth_1(save)],
            6: [self.whistle2, self.whistles_2(save)],
            62: [self.whistle3, self.whistles(save, "v2")],

            
            #   Melodic Synths   #
            # 9: [self.bell1, self.bell_1(save)],

            #   Stringy Synths  #

            #   Percussion  #
            7: [self.clap1, self.clap_1(save)],
            8: [self.kick1, self.kick_1(save)],

        }

        return instruments
    
    def set_instruments(self, save = False):
        self.instruments = self.get_instruments(save)


    def save(self, sound, name = "", convert = True):
        """Save the sound to the desired folder"""
        super().save(sound, name, True, convert, os.path.join("Tangible_Light", "ost", "07"))
    
    
    def hats(self, save = False):
        t = self.tap1

        m1 = [
            t.n(C3, self.q),
            t.n(C3, self.q),
            t.n(C3, self.q),
            t.n(C3, self.q),
        ]

        v1 = m1 + m1 + m1 + m1

        part = v1

        if save:
            self.save(part, "hats")

        return part
    
    def bass(self, save = False, variant = "v1"):
        s = self.bass1

        #   Variant 1   #
        m1 = [
            s.n(B3, self.e, 0.8), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(E3, self.e), s.n(D3, self.e + self.q),
            s.n(D3, self.s),
        ]

        m2 = [
            s.n(B3, self.e, 0.8), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(E3, self.e), s.n(F3, self.e + self.q),
            s.n(D3, self.s)
        ]

        m3 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s), # 1.5
            s.n(G3, self.h + self.s), # 3.75
            s.n(D3, self.s)
        ]

        m4 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s),
            s.n(G3, self.h + self.e), # 4
        ]
        v1 = m1 + m2 + m3 + m4

        #   Variant 2   #
        m5 = [
            s.n(B3, self.e + self.s, 0.8), s.n(A3, self.s), # 1
            s.n(G3, self.s), s.n(F3, self.e), # 1.75
            s.n(E3, self.e), s.n(D3, self.e + self.q), # 3.75
            s.n(D3, self.s),
        ]
        
        m6 = [
            s.n(B3, self.e, 0.8), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(E3, self.h - self.s),
            s.n(D3, self.e)
        ]

        m7 = [
            s.n(A3, self.e), rest(self.s), s.n(A3, self.e), rest(self.s),
            s.n(G3, self.h + self.s), s.n(D3, self.s),
        ]

        m8 = [
            s.n(A3, self.e), rest(self.s), s.n(A3, self.e), rest(self.s),
            s.n(G3, self.h + self.e),
        ]

        v2 = m5 + m6 + m7 + m8

        v0 = m7 + m4
        part = v0 + v1 + v2 + v1 + v2 +\
        v1 + v2 + v1 + v2

        if save:
            self.save(part, "bass synth")
        return part
    
    def acou_1(self, save = False, variant = "v1"):
        if variant == "v2":
            s = Acoustic3(amp=0.3, freq_mod=1.0, sustain=1.0,
                               vol_1 = 1.0, vol_2 = 1.0)
        else:
            s = self.acou1
        
        #   Variant 1   #
        m1 = [
            s.n(B3, self.e), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(E3, self.e), s.n(D3, self.q + self.s, fade=True),
            rest(self.s), s.n(D3, self.s),
        ]

        m2 = [
            s.n(B3, self.e), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(E3, self.e), s.n(D3, self.e + self.q),
            s.n(D3, self.s)
        ]

        m3 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s), # 1.5
            s.n(G3, self.s), s.n(F3, self.s), s.n(G3, self.q + self.e + self.s), # 3.75
            s.n(D3, self.s)
        ]

        m4 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s),
            s.n(G3, self.h + self.e, fade = True),
        ]
        

        #   Variant 2   #
        m5 = [
            s.n(B3, self.e), s.n(A3, self.s),
            s.n(G3, self.s), s.n(F3, self.s), # 1.25

            s.n(E3, self.e),  # 1.75

            s.n(B3, self.e), s.n(A3, self.e), # 2.75
            s.n(G3, self.s), s.n(F3, self.s), # 3.25
            
            s.n(D3, self.q - self.s),
        ]
        
        m6 = [
            s.n(B3, self.e), s.n(A3, self.s),
            s.n(G3, self.e), s.n(F3, self.e),
            s.n(G3, self.h, fade=True),
            s.n(D3, self.s),
        ]

        m7 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s),
            s.n(G3, self.e), s.n(F3, self.s),
            s.n(G3, self.h - self.s, fade=True),
        ]
        
        m8 = [
            s.n(A3, self.e + self.s), s.n(F3, self.e + self.s), # 1.5
            s.n(G3, self.s), s.n(F3, self.s), s.n(G3, self.q + self.q, fade=True), # 3.75
        ]

        v1 = m1 + m6 + m7 + m4
        v2 = m5 + m6 + m7 + m8
        part = self.v0 + v1 + v2 + v1 + v2 +\
        v1 + v2 + v1 + v2

        if save: 
            if variant == "v2":
                self.save(part, "acoustic synth 2")
            else:
                self.save(part, "acoustic synth")
        return part
    
    def whistles(self, save = False, variant = "v1"):
        if variant == "v1":
            s = self.whistle1
        elif variant == "v2":
            s = self.whistle3

        m1 = [
            s.n(B5, self.w - self.q), # 1
            s.n(C6, self.q)
        ]
        
        m2 = [
            s.n(A5, self.w - self.q), # 2.5
            s.n(G5, self.q),
         ]

        m3 = [
            s.n(A5, self.w - self.q),
            s.n(G5, self.q),
        ]

        m4 = [
            s.n(A5, self.w),
        ]

        off = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4

        part = self.v0 + off + v1 + off + v1 +\
        off + v1 + off + v1

        if save:
            if variant == "v2":
                self.save(part, "whistle synth 2")
            else:
                self.save(part, "whistle synth")
        return part
    
    
    def whistles_2(self, save = False, variant = "v1"):
        if variant == "v1":
            s = self.whistle2
        
        quiet = 0.7
        m3 = [
            s.n(A3, self.e, quiet), rest(self.s), s.n(A3, self.e, quiet), rest(self.s),
            s.n(G3, self.h + self.s, quiet), rest(self.s),
        ]

        m4 = [
            s.n(A3, self.e, quiet), rest(self.s), s.n(A3, self.e, quiet), rest(self.s),
            s.n(G3, self.h + self.e, quiet),
        ]

        amp = 1.0
        m7 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(A3, self.e, amp), rest(self.s),
            s.n(G3, self.h + self.s, amp), rest(self.s),
        ]

        m8 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(A3, self.e, amp), rest(self.s),
            s.n(G3, self.h + self.e, amp),
        ]

        off = [rest(self.w*4)]
        v1 = [rest(self.w*2)] + m3 + m4
        v2 = [rest(self.w*2)] + m7 + m8

        part = self.v0 + v1 + v1 + v1 + v2 +\
        v1 + v2 + v1 + v2
        
        if save:
            self.save(part, "whistle punches")
        return part
    

    def punch_1(self, save = False, variant = "v1"):
        """Punchy sounds every 7th and 8th bar"""

        if variant == "v1":
            s = self.punch1
        
        quiet = 0.4
        m3 = [
            s.n(A3, self.e, quiet), rest(self.s), s.n(A3, self.e, quiet), rest(self.s),
            s.n(G3, self.h + self.s, quiet), rest(self.s),
        ]

        m4 = [
            s.n(A3, self.e, quiet), rest(self.s), s.n(A3, self.e, quiet), rest(self.s),
            s.n(G3, self.h + self.e, quiet),
        ]

        amp = 1.0
        m7 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(A3, self.e, amp), rest(self.s),
            s.n(G3, self.h + self.s, amp), rest(self.s),
        ]

        m8 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(A3, self.e, amp), rest(self.s),
            s.n(G3, self.h + self.e, amp),
        ]


        amp = 1.7
        m11 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(F3, self.e, amp), rest(self.s),
            s.n(G3, self.h + self.s, amp), s.n(D3, self.s, amp),
        ]

        m12 = [
            s.n(A3, self.e, amp), rest(self.s), s.n(F3, self.e, amp), rest(self.s),
            s.n(G3, self.s, amp), s.n(F3, self.s, amp),
            s.n(G3, self.h, amp),
        ]

        off = [rest(self.w*4)]
        v1 = [rest(self.w*2)] + m3 + m4
        v2 = [rest(self.w*2)] + m7 + m8
        v3 = [rest(self.w*2)] + m11 + m12
        part = self.v0 + off + v1 + off + v2 +\
        off + v3 + off + v3
        if save:
            self.save(part, "punchy synth")
        return part
    

    def synth_1(self, save = False, variant = "v1"):
        s = self.synth1

        m1 = [
            s.n(B5, self.w - self.q), # 1
            s.n(C6, self.q)
        ]
        
        m2 = [
            s.n(A5, self.w - self.q), # 2.5
            s.n(G5, self.q),
         ]

        m3 = [
            s.n(A5, self.w - self.q),
            s.n(G5, self.q),
        ]

        m4 = [
            s.n(A5, self.w),
        ]

        off = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4

        part = self.v0 + off + off + v1 + v1 +\
        v1 + v1 + v1 + v1

        if save:
            self.save(part, "synth 1")
        return part
    

    def synth_1(self, save = False, variant = "v1"):
        s = self.synth1

        m1 = [
            s.n(B5, self.w - self.q), # 1
            s.n(C6, self.q)
        ]
        
        m2 = [
            s.n(A5, self.w - self.q), # 2.5
            s.n(G5, self.q),
         ]

        m3 = [
            s.n(A5, self.w - self.q),
            s.n(G5, self.q),
        ]

        m4 = [
            s.n(A5, self.w),
        ]

        off = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4

        part = self.v0 + off + off + v1 + v1 +\
        v1 + v1 + v1 + v1

        if save:
            self.save(part, "synth 1")
        return part
        
    
    def clap_1(self, save = False):
        c = self.clap1
        m0 = [
            rest(self.w - (self.q + self.s)),
            c.n(C1, self.s), c.n(C1, self.s), rest(self.s), c.n(C1, self.s),
            rest(self.s)
        ]
        
        m1 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.q),
            c.n(C1, self.e), c.n(C1, self.e),
        ]

        m2 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.q),
            c.n(C1, self.s), rest(self.s*2), c.n(C1, self.s),
        ]

        m3 = m1

        m4 = [
            rest(self.q),
            c.n(C1, self.q),
            rest(self.q),
            c.n(C1, self.s), rest(self.s), c.n(C1, self.s), c.n(C1, self.s),
        ]


        off = [rest(self.w*4)]
        v0 = [rest(self.w*3)] + m0
        v1 = m1 + m2 + m3 + m4
        v2 = v1
        part = self.v0 + off + off + off + v0 +\
        v1 + v2 + v1 + v2

        if save:
            self.save(part, "claps")
        return part


    def kick_1(self, save = False):
        c = self.kick1

        m0 = [
            rest(self.w - (self.q + self.s)),
            c.n(C1, self.e), rest(self.s), c.n(C1, self.e),
        ]
        
        m1 = [
            c.n(C1, self.e), c.n(C1, self.e),
            rest(self.s*3), c.n(C1, self.s),
            c.n(C1, self.s), rest(self.s), rest(self.s), c.n(C1, self.s),
            rest(self.e), c.n(C1, self.s), c.n(C1, self.s),
        ]

        m2 = [
            c.n(C1, self.s), rest(self.s*2), c.n(C1, self.s),
            rest(self.e), c.n(C1, self.e),
            c.n(C1, self.q),
            c.n(C1, self.s), rest(self.s*2), c.n(C1, self.s)
        ]

        m3 = m1

        m4 = m2


        off = [rest(self.w*4)]
        v0 = [rest(self.w*3)] + m0
        v1 = m1 + m2 + m3 + m4
        v2 = v1
        part = self.v0 + off + off + off + v0 +\
        v1 + v2 + v1 + v2

        if save:
            self.save(part, "kicks")
        return part
    

    def bell_1(self, save = False):
        c = self.bell1

        m1 = [
            c.n(D4, self.e), c.n(B3, self.s),
            c.n(A3, self.e + self.s), c.n(G3, self.s),
            c.n(F3, self.s), c.n(D3, self.e),
            rest(self.q + self.e)
        ]

        m2 = [
            c.n(D4, self.e), c.n(B3, self.s), # .75
            c.n(A3, self.e + self.s), c.n(G3, self.s), # 1.75
            c.n(B3, self.q + self.s), # 2.75
            c.n(A3, self.q), # 3.25
        ]

        m3 = [
            c.n(G3, self.e), c.n(A3, self.s), # .75
            c.n(G3, self.e), c.n(A3, self.e), # 1.5
            c.n(B3, self.e), c.n(B3, self.e), # 2.5
            c.n(A3, self.e), c.n(G3, self.s), # 3.25
            c.n(E3, self.e),
        ]

        # C4 B3 C4 B3 A3 F3
        m4 = [
            c.n(C4, self.e), c.n(B3, self.e), # 1
            c.n(C4, self.s), c.n(B3, self.e), # 1.75
            c.n(A3, self.q + self.s), # 2.75
            c.n(F3, self.q) # 4
        ]

        off = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4

        part = self.v0 + off + off + off + off +\
        v1 + v1 + v1 + v1

        if save:
            self.save(part, "beru")
        return part


def main():
    beat = O7(40)

    #   Export each instrument  #
    beat.get_instruments(save=True)

    #   Export the full beat    #
    # beat.set_instruments(save=False)
    # beat.produce_full()
    # beat.save(beat.production, "_prod", convert=False)

