from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Title(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "01"))
        #   ----- Melody -----  #


        #   ----- Rhythm / Percussion -----  #
        mod = 0.5
        self.bass1 = LowSynth(2.0)
        
        self.bass2 = Bass_1(amp=1.0, attack=0.0, attack_max = 0.15, freq_mod = mod, decay = 0.00, sustain=0.3, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)

        # hat 1
        self.hat4 = Hat_4(amp=0.00005)
        # hat 2
        self.quick_hat = GlobalSample(0.000004, os.path.join("samples", "hats", "quicky.wav"))
        # hat 3
        self.hatd = Rapping.Drill_Hat(amp=0.00004)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        self.punchy_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "punchy_snare.wav"))
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       
       
        ##  Kicks   ##
        self.kick1 = Tap4(1.0, attack=0.001, decay = 0.03, sustain=0.0, noise_amount=0.0)

        #   ----- MIDIs -----   #
        self.midi = GlobalSample(0.00001, os.path.join("samples", "AMTR", "01_MIDI.wav"))


        #   ----- Samples ----- #
        #   Samples #
        self.go = Go(amp=0.00001)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.scratch1 = GlobalSample(0.00003, os.path.join("samples", "records", "scratch_1.wav"))
        self.scratch2 = GlobalSample(0.00003, os.path.join("samples", "records", "scratch_2.wav"))
        
        self.instruments = {}


    def get_instruments(self, verse = "main"):
        self.instruments = {
            #   Rhythm and Bass #
            'bass1':[None, self.bass_1(verse)],
            'snares':[None, self.snare_1(verse)],
            'snare_echo':[None, self.snare_2(verse)],
            'kicks':[None, self.kick_1(verse)],
            'hats':[None, self.hats_1(verse)],
            'hats_2':[None, self.hats_2(verse)],
            # 'hats_3':[None, self.hats_3(verse)],

            #   Melody  #

            #   Samples / Libs  #
            "midi": [None, self.midi_1(verse)]

        }

    def midi_1(self, verse):
        m = self.midi

        v0 = [rest(self.w*4)]

        v1 = [m.n(self.w*8)]

        if verse == "intro":
            return \
            v0 + v0

        elif verse == "loop":
            return \
            v0 + v0 +\
            \
            v0 + v0 +\
            v1
        
        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        \
        v1
    
    def hats_1(self, verse = "main"):
        h1 = self.hat4
        v0 = [rest(self.w*4)]

        m1 = [
            h1.n(self.s), h1.n(self.s), h1.n(self.s), rest(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s/2), h1.n(self.s/2), h1.n(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s/2), h1.n(self.s/2), h1.n(self.s),
            h1.n(self.s), rest(self.s), h1.n(self.s), h1.n(self.s),
        ]

        m2 = [
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s/2), h1.n(self.s/2), h1.n(self.s),
            h1.n(self.s), h1.n(self.s), h1.n(self.s/2), h1.n(self.s/2), h1.n(self.s),
            h1.n(self.s), rest(self.s), h1.n(self.s), h1.n(self.s),
        ]
        
        m3 = [
            h1.n(self.s), h1.n(self.s), rest(self.e),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            rest(self.q),
            h1.n(self.s), rest(self.s), h1.n(self.s), h1.n(self.s),
        ]

        m4 = [
            h1.n(self.s), h1.n(self.s), rest(self.e),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
            rest(self.e), h1.n(self.e),
            h1.n(self.s), rest(self.s), h1.n(self.s), h1.n(self.s),
        ]

        m8 = [
            h1.n(self.e), h1.n(self.e),
            h1.n(self.e), h1.n(self.e),
            rest(self.e), h1.n(self.e),
            h1.n(self.s), h1.n(self.s), h1.n(self.s), h1.n(self.s),
        ]

        v1 = m1 + m2 + m3 + m4

        if verse == "intro":
            return \
            v0 + v0
        
        elif verse == "loop":
            return \
            v0 + v1 +\
            \
            v1 + v1 +\
            v1 + v1
        
        return \
        v0 + v0 +\
        \
        v0 + v1 +\
        \
        v1 + v1 +\
        v1 + v1
    
    def hats_2(self, verse = "main"):
        h = self.quick_hat

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.q),
            rest(self.q),
            rest(self.e), h.n(self.e),
            rest(self.e), h.n(self.e)
        ]

        m2 = [
            rest(self.q),
            rest(self.q),
            rest(self.e), h.n(self.e),
            rest(self.e), rest(self.e),
        ]

        m3 = [
            rest(self.q),
            h.n(self.q),
            rest(self.e), h.n(self.e),
            rest(self.e), rest(self.e),
        ]


        m4 = [
            rest(self.q),
            rest(self.q),
            rest(self.e), rest(self.e),
            rest(self.e), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2), h.n(self.s/2)
        ]

        m5 = [
            rest(self.q),
            h.n(self.q),
            rest(self.e), h.n(self.e),
            rest(self.e), h.n(self.e)
        ]

        m8 = [
            rest(self.q),
            rest(self.q),
            rest(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        m0 = [rest(self.w)]

        v1 = m0 + m0 + m0 + m4

        v2 = m1 + m2 + m1 + m8

        if verse == "intro":
            return \
            v1 + v2
        
        elif verse == "loop":
            return \
            v1 + v2 +\
            \
            v1 + v2 +\
            v1 + v2
        
        return \
        v1 + v2 +\
        \
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2
        
    
    def hats_3(self, verse = "main"):
        """More skirty"""
        h = self.hatd

        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m1

        if verse == "intro":
            return \
            v0 + v0
        
        elif verse == "loop":
            return \
            v0 + v0 +\
            \
            v1 + v0 +\
            v1 + v0
        
        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        \
        v1 + v0 +\
        v1 + v0
        
    
    def kick_1(self, verse = "main"):
        k = self.kick1
        # n1 = F3
        n1 = F2
        n2 = C3
        n3 = A2


        v0 = [rest(self.w*4)]
        m1 = [
            k.n(n3, self.q),
            # rest(self.q),
            rest(self.q),
            rest(self.e), k.n(n2, self.e),
            rest(self.s), k.n(n2, self.e), rest(self.s)
        ]

        m3 = [
            k.n(n3, self.q),
            # rest(self.q),
            k.n(n3, self.q),
            rest(self.e), k.n(n2, self.e),
            rest(self.s), k.n(n2, self.e), rest(self.s)
        ]

        m4 = [
            k.n(n3, self.q),
            # rest(self.q),
            k.n(C3, self.q),
            rest(self.e), k.n(n2, self.e),
            rest(self.s), k.n(n2, self.e), rest(self.s)
        ]

        #   V1 -- Just Intro
        v1 = m1 + m1 + m3 + m4
        #   V2 -- Main beat
        v2 = m1 + m1 + m3 + m3

        if verse == "intro":
            return \
            v0 + v1
        
        elif verse == "loop":
            return \
            v2 + v2 +\
            \
            v2 + v2 +\
            v2 + v2
        
        return \
        v0 + v1 +\
        \
        v2 + v2 +\
        \
        v2 + v2 +\
        v2 + v2
        
    
    def bass_1(self, verse = "main"):
        b1 = self.bass1
        b2 = self.bass2

        m1 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q),
            b1.n(D2, self.q + self.e),
        ]

        m2 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q), rest(self.e),
            b1.n(D2, self.q),
        ]

        m3 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q),
            b1.n(D2, self.q + self.e),
        ]


        m4 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q), rest(self.e),
            b1.n(D2, self.q),
        ]
        


        m5 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q + self.e + self.q),
        ]

        m6 = [
            b1.n(E2, self.q + self.e),
            b1.n(G2, self.q + self.e),
            b1.n(D2, self.q),
        ]

        m7 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e + self.q),
        ]

        m8 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e),
            b1.n(D2, self.e), b1.n(E2, self.e),
        ]

        
        m9 = m5
        m10 = m6
        m11 = [
            b1.n(C2, self.q + self.e),
            b1.n(E2, self.q + self.e + self.q),
        ]
        v1 = m1 + m2 + m3 + m4
        v1b = m5 + m6 + m7 + m8
        
        v2 = m5 + m6 + m7 + m8

        v3 = m5 + m6 + m7 + m8

        if verse == "intro":
            return \
            v1 + v1b
        
        elif verse == "loop":
            return \
            v2 + v2 +\
            \
            v2 + v2 +\
            v2 + v2
    
        return \
        v1 + v1b +\
        \
        v2 + v2 +\
        \
        v2 + v2 +\
        v2 + v2
        
    
    def snare_1(self, verse = "main"):
        s = self.punchy_snare

        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
        ]

        m2 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.e), s.n(self.e),
        ]

        m4 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.s/2), s.n(self.s/2), s.n(self.s), s.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m4

        if verse == "intro":
            return \
            v0
        
        elif verse == "loop":
            return \
            v1 + v1 +\
            \
            v1 + v1 +\
            v1 + v1
        
        return \
        v0 +\
        \
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1
        

    def snare_2(self, verse = "main"):
        s = self.clicky_snare
        s1 = self.afro_snare

        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            rest(self.e), s.n(self.e),
            rest(self.q),
            rest(self.q),
        ]

        m2 = [
            rest(self.w)
        ]

        m6 = [
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
            s.n(self.q),
        ]

        m0 = [rest(self.w)]
        v1 = m1 + m1 + m2 + m2
        v2 = m1 + m1 + m2 + m2
        v3 = m1 + m1 + m0 + m6

        if verse == "intro":
            return \
            v0
        
        elif verse == "loop":
            return \
            v1 + v2 +\
            \
            v3 + v2 +\
            v3 + v2
        
        return \
        v0 +\
        \
        v1 + v2 +\
        \
        v3 + v2 +\
        v3 + v2
        


def main():
    beat = Title(78)
    vol = 18_000

    # beat.get_instruments()
    # beat.export_selection(name = "01_full", volume=vol)

    beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    beat.get_instruments("intro")
    beat.export_selection(name = "01_intro", volume=vol)
    beat.get_instruments("loop")
    beat.export_selection(name = "01_main", volume=vol)