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

        self.snare5 = GlobalSample(0.00005, os.path.join("samples", "snares", "snare_5.wav"))
        
        self.lofi_snare = Rapping.Lofi_Snare(amp=0.00005)
        
        self.crackle_snare = Rapping.Crackle_Snare(amp=0.00001)
        
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.wav"))
        
        self.lofi_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "lofi_snare.wav"))
        
        self.punchy_snare = GlobalSample(0.00008, os.path.join("samples", "snares", "punchy_snare.wav"))
        
        self.clicky_snare = GlobalSample(0.00005, os.path.join("samples", "snares", "clicky_snare.wav"))
       

       #    Kicks   #
        self.kick1 = Tap4(1.0, attack=0.001, decay = 0.03, sustain=0.0, noise_amount=0.0)
        
        self.kick2 = GlobalSample(amp=0.00002, file_path=os.path.join("samples", "kick", "new-kick.wav"))
        
        self.kick3 = GlobalSample(amp=0.000005, file_path=os.path.join("samples", "kick", "new-kick_2.wav"))

        self.kick4 = GlobalSample(amp=0.00001, file_path=os.path.join("samples", "kick", "kick_1.wav"))


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
        self.main_midi = GlobalSample(0.00005, os.path.join("samples", "AMTR", "07_MIDI.wav"))
        self.v1_midi = GlobalSample(0.00005, os.path.join("samples", "AMTR", "07_v1.wav"))
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
            "kicks": [0, self.kick(verse)],
            "snare": [0, self.snare(verse)],

            #   Melody  #



            #   Samples / Libs  #
        }

    
    def kick(self, verse):
        # k = self.kick3
        k = self.kick4


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
            k.n(self.q),
            rest(self.q),
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
            v2 + v1 + v3 +\
            \
            v4
        
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

    
    

def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Rev(120)
    beat.get_instruments("full")
    beat.export_selection(name="07_full", volume=30_500)

    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    # beat.get_instruments("intro")
    # beat.export_selection(name="07_intro", volume=30_500)

    # beat.get_instruments("main")
    # beat.export_selection(name="07_main", volume=30_500)