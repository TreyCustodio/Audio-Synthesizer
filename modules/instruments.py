"""Given an octave and a measure length,
generate every possible note for each instrument."""

from .audio import *
from .sampler import Sampler
from synthesizer import synthesize, log, exp, lin, bass_harms

class Instrument:
    def __init__(self, octave, measure, func, type=""):
        
        self.func = func
        self.type = type

        coeff = 2 ** (octave - 1)

        #   (1) Sixteenth Notes
        t = measure / 16
        
        self.s_c = func(C1 * coeff, t)
        self.s_cs = func(Cs1 * coeff, t)
        self.s_d = func(D1 * coeff, t)
        self.s_ds = func(Ds1 * coeff, t)
        self.s_e = func(E1 * coeff, t)
        self.s_f = func(F1 * coeff, t)
        self.s_fs = func(Fs1 * coeff, t)
        self.s_g = func(G1 * coeff, t)
        self.s_gs = func(Gs1 * coeff, t)
        self.s_a = func(A1 * coeff, t)
        self.s_as = func(As1 * coeff, t)
        self.s_b = func(B1 * coeff, t)


        #   (2) Eighth Notes
        t = measure / 8

        self.e_c = func(C1 * coeff, t)
        self.e_cs = func(Cs1 * coeff, t)
        self.e_d = func(D1 * coeff, t)
        self.e_ds = func(Ds1 * coeff, t)
        self.e_e = func(E1 * coeff, t)
        self.e_f = func(F1 * coeff, t)
        self.e_fs = func(Fs1 * coeff, t)
        self.e_g = func(G1 * coeff, t)
        self.e_gs = func(Gs1 * coeff, t)
        self.e_a = func(A1 * coeff, t)
        self.e_as = func(As1 * coeff, t)
        self.e_b = func(B1 * coeff, t)

        
        #   (3) Quarter Notes
        t = measure / 4

        self.q_c = func(C1 * coeff, t)
        self.q_cs = func(Cs1 * coeff, t)
        self.q_d = func(D1 * coeff, t)
        self.q_ds = func(Ds1 * coeff, t)
        self.q_e = func(E1 * coeff, t)
        self.q_f = func(F1 * coeff, t)
        self.q_fs = func(Fs1 * coeff, t)
        self.q_g = func(G1 * coeff, t)
        self.q_gs = func(Gs1 * coeff, t)
        self.q_a = func(A1 * coeff, t)
        self.q_as = func(As1 * coeff, t)
        self.q_b = func(B1 * coeff, t)

       
        #   (4) Half Notes
        t = measure / 2

        self.h_c = func(C1 * coeff, t)
        self.h_cs = func(Cs1 * coeff, t)
        self.h_d = func(D1 * coeff, t)
        self.h_ds = func(Ds1 * coeff, t)
        self.h_e = func(E1 * coeff, t)
        self.h_f = func(F1 * coeff, t)
        self.h_fs = func(Fs1 * coeff, t)
        self.h_g = func(G1 * coeff, t)
        self.h_gs = func(Gs1 * coeff, t)
        self.h_a = func(A1 * coeff, t)
        self.h_as = func(As1 * coeff, t)
        self.h_b = func(B1 * coeff, t)
        
        
        #   (5) Trey Notes
        t = (measure / 4) * 3

        self.t_c = func(C1 * coeff, t)
        self.t_cs = func(Cs1 * coeff, t)
        self.t_d = func(D1 * coeff, t)
        self.t_ds = func(Ds1 * coeff, t)
        self.t_e = func(E1 * coeff, t)
        self.t_f = func(F1 * coeff, t)
        self.t_fs = func(Fs1 * coeff, t)
        self.t_g = func(G1 * coeff, t)
        self.t_gs = func(Gs1 * coeff, t)
        self.t_a = func(A1 * coeff, t)
        self.t_as = func(As1 * coeff, t)
        self.t_b = func(B1 * coeff, t)
        
        
        #   (6) Whole Notes
        t = measure

        self.w_c = func(C1 * coeff, t)
        self.w_cs = func(Cs1 * coeff, t)
        self.w_d = func(D1 * coeff, t)
        self.w_ds = func(Ds1 * coeff, t)
        self.w_e = func(E1 * coeff, t)
        self.w_f = func(F1 * coeff, t)
        self.w_fs = func(Fs1 * coeff, t)
        self.w_g = func(G1 * coeff, t)
        self.w_gs = func(Gs1 * coeff, t)
        self.w_a = func(A1 * coeff, t)
        self.w_as = func(As1 * coeff, t)
        self.w_b = func(B1 * coeff, t)

        #   (7) Double Whole Notes
        t = measure * 2

        self.w2_c = func(C1 * coeff, t)
        self.w2_cs = func(Cs1 * coeff, t)
        self.w2_d = func(D1 * coeff, t)
        self.w2_ds = func(Ds1 * coeff, t)
        self.w2_e = func(E1 * coeff, t)
        self.w2_f = func(F1 * coeff, t)
        self.w2_fs = func(Fs1 * coeff, t)
        self.w2_g = func(G1 * coeff, t)
        self.w2_gs = func(Gs1 * coeff, t)
        self.w2_a = func(A1 * coeff, t)
        self.w2_as = func(As1 * coeff, t)
        self.w2_b = func(B1 * coeff, t)

    def getADSR(self):
        return self.a, self.d, self.s, self.r
    
    def create_note(self, frequency, duration):
        """Specify a brand new note with a pitch and duration"""
        return self.func(frequency, duration)
    
    def create_note_octave(self, note, duration, octave):
        coeff = 2 ** (octave - 1)
        return self.func(note * coeff, duration)

    def create_slur(self, pitch1, pitch2, duration, wait):

        sound = slur(pitch1, pitch2, duration, wait)
        a,d,s,r = self.getADSR()

        a *= duration
        d *= duration
        r *= duration

        return envelope(sound, a,d,s,r)

    
    def note(self, pitch: str = "", dur: float = 0.0):
        """Get a note based on a pitch and a duration"""

        return self.func(pitch, dur)

