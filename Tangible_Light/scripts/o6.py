from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class TrapPop(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("Tangible_Light", "ost", "06"))

        # self.bass1 = WhinyBass(amp=3.0, freq_mod=0.5)
        self.bass1 = Tangible_Light.Boss_Bass(amp=1.3)

        self.snare1 = Snare()

        self.dub1 = Double()

        self.skirt1 = Tap3(1.0, 90, 0.0, 0.5)
        self.skirt2 = Tap3(1.0, 40, 0.0, 0.7)


        # self.crash1 = HipSkirt()
        # self.crash1 = Hi_Hat(amp=1.0, noise_amount=0.5)
        self.crash1 = Tap3(amp=3.0, attack=15, noise_amount=0.5)

        self.synth1 = Clean_Synth(amp=1.3)

        self.acou1 = Acoustic1()

        self.pluck1 = Clean_Pluck(amp=1.3)

        self.chime1 = Tap3(amp=3.0, attack=100, noise_amount=0.0)

        self.instruments = {
            #   Bass    #
            0: [self.bass1, self.bass()],
            

            #   Middle Synths   #
            1: [self.synth1, self.synth()],
            # 2: [self.acou1, self.acoustic1()],
            3: [self.pluck1, self.plucks()],

            #   Percussion  #
            5: [self.pluck1, self.chimes()],
            6: [self.skirt1, self.skirts()],
            7: [self.skirt1, self.skirts_2()],
            8: [self.skirt1, self.crash()],
            # 9: [None, self.go()]



            
        }
    

    def bass(self):
        s = self.bass1


        # m1 = [
        #     s.note(A3, self.e), s.note(A3, self.e),
        #     s.note(A3, self.e), s.note(A3, self.e),
        #     s.note(F3, self.e), s.note(F3, self.e),
        #     s.note(F3, self.e), s.note(F3, self.e),
        # ]

        # m2 = [
        #     s.note(G3, self.e), s.note(G3, self.e),
        #     s.note(G3, self.e), s.note(G3, self.e),
        #     s.note(E3, self.e), s.note(E3, self.e),
        #     s.note(E3, self.e), s.note(E3, self.e),
        # ]

        m0 = [
            s.note(F4, self.e), s.note(G4, self.e),
            s.note(A4, self.e), s.note(F4, self.e), 
            s.note(G4, self.e), s.note(A4, self.e),
            s.note(F4, self.e), s.note(G4, self.e),
        ]
        
        m1 = [
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(G4, self.e), rest(self.e)
        ]

        m2 = [
           s.note(G4, self.s), s.note(A4, self.s), s.note(B4, self.e),
            s.note(G4, self.s), s.note(A4, self.s), s.note(B4, self.e),
            s.note(G4, self.s), s.note(A4, self.s), s.note(B4, self.e),
            s.note(A4, self.e), rest(self.e) 
        ]

        m3 = [
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(F4, self.s), s.note(G4, self.s), s.note(A4, self.e),
            s.note(G4, self.e), s.note(F4, self.e),
        ]

        m4 = [
            s.note(F4, self.w)
        ]


        m5 = [
            s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s), # 1
            s.note(C2, self.e), s.note(C2, self.s), # 1.75
            s.note(C2, self.e), s.note(C2, self.s), # 2.5
            s.note(C2, self.e), s.note(C2, self.e), # 3.5
            s.note(C2, self.e),
        ]

        d = Ds2
        m6 = [
            s.note(d, self.s), s.note(d, self.s), s.note(d, self.s), s.note(d, self.s), # 1
            s.note(d, self.e), s.note(d, self.s), # 1.75
            s.note(d, self.e), s.note(d, self.s), # 2.5
            s.note(d, self.e), s.note(d, self.e), # 3.5
            s.note(d, self.e),
        ]

        v1 = m5 + m5 + m5 + m5
        v2 = m6 + m6 + m6 + m6
        
        off = [rest(self.w*4)]
        part = \
        off +\
        \
        v1 +\
        v1 +\
        v1 +\
        v1 +\
        v1

        self.save(part, "06_bass")
        return part
    
    def acoustic1(self):
        a = self.acou1

    
    def plucks(self):
        p = self.pluck1

        d = D4
        m1 = [
            rest(self.q),
            p.note(d, self.e), rest(self.e),
            rest(self.q),
            p.note(d, self.e), rest(self.e)
        ]

        m2 = [
            rest(self.q),
            p.note(d, self.e), rest(self.e),
            rest(self.q),
            p.note(d, self.e), p.note(d, self.e),
        ]

        m4 = [
            rest(self.q),
            p.note(d, self.e), rest(self.e),
            rest(self.q - self.s), p.note(d, self.s),
            p.note(d, self.s), p.note(d, self.s), p.note(d, self.s), p.note(d, self.s),
        ]

        v1 = m1 + m2 + m1 + m4

        amp=1.75
        m5 = [
            rest(self.q),
            p.note(d, self.e, amp), rest(self.e),
            rest(self.q),
            p.note(d, self.e, amp), rest(self.e)
        ]

        m6 = [
            rest(self.q),
            p.note(d, self.e, amp), rest(self.e),
            rest(self.q),
            p.note(d, self.e, amp), p.note(d, self.e),
        ]

        m8 = [
            rest(self.q),
            p.note(d, self.e, amp), rest(self.e),
            rest(self.q - self.s), p.note(d, self.s, amp),
            p.note(d, self.s, amp), p.note(d, self.s, amp), p.note(d, self.s, amp), p.note(d, self.s, amp),
        ]

        v2 = m5 + m6 + m5 + m8


        part =  \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        v2 +\
        v2

        self.save(part, "06_plucks")
        return part


    def synth(self):
        s = self.synth1

        m1 = [
            s.note(A3, self.e), s.note(F3, self.e),
            s.note(E3, self.e), s.note(D3, self.e),
            s.note(G3, self.e), s.note(F3, self.e),
            s.note(E3, self.e), s.note(D3, self.e)
        ]

        m2 = [
            s.note(A4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e),
            s.note(G4, self.e), s.note(F4, self.e),
            s.note(E4, self.e), s.note(D4, self.e)
        ]

        m3 = [
            s.note(A2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e),
            s.note(G2, self.e), s.note(F2, self.e),
            s.note(E2, self.e), s.note(D2, self.e)
        ]

        v1 = m1 + m1 + m1 + m1


        amp = 0.7
        m5 = [
            s.note(A3, self.e, amp), s.note(F3, self.e, amp),
            s.note(E3, self.e, amp), s.note(D3, self.e, amp),
            s.note(G3, self.e, amp), s.note(F3, self.e, amp),
            s.note(E3, self.e, amp), s.note(D3, self.e, amp)
        ]
        v2 = m5 + m5 + m5 + m5

        part =  \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        v2 +\
        v2 

        self.save(part, "06_synth")
        return part
    
    
    def crash(self):
        c = self.crash1

        # m1 = [
        #     rest(self.h),
        #     c.note(C2, self.e), rest(self.e),
        #     rest(self.e), c.note(C2, self.e),
        # ]

        # m2 = [
        #     rest(self.e), c.note(C2, self.e),
        #     rest(self.e), c.note(C2, self.e),
        #     c.note(C2, self.e), rest(self.e), 
        #     rest(self.e), rest(self.e),
        # ]

        m1 = [
            c.note(C2, self.e), rest(self.e),
            rest(self.e), c.note(C2, self.e),
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.e),
        ]

        m2 = [
            c.note(C2, self.e), rest(self.e),
            rest(self.e), c.note(C2, self.e),
            rest(self.e), rest(self.e),
            c.note(C2, self.e), c.note(C2, self.e),
        ]

        m3 = [
            c.note(C2, self.e), rest(self.e),
            rest(self.e), c.note(C2, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e),
        ]

        m4 = [
            c.note(C2, self.e), c.note(C2, self.e),
            rest(self.e), c.note(C2, self.e), 
            rest(self.e), rest(self.e),
            c.note(C2, self.e), rest(self.e),
        ]



        off = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m2
        v2 = m3 + m4 + m3 + m4

        part =  \
        off +\
        \
        v1 +\
        v2 +\
        v1 +\
        off +\
        off
        
        self.save(part, "06_crash")
        return part

    def skirts(self):
        k = self.skirt1

        m1 = [
            k.note(C3, self.e), k.note(C3, self.e), 
            k.note(C3, self.e), k.note(C3, self.e),
            k.note(C3, self.e), k.note(C3, self.e),
            k.note(C3, self.e), k.note(C3, self.e),
        ]

        m2 = [
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
            k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s), k.note(C3, self.s),
        ]





        off = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m1
        v2 = m2 + m2 + m2 + m2
        part =  \
        off +\
        \
        v1 +\
        v2 +\
        v2 +\
        off +\
        off

        self.save(part, "06_skirts_1")
        return part
    
    def skirts_2(self):
        k = self.skirt2
        amp=3.0

        m3 = [
            rest(self.q),
            rest(self.q),
            rest(self.e), k.note(C3, self.s, amp), k.note(C3, self.s, amp),
            k.note(C3, self.s, amp), rest(self.s), k.note(C3, self.s, amp), rest(self.s),
        ]
        off = [rest(self.w*4)]

        m1 = [rest(self.whole)]
        v1 = m1 + m1 + m1 + m3


        m5 = [
            rest(self.q),
             rest(self.e), k.n(A3, self.e, amp),
            rest(self.q),
            rest(self.e), k.n(A3, self.e, amp),
        ]

        m6 = [
            rest(self.q),
             rest(self.e), k.n(A3, self.e, amp),
            rest(self.q),
            k.n(A3, self.e, amp), k.n(A3, self.e, amp),
        ]

        v2 = m5 + m6 + m5 + m6

        part =  \
        off +\
        \
        v1 +\
        v1 +\
        v1 +\
        v2 +\
        v2 

        self.save(part, "06_skirts_2")
        return part
    
    def chimes(self):
        k = self.chime1

        m1 = [rest(self.w)]
        m4 = [
            rest(self.trey),
            k.note(A6, self.s), k.note(F6, self.s), k.note(A6, self.e)
        ]
        
        m5 = [
            rest(self.trey-(self.s*2 + self.e)),
            k.note(A6, self.s), k.note(F6, self.s), k.note(A6, self.e),
            rest(self.s*2 + self.e)
        ]
        v1 = m1 + m1 + m1 + m4
        v2 = m1 + m1 + m1 + m5

        off = [rest(self.w*4)]
        part =  \
        v1 +\
        \
        v1 +\
        v1 +\
        v1 +\
        v1 +\
        v1 

        self.save(part, "06_chimes")
        return part


def main():
    beat = TrapPop(82)
    beat.export_full()