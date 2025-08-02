from modules.beat import *
from modules.instruments import *
from modules.audio import *


class First(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        super().__init__(bpm)
        
        #   Bass    #
        self.bass1 = Bass(amp=0.3)
        self.bass2 = Bass()

        #   Synths  #
        self.synth1 = First4()
        self.synth2 = Church(amp = 0.5)

        #   Drums   #
        self.drum1 = Skirt()
        self.drum2 = Hi_Hat(amp=2.0)
        self.drum3 = Snare()
        self.drum4 = Bass()

        #   Instrument Dictionary   #
        self.instruments = {
            0: [self.bass1, self.bass()],
            1: [self.bass2, self.high_bass()],
            2: [self.bass2, self.high_bass2()],
            3: [None, self.islands()],
            4: [None, self.drums()],
            5: [self.synth1, self.synth_1()],
            6: [self.synth2, self.synth_2()]
        }
    

    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=10_000)


def main():
    beat = First(62)
    beat.produce_full()
    beat.save(beat.production, "03_First Up")

