from modules import *

"""
Project Frozen FLame
"""

class FF(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path=os.path.join("project_frozen-flame"))

        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Whistle ##
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = True, wave_3=False,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 1.0)

        ##  Hats    ##
        self.hat1 = Rapping.Hat_1(amp=0.000025)
        self.hat2 = Rapping.Hat_2(amp=0.00003)
        self.hat3 = Rapping.Hat_3(amp=0.00012)
        self.hat4 = Hat_4(amp=0.00004)
        self.hatd = Rapping.Drill_Hat(amp=0.00005)

        ##  Snares  ##
        self.snare1 = Rapping.Snare_1(amp=0.00001)
        self.snare2 = Rapping.Snare_2(amp=0.00001)
        self.snare3 = Rapping.Snare_3(amp=0.00001)
        self.snare4 = Rapping.Lofi_Snare(amp=0.00005)
        self.snare5 = Rapping.Crackle_Snare(amp=0.00001)
        self.afro_snare = GlobalSample(0.00003, os.path.join("samples", "snares", "afro_snare.mp3"))

        ##  Kicks   ##
        self.kick1 = Tap4(6.0, attack=0.001, decay = 0.05, sustain=0.0, noise_amount=0.00000)

        #   Samples #
        self.go = Go(amp=0.00001)
        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Main Melody #
            
            #   Rhythm and Bass #
            'snares':[None, self.snare_1()]

            #   Melody  #

            #   Samples / Libs  #
        }

    def snare_1(self):
        """Begin at M13"""

        s = self.snare1
        m1 = [
            s.n(self.q),
            s.n(self.q),
            s.n(self.q),
            s.n(self.q),
        ]

        v1 = m1 + m1 + m1 + m1

        return v1 * 2



def main():
    beat = FF(41)
    beat.get_instruments()
    beat.export_selection()