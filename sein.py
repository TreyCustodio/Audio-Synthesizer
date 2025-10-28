from modules import *

"""
Their Sein
"""

class Sein(Beat):

    def __init__(self, bpm):
        super().__init__(bpm, path=os.path.join("their-sein"))

        #   Instruments #

        #   Melody  #
        self.synth1 = GlobalSample(0.0001, os.path.join("samples", "sein", "synth_1.wav"))
        self.synth2 = GlobalSample(0.0001, os.path.join("samples", "sein", "synth_2.wav"))

        self.acoust1 = Acoustic3(amp=0.5, harmonics=12, attack=0.001, attack_max=0.01, decay=0.0, sustain=1.0, release=0.01,
                                # vol_1 = 4.0, vol_2 = 0.3,
                                vol_3 = 1.0, vol_4=0.000000000001,
                                )
        self.key1 = Tangible_Light.Bell(amp=0.5, freq_mod=1.5, wave_2 = False, wave_3=False)

        #   Rhythm / Percussion  #
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = True, wave_3=False,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 1.0)
        mod = 1
        self.bass1 = Bass_1(amp=1.0, attack=0.01, attack_max = 0.02, freq_mod = 1, sustain=1.0, release= 0.01, amp_final = 0.00000000001, harmonics=3)
        self.bass2 = Bass_1(amp=1.0, attack=0.003, attack_max = 0.005, freq_mod = mod, sustain=1.0, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)
        self.hat4 = Hat_4(amp=0.00004)
        self.hatd = Rapping.Drill_Hat(amp=0.00005)

        self.snare1 = Rapping.Snare_1(amp=0.0005)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)

        self.kick1 = Tap4(24.0, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)
        self.kick0 = Tap4(5, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)


        #   Samples #
        self.navi = Navi(amp=0.00001)
        self.go = Go(amp=0.00001)
        self.surprise = Rapping.Surprise(amp=0.00000002)

        
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Rhythm and Bass #
            'kick1': [self.kick1, self.kick_1()],
            'snare1': [self.snare1, self.snare_1()],
            # 'hats1': [self.hat1, self.hats_1()],
            # 'hats2': [self.hat2, self.hats_2()],
            # 'bass1': [self.bass1, self.bass_1()],


            #   Melody  #
            'synth1': [self.synth1, self.synth_1()],

            #   Samples / Libs  #
            # 'navi': [self.navi, self.navi_1()],
        }

    def kick_1(self):
        k = self.kick1
        k0 = self.kick0

        ma = [
            k0.n(C1, self.e), k0.n(C1, self.e),
            k0.n(C1, self.q),
            rest(self.h - self.e),
            k0.n(C1, self.e)
        ]

        mb= [
            rest(self.q),
            k0.n(C1, self.q),
            rest(self.q),
            k0.n(C1, self.q)
        ]

        mc = [
            k0.n(C1, self.q),
            k0.n(C1, self.q),
            rest(self.h - self.e),
            k0.n(C1, self.e)
        ]

        md = [
            rest(self.q),
            k0.n(C1, self.q),
            rest(self.q),
            k0.n(C1, self.e), k0.n(C1, self.e),
        ]

        v0 = ma + mb + mc + md + ma + mb + mc + md

        m1 = [
            k.n(C1, self.e), k.n(C1, self.e),
            k.n(C1, self.q),
            rest(self.h - self.e),
            k.n(C1, self.e)
        ]

        m2 = [
            rest(self.q),
            k.n(C1, self.q),
            rest(self.q),
            k.n(C1, self.q)
        ]

        m3 = [
            k.n(C1, self.q),
            k.n(C1, self.q),
            rest(self.h - self.e),
            k.n(C1, self.e)
        ]

        m4 = [
            rest(self.q),
            k.n(C1, self.q),
            rest(self.q),
            k.n(C1, self.e), k.n(C1, self.e),
        ]

        v1 = m1 + m2 + m1 + m4 + m1 + m2 + m1 + m4


        return \
            v0 +\
            v1 + v1
    
    def snare_1(self):
        s = self.snare1
        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        m2 = [
            rest(self.q),
            rest(self.q),
            s.n(self.q), 
            rest(self.e), s.n(self.e),
        ]

        v1 = m1 + m1 + m1 + m2 + m1 + m2 + m1 + m2

        return \
            v0 +\
            v1 + v1
    
    def hat_open(self):
        return
    
    def hat_closed(self):
        return
    
    def navi_1(self):
        n = self.navi

        v0 = [rest(self.w*8)]

        m1 = [
            rest(self.q),
            rest(self.q),
            n.n(self.q),
            rest(self.q)
        ]

        v1 = m1 + m1 + m1 + m1 +\
        m1 + m1 + m1 + m1

        return v0 + v1
    
    def synth_1(self):
        intro = self.synth1
        s2 = self.synth2

        v0 = [rest(self.w*8)]

        v1 = [intro.n(self.w*8)]
        v2 = [s2.n(self.w*8)]

        return \
        v1 +\
        v2 + v2
    
def main():
    beat = Sein(151)
    beat.export_full()