from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Bio(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "05"))
        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Bass    ##5
        mod = 0.5
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)

        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)
        
        self.bass1 = LowSynth(2.0)
        
        self.bass2 = Bass_1(amp=0.6, attack=0.05, attack_max = 0.15, freq_mod = mod, decay = 0.0, sustain=1.0, release= 0.05, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Whistle ##
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = False, wave_3=True,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 0.3)

        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)

        # hat 1
        self.hat4 = Hat_4(amp=0.00005)
        # hat 2
        self.quick_hat = GlobalSample(0.000005, os.path.join("samples", "hats", "quicky.wav"))
        # hat 3
        self.hatd = Rapping.Drill_Hat(amp=0.00002)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        self.punchy_snare = GlobalSample(0.00008, os.path.join("samples", "snares", "punchy_snare.wav"))
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       
       
        ##  Kicks   ##
        self.kick1 = Tap4(1.0, attack=0.001, decay = 0.03, sustain=0.0, noise_amount=0.0)
        self.kick2 = GlobalSample(amp=0.00002, file_path=os.path.join("samples", "kick", "new-kick.wav"))
        self.kick3 = GlobalSample(amp=0.00002, file_path=os.path.join("samples", "kick", "new-kick_2.wav"))


        #   Samples #
        self.bass_mid = GlobalSample(0.00001, os.path.join("samples", "AMTR", "05_Bass_synth.wav"))
        self.key_mid = GlobalSample(0.00003, os.path.join("samples", "AMTR", "05_Keys.wav"))
        self.tag = GlobalSample(0.0001, os.path.join("samples", "tag.wav"))

        self.go = GlobalSample(0.00001, os.path.join("samples", "go_low.wav"))
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.scratch1 = GlobalSample(0.00003, os.path.join("samples", "records", "scratch_1.wav"))
        self.scratch2 = GlobalSample(0.00003, os.path.join("samples", "records", "scratch_2.wav"))
        self.drop = GlobalSample(0.00025, os.path.join("samples", "ambience", "drop_1.wav"))
        self.wind1 = GlobalSample(0.000005, os.path.join("samples", "ambience", "wind_1.wav"))
        self.wind2 = GlobalSample(0.000005, os.path.join("samples", "ambience", "wind_2.wav"))
        self.wind3 = GlobalSample(0.000005, os.path.join("samples", "ambience", "wind_3.wav"))
        self.squeak = GlobalSample(0.000005, os.path.join("samples", "ambience", "squeak_1.wav"))

        
        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            "hats1": [None, self.hats_1(verse)],
            "hats2": [None, self.hats_2(verse)],
            "kicks1": [None, self.kick(verse)],
            "snare1": [None, self.snare(verse)],
            "chimes": [None, self.skirts(verse)],


            #   Melody  #
            "key1": [None, self.keys_1(verse)],
            "key2": [None, self.keys_2(verse)],
            "key3": [None, self.keys_3(verse)],



            #   Samples / Libs  #
            "go": [self.go, self.go_1(verse)],
            # "tag": [self.go, self.producer_tag(verse)],
            "squeak": [self.go, self.squeak_1(verse)],
            "drop": [None, self.drop_1(verse)],
            "wind": [None, self.wind_1(verse)]

        }

    def producer_tag(self, verse):
        t = self.tag
        
        m0 = [
            rest(self.w)
        ]

        m1 = [
            t.n(self.w)
        ]

        v1 = [rest(40.0)] + m1

        return v1
    
    def wind_1(self, verse = "full"):
        w1 = self.wind1
        w2 = self.wind2
        w3 = self.wind3

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            w1.n(self.w)
        ]

        m2 = [
            w2.n(self.w)
        ]

        m3 = [
            w3.n(self.w*2)
        ]

       

        
        v1 = m1 + m2 + m3

        if verse == "intro":
            return \
            v1 + v1 + v1
        
        if verse == "main":
            return \
            v0 + v0 +\
            v0 +\
            v1 + v1

        return \
        v1 + v1 + v1 +\
        v0 + v0 +\
        v0 +\
        v1 + v1
    
    def drop_1(self, verse = "full"):
        d = self.drop

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.e*3), d.n(self.e),
            rest(self.h)
        ]

        v1 = m1 + m1 + m1 + m1

        if verse == "intro":
            return \
            v0 + v1 + v1
        
        if verse == "main":
            return \
            v1 + v1 +\
            v1 +\
            v1 + v1
        
        return \
        v0 + v1 + v1 +\
        v1 + v1 +\
        v1 +\
        v1 + v1
    
    def skirts(self, verse = "full"):
        s1 = self.chime1
        s2 = self.chime2
        s3 = self.squeak
        
        v0 = [rest(self.w*4)]
        
        m0 = [
            rest(self.w)
        ]

        m1 = [
            rest(self.w - self.e),
            s1.n(C1, self.s), s1.n(C1, self.s),
        ]

        m2 = [
            rest(self.w - self.q),
            s1.n(C1, self.s), rest(self.e), s1.n(C1, self.s),
        ]

        m3 = [
            rest(self.w - self.e),
            s1.n(C1 / 2, self.s), s1.n(C1 /2, self.s),
        ]

        m4 = [
            rest(self.w - self.q),
            s1.n(C1 / 2, self.s), rest(self.e), s1.n(C1, self.s),
        ]
    
        
        vi = m0 + m0 + m0 + m4
        v1 = m1 + m2 + m3 + m4

        if verse == "intro":
            return \
            vi + vi + vi
        
        if verse == "main":
            return \
            v1 + v1 +\
            v0 +\
            v1 + v1
        
        return \
        vi + vi + vi +\
        v1 + v1 +\
        v0 +\
        v1 + v1


    def squeak_1(self, verse = "full"):
        s = self.squeak

        v0 = [rest(self.w*4)]
        m0 = [rest(self.w)]

        m1 = [
            rest(self.q),
            s.n(self.e), rest(self.e),
            rest(self.q),
            rest(self.q),
        ]
    
        v1 = m1 + m0 + m0 + m0
        v2 = m1 + m1 + m1 + m1

        if verse == "intro":
            return \
            v1 + v0 + v0
        
        if verse == "main":
            return \
            v0 + v0 +\
            v0 +\
            v2 + v2
        
        return \
        v1 + v0 + v0 +\
        v0 + v0 +\
        v0 +\
        v2 + v2

    def kick(self, verse = "full"):
        k = self.kick2
        k2 = self.kick3
        s = self.squeak

        v0 = [rest(self.w*4)]
        
        m0 = [
            rest(self.w)
        ]

        m1 = [
            k.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
        ]

        v1 = m1 + m1 + m1 + m1

        v2 = m0 + m1 + m1 + m1

        m5 = [
            k.n(self.s), k.n(self.s), k2.n(self.s/2), k2.n(self.s/2), k2.n(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), k.n(self.s),
            rest(self.s), k.n(self.s), rest(self.s), rest(self.s)
        ]

        m6 = [
            k.n(self.s/2), k.n(self.s/2), k.n(self.s), k2.n(self.s), k2.n(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), k.n(self.s),
            rest(self.s), k.n(self.s), rest(self.s), rest(self.s)
        ]

        m7 = [
            k.n(self.s), k.n(self.s), k2.n(self.s/2), k2.n(self.s/2), k2.n(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            rest(self.s), k2.n(self.s/2), k2.n(self.s/2), k2.n(self.s), k.n(self.s),
            rest(self.s), k.n(self.s), rest(self.s), rest(self.s)
        ]

        m8 = [
            k.n(self.s/2), k.n(self.s/2), k.n(self.s), k2.n(self.s), k2.n(self.s),
            rest(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            rest(self.s), k.n(self.s/2), k.n(self.s/2), k.n(self.s), k.n(self.s),
            rest(self.s), k.n(self.s), rest(self.s), rest(self.s)
        ]

        v3 = m5 + m8 + m7 + m6

        if verse == "intro":
            return \
            v0 + v0 + v0
        
        if verse == "main":
            return \
            v1 + v1 +\
            v2 +\
            v3 + v3
        
        return \
        v0 + v0 + v0 +\
        v1 + v1 +\
        v2 +\
        v3 + v3
    
    def tap(self, verse = "full"):
        return
    

    def snare(self, verse = "full"):
        s = self.punchy_snare
        v0 = [rest(self.w*4)]
        m0 = [rest(self.w)]

        m1 = [
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.s), s.n(self.s),  
        ]

        m2 = [
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            s.n(self.e), s.n(self.e),  
        ]

        m4 = [
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.e),
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.s), s.n(self.s),  
        ]

        v1 = m1 + m2 + m1 + m4
        v2 = m0 + m1 + m1 + m4

        m5 = [
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            s.n(self.s), rest(self.s), rest(self.s), s.n(self.s),
            rest(self.s), rest(self.s), rest(self.s), rest(self.s),
            s.n(self.s), rest(self.s), s.n(self.s), rest(self.s)
        ]

        v3 = m5 + m5 + m5 + m5

        if verse == "intro":
            return \
            v0 + v0 + v0
        
        if verse == "main":
            return \
            v1 + v1 +\
            v2 +\
            v3 + v3
        
        return \
        v0 + v0 + v0 +\
        v1 + v1 +\
        v2 +\
        v3 + v3
    
    def hats_1(self, verse="full"):
        h = self.hat2

        v0 = [rest(self.w*4)]
        
        m1 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        m2 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            rest(self.s), h.n(self.e), rest(self.s),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s), h.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m2
        v2 = m2 + m2 + m2 + m2

        if verse == "intro":
            return \
            v0 + v1 + v1
        
        if verse == "main":
            return \
            v1 + v1 +\
            v0 +\
            v1 + v1
        
        return\
        v0 + v1 + v1 +\
        v1 + v1 +\
        v0 +\
        v1 + v1
    

    def hats_2(self, verse = "full"):
        h = self.hatd
        v0 = [rest(self.w*4)]

        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        m1 = [
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),

            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2),
        ]

        v1 = m1 + m1 + m1 + m1

        if verse == "intro":
            return \
            v0 + v0 + v1
        
        if verse == "main":
            return \
            v1 + v1 +\
            v0 +\
            v1 + v1
        
        return \
        v0 + v0 + v1 +\
        v1 + v1 +\
        v0 +\
        v1 + v1
    
    def go_1(self, verse="full"):
        g = self.go

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e*7), g.n(self.e)
        ]

        m2 = [
            rest(self.e*7), g.n(self.s), g.n(self.s)
        ]


        m4 = [
            rest(self.e*6), g.n(self.e), rest(self.s), g.n(self.s/2), rest(self.s/2)
        ]

        v1 = m1 + m2 + m1 + m4

        if verse == "intro":
            return \
            v0 + v1 + v1
        
        if verse == "main":
            return \
            v0 + v1 +\
            v1 +\
            v0 + v1
        
        return \
        v0 + v1 + v1 +\
        v0 + v1 +\
        v1 +\
        v0 + v1
    
    def keys_1(self, verse = "full"):
        m0 = [rest(self.w)]
        v0 = [rest(self.w*4)]

        """
        # k1 = self.bell
        k1 = self.bass2

        m1 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2), 
            k1.n(B2, self.q + self.s/2),
            k1.n(E2, self.q + self.e),
            k1.n(C2, self.e), k1.n(A1, self.e),
        ]

        
        m2 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2),
            k1.n(B2, self.q + self.s/2),
            k1.n(E2, self.q + self.e),
            k1.n(C2, self.e), k1.n(E2, self.e),
        ]

        m3 = [
        ]

        m4 = [
        ]

        v1 = m1 + m2 + m1 + m2
        """

        v1 = [self.bass_mid.n(self.w*4)]

        # if verse == "intro":
        #     return \
        #     v0 + v0
        
        # elif verse == "main":
        #     return \
        #     v0 + v1 +\
        #     \
        #     v1 + v1 +\
        #     v1 + v1
        
        if verse == "intro":
            return \
            v1 + v1 + v1
        
        if verse == "main":
            return \
            v1 + v1 +\
            v0 +\
            v1 + v1
        
        return \
        v1 + v1 + v1 +\
        v1 + v1 +\
        v0 +\
        v1 + v1
    
    def keys_2(self, verse = "full"):
        v0 = [rest(self.w*4)]
        m0 = [rest(self.w)]

        """
        k1 = self.bell2

        
        amp=0.5
        

        m1 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2), 
            k1.n(B2, self.q + self.s/2),
            k1.n(C3, self.q + self.e, amp),
            k1.n(B2, self.q, amp),
        ]

        
        m2 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2), 
            k1.n(B2, self.q + self.s/2),
            k1.n(C3, self.q + self.e, amp),
            k1.n(B2, self.q, amp),
        ]

        m3 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2),
            k1.n(B2, self.q + self.s/2),
            k1.n(C3, self.q + self.e, amp),
            k1.n(B2, self.e, amp), rest(self.s), k1.n(B2, self.s, amp)
        ]

        m4 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2),
            k1.n(B2, self.q + self.s/2),
            k1.n(C3, self.q + self.e, amp),
            k1.n(B2, self.s, amp), rest(self.e), k1.n(B2, self.s, amp)
        ]

        v1 = m1 + m2 + m1 + m2
        """

        v1 = [self.key_mid.n(self.w*4)]


        # if verse == "intro":
        #     return \
        #     v0 + v0
        
        # elif verse == "main":
        #     return \
        #     v0 + v1 +\
        #     \
        #     v1 + v1 +\
        #     v1 + v1

        if verse == "intro":
            return \
            v0 + v0 + v0
        
        if verse == "main":
            return \
            v1 + v1 +\
            v0 +\
            v1 + v1
        
        return \
        v0 + v0 + v0 +\
        v1 + v1 +\
        v0 +\
        v1 + v1
    

    def keys_3(self, verse = "full"):

        k1 = self.bass2

        m0 = [rest(self.w)]
        v0 = [rest(self.w*4)]

        

        m1 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2), 
            k1.n(B2, self.q + self.s/2),
            k1.n(E2, self.q + self.e),
            k1.n(C2, self.e), k1.n(A1, self.e),
        ]

        
        m2 = [
            k1.n(E2, self.s), k1.n(G2, self.s/2),
            k1.n(B2, self.q + self.s/2),
            k1.n(E2, self.q + self.e),
            k1.n(C2, self.e), k1.n(E2, self.e),
        ]

        m3 = [
        ]

        m4 = [
        ]

        v1 = m1 + m2 + m1 + m2

        # if verse == "intro":
        #     return \
        #     v0 + v0
        
        # elif verse == "main":
        #     return \
        #     v0 + v1 +\
        #     \
        #     v1 + v1 +\
        #     v1 + v1
        
        if verse == "intro":
            return \
            v1 + v1 + v1
        
        if verse == "main":
            return \
            v1 + v1 +\
            v1 +\
            v1 + v1
        
        return \
        v1 + v1 + v1 +\
        v1 + v1 +\
        v1 +\
        v1 + v1

    
def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Bio(70)
    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="05_full", volume=30_500)

    """
    #   Intro   #
    beat.get_instruments("intro")
    #   Drums
    drums = {}
    for i in beat.instruments:
        if i == "hats1" or i == "hats2":
            drums[i] = beat.instruments[i]
    beat.export_selection(drums, name="05_drums_intro", volume=15_500)
    
    #   Main
    main = {}
    for i in beat.instruments:
        if i != "hats1" and i != "hats2":
            main[i] = beat.instruments[i]

    beat.export_selection(main, name="05_intro", volume=15_500)


    #   Main    #
    beat.get_instruments("main")
    #   Drums
    drums = {}
    for i in beat.instruments:
        if i == "hats1" or i == "hats2":
            drums[i] = beat.instruments[i]
    beat.export_selection(drums, name="05_drums", volume=15_500)
    
    #   Main
    main = {}
    for i in beat.instruments:
        if i != "hats1" and i != "hats2":
            main[i] = beat.instruments[i]

    beat.export_selection(main, name="05_main", volume=15_500)

    

    # beat.get_instruments("intro")
    # beat.export_selection(name = "04_intro", volume=14_500)
    # beat.get_instruments("main")
    # beat.export_selection(name = "04_main", volume=14_500)
    """