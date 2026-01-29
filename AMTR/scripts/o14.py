from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Exp(Beat):
    def __init__(self, bpm, name="14"):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", name))
        #   Instruments #


        #   Melody  #
            

        #   Rhythm / Percussion  #
        ##  Bass    ##
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
        self.tight_kick = Nine_Sample(amp=0.00003, name="kick-tight.wav")
        self.dry_kick = Nine_Sample(amp=0.00007, name="kick-dry.wav")

        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")
        self.crash2 = Nine_Sample(name="crash-808.wav")


        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.closed2 = Nine_Sample(name="hihat-electro.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")
        self.digi1 = Nine_Sample(name="hihat-digital.wav")
        self.perc = Nine_Sample(name="perc-808.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")
        self.snare5 = Nine_Sample(amp=0.00007, name="snare-analog.wav")


        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")
        self.sumo_snare = Nine_Sample(name="snare-sumo.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #
        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))
        self.fx9 = E1_Samples(name="fx09.wav")
        self.hey = GlobalSample(0.0001, os.path.join("samples", "hey.wav"))
        self.drop = GlobalSample(0.001, os.path.join("samples", "ambience", "drop_1.wav"))
        self.square = GlobalSample(0.0001, os.path.join("samples", "playful_square_80.wav"))
        self.steel_c = GlobalSample(0.000012, os.path.join("samples", "steel", "steel_pan_c.wav"))
        self.steel_a = GlobalSample(0.000012, os.path.join("samples", "steel", "steel_pan_a.wav"))

        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],
            'chimes': [0, self.chimes(verse)],


            #   Melody  #


            #   Samples / Libs  #
            'square': [0, self.sq(verse)]
        }

    def sq(self, verse):
        s = self.square
        

        v1 = [
            s.n(self.w*2, fadeIn = True, fade_amount=1),
            s.n(self.w*2),
        ]

        v2 = [
            s.n(self.w*2),
            s.n(self.w*2),
        ]

        v3 = [
            s.n(self.w*2, amp = 0.3),
            s.n(self.w*2, amp = 0.3),
        ]

        return \
        v1 +\
        v2 +\
        v2 + v3 + v2
    
    def chimes(self, verse):
        sC = self.steel_c
        sA = self.steel_a

        m0 = [
            rest(self.w)
        ]

        m1 = [
            sC.n(self.q),
            rest(self.t)
        ]

        m2 = [
            sC.n(self.q),
            rest(self.q),
            rest(self.q),
            rest(self.e), sA.n(self.e),
        ]

        m5 = [
            sC.n(self.q),
            rest(self.h),
            rest(self.e), sA.n(self.e)
        ]

        m8 = [
            sC.n(self.q),
            rest(self.q),
            rest(self.e), sA.n(self.e),
            rest(self.s), sA.n(self.q - self.s),
        ]

        v1 = m0 + m0 + m1 + m2
        v2 = m1 + m5 + m1 + m2
        v3 = m5 + m1 + m5 + m8

        return \
        v1 +\
        v2 + \
        v3 + v3 + v3

    def hats(self, verse):
        h = self.perc
        h2 = self.closed2

        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            rest(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            rest(self.s), h.n(self.s), h.n(self.s/2), h.n(self.s/2), h.n(self.s),
        ]

        m2 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            rest(self.q),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
        ]

        m1b = [
            h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), 
            rest(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s),
            h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), 
            rest(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s/2) + h2.n(self.s/2), h.n(self.s/2) + h2.n(self.s/2), h.n(self.s) + h2.n(self.s),
        ]

        m2b = [
            h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s),
            rest(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s),
            h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s),
            h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s), h.n(self.s) + h2.n(self.s),
        ]

        m5 = [
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
        ]

        m6 = [
            h2.n(self.s), h2.n(self.s), h2.n(self.s), rest(self.s),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m2
        v2 = m1b + m2b + m1b + m2b
        v3 = m5 + m6 + m5 + m6

        return \
        v0 +\
        v1 +\
        v2 + v3 + v2
    
        
    def drums(self, verse):
        k = self.tight_kick
        s = self.snare5
        s2 = self.snare_lof


        m1 = [
            k.n(self.s), k.n(self.s), rest(self.s), k.n(self.s),
            delaycombo(s.n(self.q), s2.n(self.e), rest_time = self.e, silence=False),
            rest(self.e), k.n(self.e),
            s.n(self.e), rest(self.s), s.n(self.s)
        ]

        m2 = [
            k.n(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            delaycombo(s.n(self.q), s2.n(self.e), rest_time = self.e, silence=False),
            rest(self.e), k.n(self.e),
            delaycombo(s.n(self.e), k.n(self.s), rest_time = self.s, silence = False), s.n(self.e),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m2

        return \
        v0 +\
        v0 +\
        v1 + v1 + v1
    
def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Exp(80)

    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="production", volume=30_500)
    # beat.export_selection(name="03_prod", volume=30_500)