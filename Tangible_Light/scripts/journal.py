from . import *

class Journal(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

        self.instr1 = Tangible_Light.Journ()
        self.instr2 = Church()
        self.instr3 = Tangible_Light.Title_Bass()
        # self.instr4 = FirstP(amp=0.2)

        self.instr5 = KickBass(amp=2.0)
        self.instr6 = Skirt(amp=1.5, noise_amount=0.1, attack=10)
        self.instr7 = Tap2(amp=2.0, atk=150)
        self.instr8 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        self.instruments = {
            0: [self.instr1, self.synth(1)],
            # 1: [self.instr2, self.synth(2)],
            2: [self.instr3, self.bass()],
            3 :[self.instr4, self.beeps()],
            4: [self.instr5, self.kicks()],
            5: [self.instr6, self.skirts()],
            6: [self.instr7, self.taps()]
        }

    def synth(self, part=""):
        if part == 1:
            n = self.instr1
        elif part == 2:
            n = self.instr3

        #   Verse 1 #
        m1 = [
            rest(self.e), n.note(F3, self.e),
            rest(self.s), n.note(F3, self.e), rest(self.s), # 2
            n.note(D3, self.s), n.note(E3, self.e), # 2.75

            rest(self.q + self.s)
        ]

        m2 = [
            rest(self.e), n.note(F3, self.e),
            n.note(E3, self.s), n.note(F3, self.e), rest(self.s), # 2
            n.note(D3, self.e), n.note(D3, self.e),
            n.note(E3, self.e), n.note(E3, self.e),
        ]

        m3 = [
            n.note(F3, self.e), rest(self.s),
            n.note(F3, self.e), rest(self.s),
            n.note(D3, self.e), n.note(E3, self.e),
            rest(self.e)
        ]

        m4 = [
            rest(self.e), n.note(F3, self.e),
            n.note(E3, self.s), n.note(F3, self.e), rest(self.s), # 2
            n.note(D3, self.e + self.s), n.note(D3, self.s),
            n.note(E3, self.e), n.note(E3, self.e),
        ]
        v1 = m1 + m2 + m1 + m4
        empty = [rest(self.whole * 4)]


        #   Verse 2 #
        m5 = [
            n.note(G3, self.s), rest(self.s), n.note(G3, self.s), rest(self.s),# 1
            n.note(A3, self.e), n.note(G3, self.s), # 1.75
            n.note(A3, self.e), n.note(G3, self.s), # 2.5
            n.note(A3, self.e), n.note(A3, self.s), # 3.25
            n.note(G3, self.e), rest(self.s),
        ]

        m6 = [
            n.note(G3, self.s/2), n.note(F3, self.s/2), n.note(G3, self.s), n.note(G3, self.e), # 1
            n.note(A3, self.e), n.note(G3, self.s), n.note(Fs3, self.e), # 2.25
            n.note(G3, self.s), n.note(Fs3, self.e), # 3
            n.note(E3, self.e), n.note(Fs3, self.e)
        ]

        m7 = [
            n.note(B3, self.e), n.note(G3, self.s), rest(self.s), # 1
            n.note(G3, self.s), n.note(Fs3, self.s), n.note(G3, self.s), # 1.75
            n.note(B3, self.e), n.note(G3, self.s), rest(self.s), # 2.75
            n.note(G3, self.s), rest(self.s), # 3.25
            rest(self.s), n.note(G3, self.s), n.note(G3, self.s),
        ]

        m8 = [
            n.note(G3, self.e), n.note(G3, self.s), n.note(A3, self.s),
            rest(self.s), n.note(G3, self.s), rest(self.s), n.note(Fs3, self.s),
            rest(self.s), n.note(G3, self.s), n.note(Fs3, self.s), rest(self.s),
            n.note(E3, self.s/2), n.note(D3, self.s/2), n.note(E3, self.s), n.note(A3, self.e),
        ]

        v2 = m5 + m6 + m7 + m8

        return \
        empty +\
        \
        v2
    
    def bass(self, part=""):
        n = self.instr3
        m1 = [
            n.note(G2, self.q), rest(self.e),
            n.note(F2, self.s), n.note(G2, self.e),
            rest(self.s + self.e + self.q)
        ]

        m2 = [
            n.note(G2, self.q), # 1
            rest(self.e), n.note(F2, self.s), n.note(G2, self.e), # 2.25
            rest(self.s + self.e), # 3
            n.note(F2, self.q), # 4
        ]

        m3 = [
            n.note(E2, self.q), rest(self.e),
            n.note(D2, self.s), n.note(E2, self.e),
            rest(self.s + self.e + self.q)
        ]

        m4 = [
            n.note(E2, self.q), rest(self.e),
            n.note(D2, self.s), n.note(E2, self.e),
            rest(self.s + self.e),
            n.note(F2, self.q),
        ]
        v1 = m1 + m2 + m3 + m4

        return \
        v1 +\
        v1


    def beeps(self, part=0):
        n = self.instr4

        m1 = [
            rest(self.e),
            n.note(C2, self.s), n.note(C2, self.s/2), n.note(C2, self.s), rest(self.s/2), n.note(C2, self.s),
            rest(self.e),
            n.note(C2, self.s), n.note(C2, self.s), n.note(C2, self.s), n.note(C2, self.s),
            rest(self.q)
        ]
        m2 = [
            rest(self.q),
            rest(self.q),
            rest(self.e),
            n.note(A2, self.e), n.note(G2, self.e),
            rest(self.e)
        ]

        m3 = [
            rest(self.t),
            n.note(G2, self.q)
        ]

        m4 = [
            rest(self.t),
            n.note(F2, self.q)
        ]

        empty = [rest(self.whole)]
        v1 = empty + empty + m1 + empty

        return \
        v1 +\
        v1


    def kicks(self, part=0):
        n = self.instr5
        intro = [rest(self.whole*4)]
        
        m1 = [
            n.note(C1, self.e), rest(self.e),
            rest(self.q),
            n.note(C1, self.e), n.note(C1, self.e),
            rest(self.q)
        ]

        v1 = m1 + m1 + m1 + m1

        return \
        v1 +\
        v1
    
    def skirts(self, part=0):
        n = self.instr6
        n2 = self.instr8
        intro = [rest(self.whole*4)]
        
        m1 = [
            rest(self.q),
            n.note(C4, self.q),
            rest(self.q),
            n2.note(C4, self.q)
        ]

        m2 = [
            rest(self.q),
            n.note(C4, self.q),
            rest(self.q),
            n2.note(C4, self.e), n.note(C4, self.e),
        ]

        m3 = [
            rest(self.q),
            n.note(C4, self.q),
            rest(self.q),
            n2.note(C4, self.q)
        ]

        m4 = [
            rest(self.q),
            n.note(C4, self.q),
            rest(self.q),
            n2.note(C4, self.s), n2.note(C4, self.s), n.note(C4, self.e),
        ]
        v1 = m1 + m2 + m3 + m4

        return \
        v1 +\
        v1
    
    def taps(self, part=0):
        n = self.instr7
        m1 = [
            rest(self.q),
            rest(self.q),
            n.note(C3, self.s), n.note(C3, self.s), n.note(C3, self.s), n.note(C3, self.s),
            rest(self.q)
        ]

        intro = [rest(self.whole*4)]
        v1 = m1 + m1 + m1 + m1

        return \
        v1 +\
        v1
    
    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("Tangible_Light", "ost"), name, norm=norm, volume_factor=10_000)


def main():
    beat = Journal(41)
    beat.produce_full()
    beat.save(beat.production, "02_Journal")