class Hey(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.0
        self.s = 1.0
        self.r = 0.0

        def func(frequency, duration):
            return Sampler.sample(os.path.join("samples", "Navi", "hey.wav"))

        self.func = func

class Bass(Instrument):
    def __init__(self, octave=0, measure=0, type=""):
        self.a = 0.01
        self.d = 0.7
        self.s = 0.75
        self.r = 0.2
        
        def dress(frequency, duration):
            """DressB"""
            #   Synthesizer 1 Parameters  #
            harmonics = 60
            coeff = 2
            freq_func = None #exp(2)
            amp_func = lin(5) #None #exp(6) #log #exp(80) #log
            

            #   Function Call   #
            synth1 = synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            )
            

            """DressD 2 Octaves Higher"""
            #   Synthesizer 2 Parameters  #
            harmonics = 5
            coeff = 1
            freq_func = None #exp(2)
            amp_func = exp(6) #log
            a = 0.001
            d = 0.5
            s = 0.0
            r = 0.0

            #   Function Call   #
            synth2 = synthesize(frequency * 3, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) \
                            + synthesize((frequency / 4) * 3, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) * 0.2


            """Combine em   """
            return synth1 + synth2
        
        self.func = dress

class Skirt(Instrument):
    def __init__(self):
        self.a = 0.01
        self.d = 0.0
        self.s = 0.75
        self.r = 0.01
        
        def func(frequency, duration):
            """Create a skirt sound by combining a metallic, modulated wave with noise"""
            
            #   Generate a time array for the duration of the sound    #
            t = np.linspace(0, duration, int(44100 * duration), endpoint=False)

            #   Create a modulated sine wave and noise   #
            base = frequency * 85
            mod = 120
            mod_index = 0.2

            wave = np.sin(2 * np.pi * base * t + 
                        mod_index * np.sin(2 * np.pi * mod * t))
            
            noise = np.random.normal(0, 0.5, wave.shape) * np.exp(-t * 50)
            

            #   Apply an exponential decay to the wave and noise    #
            wave *= np.exp(-t * 50)
            noise *= np.exp(-t * 50)
            wave += noise


            #   Wrap the wave in an envelope    #
            wave = envelope(wave, self.a, self.d, self.s, self.r)

            return wave
        
        self.func = func
