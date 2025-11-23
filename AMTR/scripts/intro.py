from modules import *

"""
05 - Intro
"""

class Intro(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, name = "Welcome_To_Earth", path=os.path.join("AMTR", "ost", "05"))

        #   Instruments #


        #   Melody  #
        self.saw = Saw()
        self.synth1 = Acoustic3(amp=0.5, harmonics=12, attack=0.001, attack_max=0.01, decay=0.0, sustain=1.0, release=0.01,
                                # vol_1 = 4.0, vol_2 = 0.3,
                                vol_3 = 1.0, vol_4=0.000000000001,
                                )
        
        self.key1 = Tangible_Light.Bell(amp=0.5, freq_mod=1.5, wave_2 = False, wave_3=False)
        self.key2 = Tangible_Light.Bell(amp=0.5, freq_mod=3, wave_2 = False, wave_3=False)

        #   Rhythm / Percussion  #
        ##  Bass    ##
        mod = 0.5
        # self.bass1 = Bass_1(amp=1.0, attack=0.005, attack_max = 0.003, freq_mod = mod, sustain=0.3, release= 0.01, amp_final = 0.1, top_freq = 2, harmonics=2)
        # self.bass1 = Acoustic3(amp=0.2,
        #                        freq_mod=1, harmonics=4,
        #                        attack=0.01, attack_max=0.055, decay=0.1, sustain=1.0, release=0.01,
        #                        vol_1=1.0, vol_2=1.0,
        #                        vol_3=1.0, vol_4=1.0,
        #                        vol_5=1.0, vol_6=1.0,
        #                        vol_7=0.0, vol_8=0.0
        #                        )
        self.bass1 = Bass_1(amp=0.3, attack=0.01, attack_max = 0.02, freq_mod = 1, sustain=1.0, release= 0.01, amp_final = 0.00000000001, harmonics=3)
        # self.bass2 = Bass_1(amp=1.0, attack=0.003, attack_max = 0.005, freq_mod = mod, sustain=1.0, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)
        self.hat4 = Hat_4(amp=0.00004)
        self.hatd = Rapping.Drill_Hat(amp=0.00005)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00005)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)

        ##  Kicks   ##
        self.kick1 = Tap4(5.0, attack=0.001, decay = 0.025, sustain=0.0, noise_amount=0.00000)
        self.kick2 = GlobalSample(amp=0.00003, file_path=os.path.join("samples", "kick", "new-kick.wav"))


        #   Samples #
        self.go = Go(amp=0.00001 * 1.5)
        self.surprise = Rapping.Surprise(amp=0.00000002)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.record1 = GlobalSample(0.00003, os.path.join("samples", "records", "record_1.wav"))
        self.record2 = GlobalSample(0.00003, os.path.join("samples", "records", "record_2.wav"))
        self.bass_m = GlobalSample(0.0001, os.path.join("samples", "AMTR", "05_Bass_MIDI.wav"))
        

        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'kick1': [self.kick1, self.kicks(self.kick1, verse = verse)],
            'snare1': [self.snare1, self.snares_1(verse = verse)],
            # 'hats1': [self.hat1, self.hats_1()],
            'bass1': [self.bass1, self.bass_1(verse = verse)],
            'bass_midi': [self.bass1, self.bass_midi(verse = verse)],

            

            #   Melody  #
            'key1': [self.saw, self.key_1(verse = verse)],
            'key1b': [self.saw, self.key_1b(Tangible_Light.Bell(amp=0.25, freq_mod=1.5, wave_2 = False, wave_3=False), verse = verse)],
            'key1c': [self.saw, self.key_1c(Tangible_Light.Bell(amp=0.25, freq_mod=1.5, wave_2 = False, wave_3=False), verse = verse)],
            
            'key2': [self.saw, self.key_2(verse = verse)],
            'key2b': [self.saw, self.key_2b(Tangible_Light.Bell(amp=0.25, freq_mod=3, wave_2 = False, wave_3=False), verse = verse)],
            'key2c': [self.saw, self.key_2c(Tangible_Light.Bell(amp=0.25, freq_mod=3, wave_2 = False, wave_3=False), verse = verse)],


            #   Samples / Libs  #
            # 'goha': [self.go, self.go_1()],


            #   Tag #
            # 'tag': [self.t, self.tag()],


        }

    def __str__(self):
        return \
        "\n\
        Track Name: " + self.fileName + "\n\
        \n\
        Instrument Sections:\
        \n\
        Intro: 12 Bars\n\
        Main: 16 Bars\n\
        \n\
        Full Length: 28 Bars\n\
        Total Time: " + str(self.str_total_time()) + " seconds"   
    
    def str_total_time(self):
        duration = self.get_duration()
        minutes = int(duration / self.bpm)
        seconds = duration % self.bpm

        return str(minutes) + ":" + str(seconds)

    def get_duration(self):
        # I have 28 bars
        # Each bar has 4 beats
        # Thus I have 28 * 4 beats
        # Which is 112 beats.
        #
        # There are 64 beats per minute
        #   
        # And I have 112 beats to get through.
        # 112 / 64 = 1 minute with 48 beats left over.
        # 
        print(len(self.production))
        return (round((self.bpm / 60) * 28, 2)) + 60

    def bass_midi(self, verse = "full"):
        b = self.bass_m

        if verse == "main":
            return [b.n(self.w * 16, start_time = self.w*12)]

        elif verse == "intro":
            return [b.n(self.w * 12)]
        
        return [b.n(self.w * 28)]
    
    def bass_1(self, verse="full"):
        """Bass part 1"""
        b = self.bass1

        v0 = [rest(self.w*4)]

        m1 = [
            b.n(A1, ((self.w * 2) - self.e)),
            b.n(G1, self.e) # 7.5
        ]

        m2 = [
            b.n(A1, (self.w)),
            b.n(A1, self.w - self.e),
            b.n(G1, self.e) # 7.5
        ] 

        m3 = [
            b.n(A1, (self.w*2)),
        ]

        m4 = [
            b.n(A1, self.w)
        ]

        v1 = m1 + m2 # 4
        v2 = m3 + m3 # 8
        v3 = m4 + m4 + m4 + m4 # 12

        if verse == "main":
            #   16 Bars
            return \
            v1 + v3 +\
            v1 + v0
        
        elif verse == "intro":
            #   12 Bars
            return \
            v1 + v2 + v3
            
        #   28 Bars
        return \
        v1 + v2 + v3 +\
        v1 + v3 +\
        v1 + v0
        
        
    
    def key_1(self, verse = "full"):
        k = self.key1

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(A3, self.e), # 2.5
            rest(self.s), k.n(G3, self.e), # 3.25
            rest(self.s), k.n(A3, self.e), # 4
        ]

        v2 = m5 + m5 + m5 + m5

        
        if verse == "main":
            return \
            v1 + v2 +\
            v1 + v2
        
        elif verse == "intro":
            return \
            v0 + v1 + v2
        
        return \
        v0 + v1 + v2 +\
        v1 + v2 +\
        v1 + v2
    
    def key_1b(self, k, verse = "full"):
        """Echo of key1"""
        amp = 1.0

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), rest(self.s), k.n(A3, self.s, amp), k.n(A3, self.s, amp), # 1.25
            rest(self.s), k.n(G3, self.s, amp), k.n(G3, self.s, amp), # 2
            rest(self.s), k.n(A3, self.s, amp), k.n(A3, self.s, amp), # 2.75
            rest(self.s), k.n(G3, self.s, amp), k.n(G3, self.s, amp), # 3.5
            rest(self.s), k.n(A3, self.s, amp), # 4.25
        ]

        m6 = [
            k.n(A3, self.s, amp), rest(self.s), rest(self.e),
            k.n(A3, self.s, amp), rest(self.e), 
            k.n(G3, self.s, amp), rest(self.e),
            k.n(A3, self.s, amp), rest(self.e),
            k.n(G3, self.s, amp), rest(self.e),
        ]

        v2 = m5 + m6 + m5 + m6

        if verse == "main":
            return \
            v0 + v0 +\
            v1 + v2
        
        elif verse == "intro":
            return \
            v0 + v0 + v0
        
        return \
        v0 + v0 + v0 +\
        v0 + v0 +\
        v0 + v2

    def key_1c(self, k, verse = "full"):
        """Echo of key1"""
        amp = 1.0

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), rest(self.s), rest(self.s), k.n(A3, self.s, amp), # 1.25
            rest(self.s), rest(self.s), k.n(G3, self.s, amp), # 2
            rest(self.s), rest(self.s), k.n(A3, self.s, amp), # 2.75
            rest(self.s), rest(self.s), k.n(G3, self.s, amp), # 3.5
            rest(self.s), rest(self.s), # 4.25
        ]

        m6 = [
            k.n(A3, self.s, amp), rest(self.s), rest(self.e),
            k.n(A3, self.s, amp), rest(self.e), 
            k.n(G3, self.s, amp), rest(self.e),
            k.n(A3, self.s, amp), rest(self.e),
            k.n(G3, self.s, amp), rest(self.e),
        ]

        v2 = m5 + m6 + m5 + m6


        if verse == "main":
            return \
            v0 + v2 +\
            v0 + v0
        
        elif verse == "intro":
            return \
            v0 + v0 + v0
        
        return \
        v0 + v0 + v0 +\
        v0 + v2 +\
        v0 + v0


    def key_2(self, verse = "full"):
        k = self.key2

        m0 = [rest(self.w)]
        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(A3, self.e), # 2.5
            rest(self.s), k.n(G3, self.e), # 3.25
            rest(self.s), k.n(A3, self.e), # 4
        ]

        v2 = m0 + m0 + m5 + m5

        if verse == "main":
            return \
            v0 + v2 +\
            v0 + v2
        
        elif verse == "intro":
            return \
            v0 + v0 + v2
        
        return \
        v0 + v0 + v2 +\
        v0 + v2 +\
        v0 + v2
    
    def key_2b(self, k, verse = "full"):
        """Echo of key1"""

        v0 = [rest(self.w*4)]
        m0 = [rest(self.w)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), rest(self.s), k.n(A3, self.s), k.n(A3, self.s), # 1.25
            rest(self.s), k.n(G3, self.s), k.n(G3, self.s), # 2
            rest(self.s), k.n(A3, self.s), k.n(A3, self.s), # 2.75
            rest(self.s), k.n(G3, self.s), k.n(G3, self.s), # 3.5
            rest(self.s), k.n(A3, self.s), # 4.25
        ]

        m6 = [
            k.n(A3, self.s), rest(self.s), rest(self.e),
            k.n(A3, self.s), rest(self.e), 
            k.n(G3, self.s), rest(self.e),
            k.n(A3, self.s), rest(self.e),
            k.n(G3, self.s), rest(self.e),
        ]

        v2 = m0 + m0 + m5 + m6


        if verse == "main":
            return \
            v0 + v0 +\
            v0 + v2
        
        elif verse == "intro":
            return \
            v0 + v0 + v0
        
        return \
        v0 + v0 + v0 +\
        v0 + v0 +\
        v0 + v2
    
    def key_2c(self, k, verse = "full"):
        """Echo of key1"""

        v0 = [rest(self.w*4)]
        m0 = [rest(self.w)]

        m1 = [
            rest(self.e), k.n(A3, self.e), # 1
            rest(self.s), k.n(G3, self.e), # 1.75
            rest(self.s), k.n(F3, self.e), # 2.5
            rest(self.s), k.n(E3, self.e), # 3.25
            rest(self.s), k.n(D3, self.e), # 4
        ]

        m2 = [
            rest(self.e), k.n(A3, self.e),
            rest(self.s), k.n(G3, self.e), 
            rest(self.s), k.n(F3, self.e),
            rest(self.s), k.n(E3, self.e), 
            rest(self.s), k.n(F3, self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        m5 = [
            rest(self.e), rest(self.s), rest(self.s), k.n(A3, self.s), # 1.25
            rest(self.s), rest(self.s), k.n(G3, self.s), # 2
            rest(self.s), rest(self.s), k.n(A3, self.s), # 2.75
            rest(self.s), rest(self.s), k.n(G3, self.s), # 3.5
            rest(self.s), rest(self.s), # 4.25
        ]

        m6 = [
            k.n(A3, self.s), rest(self.s), rest(self.e),
            k.n(A3, self.s), rest(self.e), 
            k.n(G3, self.s), rest(self.e),
            k.n(A3, self.s), rest(self.e),
            k.n(G3, self.s), rest(self.e),
        ]

        v2 = m0 + m0 + m5 + m6

        if verse == "main":
            return \
            v0 + v2 +\
            v0 + v0
        
        elif verse == "intro":
            return \
            v0 + v0 + v0
        
        return \
        v0 + v0 + v0 +\
        v0 + v2 +\
        v0 + v0
    
    def kicks(self, amp=1.4, verse = "full"):
        """Kick part 1"""
        k = self.kick2
        v0 = [rest(self.w*4)]
        
        mi = [
            k.n(self.q),
            rest(self.q*3)
        ]

        m0 = [
            rest(self.w)
        ]

        m1 = [
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
        ]

        m3 = [
            k.n(self.q),
            rest(self.q),
            k.n(self.q),
            rest(self.q),
        ]

        v1 = m1 + m1 + m3 + m3

        
        m6 = [
            k.n(self.e), k.n(self.e),
            rest(self.q),
            k.n(self.q),
            k.n(self.q),
        ]

        m8 = [
            k.n(self.e), k.n(self.e),
            k.n(self.q),
            k.n(self.q),
            k.n(self.q),
        ]

        v2 = m1 + m6 + m6 + m8
        v2b = m6 + m6 + m6 + m6

        v0a = mi + m0 + mi + m0
        v0b = mi + mi + mi + mi
        v0c = mi + m0 + mi + mi


        if verse == "main":
            return \
            v1 + v2 +\
            v1 + v2
        
        elif verse == "intro":
            return v0a + v0b + v0c
        
        return \
        v0a + v0b + v0c +\
        v1 + v2 +\
        v1 + v2
    
    def snares_1(self, verse = "full"):
        """Snare part 1"""
        s = self.snare1
        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), s.n(self.e),
            rest(self.s), s.n(self.e),
            rest(self.s), s.n(self.e),
            rest(self.s), s.n(self.e),
            rest(self.s), s.n(self.e),
        ]

        v1 = m1 + m1 + m1 + m1

        if verse == "main":
            return \
            v1 + v1 +\
            v1 + v0
        
        elif verse == "intro":
            return \
            v0 + v0 + v0
        
        return \
        v0 + v0 + v0 +\
        v1 + v1 +\
        v1 + v0
    
    
def main():
    beat = Intro(64)
    print(beat)

    # beat.export_full()

    beat.get_instruments(verse = "main")
    beat.export_selection(name="05_main")

    beat.get_instruments(verse = "intro")
    beat.export_selection(name="05_intro")

    # beat.export_selection(name = '02_full')

    # drums = {}
    # for k in beat.instruments:
    #     if k == "kick2" or k == "snare1" or k == "hats2":
    #         drums[k] = beat.instruments[k]
    
    # main = {}
    # for k in beat.instruments:
    #     if k != "kick2" and k != "snare1" and k != "hats2":
    #         main[k] = beat.instruments[k]
    
    # beat.export_selection(name="05_intro")
    # beat.export_selection(drums, "05_drums")
