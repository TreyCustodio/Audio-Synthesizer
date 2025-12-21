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
        
        self.bass1 = LowSynth(2.0)
        
        self.bass2 = Bass_1(amp=0.6, attack=0.05, attack_max = 0.15, freq_mod = mod, decay = 0.0, sustain=1.0, release= 0.05, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

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
    
    

    
def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Pan(115)
    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="01_prod", volume=30_500)