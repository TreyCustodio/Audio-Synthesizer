from modules import *

"""
05 - Intro
"""

class PTW(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, name = "Pave_The_Way", path=os.path.join("AMTR", "ost", "11"))

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
        self.hat3 = Rapping.Hat_3(amp=0.0004)
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
        
        self.clap = GlobalSample(0.00005, os.path.join("samples", "claps", "dance_clap.wav"))
        

        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            # 'kick1': [self.kick1, self.kicks(self.kick1, verse = verse)],
            'snare1': [self.snare1, self.snares_1(verse = verse)],
            'hats1': [self.hat1, self.hats_1()],
            'hats2': [self.hat2, self.hats_2()],


            

            #   Melody  #


            #   Samples / Libs  #
            # 'goha': [self.go, self.go_1()],


            #   Tag #


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
        print(len(self.production))
        return (round((self.bpm / 60) * 28, 2)) + 60

    def hats_1(self, verse="full"):
        
        h = self.hat4

        m1 = [
            h.n(self.e), h.n(self.e),
            rest(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            rest(self.q),
        ]

        m2 = [
            h.n(self.e), rest(self.e),
            rest(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            rest(self.q),
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v1 + v1
    
    def hats_2(self, verse="full"):
        h = self.hat3

        m1 = [rest(self.w)]
        m4 = [
            rest(self.t),
            h.n(self.s), h.n(self.s), h.n(self.e)
        ]

        v1 = m1 + m1 + m1 + m4

        return \
        v1 + v1
    
    def kicks(self, amp=1.4, verse = "full"):
        """Kick part 1"""
        return
        
    def snares_1(self, verse = "full"):
        """Snare part 1"""
        s = self.clap
        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.e), rest(self.e),
            s.n(self.q),
            rest(self.e), rest(self.e),
            s.n(self.q),
        ]

        m4 = [
            rest(self.e), rest(self.e),
            s.n(self.q),
            rest(self.e), rest(self.e),
            s.n(self.e), s.n(self.e),
        ]

        v1 = m1 + m1 + m1 + m4

        
        return \
        v1 + v1
    
    
def main():
    beat = PTW(156)
    beat.get_instruments(verse = "main")
    beat.export_selection(name="11_main")

