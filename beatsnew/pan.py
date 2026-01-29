from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Pan(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("beatsnew", "experiments", "01"))
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
        
        self.bass1 = LowSynth(3.0, wave_2=False)
        self.bass3 = Bass_1(amp=0.6, attack=0.05, attack_max = 0.15, freq_mod = mod, decay = 0.0, sustain=1.0, release= 0.05, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

        #   Percussion  #
        ##  Chimes
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Kicks
        self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")

        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")

        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #

        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))

        
        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            # 'kick': [0, self.kicks(verse)],
            'hats': [0, self.hats(verse)],
            # 'crash': [0, self.cymbals(verse)],



            #   Melody  #
            'flute': [0, self.pan(verse)]


            #   Samples / Libs  #

        }

    
    
    def pan(self, verse="full"):
        p = self.pan1

        v1 = [p.n(self.w * 8)]

        return v1
    
    def cymbals(self, verse="full"):
        c = self.crash1
        m1 = [
            c.n(self.w)
        ]

        v1 = [rest(4.673)] + m1

        return v1
    
    def hats(self, verse="full"):
        h = self.closed1

        m1  = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]
        v1 = [rest(4.673)] + m1 + m1 + m1 + m1

        return v1

        
    def kicks(self, verse = "full"):
        k = self.kick1

        v0 = [rest(self.w*4)]
        
        m0 = [
            rest(self.w)
        ]

        m1 = [
            rest(self.q),
            k.n(self.q),
            rest(self.q),
            k.n(self.q),
        ]

        m2 = [
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
        ]

        v1 = m0 + m0 + m1 + m1

        v2 = m2 + m2 + m2 + m2
        
        return \
        v1 + v2
    
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
    
    


class Chill(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("beatsnew", "experiments", "01"))
        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Bass    ##5
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)

        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)
        
        self.bass1 = LowSynth(1.5, wave_1 = False, wave_2 = True, wave_3 = False, sustain=0.6)
        self.bass2 = LowSynth(1.0, wave_1 = False, wave_2=False, wave_3 = True,
                              sustain=1.0)
        self.bass3 = Bass_1(amp=0.8, 
                            freq_mod = (1.5), 
                            attack=0.01, attack_max = 0.02, decay=0.0, sustain=1.0, release=0.01,
                            amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

        #   Percussion  #
        ##  Chimes
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Kicks
        # self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")
        self.kick1 = Nine_Sample(amp=0.00003, name="kick-classic.wav")
        self.kick2 = E1_Samples(amp=0.00003, name="kick16.wav")

        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")

        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #
        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))

        
        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            # 'kick': [0, self.kicks(verse)],
            # 'snare': [0, self.snares(verse)],
            'drums1': [0, self.drums(verse)],
            'bass': [0, self.bass(verse)],
            # 'synth': [0, self.synths(verse)],



            # 'hats': [0, self.hats(verse)],
            # 'crash': [0, self.cymbals(verse)],



            #   Melody  #


            #   Samples / Libs  #
        }

    def synths(self, verse):
        b = self.bass1
        b2 = self.bass2

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.w)
        ]

        m2 = [
            b2.n(C3, self.s), b2.n(D3, self.s), b2.n(F3, self.s), b2.n(G3, self.s),
            b2.n(F3, self.s), b2.n(D3, self.s), rest(self.e),
            b2.n(C3, self.s), b2.n(D3, self.s), b2.n(F3, self.s), b2.n(G3, self.s),
            b2.n(F3, self.s), b2.n(E3, self.s), rest(self.e),
        ]

        m3 = [
            rest(self.q),
            b2.n(D3, self.e), b2.n(C3, self.e),
            b2.n(D3, self.q),
            b2.n(C3, self.q),
        ]

        v1 = m1 + m2 + m3 + m2

        return \
        v0 +\
        v1 + v1
    
    def bass(self, verse):
        b3 = self.bass3

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.q),
            b3.n(C1, self.q),
            rest(self.q),
            b3.n(C1, self.e), b3.n(D1, self.e)
        ]

        m2 = [
            rest(self.q),
            b3.n(C1, self.q),
            rest(self.q),
            b3.n(C1, self.q),
        ]

        m2b = [
            rest(self.q),
            rest(self.e), b3.n(C1, self.e),
            rest(self.q),
            rest(self.e), b3.n(C1, self.s), b3.n(B0, self.s),
        ]

        m3 = [
            b3.n(C1, self.q, amp = 0.6),
            rest(self.q),
            rest(self.q),
            rest(self.q)
        ]

        m4 = [
            rest(self.t),
            rest(self.e), b3.n(C1, self.s/2), b3.n(B0, self.s/2), b3.n(C1, self.s)
        ]

        m4b = [
            rest(self.q),
            rest(self.e), b3.n(C1, self.e),
            rest(self.q),
            rest(self.e), b3.n(C1, self.s/2), b3.n(B0, self.s/2), b3.n(C1, self.s)
        ]

        v0 = m2 + m0 + m2 + m4
        v1 = m1 + m2b + m3 + m4b

        return \
        v0 +\
        v1 + v1

    def drums(self, verse):
        k = self.kick1
        k2 = self.kick2
        s = self.snare4

        m1 = [
            k.n(self.q),
            s.n(self.q),
            k.n(self.q),
            s.n(self.e), s.n(self.e)
        ]

        m2 = [
            k.n(self.s), k.n(self.s), rest(self.s), s.n(self.e),
            k.n(self.s), s.n(self.e),
            k.n(self.e), k.n(self.e),
            s.n(self.q)
        ]

        m3 = [
            k.n(self.q),
            s.n(self.q),
            k.n(self.e), k.n(self.e),
            s.n(self.q)
        ]

        m4 = [
            k.n(self.s), k.n(self.s), rest(self.s), s.n(self.e),
            k.n(self.s), s.n(self.e),
            k.n(self.e), k.n(self.e),
            s.n(self.q)
        ]


        

        #   A couple ways to solve the bass overload issue  #
        # Could rest kick on bass
        # Could rest bass on kick
        # Decrease kick amp
        amp=0.6

        m5 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.e), s.n(self.e)
            ]
        
        m6a = [
            rest(self.e), rest(self.s), s.n(self.e),
            k.n(self.s), s.n(self.e),
            rest(self.e), rest(self.e),
            s.n(self.e), k.n(self.e)
        ]

        m6 = [
            k.n(self.s, amp), k.n(self.s, amp), rest(self.s), s.n(self.e),
            k.n(self.s, amp), s.n(self.e),
            k.n(self.e, amp), k.n(self.e, amp),
            s.n(self.q)
        ]

        m7 = [
            k.n(self.q, amp),
            s.n(self.q),
            k.n(self.e, amp), k.n(self.e, amp),
            s.n(self.q)
        ]

        m8 = [
            k.n(self.s, amp), k.n(self.s, amp), rest(self.s), s.n(self.e),
            k.n(self.s, amp), s.n(self.e),
            k.n(self.e, amp), k.n(self.e, amp),
            s.n(self.q)
        ]

        v1 = m1 + m2 + m3 + m4
        # v2 = m5 + m6 + m7 + m8
        v2 = m3 + m6 + m7 + m8

        return \
        v1 +\
        v2 + v2

def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Chill(64)
    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    # beat.export_selection(name="01_prod", volume=30_500)

    # beat.export_selection(name="02_prod", volume=30_500)
    beat.export_selection(name="02_drumsnbass", volume=30_500)