class Funk(Instrument):
    def __init__(self):
        # self.a = 0.0
        # self.d = 0.35
        # self.s = 0.0
        # self.r = 0.0

        self.a = 0.5
        self.d = 0.0
        self.s = 1.0
        self.r = 0.5

        def func(freq, dur):
            
            harmonics = 30
            coeff = 1
            freq_func = None
            amp_func = None


            synth1 = synthesize(freq / 2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 0.25, dur, 0,
                                harmonics, 1, None, None,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 2, dur, 0,
                                harmonics, 1, None, None,
                               self.a, self.d, self.s, self.r) * 0.1 + \
                    synthesize(freq, dur, 0,
                                20, coeff, bass_harms(2), "hold",
                                0.7, 0.0, 1.0, 0.3)
                     

            # t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            # noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
            
            # wave = synth1 + noise

            return synth1
        
        self.func = func

class Deep_Synth(Instrument):
    def __init__(self):
        # self.a = 0.0
        # self.d = 0.35
        # self.s = 0.0
        # self.r = 0.0

        self.a = 0.5
        self.d = 0.0
        self.s = 1.0
        self.r = 0.5

        def func(freq, dur):
            
            harmonics = 30
            coeff = 1
            freq_func = None
            amp_func = None


            synth1 = synthesize(freq / 2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 0.25, dur, 0,
                                harmonics, 1, None, None,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 2, dur, 0,
                                harmonics, 1, None, None,
                               self.a, self.d, self.s, self.r) * 0.1 + \
                    synthesize(freq, dur, 0,
                                20, coeff, bass_harms(2), "hold",
                                0.7, 0.0, 1.0, 0.3)
                     

            # t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            # noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
            
            # wave = synth1 + noise

            return synth1
        
        self.func = func

class Buzz(Instrument):
    def __init__(self):
        # self.a = 0.0
        # self.d = 0.35
        # self.s = 0.0
        # self.r = 0.0

        self.a = 0.5
        self.d = 0.0
        self.s = 1.0
        self.r = 0.5

        def func(freq, dur):
            
            harmonics = 30
            coeff = 1
            freq_func = None
            amp_func = None


            synth1 = synthesize(freq / 2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 0.25, dur, 0,
                                harmonics, 1, None, None,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq * 2, dur, 0,
                                harmonics, 1, None, None,
                               self.a, self.d, self.s, self.r) * 0.1 + \
                    synthesize(freq, dur, 0,
                                50, coeff, freq_func, lin(-1),
                                self.a, self.d, self.s, self.r)
                     

            # t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            # noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
            
            # wave = synth1 + noise

            return synth1
        
        self.func = func

class Tester(Instrument):
    """Do not initialize all the notes upfront"""
    def __init__(self, measure):
        def func(freq, dur):
            self.a = 0.01
            self.d = 0.2
            self.s = 0.5
            self.r = 0.7

            sound = sine_wave(freq, dur)
            sound = envelope(sound, self.a, self.d, self.s, self.r)

            return sound

        self.func = func

    #   Don't call super().__init__

class Template(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.2
        self.d = 0.2
        self.s = 0.8
        self.r = 0.2

        def func(freq, dur):
            
            harmonics = 0
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r)

            return synth1
        
        super().__init__(octave, measure, func, type)


