"""
1 Beat a day.
50 Beats a day.
"""

from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class TA(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, "Still Trey")

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "training"), name)
    
    def kicks(self, part=""):
        if part == "v1" or part == "v0":
            k = KickBass2()

            #   V1  #
            m1 = build_measure(
                k.note(C3, self.q),
                rest(self.q),
                k.note(C3, self.q),
                k.note(C3, self.q),
            )

            m2 = build_measure(
                rest(self.q),
                k.note(D3, self.q),
                rest(self.q),
                k.note(C3, self.q),
            )

            m3 = build_measure(
                rest(self.q),
                k.note(C3, self.q),
                k.note(C3, self.q),
                rest(self.q)
            )

            m4 = build_measure(
                k.note(D3, self.q), 
                k.note(C3, self.q),
                k.note(D3, self.q),
                k.note(E3, self.q),
            )


            m5 = build_measure(
                k.note(F3, self.q),
                rest(self.q),
                k.note(F3, self.q),
                k.note(F3, self.q),
            )

            m6 = build_measure(
                rest(self.q),
                k.note(G3, self.q),
                rest(self.q),
                k.note(F3, self.q),
            )

            m7 = build_measure(
                rest(self.q),
                k.note(F3, self.q),
                k.note(F3, self.q),
                rest(self.q)
            )

            m8 = build_measure(
                k.note(G3, self.q), 
                k.note(F3, self.q),
                k.note(G3, self.q),
                k.note(A3, self.q),
            )

            m9 = build_measure(
                k.note(A3, self.q),
                rest(self.q),
                k.note(A3, self.q),
                k.note(A3, self.q),
            )

            m10 = build_measure(
                rest(self.q),
                k.note(C4, self.q),
                rest(self.q),
                k.note(A3, self.q),
            )

            m11 = build_measure(
                rest(self.q),
                k.note(A3, self.q),
                k.note(A3, self.q),
                rest(self.q)
            )

            m12 = build_measure(
                k.note(B3, self.q), 
                k.note(A3, self.q),
                k.note(B3, self.q),
                k.note(C4, self.q),
            )
            
            if part == "v1":
                v1 = build_measure(
                    m1, m2, m3, m4, # 4 Bars
                    m5, m6, m7, m8, # 8 Bars

                    m9, m10, m11, m12, # 12 Bars
                    m5, m6, rest(self.whole*2) # 16 Bars

                )
                return v1
            

            #   14-Bars; No rest at end #
            elif part == "v0":
                v0 = build_measure(
                    m1, m2, m3, m4, # 4 Bars
                    m5, m6, m7, m8, # 8 Bars

                    m9, m10, m11, m12, # 12 Bars
                    m5, m6, # 14 Bars
                )

                return v0


        elif part == "v2":
            k = Bass(amp=0.75, freq_mod = 6, dist=4.0)

            v5 = build_measure(
                k.note(D3, self.whole * 3),
                k.note(E3, self.whole),
                k.note(D3, self.whole * 3),
                k.note(E3, self.whole),
                k.note(F3, self.whole*3),
                k.note(G3, self.whole),
                k.note(F3, self.whole),
                k.note(E3, self.whole),
            )

            return v5
        
        elif part == "v3":
            k = Bass(amp=1.0, freq_mod = 6, dist=10.0)

            v6 = build_measure(
                fade_out(k.note(C3, self.whole * 8), 6.0)
            )

            return v6
        
        elif part == "r1":
            k = Bass(amp=1.0, freq_mod = 6, dist=10.0)

            #   Refrain After the first section of drums    #
            m7 = build_measure(
                rest(self.q),
                k.note(F3, self.q),
                k.note(F3, self.q),
                rest(self.q)
            )

            m8 = build_measure(
                k.note(G3, self.q), 
                k.note(F3, self.q),
                k.note(G3, self.q),
                k.note(A3, self.q),
            )

            return build_measure(m7, m8)


    def shots(self, part=""):
        """Kick-like shots that appear in the intro"""
        if part == "v1" or part == "v0":
            s = KickBass2()
            m1 = build_measure(
                rest(self.q),
                s.note(C3, self.q) + s.note(C4, self.q),
                rest(self.q),
                s.note(C3, self.q) + s.note(C4, self.q),
            )

            m2 = build_measure(
                rest(self.q),
                s.note(C3, self.e) + s.note(C4, self.e), s.note(C3, self.e) + s.note(C3, self.e),
                rest(self.q),
                s.note(C3, self.q) + s.note(C4, self.q),
            )
            
            m3 = m1

            m4 = build_measure(
                rest(self.q),
                s.note(C3, self.e) + s.note(C4, self.e), s.note(C3, self.e) + s.note(C4, self.e),
                rest(self.e), s.note(C4, self.e) + s.note(C3, self.e),
                s.note(C4, self.e) + s.note(C3, self.e), s.note(C4, self.e) + s.note(C3, self.e),
            )

            m5 = build_measure(
                rest(self.q),
                s.note(C3, self.e) + s.note(C4, self.e), s.note(C3, self.e) + s.note(C4, self.e),
                s.note(C4, self.e) + s.note(C3, self.e), rest(self.e), 
                s.note(C4, self.e) + s.note(C3, self.e), s.note(C4, self.e) + s.note(C3, self.e),
            )
            """
            m1 = rest(self.whole)

            m2 = build_measure(
                rest(self.h),
                s.note(C3, self.e), rest(self.e),
                s.note(C3, self.e), rest(self.e),
            )

            m3 = build_measure(
                s.note(C3, self.e), s.note(C3, self.e),
                s.note(C3, self.e), rest(self.e),
                rest(self.h)
            )

            m4 = build_measure(
                s.note(C3, self.s), s.note(C3, self.s), s.note(C3, self.s), s.note(C3, self.s),
                rest(self.q),
                s.note(C3, self.s), s.note(C3, self.s), s.note(C3, self.s), s.note(C3, self.s),
                rest(self.q)
            )
            """

            if part == "v1":
                v1 = build_measure(
                    m1, m2, m3, m4, # 4
                    m1, m2, m3, m5, # 8
                    m1, m2, m3, m4, # 12
                    m1, m2, m3, m5,

                    #rest(self.whole*4) # 16
                )

                return v1

            elif part == "v0":
                v0 = build_measure(
                    m1, m2, m3, m4, # 4
                    m1, m2, m3, m5, # 8
                    m1, m2, m3, m4, # 12
                    m1, rest(self.whole*1) # 14
                )
                return v0

    def bass(self, part=""):

        if part == "v1":
            k = Bass(amp=1.0, freq_mod = 6, dist=10.0)

            #   V1  #
            m1 = build_measure(
                k.note(F3, self.q),


            )

            m2 = build_measure(
                rest(self.whole)
            )

            m3 = build_measure(
                rest(self.whole)
            )

            m4 = build_measure(
                k.note(D3, self.q), 
                k.note(C3, self.q),
                k.note(D3, self.q),
                k.note(E3, self.q),
            )


            m5 = build_measure(
                rest(self.whole)
            )

            m6 = build_measure(
                rest(self.whole)
            )

            m7 = build_measure(
                rest(self.whole)
            )

            m8 = build_measure(
                rest(self.whole)
            )

            m9 = build_measure(
                rest(self.whole)
            )

            m10 = build_measure(
                rest(self.whole)
            )

            m11 = build_measure(
                rest(self.whole)
            )

            m12 = build_measure(
                rest(self.whole)
            )

            v1 = build_measure(
                m1, m2, m3, m4, # 4 Bars
                m1, m2, m3, m8, # 8 Bars

                m5, m6, m7, m12, # 12 Bars
                m9, m10, m7, m8  # 16 Bars
            )

            return v1

        elif part == "v2":
            k = Bass(amp=0.75, freq_mod = 6, dist=4.0)

            v5 = build_measure(
                k.note(D3, self.whole * 3),
                k.note(E3, self.whole),
                k.note(D3, self.whole * 3),
                k.note(E3, self.whole),
                k.note(F3, self.whole*3),
                k.note(G3, self.whole),
                k.note(F3, self.whole),
                k.note(E3, self.whole),
            )

            return v5
        
        elif part == "v3":
            k = Bass(amp=1.0, freq_mod = 6, dist=10.0)

            v6 = build_measure(
                fade_out(k.note(C3, self.whole * 8), 6.0)
            )

            return v6
        
        elif part == "r1":
            k = Bass(amp=1.0, freq_mod = 6, dist=10.0)

            #   Refrain After the first section of drums    #
            m7 = build_measure(
                rest(self.q),
                k.note(F3, self.q),
                k.note(F3, self.q),
                rest(self.q)
            )

            m8 = build_measure(
                k.note(G3, self.q), 
                k.note(F3, self.q),
                k.note(G3, self.q),
                k.note(A3, self.q),
            )

            return build_measure(m7, m8)

    def drums(self, part=""):
        """ if part == "v1" or part == "v0":
            #   V1  #
            k = Snare(amp=10)
            s = HipSkirt(attack=7)

            m1 = build_measure(
                k.note(C1, self.q),
                k.note(C1, self.q),
                s.note(C2, self.q),
                s.note(C3, self.q),
            )

            m2 = build_measure(
                k.note(C1, self.q),
                rest(self.q),
                s.note(C2, self.q),
                rest(self.q)
            )

            m3 = build_measure(
                k.note(C1, self.q),
                k.note(C1, self.q),
                s.note(C2, self.e), rest(self.s), s.note(C2, self.s),
                s.note(C2, self.e), rest(self.e)
            )
            
            m4 = build_measure(
                k.note(C1, self.q),
                rest(self.q),
                s.note(C2, self.q),
                rest(self.q),
            )

            m5 = build_measure(
                k.note(C1, self.q),
                k.note(C1, self.q),
                s.note(C3, self.e) + s.note(C2, self.e), rest(self.s), s.note(C3, self.s) + s.note(C2, self.s),
                s.note(C3, self.e) + s.note(C2, self.e), rest(self.e)
            )
        """
        #   Drumline from Training B    #
        s = HipSkirt(amp=5, attack = 65, dist=20.0, high=5000)
        c = HipSkirt(attack = 17, low = 8000, dist = 12.0)
        d = Snare(amp = 10, freq_mod = 2)


        if part == "v1" or "v0":
            m1 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q),
                s.note(C1, self.e) + d.note(C1, self.e), s.note(C1, self.e) + d.note(C1, self.e),
                c.note(C1, self.q) + d.note(C3, self.q) + d.note(C1, self.q),
                s.note(C1, self.e) + d.note(C1, self.e), # 3.5
            )

            m2 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q), # 4.5
                s.note(C1, self.e) + d.note(C1, self.e), # 5
                s.note(C1, self.q) + d.note(C1, self.q), # 6
                c.note(C1, self.q) + d.note(C3, self.q) + d.note(C1, self.q), # 7
                s.note(C1, self.q) + d.note(C1, self.q), # 8
            )
            

            m4 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q), # 4.5
                s.note(C1, self.e) + d.note(C1, self.e), # 5
                s.note(C1, self.q) + d.note(C1, self.q), # 6

                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 6.5
                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 7

                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 7.5
                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 8
            )

            if part == "v1":
                v1 = build_measure(
                    m1, m2, m1, m4, # 4
                    m1, m2, m1, m4, # 8
                    m1, m2, m1, m4, # 12
                    m1, m2, m1, m4, # 16

                )
                self.save(v1, "TA_drums")
                return v1
            elif part == "v0":
                v0 = build_measure(
                    m1, m2, m1, m4, # 4
                    m1, m2, m1, m4, # 8
                    m1, m2, m1, m4, # 12
                    m1, m4, # 14
                )
                return v0
            


            """ #   16 Bars of Bass and Percussion
            if part == "v1":
                v1 = build_measure(
                    m3, m2, m1, m4,
                    m3, m2, m1, m4,
                    m3, m2, m1, m4,
                    m3, m2, rest(self.whole*2) # 16
                )

                return v1

            #   16 Bars of Bass and Percussion
            elif part == "v0":
                v0 = build_measure(
                    m3, m2, m1, m4,
                    m3, m2, m1, m4,
                    m3, m2, m1, m4,
                    m3, m2, # 14
                )

                return v0 """
    
    def highBass(self, part=""):
        if part == "v1" or part == "v0":
            b = Bass(amp=0.23)

            m1 = build_measure(
                b.note(G2, self.whole) + b.note(B2, self.whole)
            )

            m2 = build_measure(
                b.note(G2, self.e) + b.note(B2, self.e),
                b.note(A2, self.q) + b.note(C3, self.q),
                b.note(B2, self.q) + b.note(D3, self.q),
                b.note(C3, self.e) + b.note(E3, self.e), 
                b.note(D3, self.q) + b.note(F3, self.q),
            )

            m3 = build_measure(
                b.note(D3, self.t + self.e) + b.note(F3, self.t + self.e),
                b.note(D3, self.e) + b.note(F3, self.e),
            )

            m4 = build_measure(
                b.note(F3, self.e) + b.note(A3, self.e),
                b.note(E3, self.q) + b.note(G3, self.q), # 1.5

                b.note(D3, self.q) + b.note(F3, self.q), # 2.5
                b.note(C3, self.e) + b.note(E3, self.e), # 3
                b.note(B2, self.q) + b.note(D3, self.q), # 4
            )

            m5 = build_measure(

                b.note(A2, self.w) + b.note(C3, self.w),
            )

            m6 = build_measure(
                b.note(A2, self.h) + b.note(C3, self.h),
                b.note(G2, self.h) + b.note(B2, self.h),
            )

            m7 = build_measure(
                b.note(F2, self.q) + b.note(A2, self.q), # 1
                b.note(G2, self.e) + b.note(B2, self.e), # 1.5
                b.note(F2, self.q) + b.note(A2, self.q), # 2.5
                b.note(G2, self.q) + b.note(B2, self.q), # 3.5
                rest(self.e) # 4
            )

            m8 = build_measure(
                b.note(A2, self.w) + b.note(C3, self.w),
            )

            m9 = build_measure(
                b.note(G2, self.q) + b.note(B2, self.q),
                b.note(A2, self.e) + b.note(C3, self.e),
                b.note(G2, self.q) + b.note(B2, self.q),
                b.note(A2, self.q) + b.note(C3, self.q),
                rest(self.e)
                # could add rest(e) here; but cut out sixteenth notes in m11 if so
            )

            m10 = build_measure(
                b.note(B2, self.w) + b.note(D3, self.w),
            )

            m11 = build_measure(
                #b.note(A2, self.s) + b.note(C3, self.s), b.note(A2, self.s) + b.note(C3, self.s),
                b.note(A2, self.q) + b.note(C3, self.q), # 1.5
                b.note(B2, self.e) + b.note(D3, self.e), # 2
                b.note(A2, self.q) + b.note(C3, self.q), # 3
                b.note(B2, self.q) + b.note(D3, self.q), # 4
            )

            m12 = build_measure(
                b.note(C3, self.w) + b.note(E3, self.w),
            )

            m13 = build_measure(
                b.note(A2, self.s) + b.note(C3, self.s), b.note(A2, self.s) + b.note(C3, self.s),
                b.note(F3, self.q) + b.note(A3, self.q), # 1.5
                b.note(E3, self.e) + b.note(G3, self.e), # 2
                b.note(D3, self.q) + b.note(F3, self.q), # 3
                b.note(C3, self.q) + b.note(E3, self.q), # 4
            )

            m14 = build_measure(
                b.note(B2, self.q) + b.note(D3, self.q),
                b.note(B2, self.q) + b.note(D3, self.q),
                b.note(B2, self.e) + b.note(D3, self.e), # 2.5
                b.note(A2, self.e) + b.note(C3, self.e), b.note(A2, self.e) + b.note(C3, self.e), # 3.5
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e), # 4.5
            )

            #   16 Bars
            if part == "v1":
                v1 = build_measure(
                    m1, m2, m3, m4,
                    m5, m6, m7, m8,
                    m9, m10, m11, m12,
                    m13, m14, rest(self.whole*2) # 16
                    )

                return v1
            
            #   14 Bars
            elif part == "v0":
                v1 = build_measure(
                    m1, m2, m3, m4,
                    m5, m6, m7, m8,
                    m9, m10, m11, m12,
                    m13, m14, # 14
                    )

                return v1

        elif part == "v2" or part == "v3":
            b = Bass(amp=0.35)

            m1 = build_measure(
                b.note(F2, self.q) + b.note(A2, self.q),
                b.note(G2, self.e) + b.note(B2, self.e),
                b.note(F2, self.q) + b.note(A2, self.q),
                b.note(G2, self.q) + b.note(B2, self.q),
            )

            m2 = build_measure(
                b.note(A2, self.w) + b.note(C3, self.w),
            )

            m3 = build_measure(
                b.note(G2, self.e) + b.note(B2, self.e),
                b.note(G2, self.q) + b.note(B2, self.q),
                b.note(A2, self.e) + b.note(C3, self.e),
                b.note(G2, self.q) + b.note(B2, self.q),
                b.note(A2, self.q) + b.note(C3, self.q),
            )

            m4 = build_measure(
                b.note(B2, self.w) + b.note(D3, self.w),
            )

            m5 = build_measure(
                b.note(A2, self.s) + b.note(C3, self.s), b.note(A2, self.s) + b.note(C3, self.s),
                b.note(A2, self.q) + b.note(C3, self.q),
                b.note(B2, self.e) + b.note(D3, self.e),
                b.note(A2, self.q) + b.note(C3, self.q),
                b.note(B2, self.q) + b.note(D3, self.q),
            )

            m6 = build_measure(
                b.note(C3, self.w) + b.note(E3, self.w),
            )

            m7 = build_measure(
                b.note(A2, self.s) + b.note(C3, self.s), b.note(A2, self.s) + b.note(C3, self.s),
                b.note(F3, self.q) + b.note(A3, self.q),
                b.note(E3, self.e) + b.note(G3, self.e),
                b.note(D3, self.q) + b.note(F3, self.q),
                b.note(C3, self.q) + b.note(E3, self.q),
            )

            m8 = build_measure(
                b.note(B2, self.q) + b.note(D3, self.q),
                b.note(B2, self.q) + b.note(D3, self.q),
                b.note(B2, self.e) + b.note(D3, self.e), b.note(A2, self.e) + b.note(C3, self.e),
                b.note(A2, self.e) + b.note(C3, self.e), b.note(C3, self.e) + b.note(E3, self.e),
                b.note(B2, self.e) + b.note(D3, self.e), # 1/8 from m1 accounted for here
            )

            m9 = build_measure(
                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),
                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),

                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),
                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),

                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),
                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),

                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),
                rest(self.q),
                b.note(C3, self.e) + b.note(E3, self.e), b.note(B2, self.e) + b.note(D3, self.e),
            )
            m9 = fade_out(m9, 6.0)
            
            if part == "v2":
                #   8 Bars  #
                v2 = build_measure(
                    m1, m2, m3, m4,
                    m5, m6, m7, m8,
                )
                return v2

            elif part == "v3":
                #   Final 12 Bars with a 4-bar fadeout    #
                v3 = build_measure(
                    m1, m2, m3, m4,
                    m5, m6, m7, m8,

                    m1, m2, m3, m4,
                    m5, m6, m7, m8,

                    m9 # 3-bar fadeout; 16 Bars total
                )
                return v3


    def keys(self, part=""):
        k = DontTell(octave_shift=2)

        if part == "v1":
            #   V1  #
            m1 = build_measure(
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),

            )

            m2 = build_measure(
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
            )

            m3 = build_measure(
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(D3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
            )

            m4 = build_measure(
                k.note(D3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(D3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(D3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(D3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
            )

            v1 = build_measure(m1, m2, m3, m4)
            return v1

        #   V2  #
        elif part == "v2":
            m5 = build_measure(
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
            )

            m6 = build_measure(
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(D3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
            )

            m7 = build_measure(
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
            )

            m8 = build_measure(
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
                k.note(C3, self.q) + k.note(A3, self.q) + k.note(C4, self.q),
            )

            v2 = build_measure(
                m5, m6, m7, m8
            )
            return v2

        elif part == "v3":
            m5 = build_measure(
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
            )

            m6 = build_measure(
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
                k.note(C3, self.q) + k.note(G3, self.q) + k.note(B3, self.q),
            )

            m7 = build_measure(
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
            )

            m8 = build_measure(
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
                k.note(C3, self.q) + k.note(F3, self.q) + k.note(A3, self.q),
            )

            v3 = build_measure(
                m5, m6, m7, m8
            )

            return v3
        
        elif part == "v4" or part == "v5":
            m5 = build_measure(
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
            )

            m7 = build_measure(
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
            )

            m8 = build_measure(
                k.note(B2, self.q) + k.note(D3, self.q),
                k.note(B2, self.q) + k.note(D3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
                k.note(C3, self.q) + k.note(E3, self.q),
            )

            #   16 Bars for verse   #
            if part == "v4":
                v4 = build_measure(
                    m5, m8, rest(self.whole*2)
                )
                return v4
            
            #   14 Bars for the Intro; jump right into Bass #
            elif part == "v5":
                v5 = build_measure(
                    m5, m8
                )
                return v5




    def produce(self):
        """
        16-Bar Sections
        """
        #   Gather Each Section of the song    #
        ##  High Bass   #
        hb0 = self.highBass("v0")
        hb1 = self.highBass("v1")
        hb2 = self.highBass("v2")
        hb3 = self.highBass("v3")


        ##  Keys    #
        k1 = self.keys("v1") # 4 bars
        k2 = self.keys("v2") # 4 bars
        k3 = self.keys("v3") # 4 bars
        k4 = self.keys("v4") # 4 bars
        k5 = self.keys("v5") # 2 bars
        intro_keys = build_measure(k1, k2, k3, k5) # 14 bars
        keyline = build_measure(k1, k2, k3, k4) # 16 bars


        ##  Shots  #
        # s0 = self.shots("v0") # 14 bars
        # s1 = self.shots("v1") # 16 bars


        ##  Drums    #
        d0 = self.drums("v0") # 14 bars
        d1 = self.drums("v1") # 16 bars
        

        ##  Bass with Kick    #
        # b1 = self.bass("v1") # 14 bars; baseline
        # kick1 = self.kicks("v1")
        # b1 = combine(b1, kick1)

        # b2 = self.bass("v2") # 14 bars; long bass notes
        # kick2 = self.kicks("v2")
        # b2 = combine(b2, kick2)


        # b3 = self.bass('v3') # 2 bars; long notes in intro
        # kick3 = self.kicks("v3")
        # b3 = combine(b3, kick3)


        # br1 = self.bass("r1")
        # kickr = self.kicks("r1")
        # br1 = combine(br1, kickr)


        #   Silence Specific Sections   #
        b1 = rest(self.q)
        b2 = rest(self.q)

        v1 = mix(intro_keys) # Intro Keys and shots

        v2 = mix(
            keyline,
            b2
        ) # Long Bass Tones

        v3 = mix(keyline, b1, d1) 

        v4 = mix(intro_keys, b2, d0)
        #   Consider mixing b5 and baseline

        v5 = mix(hb0, d0)

        v6 = mix(hb2) # Solo High Bass

        v7 = mix(hb3, keyline, b1, d1) # Bring it all together

        prod = build_measure(
            rest(self.whole),
            #   14-Bar Intro   #
            v1,

            #   32-Bar Verse 1 -- 16 Bars, 16 Bars  #
            ##  Consider playing with a 2-Bar refrain added
            v3, 
            #br1, 
            v3,
            
            #   14-Bar Bridge   #
            v4,
            
            #   24-Bar Hook -- 14 Bars, 14 Bars High Bass Solo   #
            v5, v6,
            
            #   16-Bar Quota -- 12 Bars, 4 Bars of fadeout#
            v7
        )

        
        self.save(prod, "TrainingA")

        return prod

"""
Training B - Tupac
"""
class TB(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    def save(self, sound, name = ""):
        write(sound, os.path.join("beatsnew", "training"), name)

    def bass(self, part=""):
        b = Bass(amp = 10, freq_mod = 2)


        v1 = build_measure(
        )

        return v1

    def drums(self, part = ""):
        s = HipSkirt(attack = 40, dist=20)
        c = HipSkirt(attack = 10, low = 6000, dist = 12.0)
        d = Snare(amp = 10, freq_mod = 2)

        if part == "v1":
            m1 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q),
                s.note(C1, self.e) + d.note(C1, self.e), s.note(C1, self.e) + d.note(C1, self.e),
                c.note(C1, self.q) + d.note(C3, self.q) + d.note(C1, self.q),
                s.note(C1, self.e) + d.note(C1, self.e), # 3.5
            )

            m2 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q), # 4.5
                s.note(C1, self.e) + d.note(C1, self.e), # 5
                s.note(C1, self.q) + d.note(C1, self.q), # 6
                c.note(C1, self.q) + d.note(C3, self.q) + d.note(C1, self.q), # 7
                s.note(C1, self.q) + d.note(C1, self.q), # 8
            )
            


            m4 = build_measure(
                s.note(C1, self.q) + d.note(C1, self.q), # 1
                s.note(C1, self.e) + d.note(C1, self.e), # 1.5
                s.note(C1, self.q) + d.note(C1, self.q), # 2.5

                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 3
                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 3.5

                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e), # 4
                c.note(C1, self.e) + d.note(C3, self.e) + d.note(C1, self.e),
            )

            v1 = build_measure(
                m1, m2, 
                m1, m2,

                m1, m2,
                m1, m4
            )

            return v1
    
    def produce(self):
        d1 = self.drums("v1")
        b1 = self.bass("v1")

        v1 = d1
        #v2 = mix(d1, b1)

        prod = build_measure(
            v1, v1
        )

        self.save(prod, "TrainingB")


"""
Training C - "Know Yourself" Type Beat
"""
class TC(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, "Thug Step")

    def save(self, sound, name = ""):
        write(sound, os.path.join("beatsnew", "training"), name)

    def bass(self, part=""):
        return

    def high_synth(self, part=""):
        s = ChimySynth()

        m1 = build_measure(
            s.note(Gs3, self.q),
            rest(self.t)
        )

        v1 = build_measure(
            m1, m1, m1, m1
        )

        return v1

    def low_synth(self, part=""):
        s = LowSynth(dist = 8.0, freq_mod = 2, amp = 2.0)

        m1 = build_measure(
            s.note(C2, self.q), 
            s.note(C2, self.q),
            delaycombo(s.note(C2, self.q + self.q), s.note(B1, self.q), self.q)
        )

        m2 = build_measure(
            rest(self.q),
            s.note(A1, self.q),
            delaycombo(
            s.note(B1, self.q + self.q),
            s.note(A1, self.q),
            self.q
            )
        )

        m3 = m1

        m4 = build_measure(
            rest(self.q),
            delaycombo(
            s.note(C2, self.q + self.q),
            s.note(B1, self.q),
            self.q
            ),
            s.note(A1, self.q),
        )

        m5 = build_measure(
            s.note(D2, self.q),
            s.note(D2, self.q),

            delaycombo(
            s.note(D2, self.q + self.q),
            s.note(C2, self.q),
            self.q
            )
        )

        m6 = build_measure(
            rest(self.q),
            delaycombo(
            s.note(B1, self.q + self.q),
            s.note(C2, self.q),
            self.q
            ),
            s.note(B1, self.q),
        )

        m7 = m5

        m8 = build_measure(
            rest(self.q),
            s.note(D2, self.q),
            delaycombo(
            s.note(C2, self.q + self.q),
            s.note(B1, self.q),
            self.q
            )
        )

        v1 = build_measure(
            m1, m2, m3, m4,
            m5, m6, m7, m8
        )

        return v1
    
    def taps(self, part=""):
        s = HipSkirt(attack = 60, dist=20.0, amp=0.4, low = 10000)
        
        m1 = build_measure(
            s.note(C2, self.e), s.note(C2, self.e),
            s.note(C2, self.e), s.note(C2, self.e),
            s.note(C2, self.e), s.note(C2, self.e),
            s.note(C2, self.e), s.note(C2, self.e),
        )

        m2 = build_measure(
            s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s),
            s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s), s.note(C2, self.s),
            s.note(C2, self.e), s.note(C2, self.e),
            s.note(C2, self.e), s.note(C2, self.e),
        )

        v1 = build_measure(
            m2, m1, m2, m1,
            m1, m1, m1, m1
        )

        return v1


    def kicks(self, part = ""):
        d = KickBass2(amp = 3, dist = 20)
        
        m1 = build_measure(
            d.note(C1, self.q),
            rest(self.q),
            d.note(C1, self.q),
            rest(self.q)
        )
        
        m2 = build_measure(
            d.note(C1, self.q),
            d.note(C1, self.q),
            d.note(C1, self.q),
            d.note(C1, self.q),
        )
        
        m3 = m1

        m4 = build_measure(
            d.note(C1, self.q),
            rest(self.q),
            d.note(C1, self.q),
            d.note(C1, self.q),
        )


        m5 = m1

        m6 = build_measure(
            rest(self.h),
            d.note(C1, self.e), d.note(C1, self.e), 
            d.note(C1, self.q),
        )

        m7 = m1

        m8 = build_measure(
            rest(self.q),
            d.note(C1, self.e), d.note(C1, self.q),
            rest(self.e),
            d.note(C1, self.q),
        )


        v1 = build_measure(
            m1, m2, m3, m4,

            m5, m6, m7, m8,
        )

        return v1
        
    def drums(self, part):
        s = HipSkirt(attack = 60, dist=20.0, amp=0.4, low = 10000)
        c = HipSkirt(amp = 0.7, attack = 10, low = 6000, dist = 12.0)

        m1 = build_measure(
            c.note(C2, self.q),
            rest(self.q),
            c.note(C2, self.q),
            rest(self.q)
        )

        m2 = build_measure(
            c.note(C2, self.q),
            c.note(C2, self.e), c.note(C2, self.e),
            rest(self.q), 
            c.note(C2, self.q),
        )

        m3 = m1

        m4 = build_measure(
            c.note(C2, self.q),
            c.note(C2, self.e), c.note(C2, self.e),
            rest(self.e), c.note(C2, self.e), 
            rest(self.e), c.note(C2, self.e),

        )

        m5 = m1

        m6 = build_measure(
            rest(self.q),
            c.note(C2, self.e), c.note(C2, self.e),
            rest(self.q),
            c.note(C2, self.q)
        )

        m7 = m5

        m8 = m6

        v1 = build_measure(
            m1, m2, m3, m4,
            m5, m6, m7, m8

        )

        return v1

    def produce(self):
        #   Bass / Percussion   #
        t1 = self.taps("v1")
        k1 = self.kicks("v1")
        d1 = self.drums("v1")
        b1 = self.bass("v1")

        #   Synths / Keys   #
        hs1 = self.high_synth("v1")
        ls1 = self.low_synth("v1")


        v1 = mix(ls1, highpass(t1, 10000))
        ###  Decide on High Pass or not for V2   #
        v2 = mix(ls1, highpass(t1, 1600))
        #v2 = mix(ls1, t1)

        v3 = mix(v2, k1)

        v4 = mix(v3, d1)

        prod = build_measure(
            v1, v2, v3,
            v4, v4,
            v4, v4,
            v4, v4
        )

        self.save(prod, "TrainingC")
        self.production = prod






















class TD(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, "Provocative Interface")
        
        self.instruments = {
            #   [Instrument, wave]  #
            0: [Bass(), []],
            1: [DontMind(), []]
        }

        self.prep()

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "training"), name)

    def prep(self):
        i = self.instruments[0][0]
        j = self.instruments[1][0]

        m1 = [
                i.note(C1, self.q),
                i.note(C1, self.q),
                i.note(C1, self.q),
                i.note(C1, self.q),

                i.note(E1, self.q),
                i.note(E1, self.q),
                i.note(E1, self.q),
                i.note(E1, self.q),

                i.note(D1, self.q),
                i.note(D1, self.q),
                i.note(D1, self.q),
                i.note(D1, self.q),

                i.note(C1, self.q),
                i.note(C1, self.q),
                i.note(E1, self.q),
                i.note(E1, self.q),
        ]

        m2 = [
                j.note(C5, self.q),
                j.note(C5, self.q),
                j.note(C5, self.q),
                j.note(C5, self.q),

                j.note(E5, self.q),
                j.note(E5, self.q),
                j.note(E5, self.q),
                j.note(E5, self.q),
        ]

        self.instruments[0][1] = m1
        self.instruments[1][1] = m2



def main():
    TA(90).produce()
    #TA(90).drums("v1")

    #TB(100).produce()
    #TC(135).produce()
