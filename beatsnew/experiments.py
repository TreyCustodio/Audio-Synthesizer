from modules.beat import *
from modules.instruments import *
from modules.audio import *

class Exp(Beat):
    def __init__(self, bpm, name="00"):
        super().__init__(bpm, path = os.path.join("beatsnew", "experiments", name))
        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Bass    ##
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)

        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)
        
        self.bass1 = LowSynth(1.5, wave_1 = False, wave_2 = True, wave_3 = False, sustain=0.6)
        self.bass2 = LowSynth(1.0, wave_1 = False, wave_2=False, wave_3 = True,
                              sustain=1.0)
        self.bass3 = Bass_1(amp=0.8, 
                            freq_mod = (1.5), 
                            attack=0.01, attack_max = 0.02, decay=0.0, sustain=1.0, release=0.01,
                            amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

        #   Percussion  #
        ##  Chimes
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Kicks
        # self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")
        self.kick1 = Nine_Sample(amp=0.00003, name="kick-classic.wav")
        self.kick2 = E1_Samples(amp=0.00003, name="kick16.wav")
        self.dry_kick = Nine_Sample(amp=0.00007, name="kick-dry.wav")

        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")
        self.crash2 = Nine_Sample(name="crash-808.wav")


        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.closed2 = Nine_Sample(name="hihat-electro.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")
        self.digi1 = Nine_Sample(name="hihat-digital.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")
        self.sumo_snare = Nine_Sample(name="snare-sumo.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #
        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))
        self.fx9 = E1_Samples(name="fx09.wav")
        self.hey = GlobalSample(0.0001, os.path.join("samples", "hey.wav"))
        self.drop = GlobalSample(0.001, os.path.join("samples", "ambience", "drop_1.wav"))
        
        

        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],



            #   Melody  #


            #   Samples / Libs  #
        }

    def hats(self, verse):
        return
        
    def drums(self, verse):
        return
    

