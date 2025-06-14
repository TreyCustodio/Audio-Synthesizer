"""Given an octave and a measure length,
generate every possible note for each instrument."""

from .audio import *
from .sampler import Sampler
from synthesizer import synthesize, log, exp, lin, bass_harms, inv

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

    
    def dynamic(self, pitch, dur, octave):
        coeff = 2 ** (octave - 1)
        return self.loop(pitch * coeff, dur)


    def note(self, pitch: str = "", dur: float = 0.0):
        """Get a note based on a pitch and a duration"""

        return self.func(pitch, dur)


"""
Sound Fonts
"""

class Tangible_Light:

    class Title_Synth(Instrument):
        def __init__(self, amp = 1.0):
            self.a = 0.01
            self.d = 0.2
            self.s = 0.7
            self.r = 0.01


            def func(freq, dur):
                #freq /= 2
                harmonics = 3
                coeff = 1
                freq_func = bass_harms(4)
                amp_func = inv

                #   Treble  #
                # wave1 = synthesize(freq, dur, 80,
                #                 3, coeff,
                #                 exp(2), lin(6),
                #                 0.05, 0.4, 0.5, 0.2)

                wave1 = sine_wave(freq / 2, dur)
                wave1 = envelope(wave1, 
                0.1 * dur, 0.4 * dur, 0.5, 0.2 * dur)

                wave2 = sine_wave(freq, dur)
                wave2 = envelope(wave2, 
                0.0 * dur, 0.6 * dur, 0.0, 0.0 * dur) * 0.4

                wave3 = sine_wave(freq / 2, dur)
                wave3 = envelope(wave3, 
                0.0 * dur, 0.6 * dur, 0.0, 0.0 * dur)

                wave4 = sine_wave(freq * (3 ** 2), dur) / (2 ** 4)
                wave4 = envelope(wave4, 
                0.0 * dur, 0.65 * dur, 0.0, 0.0 * dur) * 0.15
                
                final = mix(
                    wave2,
                    wave3,
                    wave4
                )

                return final * amp
        
            self.func = func
        
    class Title_Bass(Instrument):
        def __init__(self, amp = 1.0, low = 350):
            self.a = 0.1
            self.d = 0.6
            self.s = 0.0
            self.r = 0.0


            def func(freq, dur):
                harmonics = 3
                coeff = 1
                freq_func = bass_harms(4)
                amp_func = inv

                wave1 = sine_wave(freq /2, dur)

                wave2 = sine_wave(freq /4, dur)
                #wave2 = distort(wave2, 2.0)

                wave3 = sine_wave(freq /6, dur)
                #wave3 = distort(wave3, 4.0)


                wave1 = envelope(wave1,
                0.01 * dur, 0.2 * dur, 0.0, 0.0)

                wave2 = envelope(wave2,
                0.01 * dur, 0.6 * dur, 0.0, 0.0)

                wave3 = envelope(wave3,
                0.01 * dur, 0.7 * dur, 0.0, 0.0) * 0.75


                final = mix(wave1, wave2, wave3)

                return final * amp
        
            self.func = func

    class Title_Snare(Instrument):
        def __init__(self):
            self.a = 0.0
            self.d = 0.1
            self.s = 0.7
            self.r = 0.3


            def func(freq, dur):
                t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

                freqs = np.random.uniform(freq, freq / 2, 20)
                
                wave = np.zeros_like(t)
                for freq in freqs:
                    wave += np.sin(2 * np.pi * freq * t)

                wave = white_noise(wave, 0.1)
                wave = wave * np.exp(-t * 5)
                wave = wave / np.max(np.abs(wave))
                return wave * 2.0


                #   Code for a more intense skirt   #
                t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

                harmonics = 0
                coeff = 1
                freq_func = bass_harms(2)
                amp_func = inv

                wave1 = swell(freq, 1, dur * 0.1)
                wave1 = envelope(wave1, self.a * dur * 0.1, self.d* dur * 0.1, self.s, self.r* dur * 0.1)

                wave2 = synthesize(freq, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r)

                
                noise = np.random.normal(0, 0.5, wave2.shape) * np.exp(-t * 50)
                noise *= np.exp(-t * 50)

                #wave2 += noise
                wave1 = combine(wave1, wave2)
                wave1 *= np.exp(-t * 20)

                return wave1
            
            self.func = func

"""
Samples
"""

