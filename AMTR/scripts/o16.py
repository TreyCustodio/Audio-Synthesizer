from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Exp(Beat):
    def __init__(self, bpm, name="16"):
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
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

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

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")
        self.sumo_snare = Nine_Sample(name="snare-sumo.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #
        self.synth1 = Eighties_Synths(amp=0.00005)
        self.synth2 = Eighties_Synths(amp=0.00005, path=os.path.join("Arps and Leads", "105bpm", "80s_FairLead[105]-D.wav"))
        self.synth3 = Eighties_Synths(amp=0.00003, path=os.path.join("Polys and Pads", "105bpm", "80s_ProBrass[105]-A.wav"))
        self.scratch = GlobalSample(0.0001, os.path.join("samples", "records", "retro_scratch2.wav"))
        self.scratch2 = GlobalSample(0.0001, os.path.join("samples", "records", "retro_scratch3.wav"))


        
    
        self.rain1 = GlobalSample(0.0001, os.path.join("samples", "vocals", "lofi_rain.wav"))
        self.vocal1 = GlobalSample(0.00004, os.path.join("samples", "vocals", "95_slow.wav"))

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
            # 'clicks': [0, self.clicks(verse)],
            # 'chimes': [0, self.chimes(verse)],
            # 'bass':[0, self.bass(verse)],


            #   Melody  #


            #   Samples / Libs  #
            'vocal1': [0, self.vocals_1(verse)],
            'rain': [0, self.rain(verse)],

            # 'synth1': [0, self.synth(verse)],
            # 'synth2': [0, self.synth_2(verse)],
            # 'synth3': [0, self.synth_3(verse)],


        }
    
    def bass(self, verse):
        b = self.bass1

        m1 = [

        ]

        return \
        
    def vocals_1(self, verse):
        v = self.scratch
        v2 = self.scratch2


        v0 = [rest(self.w*4)]

        m4 = [
            rest(self.h),
            v.n(self.q, amp=0.1),
            rest(self.q),
        ]

        m8 = [
            rest(self.h),
            v.n(self.q, amp=0.1),
            v2.n(self.q, amp=0.1),
        ]

        v1 = [rest(self.w*3)] + m4
        v2 = [rest(self.w*3)] + m8


        return \
        v0 + v0 +\
        v1 + v2 + v1
    
    def rain(self, verse):
        r = self.rain1

        v0 = [rest(self.w*4)]
        v1 = [
            r.n(self.w*4)
        ]
        v2 = [
            r.n(self.w*4, amp=0.5)
        ]

        return \
        v1 + v2 +\
        v2 + v2 + v2


    
    def hats(self, verse):
        h = self.closed2

        v0 = [rest(self.w*4)]
        m1 = [
            h.n(self.s), h.n(self.s), rest(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), rest(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), rest(self.s*3),

        ]

        m2 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), rest(self.s*3),
        ]

        m4 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            rest(self.h)
        ]

        v1 = m1 + m2 + m1 + m4
        v2 = m1 + m2 + m1 + m4

        return \
        v0 + v0 +\
        v1 + v1 + v1
    
    def drums(self, verse):
        k = self.tight_kick
        s = self.snare8
        s2 = self.snare3


        m1 = [
            k.n(self.q),
            rest(self.q),
            k.n(self.q),
            s.n(self.q),
        ]

        m2 = [
            k.n(self.q),
            # delaycombo(s.n(self.e), s2.n(self.e), self.s, False), rest(self.s),
            s.n(self.e), k.n(self.e),
            k.n(self.q),
            s.n(self.q),
        ]

        m2b = [
            k.n(self.q),
            # delaycombo(s.n(self.e), s2.n(self.e), self.s, False), rest(self.s),
            s.n(self.e), s2.n(self.e),
            k.n(self.q),
            s.n(self.q),
        ]

        m3 = [
            k.n(self.q),
            s.n(self.e), k.n(self.e),
            k.n(self.q),
            s.n(self.e), rest(self.s), s.n(self.s),
        ]

        m5 = [
            k.n(self.e), k.n(self.e),
            s.n(self.e), k.n(self.e),
            k.n(self.q),
            s.n(self.e), rest(self.s), s.n(self.s),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m2
        v2 = m5 + m2 + m2 + m2

        return \
        v0 + v1 +\
        v2 + v2 + v2
    
def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Exp(95)



    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="production", volume=30_500)
    # beat.export_selection(name="03_prod", volume=30_500)