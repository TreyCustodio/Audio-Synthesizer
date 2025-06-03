from modules.beat import *
from modules.instruments import *
from modules.audio import *
import pygame.sndarray
import pygame.mixer

class First(Beat):
    def __init__(self, bpm):
        super().__init__(bpm)

    
    def save(self, sound, name = ""):
        """Save the sound to the desired folder"""

        write(sound, os.path.join("beatsnew", "firstup"), name)
    
    
    def bass(self):
        b = Bass()
        
        #m1 = fade_out(build_measure(b.q_c, b.q_c, b.q_c, b.q_c), 4)
        m1 = build_measure(b.note(C1, self.quarter),
                           rest(self.eighth), b.note(C1, self.s),
                           b.note(C1, self.e), b.note(C1, self.s),
                           rest(self.eighth), b.note(C1, self.e), rest(self.eighth))

        m2 = build_measure(b.note(C1, self.e), rest(self.half + self.sixteenth), # 2.5
                           b.note(C1, self.s), b.note(C1, self.e), b.note(C1, self.s), rest(self.sixteenth)
                           )

        v1 = build_measure(m1, m1, m1, m1) * 1.4
        v2 = build_measure(m2) * 1.4

        
        return v1, v2


    def funk(self):
        f = First4()


        #   V1 -- Unused    #
        m1 = build_measure(
        f.note(C4, self.e), # .5
        f.note(B3, self.s), # .75
        f.note(A3, self.s), # 1
        f.note(C4, self.q), # 2
        rest(self.s), # 2.25
        f.note(A3, self.s), # 2.5
        f.note(B3, self.e), # 3
        f.note(C4, self.q), # 4
        )

        m2 = build_measure( # Tone shift -2 full tones
        f.note(A3, self.e), # .5
        f.note(G3, self.s), # .75
        f.note(F3, self.s), # 1
        f.note(A3, self.q), # 2
        rest(self.s), # 2.25
        f.note(F3, self.s), # 2.5
        f.note(G3, self.e), # 3
        f.note(A3, self.q), # 4
        )


        amp = 0.5
        v1 = build_measure(m1, m1, m2, m2) * amp
        

        #   V2 -- Alternate version of V1   ##
        v2 = build_measure(m2, m2, m2, m2) * amp
        


        #   V3  -- Hook #
        m3 = build_measure(f.note(F3, self.e), f.note(A3, self.s),
        f.note(B3, self.e), f.note(C4, self.e),
        f.note(D4, self.e), f.note(C4, self.s),
        f.note(B3, self.e), f.note(A3, self.q)
        )

        m3b = build_measure(f.note(F3, self.e), f.note(A3, self.s),
        f.note(B3, self.e), f.note(C4, self.e),
        f.note(D4, self.e), f.note(C4, self.s),
        f.note(B3, self.e), f.note(A3, self.e), f.note(G3, self.e)
        )

        #   Pause at the start
        m3c = build_measure(rest(self.e), f.note(A3, self.s),
        f.note(B3, self.e), f.note(C4, self.e),
        f.note(D4, self.e), f.note(C4, self.s),
        f.note(B3, self.e), f.note(A3, self.e), f.note(G3, self.e)
        )

        m4 = build_measure(f.note(E3, self.e), f.note(G3, self.s),
        f.note(A3, self.e), f.note(B3, self.e),
        f.note(C4, self.e), f.note(B3, self.s),
        f.note(A3, self.e), f.note(G3, self.q)
        )

        m4b = build_measure(f.note(E3, self.e), f.note(G3, self.s),
        f.note(A3, self.e), f.note(B3, self.e),
        f.note(C4, self.e), f.note(B3, self.s),
        f.note(A3, self.e), f.note(G3, self.e), f.note(F3, self.e)
        )

        #   Pause at the start
        m4c = build_measure(rest(self.e), f.note(G3, self.s),
        f.note(A3, self.e), f.note(B3, self.e),
        f.note(C4, self.e), f.note(B3, self.s),
        f.note(A3, self.e), f.note(G3, self.e), f.note(F3, self.e)
        )

        v3 = build_measure(m3, m3c, m4, m4c)



        #   V4  -- Unused; Possibly Verse 2 #
        m5 = build_measure(f.note(D3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(D3, self.e), f.note(F3, self.e),
                           rest(self.quarter),)
        
        m6 = build_measure(f.note(D3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(F3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e))
                           
        
        m7 = build_measure(f.note(C3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(C3, self.e), f.note(E3, self.e),
                           rest(self.quarter),)
        
        m8 = build_measure(f.note(C3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(E3, self.e), rest(self.e),
                           f.note(D3, self.e), rest(self.e))

        v4 = build_measure(m5, m6, m7, m8)

        return v1, v2, v3 * 0.75, v4
    

    def drums(self, variation = ""):
        d = Skirt()
        c = Cymbal()
        s = Snare()
        b = Bass()

        m1 = build_measure(
            d.note(C3, self.e),
            d.note(C3, self.s), d.note(C3, self.s), # 1

            d.note(C3, self.e), d.note(C3, self.s), # 1.75
            d.note(C3, self.e), # 2.25
            d.note(C3, self.s), # 2.5

            d.note(C3, self.e), d.note(C3, self.e), #3.5
            d.note(C3, self.s), d.note(C3, self.s) # 4

        )

        m1c = build_measure(
            c.note(C2, self.e),
            c.note(C2, self.s), c.note(C2, self.s), # 1

            c.note(C2, self.e), c.note(C2, self.s), # 1.75
            c.note(C2, self.e), # 2.25
            c.note(C2, self.s), # 2.5

            c.note(C2, self.e), c.note(C2, self.e), #3.5
            c.note(C2, self.s), c.note(C2, self.s) # 4

        )
        #m1 = m1 + m1c


        v1 = build_measure(m1, m1, m1, m1) * 3.0

        #   Island Drum Beat  #
        m2 = build_measure(
            d.note(C3, self.e), d.note(C3, self.e),
            d.note(C5, self.e), d.note(C3, self.s), d.note(C5, self.s),
            d.note(C3, self.s), d.note(C5, self.s), d.note(C5, self.e),
            d.note(B4, self.e),
            rest(self.e)

        )

        v2 = build_measure(m2, m2, m2, m2) * 3.0


        #   Snares, Cymbals, and Bass #
        m3 = build_measure(
            s.note(C2, self.e), s.note(C2, self.e),
            c.note(C3, self.e) + s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e),
            c.note(C3, self.e) + s.note(C3, self.e),
            rest(self.e),
        )

        m4 = build_measure(
            s.note(C2, self.e), s.note(C2, self.e),
            c.note(C3, self.e) + s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e), s.note(C2, self.s),
            s.note(C3, self.e),
            c.note(C3, self.e) + s.note(C3, self.e),
            c.note(C2, self.e) + s.note(C2, self.e),
        )

        v3 = build_measure(m3, m4, m3, m4) * 3.0
        

        #   c, s, d, b
        intro_tings = build_measure(
            d.note(B4, self.e),
            )


        if variation == "refrain1":
            #   Kick drum with noise    #
            return build_measure(
                rest(self.e), rest(self.half + self.sixteenth),
                c.note(C2, self.s), c.note(E2, self.e), c.note(D2, self.s), rest(self.sixteenth)
            )

        elif variation == "intro":
            return build_measure(m1, m1, m1, m1)

        #   Island Beat with Snares, Cymbals, and Bass
        return v1, v2, v3

    def plucks(self, variation = ""):
        # l, l, s, s, s, l x2 then go down

        p = First2()

        m1 = build_measure(
            p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
            rest(self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
        )
        m2 = build_measure(
            p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e),
            rest(self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.q)
        )

        m3 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.e), rest(self.e)

        )

        m4 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
        )


        #   Chopped Versions    #
        m5 = build_measure(
            p.note(A4, self.e + self.s), rest(self.q - (self.e + self.s)),
            rest(self.quarter + self.s*2),
            p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.q)
        )

        m6 = build_measure(
            p.note(A4, self.e), p.note(B4, self.s), p.note(C5, self.s),
            p.note(D5, self.e), p.note(C5, self.e) *1.5,
            
            rest(self.e), p.note(C5, self.e) * 2.0,
            rest(self.q)
        )

        m7 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.e), rest(self.e)

        )

        m8 = build_measure(
            p.note(E5, self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s), p.note(A4, self.e), 
            rest(self.e), p.note(D5, self.s), p.note(C5, self.s),
            p.note(B4, self.s),
            p.note(A4, self.s), p.note(G4, self.e), rest(self.s)
        )



        v1 = build_measure(m1, m2, m3, m4) * 0.1

        if variation == "chopped1":
            return build_measure(m5, m6, m7, m8)

        elif variation == "faded":
            return build_measure(m1, m2, fade_out(add_waves(m3, m4), 10.0))
        
        elif variation == "intro":
            return build_measure(m1, m2, m3, m4)

        return v1

    def synth(self, variation = ""):
        f = Bass()

        #   Notes to be sung    #
        # m1 = build_measure(
        #     f.note(D2, self.q),
        #     f.note(D2, self.e), f.note(E2, self.s),
        #     f.note(F2, self.e), f.note(G2, self.e),
        #     f.note(A2, self.e),
        #     rest(self.s * 3)
        # )

        # m2 = build_measure(
        #     f.note(D2, self.e), f.note(E2, self.s),
        #     f.note(F2, self.e), f.note(G2, self.e),
        #     f.note(A2, self.e),
        #     f.note(G2, self.q + self.s*3)
        # )

        # m3 = build_measure(
        #     rest(self.q),
        #     f.note(C2, self.e), f.note(D2, self.s),
        #     f.note(E2, self.e), f.note(F2, self.e),
        #     f.note(G2, self.e), rest(self.s * 2),
        #     f.note(C2, self.s)
        # )

        # m4 = build_measure(
        #     f.note(C2, self.e), f.note(D2, self.s),
        #     f.note(E2, self.e), f.note(F2, self.e),
        #     f.note(G2, self.e),
        #     f.note(F2, self.q + self.s*3)
        # )


        #   V1 - supporting tenor   #
        m1 = build_measure(
            delaycombo(f.note(D2, self.e), f.note(F2, self.e), 0.05), rest(self.e - 0.05),
            rest(self.trey - self.e),
            f.note(D2, self.e) + f.note(F2, self.e),
        )

        m2 = build_measure(
            f.note(D2, self.e) + f.note(F2, self.e), 
            rest(self.trey),
            f.note(D2, self.e) + f.note(F2, self.e)

        )

        m3 = build_measure(
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey), # 3
           
        )

        m4 = build_measure(
            f.note(C2, self.e) + f.note(E2, self.e), f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey - self.e),
            f.note(C2, self.e) + f.note(E2, self.e)
            
        )

        m5 = build_measure(
            delaycombo(f.note(C2, self.e), f.note(E2, self.e), 0.05), rest(self.e - 0.05), # 1
            rest(self.trey - self.e), # 3
            f.note(C2, self.e) + f.note(E2, self.e),
        )

        m6 = build_measure(
            f.note(C2, self.e) + f.note(E2, self.e), 
            rest(self.trey),
            f.note(C2, self.e) + f.note(E2, self.e)
        )

        m7 = build_measure(
            rest(self.q), f.note(D2, self.e), 
            f.note(C2, self.s), f.note(D2, self.e),
            rest(self.s + self.q)
        )

        m8 = build_measure(
            rest(self.q), f.note(E2, self.e), 
            f.note(D2, self.s), f.note(E2, self.e),
            rest(self.s + self.q)
        )

        m1 = combine(m1, m7)
        m2 = combine(m2, m7)
        m3 = combine(m3, m8)
        m4 = combine(m4, m8)


        m9 = build_measure(
            rest(self.q + self.q + self.e),
            # leaving self.s + self.q
            f.note(D2, self.s), f.note(D2, self.s), f.note(D2, self.s), f.note(D2, self.s),
            f.note(D2, self.s), f.note(D2, self.s),
        )

        m4 = combine(m4, m9)
        m6 = combine(m6, m8)
        

        v1 = build_measure(m1, m2, m3, m4)

        v1b = build_measure(m1, m2, m5, m6)


        #   V2 - supporting tenor   #
        amp1 = 0.5

        m5 = build_measure(
            f.note(F1, self.q),
            rest(self.h),
            f.note(F1, self.q)
        )

        m6 = build_measure(
            f.note(F1, self.q),
            rest(self.h),
            f.note(F1, self.q)
        )

        m7 = build_measure(
            f.note(E1, self.q),
            rest(self.h),
            f.note(E1, self.q)
        )

        m8 = build_measure(
            f.note(E1, self.q),
            rest(self.h),
            f.note(E1, self.q)
        )

        m5b = build_measure(
            f.note(F2, self.q),
            rest(self.h),
            f.note(F2, self.q)
        ) * amp1

        m6b = build_measure(
            f.note(F2, self.q),
            rest(self.h),
            f.note(F2, self.q)
        ) * amp1

        m7b = build_measure(
            f.note(E2, self.q),
            rest(self.h),
            f.note(E2, self.q)
        ) * amp1

        m8b = build_measure(
            f.note(E2, self.q),
            rest(self.h),
            f.note(E2, self.q)
        ) * amp1

        m5 += m5b
        m6 += m6b
        m7 += m7b
        m8 += m8b

        v2 = build_measure(m5, m6, m7, m8)


        #   Return  #
        if variation == "v1":
            return v1
        
        elif variation == "v1b":
            return v1b

        elif variation == "v2":
            return v2
        
        elif variation == "refrain":
            bar = build_measure(
                rest(self.whole - self.e),
                f.note(D2, self.e) + f.note(F2, self.e),
                
                rest(self.whole - self.q),
                f.note(D2, self.e) + f.note(F2, self.e), f.note(C2, self.e) + f.note(E2, self.e),

                rest(self.whole - self.e),
                f.note(B1, self.e) + f.note(D2, self.e),

                rest(self.whole - self.q - self.s),
                f.note(A1, self.s) + f.note(C2, self.s), 
                f.note(C2, self.s) + f.note(E2, self.s), 
                f.note(C2, self.s)+ f.note(E2, self.s), f.note(C2, self.s) + f.note(E2, self.s), f.note(C2, self.s) + f.note(E2, self.s),
                )


            return bar

        else:
            return v1, v2



    def navi(self):
        n1 = Hey()
        
        m1 = build_measure(n1.note(), n1.note(), n1.note(), n1.note())

        return m1

    def intro(self):

        #   Gather Instruments  #
        b1, b2 = self.bass()
        f1, f2, f3, f4 = self.funk()
        d1, d2, d3 = self.drums()
        n1 = self.navi() * 0.05
        s1, s2 = self.synth()
        s1b = self.synth("v1b")


        #   Produce each section    #
        v0 = b1

        v1 = combine(b1, d1)

        v2 = b2
        v2 = combine(v2, self.drums('refrain1'))
        
        
        v3 = s1b * 0.6
        v3a = combine(v3, fade_in(d2, 1.0))
        v3b = combine(s1 * 0.6, d2)

        #v2 = combine(b1, n1)
        #v2 = combine(v2, d1)

        prod = build_measure(
            v0, v1, v2, v3a, v3b
        )


        #   Save the production #
        self.save(prod, "intro")
        return prod


    def chorus1(self):
        #   Gather Instruments  #
        b1, b2 = self.bass()
        #f1, f2, f3, f4 = self.funk()
        s1, s2 = self.synth()
        p1 = self.plucks()
        s1b = self.synth("v1b")
        d1, d2, d3 = self.drums()


        #   Produce each section    #
        v1 = s1 * 0.6
        v1 = combine(v1, p1)
        v1 = combine(v1, d2)
        v1 = combine(v1, d3)

        v1b = combine(s1b * 0.6, d2)
        v1b = combine(v1b, p1)
        v1b = combine(v1b, d3)

        #v1 = combine(d1, v1)
        #v1 = combine(v1, b1)

        prod = build_measure(v1b, v1)

        self.save(prod, "chorus1")
        return prod

    def hook1(self):
        b1, b2 = self.bass()
        f1, f2, f3, f4 = self.funk()
        s1, s2 = self.synth()
        d1, d2, d3 = self.drums()


        v2 = s2
        v2 = combine(v2, f3)
        v2_b = build_measure(b2, b2, b2, b2)
        v2 = combine(v2, v2_b)
        v2 = combine(v2, d3)

        prod = build_measure(v2, v2)

        self.save(prod, "hook1")
        return prod


    def verse1(self):
        chorus1 = self.chorus1()
        return build_measure(chorus1, chorus1)

    def refrain1(self):
        """4-bar refrain"""
        d1, d2, d3 = self.drums()
        s1 = self.synth("refrain")

        prod = combine(d3, s1)

        self.save(prod, "drum refrain")
        return prod

    def verse2(self):
        return

        

    def produce(self):
        #   Gather Each Section of the song    #
        intro = self.intro()
        chorus = self.chorus1()
        hook = self.hook1()
        verse1 = self.verse1()
        refrain1 = self.refrain1()


        #   Save the production #
        prod = build_measure(
            #   Intro   #
            intro,

            #   Chorus  #
            chorus,

            #   Hook    #
            hook,

            #   Verse 1 #
            verse1,

            #   Refrain #
            refrain1,

            #  Hook   #
            hook,

            #   Chorus  #
            chorus,

            #   Verse 2 #
            verse1,

            #   Hook (Saxophone Solo)    #
            hook,

            #   Chorus (Sax + sung) #
            chorus
        )

        # prod = (prod / np.max(np.abs(prod)) * 32767).astype(np.int16)
        # prod = np.column_stack((prod, prod))
        # sound = pygame.sndarray.make_sound(prod)
        # sound.play()
        # while pygame.mixer.get_busy():
        #     pass

        #   Save the production #

        self.save(prod, "firstup")

        return
    
def main():
    First(62).produce()
    #First(62).intro()
    #First(62).chorus1()