class FirstP(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.0
        self.r = 0.01

        def func(freq, dur):
            return synthesize(freq * 3, dur, 0,
                            10, 1, None, None,
                            0.0, 0.2, 0.0, 0.01)
        

        super().__init__(octave, measure, func, type)




    
    

class FirstF(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.5
        self.d = 0.0
        self.s = 1.0
        self.r = 0.5

        def func(freq, dur):
            
            harmonics = 0
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) + \
                     synthesize(freq / 2, dur, 0,
                                35, 1, None, None,
                                self.a, self.d, self.s, self.r)
                           

            return synth1
        
        super().__init__(octave, measure, func, type)

class First1(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.9
        self.d = 0.0
        self.s = 0.5
        self.r = 0.1

        def func(freq, dur):
            
            harmonics = 0
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) + \
                                synthesize(freq / 6, dur, 0,
                                           20, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r)

            return synth1
        
        super().__init__(octave, measure, func, type)

class First2(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.4

        def func(freq, dur):
            
            harmonics = 20
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01)

            return synth1
        
        self.func = func
        #super().__init__(octave, measure, func, type)

class First3(Instrument):
    def __init__(self, octave, measure=80, type=""):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.4

        def func(freq, dur):
            
            harmonics = 20
            coeff = 1
            freq_func = None
            amp_func = None

            #   First2  #
            synth1 = synthesize(freq, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01)
            
            #   First2, Octave Higher   #
            synth2 = synthesize(freq*2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, 0.0, 1.0, 0.15) * 0.5 + \
                     synthesize(freq*2, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01)

            #   Bass Tones  #
            def dress(frequency, duration):
                a = 0.01
                d = 0.5
                s = 0.75
                r = 0.2
                """DressB"""
                #   Synthesizer 1 Parameters  #
                harmonics = 60
                coeff = 2
                freq_func = None #exp(2)
                amp_func = lin(5) #None #exp(6) #log #exp(80) #log
                

                #   Function Call   #
                synth1 = synthesize(frequency, duration, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                a, d, s, r
                                )
            

                """DressD 2 Octaves Higher"""
                
                #   Synthesizer 2 Parameters  #
                harmonics = 5
                coeff = 1
                freq_func = None #exp(2)
                amp_func = exp(6) #log
                a = 0.001
                d = 0.5
                s = 0.0
                r = 0.0

                #   Function Call   #
                synth2 = synthesize(frequency * 1.5, duration, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                a, d, s, r
                                ) \
                                + synthesize((frequency / 4) * 1.5, duration, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                a, d, s, r
                                ) * 0.2


                """Combine em   """
                return synth1 + synth2
            
            synth3 = dress(freq, dur)
            return synth1 + synth2 + synth3

        self.func = func
        super().__init__(octave, measure, func, type)

class Tank(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.0
        self.d = 0.0
        self.s = 1.0
        self.r = 0.05

        def dress(frequency, duration):
            # return add_waves(envelope(swell(frequency + 300, frequency, duration / 2), 0.0, 0.3, 1.0, 0.2),
            #                  envelope(swell(frequency, frequency + 300, duration / 2), 0.0, 0.3, 1.0, 0.2)
            #                  ) + \
            # return  synthesize(frequency, 
            #                    duration,
            #                    harmonics = 5, freq_func=lin(1), amp_func=lin(2), a=self.a, d=self.d, s=self.s, r=self.r
            #                    ) + \
            base = sine_wave(frequency-200, duration)
            base = envelope(base, 0.0, 0.3 * duration, 0.0, 0.0)

            a = synthesize((frequency - 200), 
                               duration,
                               harmonics = 2, freq_func=lin(2), amp_func=exp(1.5), a=0.0, d=0.3, s=0.0, r=0.0
                               )
            a = distort(a, 2.0)

            b = white_noise(sine_wave(1, duration),0.05)
            b = envelope(b, 0.0, 0.3, 0.0, 0.0)

            a = combine(a, b)
            #a = distort(a, 1.0)
            return a + base
            
            #+ \
                            # synthesize((frequency - 200) * 2, 
                            #    duration,
                            #    harmonics = 0, freq_func=lin(1), amp_func=lin(1), a=0.0, d=0.3, s=0.0, r=0.0
                            #    )
        
                #    synthesize(frequency /4,
                #               duration, 80,
                #               harmonics=40,
                #               coeff=1, freq_func=None, amp_func=lin(2), a=self.a, d=self.d, s=self.s, r=self.r)
        
        super().__init__(octave, measure, dress, type)




class DressF(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.0001
        self.d = 0.3
        self.s = 0.0
        self.r = 0.05

        def dress(frequency, duration):
            return synthesize(frequency, duration, 80, 0, 1, None, lin(2), self.a, self.d, self.s, self.r)
        
        super().__init__(octave, measure, dress, type)


class DressH(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.05
        self.d = 0.1
        self.s = 0.8
        self.r = 0.2

        def dress(frequency, duration):
            return synthesize(frequency, duration, 80, 0, 1, None, lin(2), self.a, self.d, self.s, self.r)
        
        super().__init__(octave, measure, dress, type)

class DressP2(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.001
        self.d = 0.2
        self.s = 0.7
        self.r = 0.01

        
        
        def dressD(frequency, duration):
            # 0, 0.5, 0.0, 0.0
            a = 0.001
            d = 0.5
            s = 0.0
            r = 0.0

            #   Synthesizer Parameters  #
            harmonics = 5
            coeff = 1
            freq_func = None #exp(2)
            amp_func = exp(6) #log
            

            #   Function Call   #
            return synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) *0.1\
                            + synthesize(frequency / 4, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) * 0.2
        
        def dress(frequency, duration):
            return synthesize(frequency, duration, 80, 0, 1, None, None, self.a, self.d, self.s, self.r) #+ dressD(frequency, duration)
        
        
        
        super().__init__(octave, measure, dress, type)

class Dress(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.01
        self.d = 0.7
        self.s = 0.2
        self.r = 0.2
        
        def dress(frequency, duration):

            #   Synthesizer Parameters  #
            harmonics = 5
            coeff = 1
            freq_func = None #exp(2)
            amp_func = exp(6) #log
            

            #   Function Call   #
            return synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            ) \
                            + synthesize(frequency / 4, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            ) * 0.2
    
        super().__init__(octave, measure, dress, type)


    def getADSR(self):
        return self.a, self.d, self.s, self.r
    

class DressD(Instrument):
    def __init__(self, octave, measure, type=""):
        # 0, 0.5, 0.0, 0.0
        self.a = 0.001
        self.d = 0.5
        self.s = 0.0
        self.r = 0.0
        
        def dress(frequency, duration):

            #   Synthesizer Parameters  #
            harmonics = 5
            coeff = 1
            freq_func = None #exp(2)
            amp_func = exp(6) #log
            

            #   Function Call   #
            return synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            ) \
                            + synthesize(frequency / 4, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            ) * 0.2
    
        super().__init__(octave, measure, dress, type)


    def getADSR(self):
        return self.a, self.d, self.s, self.r
    

class DressP(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.1
        self.d = 0.2
        self.s = 0.75
        self.r = 0.1
        
        def dress(frequency, duration):

            #   Synthesizer Parameters  #
            harmonics = 0
            coeff = 6
            freq_func = None
            amp_func = exp(4)# None #lin(2.5) #None #exp(6) #log #exp(80) #log
            

            #   Function Call   #
            return synthesize(frequency, duration, 80,
                            1, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            ) + \
                            synthesize(frequency / 3, duration, 80,
                                                20, coeff,
                                                None, lin(4),
                                                0.01, 0.2, self.s, 0.7
                                                )
        
        super().__init__(octave, measure, dress, type)


    def getADSR(self):
        return self.a, self.d, self.s, self.r
    
class DressB(Instrument):
    def __init__(self, octave, measure, type=""):
        self.a = 0.01
        self.d = 0.7
        self.s = 0.75
        self.r = 0.2
        
        def dress(frequency, duration):
            
            """Synth 1"""
            #   Synthesizer 1 Parameters  #
            harmonics = 60
            coeff = 2
            freq_func = None #exp(2)
            amp_func = lin(5) #None #exp(6) #log #exp(80) #log
            

            #   Function Call   #
            synth1 = synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            )
            

            return synth1
        
        super().__init__(octave, measure, dress, type)


    def getADSR(self):
        return self.a, self.d, self.s, self.r
    

class DressDB(Instrument):
    """DressB + DressD 2 Octaves higher"""

    def __init__(self, octave, measure, type=""):
        self.a = 0.01
        self.d = 0.7
        self.s = 0.75
        self.r = 0.2
        
        def dress(frequency, duration):
            
            """DressB"""
            #   Synthesizer 1 Parameters  #
            harmonics = 60
            coeff = 2
            freq_func = None #exp(2)
            amp_func = lin(5) #None #exp(6) #log #exp(80) #log
            

            #   Function Call   #
            synth1 = synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r
                            )
            

            """DressD 2 Octaves Higher"""
            
            #   Synthesizer 2 Parameters  #
            harmonics = 5
            coeff = 1
            freq_func = None #exp(2)
            amp_func = exp(6) #log
            a = 0.001
            d = 0.5
            s = 0.0
            r = 0.0

            #   Function Call   #
            synth2 = synthesize(frequency * 3, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) \
                            + synthesize((frequency / 4) * 3, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            a, d, s, r
                            ) * 0.2


            """Combine em   """
            return synth1 + synth2
        
        super().__init__(octave, measure, dress, type)


    def getADSR(self):
        return self.a, self.d, self.s, self.r
    
class Chime(Instrument):
    def __init__(self, octave, measure, type=""):
        def chime(frequency, duration):
            
            harmonics = 5
            coeff = 1
            freq_func = exp(2)
            amp_func = log

            return synthesize(frequency, duration, 80,
                            harmonics, coeff,
                            freq_func, amp_func
                            )

        super().__init__(octave, measure, chime, type)


class Weeknd(Instrument):
    def __init__(self, octave, measure, type=""):
        super().__init__(octave, measure, weeknd, type)


class Piano(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, piano2, type)
        else:
            super().__init__(octave, measure, piano, type)

class PianoBass(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, pianobass2, type)
        elif type == "3":
            super().__init__(octave, measure, pianobass3, type)
        elif type == "4":
            super().__init__(octave, measure, pianobass4, type)
        else:
            super().__init__(octave, measure, pianobass, type)

    def getADSR(self):
            if self.type == "3":
                return 0.005, 0.8, 0.1, 0.05
            
class PianoTreble(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, pianotreble2)
        else:
            super().__init__(octave, measure, pianotreble, type)


class Synth(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "up":
            super().__init__(octave, measure, slurrysynth_up)
            
        elif type == "down":
            super().__init__(octave, measure, slurrysynth_down)
        
        else:
            super().__init__(octave, measure, synth)

class SpaceSynth(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "bass":
            super().__init__(octave, measure, space_synth_bass)
        else:
            super().__init__(octave, measure, space_synth)

class Dreamy(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, dream)

class Snare(Instrument):
    def __init__(self, octave, measure, typ=""):
        if typ == "2":
            super().__init__(octave, measure, snare2)
        else:
            super().__init__(octave, measure, snare)

class Pluck(Instrument):
    def __init__(self, octave, measure, type="base"):
        if type == "2":
            super().__init__(octave, measure, pluck2)
        elif type == "3":
            super().__init__(octave, measure, pluck3)

        elif type == "4":
            super().__init__(octave, measure, pluck4)
            
        else:
            super().__init__(octave, measure, pluck)

class Percussion(Instrument):
    def __init__(self, octave, measure, type=""):
        super().__init__(octave, measure, percussion)

class Xylo(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, xylo)

class XyloTech(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, xylotech2)
        else:
            super().__init__(octave, measure, xylotech)

class XyloHorn(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, xylohorn2)
        else:
            super().__init__(octave, measure, xylohorn)

class XyloBass(Instrument):
    def __init__(self, octave, measure, type=""):
        if type == "2":
            super().__init__(octave, measure, xylobass2)
        else:
            super().__init__(octave, measure, xylobass)

# class Bass(Instrument):
#     def __init__(self, octave, measure, type=""):
#         if type == "h":
#             super().__init__(octave, measure, bassh)
#         else:
#             super().__init__(octave, measure, bass)


class Symbol(Instrument):
    def __init__(self, octave, measure, type = ""):
        super().__init__(octave, measure, symbol)

# class Skirt(Instrument):
#     def __init__(self, octave, measure):
#         super().__init__(octave, measure, skirt)

# class Skirt2(Instrument):
#     def __init__(self, octave, measure):
#         super().__init__(octave, measure, skirt2)