from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Temp(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "temp"))
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

        #   Hats    #
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
        self.crash1 = Cymbal(amp=1.0)




        #   ----- Dictionary of Instruments -----   #
        self.instruments = {}

        self.vi = [rest(self.w*4 - self.e)]

    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            "kicks": [0, self.kick(verse)],
            "snare": [0, self.snare(verse)],
            "hat": [0, self.hat(verse)],



            #   Melody  #



            #   Samples / Libs  #

        }

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
            k.n(self.q),
            rest(self.q)
        ]

        m1b = [
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
        ]


        vi = m1 + m1 + m1b + m1b

        v1 = m1b + m1b + m1b + m1b


        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        vi + v1 + v1
        

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

        v1 = m1 + m1 + m1 + m1
        vi = m0 + m0 + m1 + m1


        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        v0 + vi +\
        v1

    def hat(self, verse):
        h = self.hat1


        v0 = [
            rest(self.w*4)
        ]


        m0 = [
            rest(self.w)
        ]

        m2 = [
            rest(self.h),
            rest(self.e), h.n(self.s), h.n(self.s),
            h.n(self.e), h.n(self.e),
        ]
        
        vi = m0 + m0 + m0 + m2
        v1 = m0 + m2 + m0 + m2

        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        vi + v1 + v1
    
    



class Temp2(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "temp"))
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
        self.hat1 = Rapping.Hat_2(amp=0.0001)

        #   Snares  #
        self.snare1 = E1_Samples(0.0000055, "perc12.wav")
        self.snare2 = E1_Samples(0.00005, "perc12.wav")


        #    Kicks   #
        self.kick1 = E1_Samples(amp=0.00001, name="kick04.wav")


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

        # self.crash1 = GlobalSample(0.000005, os.path.join("samples", "ambience", "crash_1.wav"))

        self.crash1 = Cymbal(amp=1.0)




        #   ----- Dictionary of Instruments -----   #
        self.instruments = {}

        self.vi = [rest(self.w*4 - self.e)]

    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            "kicks": [0, self.kick(verse)],
            "snare": [0, self.snare(verse)],
            "hat": [0, self.hat(verse)],
            # "hat2": [0, self.hat_2(verse)],



            #   Melody  #



            #   Samples / Libs  #

        }

    def kick(self, verse):
        k = self.kick1

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
            rest(self.q)
        ]



        # vi = m1 + m1 + m1b + m1b

        v1 = m1 + m1 + m1 + m1

        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        v1 + v1 + v1
        

    def hat(self, verse):
        s = self.hat1

        v0 = [rest(self.w*4)]

        m0 = [
            rest(self.w)
        ]

        m1 = [
            s.n(self.q),
            s.n(self.q),
            s.n(self.q),
            s.n(self.q),
        ]

        m2 = [
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
        ]

        m4 = [
            rest(self.e),
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
            s.n(self.q),
        ]

        v1 = m1 + m1 + m2 + m4
        vi = m0 + m0 + m1 + m1


        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        v1 + v1 + v1

    def hat_2(self, verse):
        s = self.crash1

        m0 = [
            rest(self.w)
        ]

        m2 = [
            s.n(E3, self.q),
            rest(self.e),
            s.n(C3, self.q),
            rest(self.e),
            s.n(E3, self.q),
        ]

        m4 = [
            rest(self.e),
            s.n(C3, self.q),
            rest(self.e),
            s.n(E3, self.q),
            s.n(C3, self.q),
        ]

        v1 = m0 + m0 + m2 + m4

        return \
        v1 + v1 + v1
    
    def hat_2(self, verse):
        s = self.snare2

        m0 = [
            rest(self.w)
        ]

        m2 = [
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
        ]

        m4 = [
            rest(self.e),
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
            s.n(self.q),
        ]

        v1 = m0 + m0 + m2 + m4

        return \
        v1 + v1 + v1
    
    def snare(self, verse):
        s = self.snare1


        v0 = [
            rest(self.w*4)
        ]


        m0 = [
            rest(self.w)
        ]

        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.q)
        ]
        
        v1 = m1 + m1 + m1 + m1

        if verse == "intro":
            return v1
        
        elif verse == "main":
            return \
            v1
        
        return \
        v1 + v1 + v1
    

def main():
    """
    One more Verse to loop back to verse 1.
    """

    beat = Temp2(220)
    beat.get_instruments("full")
    beat.export_selection(name="bowser_full", volume=60_500)

    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    # beat.get_instruments("intro")
    # beat.export_selection(name="07_intro", volume=60_500)

    # beat.get_instruments("main")
    # beat.export_selection(name="07_main", volume=60_500)