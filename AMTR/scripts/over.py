from modules.beat import *
from modules.instruments import *
from modules.audio import *


class O4(Beat):
    def __init__(self, bpm):
        """Hardcoded beat; not optimized for use in the editor"""
        
        
        """
        (1) Fix Bass -- sounds off
        (2) Make melody 1 octave higher for intro
        """
        
        super().__init__(bpm, path = os.path.join("AMTR", "ost", "08"))
        
        #   Bass    #
        self.bass1 = Bass_1(amp=0.3, attack=0.01, attack_max = 0.02, freq_mod = 1, sustain=1.0, release= 0.01, amp_final = 0.00000000001, harmonics=3)
        # self.bass1 = LowSynth(amp=2.0, freq_mod=2)


        #   Plucky, Accoustic Synths   #
        mod = 4
        mod2 = 2
        self.acou1 = Acoustic1(amp=0.6, freq_mod=mod2)
        self.acou2 = Acoustic2(amp=0.4, freq_mod=mod2)
        self.acou3 = Acoustic2(amp=0.1, freq_mod=mod)

        #   Supporting Synths  #
        self.synth1 = Plucky(octave_shift=mod2)
        self.synth2 = Plucky(amp=0.3, octave_shift=mod)

        #   Melody Synths   #
        self.synth3 = DontTell3(amp=0.75, freq_mod=3, attack=0.02)
        self.synth4 = DontTell3(amp=0.75, freq_mod=4, attack=0.02)


        #   Drums   #
        self.tap1 = Tap3(attack=10, amp=0.5) # clap
        self.tap2 = Tap3(attack=100, amp=0.3)

        self.hat1 = Hi_Hat(amp=2.0)
        self.chime1 = Snare(attack=3)



        #   Percussion  #
        ##  Kicks
        self.kick1 = Nine_Sample(amp=0.00007, name="kick-electro01.wav")

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

        self.snare_lof = Nine_Sample(name="snare-lofi01.wav")

        ##  Tom
        self.tom1 = Nine_Sample(name="tom-rototom.wav")


        #   Additional Samples
        self.hoy = GlobalSample(0.00004, os.path.join("samples", "vocals", "phonk-vocal-fx-wet-shot.wav"))
        self.midi_full = GlobalSample(0.00015, os.path.join("samples", "AMTR", "08_midi.wav"))


        
    def get_instruments(self):
        #   Instrument Dictionary   #
        self.instruments = {

            #   Bass    #
            0: [self.bass1, self.bass()],

            #   Accoustics  #
            1: [self.acou1, self.acoustic_1()],
            2: [self.acou2, self.acoustic_2()],
            3: [self.acou3, self.acoustic_3()],

            

            #   Percussion
            'hat': [self.hat1, self.hat_1()],

            'snare1': [self.hat1, self.snare_1()],
            'snare2': [self.hat1, self.snare_2()],

            'lofi snare': [self.hat1, self.snare_lofi()],

            'kick': [self.hat1, self.kick_1()],

            'crash': [self.hat1, self.crash()],

            #   Samples #
            # 'vocal': [self.hoy, self.vocals()],

            #   MIDI    #
            'midi': [None, self.midi()]
        }
        
    def acoustic_1(self):
        s = self.acou1

        m1 = [
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.e), s.n(D3, self.e), 
        ]

        m2 = [
            s.n(D3, self.q),
            s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.q - self.s),
            s.n(D3, self.s), s.n(D3, self.s), s.n(D3, self.s),
            s.n(D3, self.e), s.n(D3, self.e), 
        ]
        
        m3 = [
            s.n(C3, self.e + self.s), s.n(C3, self.s), s.n(C3, self.s), # 1
            s.n(C3, self.s), s.n(C3, self.e + self.s), # 2.25
            s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.s), s.n(C3, self.e), # 3.5
            s.n(C3, self.e), 
        ]


        v1 = m1 + m2 + m3 + m3

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    
    def acoustic_2(self):
        s = self.acou2

        m1 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h),
            rest(self.e)
        ]

        m2 = [
            s.n(B2, self.q),
            rest(self.e),
            s.n(B2, self.h),
            rest(self.e)
        ]

        m3 = [
            s.n(A2, self.q),
            rest(self.e),
            s.n(A2, self.h + self.e),

        ]

        m4 = [
            s.n(A2, self.q),
            rest(self.e),
            s.n(A2, self.h + self.e),

        ]
           

        v1 = m1 + m2 + m3 + m4

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1
    
    def acoustic_3(self):
        s = self.acou3
  
        # m1 = [
        #     s.n(D4, self.e + self.s), s.n(A3, self.s), s.n(A3, self.s), # 1
        #     s.n(A3, self.s), s.n(D4, self.e + self.s), # 2.25
        #     s.n(A3, self.s), s.n(A3, self.s), s.n(A3, self.s), s.n(D4, self.e), # 3.5
        #     s.n(A3, self.e),

        # ]

        # m2 = [
        #     s.n(C4, self.e + self.s), s.n(G3, self.s), s.n(G3, self.s), # 1
        #     s.n(G3, self.s), s.n(C4, self.e + self.s), # 2.25
        #     s.n(G3, self.s), s.n(G3, self.s), s.n(G3, self.s), s.n(C4, self.e), # 3.5
        #     s.n(G3, self.e),
        # ]

        # m1 = [
        #     s.n(D4, self.e), 
        #     rest(self.q),
        #     s.n(D4, self.e), # 2.25
        #     rest(self.q),
        #     s.n(D4, self.e), # 3.5
        #     rest(self.e)
        # ]

        # m2 = [
        #     s.n(C4, self.e),
        #     rest(self.q),
        #     s.n(C4, self.e), # 2.25
        #     rest(self.q),
        #     s.n(C4, self.e), # 3.5
        #     rest(self.e)
        # ]

        m1 = [
            s.n(D4, self.e), 
            s.n(A3, self.e),

            rest(self.e),
            s.n(D4, self.e),

            s.n(A3, self.e),
            rest(self.e),

            s.n(D4, self.e), # 3.5
            s.n(A3, self.e),
        ]

        m2 = [
            s.n(C4, self.e), 
            s.n(G3, self.e),

            rest(self.e),
            s.n(C4, self.e),

            s.n(G3, self.e),
            rest(self.e),

            s.n(C4, self.e), # 3.5
            s.n(G3, self.e),
        ]

        m3 = [
        ]

        m4 = [
        ]
      

        v1 = m1 + m1 + m2 + m2

        return \
            v1 +\
            v1 +\
            v1 +\
            v1 +\
            \
            \
            v1 +\
            v1 +\
            \
            v1 +\
            v1

    def midi(self, verse = "full"):
        m = self.midi_full
        
        if verse == "intro":
            return [m.n(self.w*4)]

        elif verse == "main":
            return [m.n(self.w*40, start_time=self.w*4)]
        
        return \
        [m.n(self.w*40)]
    
    """
    Deprecated instruments
    """
    def melody_1(self):
        s = self.synth3

        #   Intro 4-bar #
        v0 = [
            rest(self.w*3),
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]

        #   V1  #
        m1 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(E3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m2 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), 
            s.n(G3, self.e + self.s),
        ]

        m3 = [
            s.n(E3, self.w)
        ]

        m4 = [
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]
    
        v1 = m1 + m2 + m3 + m4


        #   V2  #
        m5 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m6 = [
            s.n(F3, self.e), s.n(D3, self.e),
            s.n(F3, self.s), s.n(D3, self.e), # 1.75
            s.n(A3, self.e), s.n(G3, self.e), # 2.75
            s.n(F3, self.e), s.n(G3, self.e +self.s)# 3.25
        ]

        m7 = [
            s.n(E3, self.w),
        ]

        m8 = [
            rest(self.whole - self.s*3),
            s.n(A3, self.s), s.n(A3, self.s), s.n(A3, self.s),
        ]

        v2 = m5 + m6 + m7 + m8


        #   V3  #
        ##  When I'm alone with you
        m9 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e),
            rest(self.t - self.s*2),
            s.n(G3, self.s)
        ]

        ##  My life becomes true--no, no, no body else.
        m10 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e), # 1.25
            s.n(B3, self.q), # 2.25

            ## no, no
            s.n(B3, self.e), s.n(B3, self.e), # 3.25
            s.n(B3, self.e + self.s),
        ]

        m11 = [
            s.n(A3, self.e), s.n(G3, self.s),
            s.n(E3, self.e), # 1.25
            rest(self.t - self.s*2),
            s.n(E3, self.s),
        ]

        m12 = [
            s.n(B3, self.e), s.n(B3, self.s), s.n(A3, self.e), # 1.25
            s.n(G3, self.e), # 1.75
            s.n(E3, self.e), # 2.25
            rest(self.s+ self.e + self.q)
        ]

        v3 = m9 + m10 + m11 + m12

        #   H1 (Hook 1) #
        m13 = [
            s.n(F3, self.e), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m14 = [
            s.n(E3, self.s), s.n(F3, self.s), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m15 = [
            s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h)
        ]

        m16 = [
            s.n(E3, self.s), s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h - self.s)
        ]

        return\
        v0 +\
        v1 +\
        v2 +\
        v3 +\
        \
        \
        v1 +\
        v2
    
    def melody_2(self):
        s = self.synth4

        #   Intro 4-bar #
        v0 = [
            rest(self.w*3),
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]

        #   V1  #
        m1 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(E3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m2 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), 
            s.n(G3, self.e + self.s),
        ]

        m3 = [
            s.n(E3, self.w)
        ]

        m4 = [
            rest(self.w - self.s),
            s.n(A3, self.s),
        ]
    
        v1 = m1 + m2 + m3 + m4


        #   V2  #
        m5 = [
            s.n(B3, self.e), s.n(B3, self.s),
            s.n(A3, self.e), s.n(G3, self.e),
            s.n(F3, self.e), s.n(D3, self.e), 
            s.n(D3, self.e), rest(self.s*3)
        ]

        m6 = [
            s.n(F3, self.e), s.n(D3, self.e),
            s.n(F3, self.s), s.n(D3, self.e), # 1.75
            s.n(A3, self.e), s.n(G3, self.e), # 2.75
            s.n(F3, self.e), s.n(G3, self.e +self.s)# 3.25
        ]

        m7 = [
            s.n(E3, self.w),
        ]

        m8 = [
            rest(self.whole - self.s*3),
            s.n(A3, self.s), s.n(A3, self.s), s.n(A3, self.s),
        ]

        v2 = m5 + m6 + m7 + m8


        #   V3  #
        ##  When I'm alone with you
        m9 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e),
            rest(self.t - self.s*2),
            s.n(G3, self.s)
        ]

        ##  My life becomes true--no, no, no body else.
        m10 = [
            s.n(A3, self.e), s.n(B3, self.s), s.n(B3, self.e), # 1.25
            s.n(B3, self.q), # 2.25

            ## no, no
            s.n(B3, self.e), s.n(B3, self.e), # 3.25
            s.n(B3, self.e + self.s),
        ]

        m11 = [
            s.n(A3, self.e), s.n(G3, self.s),
            s.n(E3, self.e), # 1.25
            rest(self.t - self.s*2),
            s.n(E3, self.s),
        ]

        m12 = [
            s.n(B3, self.e), s.n(B3, self.s), s.n(A3, self.e), # 1.25
            s.n(G3, self.e), # 1.75
            s.n(E3, self.e), # 2.25
            rest(self.s+ self.e + self.q)
        ]

        v3 = m9 + m10 + m11 + m12

        #   H1 (Hook 1) #
        m13 = [
            s.n(F3, self.e), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m14 = [
            s.n(E3, self.s), s.n(F3, self.s), s.n(G3, self.e),
            s.n(G3, self.q),
            rest(self.h),
        ]

        m15 = [
            s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h)
        ]

        m16 = [
            s.n(E3, self.s), s.n(B3, self.e), s.n(G3, self.q),
            rest(self.h - self.s)
        ]

        return\
        v0 +\
        v1 +\
        v2 +\
        v3 +\
        \
        \
        v1 +\
        v2
    
    def synth_1(self):
        """Main Melody after break"""
        s = self.synth3

        m1 = [
            s.n(A3, self.e), rest(self.e),
            s.n(D3, self.e), rest(self.e),
            rest(self.e), s.n(D3, self.e), 
            s.n(A3, self.e), rest(self.e)
        ]

        m2 = [
            s.n(D3, self.e), s.n(D3, self.s),
            s.n(A3, self.e), s.n(A3, self.s),
            s.n(D3, self.e), rest(self.e),
            s.n(A3, self.e), s.n(D3, self.e),
            rest(self.e)
        ]

        m3 = [
            s.n(G3, self.e), s.n(C3, self.e),
            rest(self.e), rest(self.e),
             rest(self.e), s.n(C3, self.e),
            s.n(G3, self.e), rest(self.e),
            
        ]

        m4 = [
            s.n(C3, self.e), s.n(C3, self.s), # 0.75
            s.n(G3, self.e), s.n(G3, self.s), # 1.5

            s.n(C3, self.e), rest(self.e), # 2.5
            s.n(G3, self.e), # 3
            s.n(C3, self.e), s.n(F3, self.e), 
        ]


        v1 = m1 + m2 + m3 + m4
        off_verse = [rest(self.whole*4)]

        return \
            off_verse +\
            off_verse +\
            off_verse +\
            off_verse +\
            \
            \
            off_verse +\
            off_verse +\
            \
            v1 +\
            v1
    
    def synth_2(self):
        s = self.synth2

        m1 = [
            rest(self.w)
        ]

        m2 = [
            rest(self.w)

        ]

        m3 = [
            rest(self.w)

            
        ]

        m4 = [
            rest(self.w - self.e*3),
            s.n(F3, self.e) + s.n(C3, self.e), 
            s.n(A3, self.e) + s.n(C3, self.e), rest(self.e)
        ]


        v1 = m1 + m2 + m3 + m4
        off_verse = [rest(self.whole*4)]

        return \
            off_verse +\
            off_verse +\
            off_verse +\
            off_verse +\
            \
            \
            off_verse +\
            off_verse +\
            \
            v1 +\
            v1
    """
    End of deprecated instruments section
    """

    def bass(self):
        """Bass melody"""
        b = self.bass1
        m1 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            b.n(D2, self.h + self.e),
        ]

        m2 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            b.n(A1, self.h + self.e),
        ]

        m3 = [
            b.n(D2, self.e), rest(self.s),
            b.n(D2, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(D2, self.e), b.n(D2, self.e),
            rest(self.e)
        ]

        m4 = [
            b.n(A1, self.e), rest(self.s),
            b.n(A1, self.e), rest(self.s), # 1.5
            rest(self.q),
            b.n(A1, self.e), b.n(A1, self.e),
            rest(self.e)
        ]
        off_verse = [rest(self.w*4)]
        v1 = m3 + m3 + m4 + m4

        return \
        off_verse +\
        off_verse +\
        off_verse +\
        off_verse +\
        \
        \
        v1 +\
        v1 +\
        \
        v1 +\
        v1
    
    def vocals(self):
        h = self.hoy

        m0 = [
            rest(self.w)
        ]
        v0 = [rest(self.w*4)]

        m1 = [
            h.n(self.w * 2)
        ]

        v1 = m1 + m0 + m0

        return \
        v0 + v0 + v0 + v0 +\
        v1 + v1 +\
        v0 + v0 + v0 + v0
    
    def hat_1(self):
        h = self.closed1

        m1 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            rest(self.s), rest(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s/2), h.n(self.s/2), h.n(self.s), h.n(self.s), h.n(self.s),
        ]

        m2 = [
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            rest(self.s), rest(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s),
        ]
        v0 = [rest(self.w*4)]

        v1 = m1 + m1 + m2 + m2

        return \
        v1 + v1 + v1 + v1 +\
        v0 + v0 +\
        v1 + v1 + v1 + v1 +\
        v0 + v1
        
    def kick_1(self):
        k = self.kick1

        v0 = [rest(self.w*4)]

        m1 = [
            k.n(self.e), rest(self.s), k.n(self.s),
            rest(self.e), k.n(self.e),
            rest(self.e), rest(self.s), k.n(self.s),
            rest(self.e), k.n(self.e),
        ]

        m2 = [
            k.n(self.e), rest(self.s), k.n(self.s),
            rest(self.e), k.n(self.s), k.n(self.s),
            rest(self.e), rest(self.s), k.n(self.s),
            rest(self.e), k.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v0 + v0 + v0 + v0 +\
        v0 + v0 +\
        v1 + v1 + v1 + v1 +\
        v1 + v1

    def snare_1(self):
        s = self.snare1
        s2 = self.snare2

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.q),
            s.n(self.e), rest(self.e),
            rest(self.q),
            s.n(self.e), rest(self.s), s.n(self.s)
        ]

        m3 = [
            rest(self.q),
            s2.n(self.e), rest(self.e),
            rest(self.q),
            s.n(self.e), rest(self.e)
        ]

        m4 = [
            rest(self.q),
            s2.n(self.e), rest(self.s), s.n(self.s),
            rest(self.q),
            s.n(self.e), s.n(self.e),
        ]


        

        v1 = m1 + m1 + m3 + m4

        return \
        v1 + v1 + v1 + v1 +\
        v0 + v0 +\
        v1 + v1 + v1 + v1 +\
        v1 + v1

    def snare_2(self):
        s = self.snare3

        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.s), s.n(self.s),
            rest(self.q),
        ]

        m2 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            s.n(self.e), rest(self.s), s.n(self.s),
            rest(self.e), s.n(self.e)
        ]

        m3 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            s.n(self.s), s.n(self.s), rest(self.s), s.n(self.s),
            rest(self.e), s.n(self.e),
        ]

        m4 = [
            rest(self.q),
            s.n(self.e), rest(self.s), s.n(self.s),
            rest(self.q),
            s.n(self.e), s.n(self.e),
        ]

        v1 = m1 + m2 + m3 + m2


        m5 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.s), s.n(self.s),
            rest(self.q),
        ]

        m6 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.s), s.n(self.s),
            rest(self.e), s.n(self.e)
        ]

        m7 = [
            rest(self.q),
            rest(self.e), rest(self.e),
            rest(self.s), s.n(self.s), rest(self.s), s.n(self.s),
            rest(self.e), s.n(self.e),
        ]

        v2 = m5 + m6 + m7 + m6

        return \
        v1 + v1 + v1 + v1 +\
        v2 + v2 +\
        v1 + v1 + v1 + v1 +\
        v1 + v1
    
    def snare_lofi(self):
        s = self.snare_lof

        m1 = [
            rest(self.q),
            rest(self.q),
            s.n(self.q),
            rest(self.q),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m1 + m1 + m1

        return \
        v0 + v0 + v0 + v0 +\
        v1 + v1 +\
        v0 + v0 + v0 + v0 +\
        v0 + v0

    def crash(self):
        c = self.crash1

        v0 = [
            rest(self.w*4)
        ]

        m0 = [
            rest(self.w)
        ]

        mi = [
            c.n(self.w, amp=0.1)
        ]
        

        v1 = mi + m0 + m0 + m0
        v2 = m0 + m0 + m0 + mi

        return \
        v1 + v0 + v0 + v0 +\
        v0 + v2 +\
        v0 + v2 + v0 + v2 +\
        v0 + v0

def main():
    beat = O4(90)
    beat.get_instruments()
    
    #   Export Here
    beat.export_selection(name="08_full")
    
    #   Export to AMTR directory
    beat.set_path(os.path.join(os.getcwd(), os.pardir, "AMTR", "ost"))
    beat.export_selection(name="08_main")
