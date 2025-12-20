from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Ice(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "07"))
        mod = 0.5
        
        #   ----- Melody -----  #
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)



        #   ----- Rhythm / Percussion -----  #
        #   Bass    #
        self.bass1 = LowSynth(2.0)
        
        self.bass2 = Bass_1(amp=0.6, attack=0.05, attack_max = 0.15, freq_mod = mod, decay = 0.0, sustain=1.0, release= 0.05, amp_final = 0.00000000001, top_freq = 2, harmonics=2)
        

        #   Hats    #
        self.hat1 = Rapping.Hat_1(amp=0.000025)

        self.hat2 = Rapping.Hat_2(amp=0.00003)

        self.hat3 = Rapping.Hat_3(amp=0.00012)

        self.hat4 = Hat_4(amp=0.00005)

        self.quick_hat = GlobalSample(0.000005, os.path.join("samples", "hats", "quicky.wav"))

        self.hatd = Rapping.Drill_Hat(amp=0.00004)


        #   Snares  #
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        
        self.snare3 = Rapping.Snare_3(amp=0.00001)

        self.snare4 = GlobalSample(0.00005, os.path.join("samples", "snares", "snare_4.wav"))

        self.snare5 = GlobalSample(0.000015, os.path.join("samples", "snares", "snare_5.wav"))
        
        self.lofi_snare = Rapping.Lofi_Snare(amp=0.00005)
        
        self.crackle_snare = Rapping.Crackle_Snare(amp=0.00001)
        
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        
        self.punchy_snare = GlobalSample(0.00008, os.path.join("samples", "snares", "punchy_snare.wav"))
        
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       

       #    Kicks   #
        self.kick4 = E1_Samples(amp=0.0000135, name="kick04.wav")
        self.kick_long = E1_Samples(amp=0.00003, name="kick08.wav")

        # self.hat1 = E1_Samples(amp=0.00001, name="perc02.wav")
        self.hat1 = E1_Samples(amp=0.000005, name="rim01.wav")
        # self.hat1 = E1_Samples(amp=0.000005, name="snare15.wav")



        
        #   Chimes  #
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)
        

        #   Whistles    #
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = False, wave_3=True,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 0.3)
        


        #   ----- MIDIs -----   #
        self.full_midi = GlobalSample(0.00005, os.path.join("samples", "AMTR", "07_full.wav"))



        #   ----- Samples ----- #
        self.go = GlobalSample(0.00001, os.path.join("samples", "go_low.wav"))
        
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))

        self.ice1 = GlobalSample(0.000004, os.path.join("samples", "ambience", "glass_1.wav"))
        self.cold1 = GlobalSample(0.00005, os.path.join("samples", "ambience", "cold_1.wav"))
        self.cold2 = GlobalSample(0.00005, os.path.join("samples", "ambience", "cold_2.wav"))
        # self.crash1 = GlobalSample(0.000005, os.path.join("samples", "ambience", "crash_1.wav"))

        self.crash1 = Cymbal(amp=0.05)




        #   ----- Dictionary of Instruments -----   #
        self.instruments = {}

        self.vi = [rest(self.w*4 - self.e)]

    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            "midi" : [0, self.midi(verse)],
            "kicks": [0, self.kick(verse)],
            "snare": [0, self.snare(verse)],
            "hat": [0, self.hat(verse)],


            #   Melody  #



            #   Samples / Libs  #
            "ice1": [0, self.ice_1(verse)],
            "cold1": [0, self.cold_1(verse)],
            "crash1": [0, self.crash_1(verse)],
        }

    def midi(self, verse = "full"):
        vf = [self.full_midi.n(self.w * 32)]
        vi = [self.full_midi.n(self.w*4 - self.e)]
        vm = [self.full_midi.n(self.w*32, start_time = self.w*4 - self.e)]
        
        
        if verse == "intro":
            return vi
        
        elif verse == "main":
            # return \
            # v2 + v1
            return \
            vm
        
        return \
        vf
    
    def ice_1(self, verse):
        i = self.ice1

        v0 = [
            rest(self.w*4 - self.e)
        ]

        m0 = [rest(self.w)]
        mi = [rest(self.w - self.e)]

        m1 = [
            rest(self.t + self.e),
            i.n(self.e),
        ]

        m1b = [
            rest(self.e),
            rest(self.t + self.e),
            i.n(self.e),
        ]

        v1 = m1 + m0 + m1 + m0

        vi = m1 + m0 + m1 + mi # - self.e

        v2 = m1b + m0 + m1 + m0


        if verse == "intro":
            return vi
        
        elif verse == "main":
            return \
            v2 + v1 + v1 +\
            \
            v1 +\
            \
            v1 + v1 + v1 +\
            \
            v0
        
        return \
        vi +\
        \
        v2 + v1 + v1 +\
        \
        v1 +\
        \
        v1 + v1 + v1 +\
        \
        vi
        
    def crash_1(self, verse):
        c = self.crash1

        v0 = [
            rest(self.w*4)
        ]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.q),
            rest(self.q),
            c.n(C6, self.q),
            rest(self.e), rest(self.e)
        ]

        m2 = [
            rest(self.q),
            rest(self.q),
            c.n(C6, self.e),
            rest(self.q),
            rest(self.e)
        ]

        v1 = m0 + m2 + m0 + m2


        if verse == "intro":
            return self.vi
        
        elif verse == "main":
            return \
            v0 + v1 + v1 +\
            \
            v0 +\
            \
            v1 + v1 + v0 +\
            \
            v0
        
        return \
        self.vi +\
        \
        v0 + v1 + v1 +\
        \
        v0 +\
        \
        v0 + v1 + v1 +\
        \
        v0
    
    def cold_1(self, verse):
        c = self.cold1

        v0 = [
            rest(self.w*4)
        ]


        vi = [c.n(self.w*4 - self.e)]
        v1 = [c.n(self.w*4)]




        if verse == "intro":
            return vi
        
        elif verse == "main":
            return \
            v0 + v0 + v0 +\
            \
            v1 +\
            \
            v0 + v0 + v0 +\
            \
            v0
        
        return \
        vi +\
        \
        v0 + v0 + v0 +\
        \
        v1 +\
        \
        v0 + v0 + v0 +\
        \
        v0
    
    def kick(self, verse):
        # k = self.kick3
        k = self.kick4
        kl = self.kick_long


        v0 = [
            rest(self.w*4)
        ]


        m0 = [
            rest(self.w)
        ]

        m1 = [
            k.n(self.q),
            rest(self.q),
            k.n(self.e), k.n(self.e),
            rest(self.e), rest(self.e),
        ]

        m2 = [
            k.n(self.q),
            rest(self.q),
            k.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
        ]

        

        m5 = [
            rest(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            kl.n(self.h),
        ]

        m6 = [
            k.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            k.n(self.q),
            k.n(self.q),
        ]

        m7 = [
            k.n(self.q),
            rest(self.e), k.n(self.e),
            k.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
        ]

        mf = [
            k.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            k.n(self.q),
            k.n(self.q),
        ]

        #   Should m7 be m1 ??
        v1 = m1 + m2 + m1 + m2

        v2 = m5 + m6 + m5 + m6

        v3 = m0 + m0 + m1 + m2

        v4 = m5 + m6 + m5 + mf

        vi = [rest(self.w*4)]

        if verse == "intro":
            return self.vi
        
        elif verse == "main":
            return \
            v1 + v2 + v1 +\
            \
            v3 +\
            \
            v1 + v2 + v3 +\
            \
            v4
        
        # Can consider swapping v2 and v1 after the refrain.

        return \
        self.vi +\
        \
        v1 + v2 + v1 +\
        \
        v3 +\
        \
        v1 + v2 + v3 +\
        \
        v4
        

    def snare(self, verse):
        s = self.snare5

        v0 = [rest(self.w*4)]

        m0 = [
            rest(self.w)
        ]

        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
        ]

        mf = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            rest(self.q),
        ]
        
        v1 = m1 + m1 + m1 + m1

        v2 = m0 + m0 + m1 + m1

        v3 = m1 + m1 + m1 + mf

        vi = [rest(self.w*4)]

        if verse == "intro":
            return self.vi
        
        elif verse == "main":
            return \
            v1 + v1 + v1 +\
            \
            v2 +\
            \
            v1 + v1 + v2 +\
            \
            v3
        
        return \
        self.vi +\
        \
        v1 + v1 + v1 +\
        \
        v2 +\
        \
        v1 + v1 + v2 +\
        \
        v3

    def hat(self, verse):
        h = self.hat1


        v0 = [
            rest(self.w*4)
        ]


        m0 = [
            rest(self.w)
        ]

        m3 = [
            rest(self.w - self.e),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
        ]
        m4 = [
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/4), h.n(self.s/4), h.n(self.s/4), h.n(self.s/4), h.n(self.s/4), h.n(self.s/4), h.n(self.s/2),
        ]

        
        #   Should m7 be m1 ??
        v1 = v0

        v2 = v0

        v3 = v0

        v4 = v0

        vi = [rest(self.w*4 - self.e)]

        vi = m0 + m0 + m3 + m4

        if verse == "intro":
            return vi
        
        elif verse == "main":
            return \
            v1 + v2 + v1 +\
            \
            v3 +\
            \
            v2 + v1 + v3 +\
            \
            v4
        
        return \
        vi +\
        \
        v1 + v2 + v1 +\
        \
        v3 +\
        \
        v1 + v2 + v3 +\
        \
        v4
    
    

def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Ice(70)
    # beat.get_instruments("full")
    # beat.export_selection(name="07_full", volume=60_500)

    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    beat.get_instruments("intro")
    beat.export_selection(name="07_intro", volume=60_500)

    beat.get_instruments("main")
    beat.export_selection(name="07_main", volume=60_500)