# ----------------- #
#   Experiment 3    #
# ----------------- #
class Exp3(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path = os.path.join("beatsnew", "experiments", "03"))
        #   Instruments #

        #   Melody  #


        #   Rhythm / Percussion  #
        ##  Bass    ##5
        self.bell = AMTR.Bell(amp=0.25, freq_mod=1.0, wave_2 = False, wave_3=False,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)

        
        self.bell2 = AMTR.IsoBell(amp=0.25, freq_mod=1.0,
                                        attack=0.01, decay=0.0, sustain=1.0, release=0.03)
        
        self.bell3 = Tangible_Light.Title_Synth(amp=0.5)
        
        self.bass1 = LowSynth(1.5, wave_1 = False, wave_2 = True, wave_3 = False, sustain=0.6)
        self.bass2 = LowSynth(1.0, wave_1 = False, wave_2=False, wave_3 = True,
                              sustain=1.0)
        self.bass3 = Bass_1(amp=0.8, 
                            freq_mod = (1.5), 
                            attack=0.01, attack_max = 0.02, decay=0.0, sustain=1.0, release=0.01,
                            amp_final = 0.00000000001, top_freq = 2, harmonics=2)

        

        #   Percussion  #
        ##  Chimes
        self.chime1 = Skirt(amp=0.25, noise_amount=0.1, attack=10)
        self.chime2 = Skirt(amp=5.0, noise_amount=0.1, attack=50)

        ##  Kicks
        # self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")
        self.kick1 = Nine_Sample(amp=0.00003, name="kick-classic.wav")
        self.kick2 = E1_Samples(amp=0.00003, name="kick16.wav")

        
        ##  Claps
        self.clap1 = Nine_Sample(name="clap-tape.wav")
        self.clap2 = Nine_Sample(name="clap-slapper.wav") # long clap

        ##  Crashes
        self.crash1 = Nine_Sample(name="crash-acoustic.wav")

        ##  Shakes
        self.shake1 = Nine_Sample(name="shaker-shuffle.wav")

        ##  Hats
        self.closed1 = Nine_Sample(name="hihat-808.wav")
        self.open1 = Nine_Sample(name="openhat-slick.wav")

        ##  Snares
        self.snare1 = Nine_Sample(amp=0.00007, name="snare-acoustic01.wav")
        self.snare2 = Nine_Sample(amp=0.00007, name="snare-acoustic02.wav")
        self.snare3 = Rapping.Snare_1()
        self.snare4 = E1_Samples(amp=0.0007, name="snare15.wav")

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Samples #
        self.pan1 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "panflute.mp3"))
        self.pan2 = GlobalSample(0.0001, os.path.join("samples", "pan-flute", "sample_1.wav"))
        
        self.instruments = {}


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            # 'kick': [0, self.kicks(verse)],
            # 'snare': [0, self.snares(verse)],
            'drums1': [0, self.drums(verse)],
            # 'bass': [0, self.bass(verse)],
            # 'synth': [0, self.synths(verse)],



            'hats': [0, self.hats(verse)],
            # 'crash': [0, self.cymbals(verse)],



            #   Melody  #


            #   Samples / Libs  #
        }

    def synths(self, verse):
        b = self.bass1
        b2 = self.bass2

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.w)
        ]

        m2 = [
            b2.n(C3, self.s), b2.n(D3, self.s), b2.n(F3, self.s), b2.n(G3, self.s),
            b2.n(F3, self.s), b2.n(D3, self.s), rest(self.e),
            b2.n(C3, self.s), b2.n(D3, self.s), b2.n(F3, self.s), b2.n(G3, self.s),
            b2.n(F3, self.s), b2.n(E3, self.s), rest(self.e),
        ]

        m3 = [
            rest(self.q),
            b2.n(D3, self.e), b2.n(C3, self.e),
            b2.n(D3, self.q),
            b2.n(C3, self.q),
        ]

        v1 = m1 + m2 + m3 + m2

        return \
        v0 +\
        v1 + v1
    
    def bass(self, verse):
        b3 = self.bass3

        v0 = [rest(self.w*4)]

        m0 = [rest(self.w)]

        m1 = [
            rest(self.q),
            b3.n(C1, self.q),
            rest(self.q),
            b3.n(C1, self.e), b3.n(D1, self.e)
        ]

        m2 = [
            rest(self.q),
            b3.n(C1, self.q),
            rest(self.q),
            b3.n(C1, self.q),
        ]

        m2b = [
            rest(self.q),
            rest(self.e), b3.n(C1, self.e),
            rest(self.q),
            rest(self.e), b3.n(C1, self.s), b3.n(B0, self.s),
        ]

        m3 = [
            b3.n(C1, self.q, amp = 0.6),
            rest(self.q),
            rest(self.q),
            rest(self.q)
        ]

        m4 = [
            rest(self.t),
            rest(self.e), b3.n(C1, self.s/2), b3.n(B0, self.s/2), b3.n(C1, self.s)
        ]

        m4b = [
            rest(self.q),
            rest(self.e), b3.n(C1, self.e),
            rest(self.q),
            rest(self.e), b3.n(C1, self.s/2), b3.n(B0, self.s/2), b3.n(C1, self.s)
        ]

        v0 = m2 + m0 + m2 + m4
        v1 = m1 + m2b + m3 + m4b

        return \
        v0 +\
        v1 + v1

    def hats(self, verse):
        h = self.closed1

        m0 = [
            rest(self.w)
        ]

        m1 = [
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        m3 = [
            rest(self.q),
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        m4 = [
            rest(self.h),
            h.n(self.e), h.n(self.e),
            h.n(self.q),
        ]

        v0 = [rest(self.w*4)]
        v1 = m3 + m3 + m3 + m4
        v2 = m3 + m3 + m3 + m4
        v3 = m0 + m0 + m0 + m4

        return \
        v0 +\
        v1 + v2 + v3 +\
        v1 + v2 + v3 +\
        v1 + v2 + v3 +\
        v1 + v2 + v3
        
        
    def drums(self, verse):
        k = self.kick1
        k2 = self.kick2
        s = self.snare4

        m1 = [
            k.n(self.e), k.n(self.e),
            s.n(self.q),
            rest(self.e), k.n(self.e),
            s.n(self.q)
        ]

        m4 = [
            k.n(self.e), k.n(self.e),
            s.n(self.q),
            rest(self.e), s.n(self.e),
            rest(self.e), s.n(self.e)
        ]
        v1 = m1 + m1 + m1 + m4

        m5 = [
            k.n(self.q),
            s.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            s.n(self.q)
        ]

        m6 = [
            k.n(self.e), k.n(self.e),
            s.n(self.e), k.n(self.e),
            rest(self.e), k.n(self.e),
            s.n(self.q)
        ]

        m8 = [
            k.n(self.e), k.n(self.e),
            s.n(self.e), k.n(self.e),
            rest(self.e), s.n(self.e),
            rest(self.e), s.n(self.e)
        ]

        v2 = m5 + m6 + m5 + m4

        m7 = [
            k.n(self.e), k.n(self.s), k.n(self.s),
            s.n(self.q),
            rest(self.e), k.n(self.e),
            delaycombo(s.n(self.e), k.n(self.e + self.s), self.s, False)
        ]

        v3 = m7 + m1 + m7 + m4

        return \
        v1 +\
        v2 + v2 + v3 +\
        v2 + v2 + v3 +\
        v2 + v2 + v3 +\
        v2 + v2 + v3








# ----------------- #
#   Experiment 4    #
# ----------------- #
class Exp4(Exp):
    def __init__(self, bpm):
        super().__init__(bpm, "04")


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],
            # 'cymbals': [0, self.cymbals(verse)],




            #   Melody  #


            #   Samples / Libs  #
        }

    def hats(self, verse):
        h = self.closed1

        m1 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        m4 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), rest(self.e*3)
        ]

        

        v1 = m1 + m1 + m1 + m4

        v2 = m1 + m1 + m1 + m1

        return \
        v1 +\
        v2 + v2 + v2 +\
        v2 + v2 + v2
        
    
    def cymbals(self, verse):
        o = self.crash1

        m8 = [
            rest(self.q),
            o.n(self.q, amp=0.5),
            o.n(self.q, amp=0.5),
            o.n(self.q, amp=0.5),

        ]

        m0 = [
            rest(self.w)
        ]
        v0 = [rest(self.w*4)]

        v1 = m0 + m0 + m0 + m8

        return \
        v0 + v1 + v1
    
    def drums(self, verse):
        k = self.dry_kick
        s = self.snare3
        sumo = self.sumo_snare

        m1 = [
            k.n(self.q),
            s.n(self.e), k.n(self.s),
            k.n(self.e), k.n(self.s),
            k.n(self.e), s.n(self.q),
        ]
        
        m2 = [
            k.n(self.q),
            s.n(self.e), k.n(self.s),
            k.n(self.e), k.n(self.s),
            k.n(self.e), s.n(self.e), s.n(self.e),
        ]

        m4 = [
            k.n(self.q),
            s.n(self.q),
            s.n(self.q),
            s.n(self.q),
        ]

        m8 = [
            k.n(self.q),
            s.n(self.q),
            rest(self.e), s.n(self.e),
            s.n(self.e), rest(self.e)
        ]

        m12 = [
            k.n(self.q),
            s.n(self.q),
            rest(self.e), s.n(self.e), rest(self.s),
            s.n(self.e), rest(self.s)
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m4
        v2 = m2 + m1 + m1 + m8
        v3 = m1 + m1 + m1 + m12

        return \
        v0 +\
        v1 + v2 + v3 +\
        v1 + v2 + v3
    

# ----------------- #
#   Experiment 5    #
# ----------------- #
class Pump(Exp):
    def __init__(self, bpm):
        super().__init__(bpm, "05")


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],
            # 'cymbals': [0, self.cymbals(verse)],




            #   Melody  #


            #   Samples / Libs  #
            'samples': [0, self.libs(verse)]

        }

    def hats(self, verse):
        h = self.closed1

        m0 = [rest(self.w)]
        m1 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        m3 = [
            rest(self.h),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]


        v1 = m1 + m1 + m3 + m1 # silent top half of bar 3
        v2 = m1 + m1 + m1 + m1
        refrain = [rest(self.w*6)]

        return \
        v1 + v2 +\
        v2 + v2 +\
        v2 + v2
        
    
    def cymbals(self, verse):
        o = self.crash1

        m8 = [
            rest(self.q),
            o.n(self.q, amp=0.5),
            o.n(self.q, amp=0.5),
            o.n(self.q, amp=0.5),

        ]

        m0 = [
            rest(self.w)
        ]
        v0 = [rest(self.w*4)]

        v1 = m0 + m0 + m0 + m8

        return \
        v0 + v1 + v1
    
    def drums(self, verse):
        k = self.dry_kick
        s = self.snare3
        sumo = self.sumo_snare

        m0 = [
            rest(self.w - (self.h)),
            rest(self.e),
            k.n(self.e),
            k.n(self.e),
            k.n(self.e),


        ]

        m1 = [
            k.n(self.q),
            k.n(self.q),
            s.n(self.e), k.n(self.e),
            s.n(self.e), k.n(self.e),
        ]
        
        m2 = [
            rest(self.e),
            k.n(self.q),
            k.n(self.e), s.n(self.e),
            k.n(self.e), s.n(self.e),
            rest(self.e)
        ]

        m3 = [
            k.n(self.q),
            k.n(self.q),
            s.n(self.q),
            rest(self.e), s.n(self.e)
        ]

        m4 = [
            rest(self.e), k.n(self.e),
            k.n(self.e), rest(self.e),
            s.n(self.q),
            s.n(self.q),
        ]

        

        m5 = [
            k.n(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        m7 = [
            k.n(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.e), s.n(self.e)
        ]

        m8 = [
            rest(self.e), k.n(self.e),
            rest(self.e), rest(self.e),
            s.n(self.q),
            s.n(self.q),
        ]

        m11 = [
            k.n(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        m12 = [
            rest(self.e), 
            k.n(self.q),
            k.n(self.e),
            s.n(self.q),
            s.n(self.q)
        ]

        m14 = [
            rest(self.e), 
            k.n(self.q),
            k.n(self.e),
            s.n(self.q),
            s.n(self.s), s.n(self.s), s.n(self.e)
        ]
        
        v0 = [rest(self.w*4)]
        vi = [rest(self.w*3)] + m0

        v1 = m1 + m2 + m3 + m4
        v2 = m5 + m2 + m5 + m4
        v3 = [rest(self.w*2)] + m11 + m12 + m11 + m14

        return \
        v1 + v2 + v1 +\
        v2 + v1 + v2 +\
        v3

    def libs(self, verse):
        h = self.hey
        d = self.drop

        m4 = [
            rest(self.q),
            h.n(self.e, amp=0.1),
            # d.n(self.e),
            rest(self.e),
            d.n(self.q, amp=2.0),
            rest(self.q)
        ]

        m4b = [
            rest(self.q),
            h.n(self.e, amp=0.1),
            # d.n(self.e),
            rest(self.e),
            d.n(self.q, amp=2.0),
            d.n(self.q, amp=2.0),
        ]

        m4c = [
            rest(self.t),
            h.n(self.q, amp=0.1)
        ]

        v1 = [rest(self.w*2)] + m4 + [rest(self.w)]
        v2 = [rest(self.w*3)] + m4b
        v3 = [rest(self.w*2)] + [rest(self.w)] + m4c


        v0 = [rest(self.w*4)]
        return \
        v1 + v2 +\
        v1 + v2 + v0 +\
        v3


class Pump2(Exp):
    def __init__(self, bpm):
        super().__init__(bpm, "Pump Me Up pt 2")


    def get_instruments(self, verse = "full"):
        self.instruments = {
            #   Rhythm and Bass #
            'drums1': [0, self.drums(verse)],
            'hats': [0, self.hats(verse)],
            # 'cymbals': [0, self.cymbals(verse)],




            #   Melody  #


            #   Samples / Libs  #
            # 'samples': [0, self.libs(verse)]

        }

    def hats(self, verse):
        # h = self.digi1
        h = self.closed1


        m0 = [rest(self.w)]
        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        mold = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
        ]

        mold2 = [
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.e), h.n(self.e),
            h.n(self.s), h.n(self.s), h.n(self.e),
        ]

        mq = [
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        m3 = [
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m1
        v2 = mq + mq + mold + mold2
        v3 = mold + mold + mold + mold2

        return \
        v0 + v0 +\
        v1 + v1 +\
        v1 + v1 +\
        v1 + v1 +\
        v2 + v3 +\
        \
        v1 + v1 +\
        v1 + v1
    
    def drums(self, verse):
        k = self.dry_kick
        s = self.snare3
        c = self.crash2
        sumo = self.sumo_snare

        m1 = [
            k.n(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.q)
        ]

        
        m2 = [
            rest(self.q),
            k.n(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        m3 = [
        ]

        m4 = [
        ]

        m5 = [
            k.n(self.q),
            k.n(self.q),
            s.n(self.q),
            k.n(self.e), s.n(self.e)
        ]

        m6 = [
            rest(self.e),
            k.n(self.e), k.n(self.e),
            rest(self.e),
            s.n(self.q),
            s.n(self.q),
        ]

        m9 = [
            k.n(self.q),
            k.n(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        m10 = [
            rest(self.q),
            k.n(self.q),
            s.n(self.q),
            rest(self.q)
        ]

        m12 = [
            rest(self.q),
            k.n(self.q),
            s.n(self.q),
            k.n(self.q) + c.n(self.q, amp=4.0, fadeIn=True, fade_amount=8),
        ]
        
        v1 = m1 + m2 + m1 + m2
        v2 = m5 + m6 + m5 + m6
        v3 = m9 + m10 + m9 + m12

        return \
        v1 + v1 +\
        v2 + v2 +\
        v2 + v2 +\
        v2 + v2 +\
        v3 + v3 +\
        \
        v2 + v2 +\
        v2 + v2


def main():
    """
    One more Verse to loop back to verse 1.
    """

    # beat = Exp3(111)
    # beat = Pump(145)
    beat = Pump2(145)

    # beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))

    beat.get_instruments()
    beat.export_selection(name="production", volume=30_500)
    # beat.export_selection(name="03_prod", volume=30_500)