class Hey(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.0
        self.s = 1.0
        self.r = 0.0

        def func(frequency, duration):
            return Sampler.sample(os.path.join("samples", "Navi", "hey.wav"))

        self.func = func


"""
Percussion and Bass
"""

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

class Skirt2(Instrument):
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
            wave *= np.exp(-t * 70)
            noise *= np.exp(-t * 50)
        
            wave += noise


            #   Wrap the wave in an envelope    #
            wave = envelope(wave, self.a, self.d, self.s, self.r)

            return wave
        
        self.func = func

class HipSkirt(Instrument):
    def __init__(self, attack = 1, amp = 1.0, low = 4000, dist = 6.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3

        def func(freq, dur):
            f = freq
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            # freqs = np.random.uniform(freq*2, freq / 2, 20)
            
            wave = np.zeros_like(t)
            # for freq in freqs:
            #     wave += np.sin(2 * np.pi * freq * t)
            
            wave += np.sin(2 * np.pi * f * 2* t)

            #   Metal   #
            m = swell(f*3, f/2, dur)
            m *= np.exp(-t * 30)
            wave += m

            #   Noise   #
            wave = white_noise(wave, 1.5)
            wave = bitcrush(wave, 2)

            #   Attack  #
            ##  Modify this last attack envelope to create longer or shorter skirts  ##
            if low > 0:
                wave = lowpass(wave, low)
            
            if dist > 0:
                wave = distort(wave, dist)

            wave = wave * np.exp(-t * attack)


            return wave * amp



        self.func = func

class KickBass(Instrument):
    """A kick drum with emphasized base tones"""
    def __init__(self, amp = 1.0, attack = 15, count = 10):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            #   Kick    #
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            wave = np.zeros_like(t)

            ##   Attempt 2   #
            freqs = np.random.uniform(freq, freq /2, count)
            for freq in freqs:
                wave += np.sin(2 * np.pi * freq * t)
            
            wave *= np.exp(-t * attack)

            #   Bass    #
            
            b = synthesize(freq / 4, dur, 80,
                                10, 1,
                                bass_harms(2), None,
                                self.a, self.d, self.s, self.r)

            #wave = combine(wave, b)
            return wave * amp


            ##   Attempt 1   #
            freqs = np.random.uniform(freq * 2, freq, 10)
            freqs_2 = np.random.uniform(freq, freq /2, 10)
            freqs_3 = np.random.uniform(freq / 2, freq / 4, 10)
            
            for freq in freqs:
                wave += np.sin(2 * np.pi * freq * t) * np.exp(-t * 15) * 0.8
            
            for freq in freqs_2:
                wave += np.sin(2 * np.pi * freq * t) * np.exp(-t * 10)
            
            for freq in freqs_3:
                wave += np.sin(2 * np.pi * freq * t) * np.exp(-t * 10)


            wave1 = swell(freq*2, freq, dur) * np.exp(-t * 30)
            wave2 = swell(freq, freq/2, dur) * np.exp(-t * 30)
            wave3 = swell(freq/2, freq/4, dur) * np.exp(-t * 30)
            wave += wave1 + wave2 + wave3

            #   Combine and add final effects   #
            #final = wave * np.exp(-t * attack)
            final = wave

            #final /= np.linalg.norm(final)
            return final * amp

        self.func = func


class Cymbal(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            freqs = np.random.uniform(freq, freq / 4, 20)
            
            wave = np.zeros_like(t)
            for freq in freqs:
                wave += np.sin(2 * np.pi * freq * t)

            wave = white_noise(wave, 1.0)

            wave = wave * np.exp(-t * 5)
            #wave = distort(wave, 0.5)
            #wave = envelope(wave, 0.0, 0.1 * dur, 0.7, 0.3 * dur)

            wave = wave / np.max(np.abs(wave))
            return wave * 2.0


        self.func = func

        
class Snare(Instrument):
        def __init__(self):
            self.a = 0.0
            self.d = 0.1
            self.s = 0.7
            self.r = 0.3


            def func(freq, dur):
                t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

                freqs = np.random.uniform(freq, freq / 2, 20)
                
                wave = np.zeros_like(t)
                for freq in freqs:
                    wave += np.sin(2 * np.pi * freq * t)

                wave = white_noise(wave, 0.1)
                wave = wave * np.exp(-t * 5)
                wave = wave / np.max(np.abs(wave))
                return wave * 2.0


                #   Code for a more intense skirt   #
                t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

                harmonics = 0
                coeff = 1
                freq_func = bass_harms(2)
                amp_func = inv

                wave1 = swell(freq, 1, dur * 0.1)
                wave1 = envelope(wave1, self.a * dur * 0.1, self.d* dur * 0.1, self.s, self.r* dur * 0.1)

                wave2 = synthesize(freq, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r)

                
                noise = np.random.normal(0, 0.5, wave2.shape) * np.exp(-t * 50)
                noise *= np.exp(-t * 50)

                #wave2 += noise
                wave1 = combine(wave1, wave2)
                wave1 *= np.exp(-t * 20)

                return wave1
            
            self.func = func
    
class Bass(Instrument):
    def __init__(self, octave=0, measure=0, type="", amp=1.0):
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
            return (synth1 + synth2) * 2.0 * amp
        
        self.func = dress


class Bass2(Instrument):
    def __init__(self, octave=0, measure=0, type="", amp=1.0):
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
            return (synth1 + synth2) * 2.0 * amp
        
        self.func = dress

"""
Synths and Keyboard Sounds
"""
class Wom(Instrument):
    """The swelling sound heard in "I Wonder" by Kanye West"""
    def __init__(self):
        self.a = 0.6
        self.d = 0.0
        self.s = 1.0
        self.r = 0.4

        def func(freq, dur):
            """40% is the buildup, 60% is the sustain"""

            #   Build-Up    #
            # wave = swell(freq / 2, freq, dur)
            # d = dur
            # wave = envelope(wave, self.a * d, 0.0, 1.0, 0.1*d)
            # return wave

            wave = swell(freq / 2, freq, dur*0.4)
            d = dur*0.4
            wave = envelope(wave, self.a * d, 0.0, 1.0, 0.1*d)
           
            wave3 = sine_wave(freq, dur*0.6)
            d = dur * 0.6
            wave3 = envelope(wave3, 0.1*d, 0.0, 1.0, self.r*d)
            
            wave = add_waves(wave, wave3)



            #   Swell  #
            t = np.linspace(0, dur, int(44100 * dur*0.6), endpoint=False)
            
            # sustain = np.zeros_like(t)
            # for i in range(1, 21):
            #     sustain += swell((freq * i) / 6, (freq*i) / 3, dur*0.6)

            sustain = swell(freq/2, freq, dur*0.6)
            sustain = envelope(sustain, self.a * dur *0.6, 0.0, 1.0, 0.1*dur*0.6)
            sustain *= 0.5

            #   Bass    #
            bass = synthesize(freq / 2, dur, 0,
                              30, 1,
                              bass_harms(2), None,
                              0.0, 0.3, self.s, 0.1)

            #   Release #
            release = sine_wave(freq*2, dur * 0.4)
            release = envelope(release, 0.3*dur*0.2, 0.0, 1.0, 0.7*dur*0.2)

            release2 = sine_wave(freq, dur * 0.4)
            release2 = envelope(release2, 0.3*dur*0.2, 0.0, 1.0, 0.7*dur*0.2)

            release += release2

            #   Final Combination   #
            final = add_waves(sustain, release)
            final = combine(final, bass)

            return final
            
        self.func = func

class Double(Instrument):
    def __init__(self, amp = 1.0):
        self.a = 0.6
        self.d = 0.0
        self.s = 1.0
        self.r = 0.4

        def func(freq, dur):
            """40% is the buildup, 60% is the sustain"""

            #   Wave 1   #
            wave = swell(freq / 2, freq, dur*0.4)
            d = dur*0.4
            wave = envelope(wave, self.a * d, 0.0, 1.0, 0.1*d)
        
            #   Wave 2  #
            wave3 = sine_wave(freq, dur*0.6)
            d = dur * 0.6
            wave3 = envelope(wave3, 0.1*d, 0.0, 1.0, self.r*d)
            
            #   Final Combination   #
            wave = add_waves(wave, wave3)


            return wave * amp
        
        self.func = func

class Dirty_Strings(Instrument):
    def __init__(self, amp = 1.0, bass = 20, bass_amp=1.0, high_bass= 20, metal_amp = 1.0, slur_amp = 1.0, bass_only = False, metal_only = False):
        self.a = 0.2
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            """Code is pretty messy here. Could do some reorganizing of specific return statements.
            Need to remove unnecessary lines.
            Determine which harmonics leave and stay.

            (1) Specific Returns
            (2) Harmonic Tones
                (i) Wave Foundation
                (ii) Metal
                (iii) Slurs
                (iv) Bass
            """
            
            #   Parameters / Metadata   #
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            harmonics = 20
            coeff = 1
            freq_func = bass_harms(2)
            amp_func = inv
            m_amp = 0.5

            
            #   (1) Specific Returns    #
            if bass_only:
                final = np.zeros_like(t)
                bass9 = synthesize(freq * 2, dur, 80,
                            high_bass, coeff,
                            freq_func, amp_func,
                            0.0, 0.6, 0.0, 0.0)
                
                wave2 = synthesize(freq, dur, 80,
                            bass, coeff,
                            freq_func, amp_func,
                            0.0, self.d, self.s, self.r) * m_amp

                wave4 = synthesize(freq/2, dur, 80,
                            bass, coeff,
                            freq_func, amp_func,
                            0.0, self.d, self.s, self.r)
                
                final = combine(final, bass9)
                final = combine(final, wave2)
                final = combine(final, wave4)
                return final * amp

            elif metal_only:
                metal = synthesize(freq*6, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.01, self.d, self.s, self.r) * 0.05

                metal2 = synthesize(freq*9, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.001

                metal3 = synthesize(freq*12, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * (0.005 / 3)

                metal4 = synthesize(freq*15, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * (0.001 /3)

                metal5 = synthesize(freq*18, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * (0.005 / 6)

                metal6 = synthesize(freq*21, dur, 80,
                                harmonics, coeff,
                                bass_harms(2), "hold",
                                self.a, self.d, self.s, self.r) * (0.001 / 6)

                metal7 = synthesize(freq*24, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * (0.005 / 9)

                metal8 = synthesize(freq*27, dur, 80,
                                harmonics, coeff,
                                freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * (0.001 / 9)
                
                metal = combine(metal, metal2)
                metal = combine(metal, metal3)
                metal = combine(metal, metal4)
                metal = combine(metal, metal5)
                metal = combine(metal, metal6)
                metal = combine(metal, metal7)
                metal = combine(metal, metal8)
                metal *= metal_amp

                return metal


            #   (2) Harmonic Tones   #

            ##   Fundamental Tones   #
            wave1 = swell(freq, 1, dur * 0.1) * m_amp

            ###   Experiment with this tone   #
            wave2 = synthesize((freq/2) * 1.5, dur, 80,
                            20, coeff,
                            bass_harms(2), "hold",
                            0.0, 0.8, 0.0, 0.0) #* 20.0
            wave2 += sine_wave((freq/2) * 16, dur) * 0.002
            wave2 *= 10

            ##   Bass Tones  #
            b_amp = 2.0
            wave3 = swell(freq/2, 1, dur * 0.1) * b_amp

            wave4 = synthesize(freq/2, dur, 80,
                            bass, coeff,
                            freq_func, amp_func,
                            0.0, 0.6, 0.0, 0.0) * b_amp
            
            wave3b = swell(freq/4, 1, dur * 0.1) * b_amp * 2

            wave4b = synthesize(freq/4, dur, 80,
                            bass, coeff,
                            freq_func, amp_func,
                            0.1, 0.6, 0.0, 0.0) * b_amp * 2
            
            wave3bb = swell(freq/6, 1, dur * 0.1) * b_amp * 4

            wave4bb = synthesize(freq/6, dur, 80,
                            bass, coeff,
                            freq_func, amp_func,
                            0.1, 0.6, 0.0, 0.0) * b_amp * 4


            ##   High Tone 1  #

            h_amp = 0.2
            wave5 = swell(freq*2, 1, dur * 0.1) * h_amp

            wave6 = synthesize(freq*2, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, self.d, self.s, 0.0) * h_amp


            ##   High Tone 2 #
            wave7 = synthesize(freq*4, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.4, 0.0, 0.0) * 0.08

            wave8 = synthesize(freq*5, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.2, 0.5, 0.0, 0.0) * 0.08
            
            wave7 = combine(wave7, wave8)


            
            waves = np.zeros_like(t)
           # waves = combine(wave1, wave2)

            if bass > 0:
                waves = combine(waves, wave3)
                waves = combine(waves, wave4)
                waves = combine(waves, wave3b)
                waves = combine(waves, wave4b)
                waves = combine(waves, wave3bb)
                waves = combine(waves, wave4bb)


            # waves = combine(waves, wave5)
            # waves = combine(waves, wave6)
            waves = combine(waves, wave7)


            ##   Slurs   #
            s1 = swell(freq * 2, freq, dur) * np.exp(-t * 15) * 1.5

            slurs = np.zeros_like(t)
            slurs = combine(slurs, s1)
            slurs *= slur_amp

            ##   Metal   #
            metal = synthesize(freq*6, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.01, self.d, self.s, self.r) * 0.05

            metal2 = synthesize(freq*9, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * 0.001

            metal3 = synthesize(freq*12, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * (0.005 / 3)

            metal4 = synthesize(freq*15, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * (0.001 /3)

            metal5 = synthesize(freq*18, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * (0.005 / 6)

            metal6 = synthesize(freq*21, dur, 80,
                            harmonics, coeff,
                            bass_harms(2), "hold",
                            self.a, self.d, self.s, self.r) * (0.001 / 6)

            metal7 = synthesize(freq*24, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * (0.005 / 9)

            metal8 = synthesize(freq*27, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r) * (0.001 / 9)
            
            metal = combine(metal, metal2)
            metal = combine(metal, metal3)
            metal = combine(metal, metal4)
            metal = combine(metal, metal5)
            metal = combine(metal, metal6)
            metal = combine(metal, metal7)
            metal = combine(metal, metal8)
            metal *= metal_amp

            ##  Bass Frequencies
            bass1 = synthesize(freq, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.3, 0.0, 0.0) * bass_amp

            bass2 = synthesize(freq / 2, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.3, 0.0, 0.0) * bass_amp
            
            bass3 = synthesize(freq / 3, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.5, 0.0, 0.0) * 0.6 * bass_amp

            bass4 = synthesize(freq / 4, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.5, 0.0, 0.0) * bass_amp

            bass5 = synthesize(freq / 5, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.6, 0.0, 0.0) * 0.6 * bass_amp

            bass6 = synthesize(freq / 6, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.6, 0.0, 0.0) * bass_amp
            
            bass7 = synthesize(freq / 7, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.7, 0.0, 0.0) * 0.6 * bass_amp

            bass8 = synthesize(freq / 8, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            0.0, 0.7, 0.0, 0.0) * bass_amp


            #   Decide if you want the high bass tone to be emphasized or not   #
            bass9 = synthesize(freq * 2, dur, 80,
                            high_bass, coeff,
                            freq_func, amp_func,
                            0.0, 0.6, 0.0, 0.0)




            basses = combine(bass1, bass2)
            # basses = combine(basses, bass3)
            basses = combine(basses, bass4)
            # basses = combine(basses, bass5)
            basses = combine(basses, bass6)
            # basses = combine(basses, bass7)
            basses = combine(basses, bass8)
            basses = combine(basses, bass9)




            #   Final Mix   #

            ##   Wave Foundation   #
            final = np.zeros_like(t)

            final = combine(final, waves)

            ##   Slurs   #
            #final = combine(final, slurs)

            ##   Metallic Tones  #
            final = combine(final, metal)
            
            ##  Bass Tones  #
            #final = combine(final, basses)


            #final = highpass(final, 50)

            return final * amp
        
        self.func = func


class DontMind(Instrument):
    def __init__(self, amp = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))
            n = 0.0
            atk = 10

            atk2 = 15
            dist = 32.0
            dist2 = 32.0

            #   Wave Foundation #
            fundamental = sine_wave(freq / 2, dur)

            wave1 = sine_wave(freq / 2, dur)
            wave1 = distort(wave1, 20)
            wave1 *= np.exp(-t * 10)
            wave1 *= 0.2

            wave2 = sine_wave(freq / 4, dur)
            wave2 = distort(wave2, 6)
            wave2 *= np.exp(-t * 16)
            wave2 *= 0.6

            wave3 = sine_wave(freq / 6, dur)
            wave3 = distort(wave3, 6)
            wave3 *= np.exp(-t * 8)


            final = mix(
            wave1,
            wave2,
            wave3
            )

            return final * amp
        
        self.func = func

class DontTell(Instrument):
    def __init__(self, amp = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))

            #   Wave Foundation #
            fundamental = sine_wave(freq, dur)

            wave1 = fundamental.copy()
            wave1 *= np.exp(-t * 10)



            final = mix(
                wave1
            )

            return final * amp
        
        self.func = func

class Clean_Synth(Instrument):
    def __init__(self, amp = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            harmonics = 20
            coeff = 1
            freq_func = bass_harms(2)
            amp_func = inv

            wave1 = swell(freq, 1, dur * 0.1)

            wave2 = synthesize(freq, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r)

            final = combine(wave1, wave2)

            return final * amp
        
        self.func = func

class Clean_Pluck(Instrument):
    def __init__(self, amp = 1.0):
        self.a = 0.0
        self.d = 0.4
        self.s = 0.0
        self.r = 0.0


        def func(freq, dur):
            harmonics = 20
            coeff = 1
            freq_func = bass_harms(2)
            amp_func = inv

            wave1 = swell(freq, 1, dur * 0.1)

            wave2 = synthesize(freq, dur, 80,
                            harmonics, coeff,
                            freq_func, amp_func,
                            self.a, self.d, self.s, self.r)

            return combine(wave1, wave2) * amp
        
        self.func = func

class Church(Instrument):
    """Church-like ambience"""
    def __init__(self):
        self.a = 0.4
        self.d = 0.1
        self.s = 0.7
        self.r = 0.4

        def func(freq, dur):
            return synthesize(freq, dur, 0,
                              10, 1,
                              bass_harms(2), None,
                              self.a, self.d, self.s, self.r) +\
                    synthesize(freq, dur, 0,
                               10, 1,
                               exp(2), None,
                               self.a, self.d, self.s, self.r)
        
        self.func = func

class Strings(Instrument):
    """WIP String Instrument"""
    def __init__(self):
        self.a = 0.4
        self.d = 0.1
        self.s = 0.7
        self.r = 0.4

        def func(freq, dur):
            return synthesize(freq, dur, 0,
                              10, 1,
                              bass_harms(2), None,
                              self.a, self.d, self.s, self.r) +\
                    synthesize(freq, dur, 0,
                               10, 1,
                               exp(2), None,
                               self.a, self.d, self.s, self.r)
        
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
        
        def loop(freq, dur):
            
            harmonics = 30
            coeff = 1
            freq_func = None
            amp_func = None


            synth1 = synthesize(freq / 2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, 0.0) * 0.5 + \
                     synthesize(freq * 0.25, dur, 0,
                                harmonics, 1, None, None,
                                self.a, self.d, self.s, 0.0) * 0.5 + \
                     synthesize(freq * 2, dur, 0,
                                harmonics, 1, None, None,
                               self.a, self.d, self.s, 0.0) * 0.1 + \
                    synthesize(freq, dur, 0,
                                20, coeff, bass_harms(2), "hold",
                                0.7, 0.0, 1.0, 0.3)
                     

            # t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            # noise = np.random.normal(0, 0.5, len(t)) * np.exp(-t * 50)
            
            # wave = synth1 + noise

            return synth1

        self.func = func
        self.loop = loop

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


# class Pluck(Instrument):
#     def __init__(self)

class FirstP(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.0
        self.r = 0.01

        def func(freq, dur):
            return synthesize(freq * 3, dur, 0,
                            10, 1, None, None,
                            0.0, 0.2, 0.0, 0.01)
        

        self.func = func



    
    

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
    def __init__(self):
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
        
        self.func = func

class First2(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.4

        def func(freq, dur):
            
            harmonics = 20
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq / 4, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5 + \
                     synthesize(freq / 2, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01) * 0.5 +\
                     synthesize(freq, dur, 0,
                                20, coeff, bass_harms(2), "hold",
                                0.7, 0.0, 1.0, 0.3) * 0.4

            return synth1
        
        self.func = func


class First4(Instrument):
    """A mod of First2"""

    def __init__(self):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.4

        def func(freq, dur):
            
            harmonics = 20
            coeff = 1
            freq_func = None
            amp_func = None

            synth1 = synthesize(freq / 4, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5+ \
                     synthesize(freq / 2, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01) * 0.5 +\
                    synthesize(freq / 2, dur, 0,
                               10, 1, bass_harms(2), None,
                               0.4, 0.1, 0.7, 0.01)
                                


            return synth1
        
        self.func = func

class First5(Instrument):
    def __init__(self):
        self.a = 0.4
        self.d = 0.1
        self.s = 0.7
        self.r = 0.01

        def func(freq, dur):
            return synthesize(freq / 2, dur, 0,
                               10, 1, bass_harms(2), None,
                               self.a, self.d, self.s, self.r)

        self.func = func


class First3(Instrument):
    def __init__(self):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.2

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

class Old:
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