from modules import *

"""
Project L
"""

class Mid(Beat):
    def __init__(self, bpm):
        super().__init__(bpm, path=os.path.join("AMTR", "ost", "02"))

        #   Instruments #


        #   Melody  #
        self.saw = Saw()
        self.synth1 = Acoustic3(amp=0.5, harmonics=12, attack=0.001, attack_max=0.01, decay=0.0, sustain=1.0, release=0.01,
                                # vol_1 = 4.0, vol_2 = 0.3,
                                vol_3 = 1.0, vol_4=0.000000000001,
                                )
        
        self.key1 = Tangible_Light.Bell(amp=0.5, freq_mod=1.5, wave_2 = False, wave_3=False)

        #   Rhythm / Percussion  #
        ##  Bass    ##
        mod = 0.5
        # self.bass1 = Bass_1(amp=1.0, attack=0.005, attack_max = 0.003, freq_mod = mod, sustain=0.3, release= 0.01, amp_final = 0.1, top_freq = 2, harmonics=2)
        # self.bass1 = Acoustic3(amp=0.2,
        #                        freq_mod=1, harmonics=4,
        #                        attack=0.01, attack_max=0.055, decay=0.1, sustain=1.0, release=0.01,
        #                        vol_1=1.0, vol_2=1.0,
        #                        vol_3=1.0, vol_4=1.0,
        #                        vol_5=1.0, vol_6=1.0,
        #                        vol_7=0.0, vol_8=0.0
        #                        )
        self.bass1 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_w1.wav"))
        self.bass2 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_w2.wav"))
        self.bass3 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_w3.wav"))
        self.bassv1 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_v1.wav"))
        self.bassv2 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_v2.wav"))
        self.bassv3 = GlobalSample(0.00003, os.path.join("samples", "project_l", "bass_v3.wav"))
        self.whistle1 = First4(freq_mod=8, wave_1 = False, wave_2 = True, wave_3=False,
                                    sustain = 0.5,
                                    decay=0.1,
                                    attack_3=0.4,
                                    amp_1 = 1.0)

        
        # self.bass1 = Bass_1(amp=1.0, attack=0.01, attack_max = 0.02, freq_mod = 1, sustain=1.0, release= 0.01, amp_final = 0.00000000001, harmonics=3)
        # self.bass2 = Bass_1(amp=1.0, attack=0.003, attack_max = 0.005, freq_mod = mod, sustain=1.0, release= 0.01, amp_final = 0.00000000001, top_freq = 2, harmonics=2)

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

        ##  Kicks   ##
        self.kick1 = Tap4(5.0, attack=0.001, decay = 0.025, sustain=0.0, noise_amount=0.00000)
        self.kick2 = GlobalSample_2(amp=0.00001, file_path=os.path.join("samples", "kick", "new-kick.wav"))


        #   Samples #
        self.go = Go(amp=0.00001 * 1.5)
        self.surprise = Rapping.Surprise(amp=0.00000002)
        self.violin1 = GlobalSample(0.00002, os.path.join("samples", "violin", "violin_1.wav"))
        self.violin2 = GlobalSample(0.00002, os.path.join("samples", "violin", "violin_2.wav"))
        self.violin3 = GlobalSample(0.00002, os.path.join("samples", "violin", "violin_layered.wav"))

        self.ha1 = GlobalSample(0.00003, os.path.join("samples", "has", "ha_1.wav"))
        self.p1 = GlobalSample(0.00003, os.path.join("samples", "piano", "gospel_1.wav"))
        self.p2 = GlobalSample(0.00003, os.path.join("samples", "piano", "note_1.wav"))
        self.p3 = GlobalSample(0.00003, os.path.join("samples", "piano", "gospel_3.wav"))
        self.pf = GlobalSample(0.00003, os.path.join("samples", "piano", "note_f.wav"))
        
        
        self.piano1 = GlobalSample(0.00003, os.path.join("samples", "project_l", "piano_1.wav"))
        self.piano2 = GlobalSample(0.00003, os.path.join("samples", "project_l", "piano_2.wav"))
        
        self.flute1 = GlobalSample(0.00003, os.path.join("samples", "project_l", "flute_1.wav"))
        self.flute2 = GlobalSample(0.00003, os.path.join("samples", "project_l", "flute_2.wav"))

        self.harp1 = GlobalSample(0.00003, os.path.join("samples", "project_l", "harp_1.wav"))
        
        self.instruments = {}


    def get_instruments(self):
        self.instruments = {
            #   Rhythm and Bass #
            'kick1': [self.kick1, self.kicks(self.kick1)],
            'kick2': [self.kick2, self.kicks(self.kick2)],
            'snare1': [self.snare1, self.snares_1()],
            'hats1': [self.hat1, self.hats_1()],
            'hats2': [self.hat2, self.hats_2()],
            'bass1': [self.bass1, self.bass_1()],
            

            #   Melody  #
            # 'saw1': [self.saw, self.saw_1()],


            #   Samples / Libs  #
            'goha': [self.go, self.go_1()],


            #   Tag #
            # 'tag': [self.t, self.tag()],
        }

    def tag(self):
        t = self.t

        v0 = [t.n(self.w)]

        return v0
    
    
    def saw_1(self):
        s = self.saw
        m1 = [
            s.n(D3, self.q + self.e),
            s.n(C3, self.q + self.e),
            s.n(B2, self.q), 
        ]

        m2 = [
            s.n(E2, self.q),
            rest(self.q),
            s.n(B2, self.h),
        ]
            

        v1 = m1 + m2 + m1 + m2

        return v1 + v1
    
    def whistle_1(self):
        w = self.whistle1

        v0 = [rest(self.w*4)]
        
        m1 = [
            w.n(D2, self.q),
            w.n(A2, self.e),
            w.n(G2, self.q),
            w.n(A2, self.q + self.e)
        ]

        m2 = [
            w.n(C2, self.q),
            w.n(A2, self.e),
            w.n(G2, self.q),
            w.n(F2, self.q + self.e)
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v0 + v0 +\
        v1 + v1 +\
        \
        v0 + v0

        
    def harp_1(self):
        h1 = self.harp1

        v0 = [rest(self.w*4)]

        v1 = [h1.n(self.w*4)]
        v2 = v1

        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        v0 + v0 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2
    

    def flute_1(self):
        p1 = self.flute1
        p2 = self.flute2

        v0 = [rest(self.w*4)]

        v1 = [p1.n(self.w*4)]
        v2 = [p2.n(self.w*4)]

        v3 = [
            p1.n(self.w*2),
            rest(self.w),
            p1.n(self.w),
        ]

        v4 = [
            p2.n(self.w*2),
            rest(self.w),
            p2.n(self.w)
        ]

        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        v0 + v0 +\
        \
        v1 + v2 +\
        v3 + v4 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2
    
    def piano_1(self):
        p2 = self.piano2

        v0 = [rest(self.w*4)]
        v1 = [p2.n(self.w*4)]
        v2 = v1

        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        v0 + v0 +\
        \
        v0 + v2 +\
        v1 + v2 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2
    
    def bass_1(self):
        """Bass part 1"""
        b1 = self.bass1
        b2 = self.bass2
        b3 = self.bass3
        bv1 = self.bassv1
        bv2 = self.bassv2
        bv3 = self.bassv3



        v0 = [rest(self.w*4)]
        v1 = [bv1.n(self.w*4)]
        v2 = v1

        v3 = [bv2.n(self.w*4)]

        v4 = [bv3.n(self.w*4)]

        return \
        v0 + v0 +\
        \
        v1 + v2 +\
        v3 + v4 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        v3 + v4 +\
        \
        v1 + v2 +\
        v3 + v4 +\
        \
        v0 + v4 +\
        v0 + v4
        
    def bass_2(self):
        """Bass part 1"""
        b1 = self.bass1
        b2 = self.bass2
        b3 = self.bass3
        bv1 = self.bassv1
        bv2 = self.bassv2
        bv3 = self.bassv3



        v0 = [rest(self.w*4)]
        v1 = [bv1.n(self.w*4)]
        v2 = v1

        v3 = [bv2.n(self.w*4)]

        v4 = [bv3.n(self.w*4)]

        return \
        v0 + v0 +\
        \
        v1 + v2 +\
        v3 + v4 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        v3 + v4 +\
        \
        v1 + v2 +\
        v3 + v4 +\
        \
        v0 + v4 +\
        v0 + v4
    
    def kicks(self, k, amp=1.4):
        """Kick part 1"""

        m1 = [
            k.n(C1, self.q, amp),
            rest(self.e),
            k.n(C1, self.q, amp),
            k.n(C1, self.q, amp),
            rest(self.e)
        ]

        m2 = [
            k.n(C1, self.q, amp),
            rest(self.q),
            k.n(C1, self.e, amp), k.n(C1, self.e, amp),
            rest(self.q)
        ]

        v0 = m1 + m2 + m1 + m2

        m1b = [
            k.n(C1, self.q),
            rest(self.e),
            k.n(C1, self.q),
            k.n(C1, self.q),
            rest(self.e)
        ]

        m2b = [
            k.n(C1, self.q),
            rest(self.q),
            k.n(C1, self.e), k.n(C1, self.e),
            rest(self.q)
        ]

        v1 = m1b + m2b + m1b + m2b
        

        #   Variant 2   #
        v2 = m1b + m1b + m1b + m2b

        m5 = [
            k.n(C1, self.q),
            rest(self.e),
            k.n(C1, self.q),
            rest(self.q),
            rest(self.e)
        ]

        m6 = [
            k.n(C1, self.q),
            rest(self.q),
            k.n(C1, self.q),
            rest(self.q)
        ]
        v3 = m5 + m2 + m1 + m2


        return \
        v0 + v0 +\
        \
        v2 + v1 +\
        v2 + v0 +\
        \
        v2 + v1 +\
        v2 + v1 +\
        v2 + v0 +\
        \
        v1 + v1 +\
        v2 + v0 +\
        \
        v2 + v1 +\
        v2 + v0
        
    
    def snares_1(self):
        """Snare part 1"""
        s = self.snare1

        m1 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.q),
        ]

        m4 = [
            rest(self.q),
            s.n(self.q),
            rest(self.q),
            s.n(self.e), s.n(self.e),
        ]
        v1 = m1 + m1 + m1 + m4

        #   Variant 2   #
        m5 = [
            rest(self.q),
            s.n(self.q),
            rest(self.e),
            s.n(self.q),
            s.n(self.e),
        ]
        v2 = m5 + m1 + m1 + m4

        return \
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1 +\
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1
        

    def hats_1(self):
        h = self.hat2
        
        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.q),
            h.n(self.q),
            rest(self.q),
            h.n(self.q),
        ]

        m2 = [
            rest(self.q),
            h.n(self.q),
            rest(self.e), h.n(self.e),
            rest(self.e), h.n(self.e),
        ]

        v1 = m1 + m2 + m1 + m2

        return \
        v0 + v1 +\
        \
        v1 + v1 +\
        v1 + v1 +\
        \
        v1 + v1 +\
        v1 + v1 +\
        v1 + v1 +\
        \
        v0 + v0 +\
        v0 + v0 +\
        \
        v1 + v1 +\
        v1 + v1
    
    def hats_2(self):
        h = self.hat4
        
        v0 = [rest(self.w*4)]

        m1 = [
            h.n(self.e), h.n(self.e),
            rest(self.q),
            h.n(self.q),
            h.n(self.q),
        ]

        m2 = [
            h.n(self.q),
            h.n(self.q),
            rest(self.q),
            h.n(self.q),
        ]

        m4 = [
            h.n(self.q),
            h.n(self.q),
            rest(self.q),
            h.n(self.s), h.n(self.s), h.n(self.s), h.n(self.s)
        ]

        v1 = m1 + m2 + m1 + m4

        m5 = [
            h.n(self.e), h.n(self.e),
            rest(self.q),
            h.n(self.e), h.n(self.e),
            rest(self.q)
        ]

        m6 = [
            h.n(self.e), rest(self.e),
            rest(self.q),
            h.n(self.e), rest(self.e),
            h.n(self.e), rest(self.s), h.n(self.s) 
        ]

        v2 = m5 + m6 + m5 + m6
        v3 = v2
        return \
        v1 + v2 +\
        \
        v1 + v2 +\
        v1 + v2 +\
        \
        v3 + v2 +\
        v3 + v2 +\
        v3 + v2 +\
        \
        v0 + v0 +\
        v3 + v2 +\
        \
        v3 + v2 +\
        v3 + v2

    def go_1(self):
        """Go sample"""
        g = self.go
        
        v0 = [rest(self.w*4)]

        m1 = [
            rest(self.q),
            g.n(C1, self.q),
            rest(self.q),
            g.n(C1, self.q),
        ]

        m2 = [
            rest(self.q),
            g.n(C1, self.q),
            rest(self.e), g.n(C1, self.e),
            rest(self.e), g.n(C1, self.e - self.s), rest(self.s)
        ]

        v1 = m1 + m2 + m1 + m2
        v2 = v1

        return \
        v0 + v0 +\
        \
        v0 + v0 +\
        v0 + v1 +\
        \
        v0 + v0 +\
        v0 + v0 +\
        v0 + v1 +\
        \
        v0 + v0 +\
        v0 + v2 +\
        \
        v0 + v0 +\
        v0 + v1
    

    def synth_1(self):
        """Synth 1"""
        s = self.key1

        v0 = [rest(self.w*4)]

        m1 = [
            s.n(C4, self.q),
            rest(self.q*3)
        ]

        m2 = [
            s.n(D4, self.q),
            rest(self.q*3)
        ]
        
        m4 = [
            delaycombo(delaycombo(s.n(B3, self.e), s.n(A3, self.e), self.s, silence = False), s.n(G3, self.q)(), self.e, silence = False, array=True),
            rest(self.q),
            rest(self.q),
            rest(self.e),
        ]

        v1 = m1 + m2 + m1 + m4

        return \
        v0 + v0 +\
        v0 + v0 +\
        \
        v1 + v1 +\
        v1 + v1
    
    def synth_2(self):
        """Synth 2"""
        s = self.key1

        v0 = [rest(self.w*4)]

        m1 = [
            s.n(C4, self.q),
            rest(self.q*3)
        ]

        m2 = [
            s.n(D4, self.q),
            rest(self.q*3)
        ]
        
        m4 = [
            #   eighth + sixth  #
            delaycombo(delaycombo(s.n(B3, self.e), s.n(A3, self.e), self.s, silence = False), s.n(G3, self.q)(), self.e, silence = False, array=True),
            rest(self.q),
            rest(self.q),
            rest(self.e),
        ]

        v1 = m1 + m2 + m1 + m4

        return \
        v0 + v0 +\
        v0 + v0 +\
        \
        v1 + v1 +\
        v1 + v1
    
def main():
    beat = Mid(152)
    beat.get_instruments()
    # beat.export_selection(name = '02_full')

    drums = {}
    for k in beat.instruments:
        if k == "kick2" or k == "snare1" or k == "hats2":
            drums[k] = beat.instruments[k]
    
    main = {}
    for k in beat.instruments:
        if k != "kick2" and k != "snare1" and k != "hats2":
            main[k] = beat.instruments[k]

    beat.export_selection(drums, "02_drums")
    beat.export_selection(main, "02_main")