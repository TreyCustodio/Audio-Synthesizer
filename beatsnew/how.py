from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class How(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = "", norm=True):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "how"), name, norm=norm)
    
    def drums(self, part=""):
        c = HipSkirt(attack =70, amp = 24.0, low = 0)

        if part == "v1":

            m1 = build_measure(
                c.note(C3, self.e), c.note(C3, self.e), # 1
                c.note(C3, self.e), c.note(C3, self.s), # 1.75
                c.note(C3, self.e), c.note(C3, self.s), # 2.5
                c.note(C3, self.e), c.note(C3, self.e), # 3.5
                c.note(C3, self.e)
            )

            
            m2 = build_measure(
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), rest(self.e)
            )

            m3 = build_measure(
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.s), c.note(C3, self.s),
            )

            m4 = build_measure(
                c.note(C3, self.e), c.note(C3, self.s), c.note(C3, self.s),
                c.note(C3, self.e), c.note(C3, self.s), c.note(C3, self.s),
                c.note(C3, self.e), c.note(C3, self.e),
                c.note(C3, self.e), c.note(C3, self.e)
            )

            v1 = build_measure(m1, m2, m3, m4)
            return v1
        
        elif part == "v2" or part == "solo":
            m1 = build_measure(
                c.note(C3, self.e), c.note(C3, self.e), # 1
                c.note(C3, self.e), c.note(C3, self.s), # 1.75
                c.note(C3, self.e), c.note(C3, self.s), # 2.5
                c.note(C3, self.e), c.note(C3, self.e), # 3.5
                c.note(C3, self.e)
            )

            v2 = build_measure(m1, m1, m1, m1)
            return v2



    def bass(self, part=""):

        b = KickBass2(amp = 180.0, attack = 10)
        b2 = Bass(amp=40.0)
        c = HipSkirt(amp = 90.0, attack = 20)



        m1 = build_measure(
            b.note(C2, self.e), b.note(C2, self.e), # 1
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.s), b.note(C2, self.e), # 2.25
            b.note(C2, self.s), b.note(C2, self.e), # 3
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.e), # 4
        )

        m2 = build_measure(
            b.note(C2, self.e), b.note(C2, self.e), # 1
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.s), b.note(C2, self.e), # 2.25
            b.note(C2, self.s), b.note(C2, self.e), # 3
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.e) + c.note(C2, self.e)# 4
        )

        m3 = build_measure(
            b.note(C2, self.e), b.note(C2, self.e), # 1
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.s), b.note(C2, self.e), # 2.25
            b.note(C2, self.s), b.note(C2, self.e), # 3
            b.note(C2, self.e) + c.note(C2, self.e), b.note(C2, self.s) + c.note(C2, self.s), b.note(C2, self.s) + c.note(C2, self.s)# 4
        )

        # if part == "bass":
        #     m4 = build_measure(
        #         b2.note(C1, self.e), b2.note(C1, self.e), # 1
        #         b2.note(C1, self.e), b2.note(C1, self.s), b2.note(C1, self.e), # 2.25
        #         b2.note(C1, self.s), b2.note(C1, self.e), # 3
        #         b2.note(C1, self.e), b2.note(C1, self.e), # 4
        #     )

        #     m5 = build_measure(
        #         b2.note(A0, self.e), b2.note(A0, self.e), # 1
        #         b2.note(A0, self.e), b2.note(A0, self.s), b2.note(A0, self.e), # 2.25
        #         b2.note(A0, self.s), b2.note(A0, self.e), # 3
        #         b2.note(A0, self.e), b2.note(A0, self.e), # 4
        #     )


        #     m1 = combine(m1, m5)
        #     m2 = combine(m2, m5)
        #     m3 = combine(m3, m5)
        
        v1 = build_measure(m1, m2, m1, m3)

        return v1


    def keys(self, part=""):
        
        #   V0 - Intro Build-up #
        if part == "v0":
            s = Dirty_Strings(amp=0.3, metal_amp = 0.0)

            #mi = fade_mult(s.note(A4, self.q), s.note(A4, self.q), 3, factor = 4.0)
                
            mi2 = build_measure(
                s.note(As4, self.q), 
                rest(self.h),

            )

            m0 = build_measure(
                s.note(A4, self.q), 
                s.note(As4, self.e),
                s.note(G4, self.q),
                s.note(As4, self.e), s.note(A4, self.e),
                s.note(F4, self.e)
            )

            m1 = build_measure(
                s.note(A4, self.e + self.e / 2), s.note(As4, self.e + self.e / 2), # 1.5
                s.note(G4, self.q), # 2.5
                s.note(As4, self.e), s.note(A4, self.e), # 3 
                s.note(F4, self.e) # 4
            )

            v0 = build_measure(m0, m1, m1, m1)
            return v0


        #   V1 - Main Loop  (Amplitude lowered) #
        elif part == "v1" or part == "bass" or part == "v3":

            #   Build the bass section  #
            s2 = Dirty_Strings(amp=0.1, bass_only = True)

            m1b = build_measure(
                rest(self.h),
                s2.note(A4, self.q),
                s2.note(A4, self.q),
            )

            if part == "bass":
                return fade_in(build_measure(rest(self.whole), rest(self.whole), rest(self.whole), m1b) * 2.0, 1.0)

            #   Build the treble / midtone section  #
            else:
                if part == "v1":
                    s = Dirty_Strings(amp=0.3,bass_amp = 2.5, high_bass = 10, metal_amp = 0.5)
                
                elif part == "v3":
                    s = Dirty_Strings(amp=0.3,bass_amp = 2.5, metal_amp = 0.75)
                    
                    
                m1 = build_measure(
                    s.note(A4, self.e + self.e / 2), s.note(As4, self.e + self.e / 2), # 1.5
                    s.note(G4, self.q), # 2.5
                    s.note(As4, self.e), s.note(A4, self.e), # 3 
                    s.note(F4, self.e) # 4
                )

                m2  = combine(m1, m1b)
                v1 = build_measure(m1, m1, m1, m2)
                return v1
        
        elif part == "metal":
            #   Build the bass section  #
            s2 = Dirty_Strings(amp=0.55, metal_only = True)

            m1b = build_measure(
                s2.note(G4, self.q),
                s2.note(G4, self.q),
                rest(self.h)
            )

            return build_measure(rest(self.whole*3), m1b)
        


        #   V2 - Refrain    #
        elif part == "v2":
            s = Dirty_Strings(amp=0.3, bass_amp = 2.5, metal_amp = 0.5)

            m1 = build_measure(
                s.note(As4, self.e + self.s), s.note(A4, self.e + self.s), #1.5
                s.note(F4, self.e + self.s), rest(self.s), #2.5
                s.note(D4, self.e + self.s), # 3.25
                rest(self.s), s.note(D4, self.e), #4
            )

            m2 = build_measure(
                s.note(F4, self.e + self.s), s.note(As4, self.e + self.s), #1.5
                s.note(A4, self.e + self.s), # 2.25
                rest(self.s), # 2.5
                s.note(A4, self.e + self.s), #3.25
                rest(self.s), #3.5
                s.note(A4, self.e) # 4
            )

            v2 = build_measure(m1, m2, m1, m2)
            return v2


    def intro(self):
        #   Gather Instruments  #
        ##   Drums and Bass  #
        b1 = self.bass("bass")
        d1 = self.drums("v1")


        #   Testing the Drum Beat   #
        # prod = combine(b1, d1)
        # prod = (prod / np.max(np.abs(prod)) * 32767).astype(np.int16)

        # self.save(prod, "intro", norm = False)
        # return

        b2 = self.bass()
        d2 = self.drums("v2")
        bs = self.bass("solo")
        ds = self.drums("solo")

        ##  Keyboard Sounds #
        k0 = self.keys("v0")
        k1 = self.keys("v1")
        k2 = self.keys("v2")
        k3 = self.keys("v3")
        kb = self.keys("bass")
        km = self.keys("metal")


        #   Put together each section   #
        b1 = combine(b1, d1)
        b2 = combine(b2, d2)
        bs = combine(bs, ds)

        v1 = k0

        #   Full Keys V1    #
        v2 = combine(k3, b1)
        
        #   Full Keys V2    #
        v3 = combine(k2, b2)
        
        #   Quiet Keys V1    #
        v4 = combine(k1, b1)

        #   Bass Solo   #
        v5 = combine(bs, kb)
        v5 = combine(v5, km)

        #v6 = combine(v3, d1)


        #   Combine Each Section    #
        prod = build_measure(
            #   Intro   #
            v1, 

            #   Verse   #
            v2, v3,
            v4, v3,

            #   Refrain or Bridge if you want   #
            v5,

            #   Quota   #
            v3, v2, v3

        )


        
        #   Normalize the audio
        prod = (prod / np.max(np.abs(prod)) * 32767).astype(np.int16)

        self.save(prod, "intro", norm = False)
        return prod

    def chorus1(self):
        return

    def hook1(self):
        return

    def verse1(self):
        return

    def refrain1(self):
        return

    def verse2(self):
        return

        

    def produce(self):
        #   Gather Each Section of the song    #
        intro = self.intro()

        #   Save the production #
        # prod = build_measure(
        #     #   Intro   #
        #     intro
        # )


        self.save(prod, "How?")

    
def main():
   How(52).intro()