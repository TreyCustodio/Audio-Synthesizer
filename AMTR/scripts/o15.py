from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Exp(Beat):
    def __init__(self, bpm, name="15"):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", name))
        #   Instruments #


        #   Melody  #
            

        #   Rhythm / Percussion  #
        ##  Bass    ##
        self.bell = AMTR.Bell(amp=0.1, freq_mod=1.0, wave_2 = False, wave_3=False,
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
        self.tight_kick = Nine_Sample(amp=0.00004, name="kick-tight.wav")
        self.dry_kick = Nine_Sample(amp=0.00007, name="kick-dry.wav")

        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")
        self.crash2 = Nine_Sample(name="crash-808.wav")


        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav", amp=0.00005)
        self.per_tambo = Nine_Sample(name="perc-tambo.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.closed2 = Nine_Sample(amp = 0.00008, name="hihat-electro.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")
        self.digi1 = Nine_Sample(name="hihat-digital.wav")
        self.perc = Nine_Sample(amp=0.00005, name="perc-808.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")
        self.snare5 = Nine_Sample(amp=0.00007, name="snare-analog.wav")
        self.snare8 = Nine_Sample(amp=0.00007, name="snare-808.wav")
        self.cold_snare = GlobalSample(0.00007, os.path.join("samples", "snares", "snare_5.wav"))


        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")
        self.sumo_snare = Nine_Sample(name="snare-sumo.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")
        self.tom2 = Nine_Sample(name="tom-short.wav")



        #   Samples #
        self.synth1 = Eighties_Synths(amp=0.00005)
        self.synth2 = Eighties_Synths(amp=0.00005, path=os.path.join("Arps and Leads", "105bpm", "80s_FairLead[105]-D.wav"))
        self.synth3 = Eighties_Synths(amp=0.00005, path=os.path.join("Arps and Leads", "105bpm", "80s_FairLead[105]-A2.wav"))

        
        
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
            'kicks2': [0, self.kick_2(verse)],
            'snare2': [0, self.snare_2(verse)],
            'hats': [0, self.hats(verse)],
            'clicks': [0, self.clicks(verse)],
            'crash': [0, self.crash(verse)],



            #   Melody  #


            #   Samples / Libs  #
            'synth1': [0, self.synth(verse)],
            'synth2': [0, self.synth_2(verse)],


        }

    def synth(self, verse):
        s = self.synth1

        v0 = [rest(self.w*4)]
        v1 = [
            s.n(self.w*4)
        ]

        return \
        v1 +\
        v1 + v1 + v1 + v1 +\
        v0 + v0 +\
        v1 + v1 + v0 + v0 +\
        v0 + v0 + v1 + v1
    
    def synth_2(self, verse):
        s = self.synth2
        s2 = self.synth3

        v0 = [rest(self.w*4)]
        v1 = [
            s.n(self.w*4)
        ]

        m1 = [
            s2.n(self.q),
            s.n(self.t),
        ]

        m3 = [
            s.n(self.q, start_time=self.w),
            s.n(self.t),
        ]

        m4 = [
            s.n(self.w, start_time = self.w*3)
        ]


        v2 = m1 + m3 + m1 + m4
        v3 = m3 + m1 + m1 + m4


        return \
        v0 +\
        v0 + v1 + v1 + v1 +\
        v1 + v1 +\
        v2 + v3 + v2 + v3 +\
        v2 + v3 + v2 + v3
    

    
    def kick_2(self, verse):
        t = self.tom2

        m1 = [
            t.n(self.w, amp=0.3),
        ]

        m2 = [
            t.n(self.q, amp=0.3),
            rest(self.h),
            rest(self.e), t.n(self.e, amp=0.3)
        ]

        m4 = [
            t.n(self.q, amp=0.3),
            rest(self.h),
            t.n(self.q, amp=0.3),
        ]

        m4b = [
            t.n(self.q, amp=0.3),
            rest(self.e), t.n(self.e, amp=0.3),
            rest(self.q),
            t.n(self.s, amp=0.3), t.n(self.s, amp=0.3), t.n(self.s, amp=0.3), t.n(self.s, amp=0.3),
        ]

        # amp = 0.1 when mixed with other instruments
        m5 = [
            t.n(self.q, amp=0.3),
            rest(self.e), t.n(self.e, amp=0.3),
            rest(self.q),
            rest(self.s), t.n(self.s, amp=0.3), t.n(self.s, amp=0.3), t.n(self.s, amp=0.3)
        ]

        m6 = [
            t.n(self.q, amp=0.3),
            rest(self.e), t.n(self.e, amp=0.3),
            rest(self.q),
            t.n(self.e, amp=0.3), t.n(self.e, amp=0.3),
        ]

        m8 = [
            t.n(self.q, amp=0.1),
            rest(self.h),
            t.n(self.s, amp=0.1), t.n(self.s, amp=0.1), t.n(self.s, amp=0.1), t.n(self.s, amp=0.1),
        ]

        
        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m4
        v1b = m5 + m6 + m5 + m4b
        v2 = m5 + m5 + m5 + m8


        return \
        v0 +\
        v0 + v0 + v0 + v0 +\
        v1 + v1b +\
        v0 + v0 + v0 + v0
    
    def clicks(self, verse):
        h = self.perc
        h2 = self.closed2

        m1 = [
            h.n(self.q),
            rest(self.t - self.e),
            h.n(self.s), h.n(self.s),
        ]

        m2 = [
            h.n(self.s), h.n(self.s), h.n(self.e),
            rest(self.t)
        ]

        m4 = [
            h.n(self.s), rest(self.s*3),
            rest(self.t)
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
        v2 = m1 + m2 + m1 + m4

        return \
        v0 +\
        v0 + v0 + v0 + v0 +\
        v1 + v2 +\
        v1 + v1 + v1 + v1
    
    def hats(self, verse):
        h = self.closed2
        h2 = self.closed2

        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            rest(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            rest(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        m2 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            h.n(self.q),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
        ]

        m4 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            h.n(self.q - self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s), 
        ]

        m5 = [
            h2.n(self.s), h2.n(self.s), h2.n(self.s), h2.n(self.s),
            h2.n(self.s), h2.n(self.s), h2.n(self.s), h2.n(self.s),
            h2.n(self.s), h2.n(self.s), h2.n(self.s), h2.n(self.s),
            h2.n(self.s), h2.n(self.s), h2.n(self.s), h2.n(self.s),
        ]

        m9 = [
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
        ]

        m10 = [
            h2.n(self.s), h2.n(self.s), h2.n(self.s), rest(self.s),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.s), h2.n(self.s), h2.n(self.s), rest(self.s),
        ]

        m12 = [
            h2.n(self.s), h2.n(self.s), h2.n(self.s), rest(self.s),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.e), h2.n(self.e),
            h2.n(self.s), h2.n(self.s), h2.n(self.s), h2.n(self.s),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m4
        v2 = m5 + m5 + m5 + m5
        v3 = m9 + m10 + m9 + m12

        return \
        v0 +\
        v0 + v1 + v2 + v1 +\
        v0 + v0 +\
        v1 + v2 + v1 + v2 +\
        v0 + v3 + v2 + v2
    
    def snare_2(self, verse):
        # s = self.snare8
        s = self.shake1
        c = self.cold_snare


        m0 = [
            rest(self.w)
        ]

        m1 = [
            rest(self.q),
            rest(self.e), s.n(self.e),
            rest(self.q),
            rest(self.q),
        ]

        m2 = [
            rest(self.q),
            rest(self.e), s.n(self.e),
            rest(self.q),
            rest(self.e), s.n(self.e),
        ]

        m5 = [
            rest(self.q),
            c.n(self.q),
            rest(self.h)
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m0 + m0 + m0
        v2 = m5 + m5 + m5 + m5

        return \
        v0 +\
        v1 + v1 + v1 + v1 +\
        v0 + v0 +\
        v1 + v1 + v1 + v1 +\
        v2 + v2 + v1 + v1
    
    def drums(self, verse):
        k = self.tight_kick
        s = self.snare5
        s2 = self.snare8
        c = self.cold_snare

        #   Variant 1   #
        m1 = [
            k.n(self.s), k.n(self.s), rest(self.s), k.n(self.s),
            s.n(self.q),
            rest(self.e), k.n(self.e),
            s.n(self.e), rest(self.s), s.n(self.s)
        ]

        m2 = [
            k.n(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            s.n(self.q),
            rest(self.e), k.n(self.e),
            delaycombo(s.n(self.e), k.n(self.s), rest_time = self.s, silence = False), s.n(self.e),
        ]

        #   Variant 2   #
        m5 = [
            k.n(self.q),
            rest(self.q),
            rest(self.e), k.n(self.e),
            rest(self.s), k.n(self.e), rest(self.s)
        ]

        m6 = [
            k.n(self.q),
            rest(self.q),
            rest(self.e), k.n(self.e),
            rest(self.q),
        ]

        m8 = [
            k.n(self.q),
            rest(self.q),
            rest(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
        ]

        #   Variant 3   #
        m9 = [
            k.n(self.s), k.n(self.s), rest(self.s), k.n(self.s),
            rest(self.q),
            rest(self.e), k.n(self.e),
            rest(self.q),
        ]

        m10 = [
            k.n(self.s), k.n(self.s), k.n(self.s), rest(self.s),
            rest(self.q),
            rest(self.e), k.n(self.e),
            rest(self.s), k.n(self.s), rest(self.e),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m1 + m2
        v2 = m5 + m6 + m5 + m8
        v3 = m9 + m10 + m9 + m10

        return \
        v0 +\
        v1 + v1 + v1 + v1 +\
        v0 + v0 +\
        v1 + v1 + v1 + v1 +\
        v2 + v3 + v1 + v1
    
    def crash(self, verse):
        c = self.crash2

        m0 = [rest(self.w)]
        m4 = [
            rest(self.t),
            c.n(self.q, amp=0.3)
        ]

        v0 = [rest(self.w*4)]
        v1 = m0 + m0 + m0 + m4
        
        return \
        v0 +\
        v0 + v0 + v0 + v0 +\
        v0 + v1 +\
        v0 + v0 + v0 + v0 +\
        v0 + v1 + v0 + v0
    
def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Exp(105)



    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="production", volume=30_500)
    # beat.export_selection(name="03_prod", volume=30_500)