from . import *

class Journal(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "02"))

        self.instr1 = Tangible_Light.Journ()
        self.instr2 = Church()
        self.bass1 = Tangible_Light.Title_Bass()
        self.beep1 = FirstP(amp=0.2)

        self.tap1 = KickBass(amp=1.5)
        # self.tap1 = Tap(amp=11.0, atk = 40)
        self.skirt1 = Skirt(amp=1.5, noise_amount=0.1, attack=10)
        self.skirt2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        self.start = [rest(self.w*4)]


    def get_instruments(self):
        self.instruments = {
            0: [self.instr1, self.synth(1)],
            # # 1: [self.instr2, self.synth(2)],
            1: [self.bass1, self.bass()],
            2:[self.beep1, self.beeps()],
            3: [self.tap1, self.kicks()],
            4: [self.skirt1, self.skirts()],
            "i": [None, self.intro()],
        }

    def intro(self):
        n = self.bass1
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

        return v1

    def synth(self, part=""):
        if part == 1:
            n = self.instr1
        elif part == 2:
            n = self.bass1

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

        part =  \
        empty +\
        empty +\
        \
        v2

        return part
    
    def bass(self, part=""):
        n = self.bass1
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

        part = \
        self.start +\
        v1 +\
        v1

        return part


    def beeps(self, part=0):
        n = self.beep1

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

        part = \
        self.start +\
        v1 +\
        v1

        return part

    def kicks(self, part=0):
        n = self.tap1
        intro = [rest(self.whole*4)]
        amp=1.4

        m1 = [
            rest(self.e), rest(self.e),
            rest(self.q),
            n.note(C1, self.e, amp), n.note(C1, self.e, amp),
            rest(self.q)
        ]

        m2 = [
            rest(self.e), rest(self.e),
            rest(self.q),
            n.note(C1, self.e), n.note(C1, self.e),
            rest(self.q)
        ]
        v1 = m1 + m1 + m1 + m1

        v2 = m2 + m2 + m2 + m2

        part = \
        self.start +\
        v1 +\
        v2

        return part
    
    def skirts(self, part=0):
        n = self.skirt1
        n2 = self.skirt2
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
            n2.note(C4, self.e), n.note(C4, self.e, 1.5),
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
            n2.note(C4, self.s), n2.note(C4, self.s), n.note(C4, self.e, 1.5),
        ]
        v1 = m1 + m2 + m3 + m4

        part = \
        self.start +\
        v1 +\
        v1

        return part



def main():
    beat = Journal(41)
    beat.export_full(stereo=False)
   