"""Given an octave and a measure length,
generate every possible note for each instrument."""

from .audio import *
from .sampler import Sampler
from synthesizer import synthesize, log, exp, lin, bass_harms, inv


class Note:
    """A class that represents a note and allows the user to easily access a note's pitch"""
    def __init__(self, waveform, pitch, amp = 1.0, stereo = False):
        if stereo:
            self.wave = np.column_stack((waveform, waveform)) * amp
        else:
            self.wave = waveform * amp
    
        self.pitch = pitch

    def __call__(self):
        return self.wave
    
    def __str__(self):
        return str(self.wave)
    
    def __repr__(self):
        return str(self.wave)
    
    def __len__(self):
        return len(self.wave)
    
    def __add__(self, other):
        if isinstance(other, Note):
            return self.wave + other.wave
        
        elif isinstance(other, np.ndarray):
            return self.wave + other
        else:
            return NotImplemented
    


class Instrument:
    def __init__(self, octave, measure, func, type="", name="untitled"):
        
        self.func = func
        self.type = type
        self.name = name

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
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return "untitled"
    
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


    def note(self, pitch: str = "", dur: float = 0.0, amp=1.0):
        """Get a note based on a pitch and a duration"""

        return Note(self.func(pitch, dur), pitch, amp)
    
    def n(self, pitch: str = "", dur: float = 0.0, amp=1.0):
        """Get a note based on a pitch and a duration"""

        return self.note(pitch, dur, amp)
    


"""
Sound Fonts
"""
class Rapping:
    class Snare_1(Instrument):
        def __init__(self, amp = 1.0):
            def func(frequency, duration):
                return Sampler.sample(os.path.join("samples", "snares", "snare_1.wav"), duration) * amp

            self.func = func

        def get_name(self):
            return "Rap Snare"
        

    class Hat_1(Instrument):
        def __init__(self, amp = 1.0):
            def func(frequency, duration):
                return Sampler.sample(os.path.join("samples", "hats", "hat_1.wav"), duration) * amp

            self.func = func

        def get_name(self):
            return "Rap Hat"


class Tangible_Light:

    class Title_Synth(Instrument):
        def __init__(self, amp = 1.0, octave_shift = 1):


            def func(freq, dur):
                t = np.linspace(0, dur, int(44100 * dur))
                freq *= octave_shift

                #   Wave Foundation #
                base1 = sine_wave(freq, dur)
                base2 = sine_wave(freq * 2, dur)


                wave1 = envelope(base1,
                                 0.01, dur - 0.01, 0.0, 0.0)
                
                wave2 = envelope(base2,
                                 0.04, dur - 0.04, 0.0, 0.0)
                wave2 *= 0.3

                final = mix(
                    wave1, 
                    wave2
                )

                return final * amp
            
            self.func = func
        
    class Title_Bass(Instrument):
        def __init__(self, amp = 1.0, low = 350, dist = 0.0, freq_mod = 1, punchy=True):
            self.a = 0.1
            self.d = 0.6
            self.s = 0.0
            self.r = 0.0


            def func(freq, dur):
                #   Decide whether to make these punchy or not by modifying atk #

                freq /= freq_mod

                base1 = sine_wave(freq /2, dur)

                base2 = sine_wave(freq, dur)

                base3 = sine_wave(freq * 0.5, dur)

                noise = np.random.normal(0, 0.1, base1.shape) #* np.exp(-t * 50)

                #   (1) Punchy  #
                if punchy:
                    wave1 = envelope(base1,
                    0.005, dur - 0.005, 0.0, 0.0)

                    wave2 = envelope(base2,
                    0.005, dur - 0.005 - 0.01, 0.5, 0.01)

                    wave3 = envelope(base3,
                    0.01, dur - 0.1, 0.3, 0.01)

                #   (2) Longer Atk and Release
                else:
                    wave1 = envelope(base1,
                    0.01, dur - 0.05, 0.0, 0.0)

                    wave2 = envelope(base2,
                    0.05, dur - 0.05 - 0.1, 0.5, 0.1)

                    wave3 = envelope(base3,
                    0.1, dur - 0.2, 0.3, 0.1)


                final = mix(
                    wave1,
                    wave2,
                    wave3
                    )

                if dist > 0.0:
                    final = distort(final, dist)

                return final * amp
        
            self.func = func

        def get_name(self):
            return "TL Bass"
    
    class Boss_Bass(Instrument):
        def __init__(self, amp = 1.0, low = 350, dist = 0.0, freq_mod = 1, punchy=True):
            self.a = 0.1
            self.d = 0.6
            self.s = 0.0
            self.r = 0.0


            def func(freq, dur):
                #   Decide whether to make these punchy or not by modifying atk #

                freq /= freq_mod

                base1 = sine_wave(freq /2, dur)

                base2 = sine_wave(freq, dur)

                base3 = sine_wave(freq * 0.5, dur)

                attacks = np.geomspace(0.05, 0.001, 3)

                wave1 = envelope(base1,
                attacks[0], 0.1, 0.0, 0.01)

                wave2 = envelope(base2,
                attacks[1], 0.1, 0.5, 0.01)

                wave3 = envelope(base3,
                attacks[2], 0.1, 0.3, 0.01)

                final = mix(
                    wave1,
                    wave2,
                    wave3
                    )

                if dist > 0.0:
                    final = distort(final, dist)

                return final * amp
        
            self.func = func

        def get_name(self):
            return "TL Bass"
    
    class Whine(Instrument):
        def __init__(self, amp=1.0, freq_mod = 1, noise_amount=0.0):

            def func(freq, dur):
                t = np.linspace(0, dur, int(44100 * dur))
                freq *= freq_mod

                #   Wave Foundation #
                base1 = sine_wave(freq, dur)
                base2 = sine_wave(freq / 2, dur)
                base3 = sine_wave(freq *2, dur)
            
                wave3 = envelope(base3,
                                0.2, 0.05, 0.4, 0.1) * 0.01
                
                wave1 = envelope(base1,
                                0.1, 0.05, 0.4, 0.1)

                wave2 = envelope(base2,
                                0.02, 0.05, 0.4, 0.1)



                final = mix(
                    wave1, 
                    wave2,
                    wave3
                )

                # geometric_decay(final)
                # final = fade_out(final, 4)

                return final * amp

            
            self.func = func


    class Bell(Instrument):
        def __init__(self, amp=1.0, freq_mod = 1, noise_amount=0.0):

            def func(freq, dur):
                freq *= freq_mod
                base = sine_wave(freq, dur)
                noise = white_noise(base, noise_amount)

                base = mix(
                    base,
                    noise
                )

                
                geometric_decay(base)

                # base = envelope(base,
                #                 0.01, 0.1, 0.3, 0.01
                # )

                return base * amp
            
            self.func = func
            
    class Ice_Synth(Instrument):
        def __init__(self, amp=1.0, sustain=0.1):
            def func(freq, dur):
                base = sine_wave(freq, dur)
                base2 = sine_wave(freq/2, dur)


                wave1 = envelope(base,
                                0.0, 0.05, sustain, 0.01)
                
                wave2 = envelope(base2,
                                0.0, 0.1, 0.5, 0.01)
                
                wave3 = envelope(base,
                                0.1, 0.1, 0.7, 0.01)
                
                final = mix(wave1, wave2, wave3)
                return final
            
            self.func = func

                

    
    
    class Title_String(Instrument):
        def __init__(self, amp = 1.0, dist = 0.0, atk = 5, freq_mod = 1):

            def func(freq, dur):
                freq /= freq_mod

                wave1 = sine_wave(freq, dur)
                wave1 = envelope(
                    wave1,
                    0.5 * dur, 0.0, 1.0, 0.3 * dur
                                 )

                wave2 = sine_wave(freq, dur)
                wave2 = envelope(
                    wave2,
                    0.3 * dur, 0.0, 1.0, 0.5 * dur
                                 )

                wave3 = sine_wave(freq, dur)
                wave3 = envelope(
                    wave3,
                    0.01, 0.2 * dur, 0.0, 0.0
                                 )

                final = mix(
                    wave1,
                    wave2,
                    wave3
                )

                if dist > 0.0:
                    final = distort(final, dist)
                
                final *= amp
                return final
            
            self.func = func

    class Title_Kick(Instrument):
        def __init__(self, amp = 1.0, dist = 0.0, atk = 5):
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

                #wave = white_noise(wave, 0.1)
                wave = wave * np.exp(-t * atk)
                wave = wave / np.max(np.abs(wave))

                return wave * amp





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

                if dist > 0.0:
                    wave1 = distort(wave1, dist)

                return wave1
            
            self.func = func
    
    class Journ(Instrument):

        def __init__(self, amp = 1.0, freq_mod = 1):
            def func(freq, dur):
                freq /= freq_mod
                base = sine_wave(freq, dur)
                base2 = sine_wave(freq*2, dur)
                base3 = sine_wave(freq*4, dur)


                attacks = np.linspace(0.001, dur - (dur/4)-0.1, 3)
                
                wave1 = envelope(base,
                    attacks[0], dur/4, 0.3, 0.1)
                
                wave2 = envelope(base2,
                    attacks[1], dur / 4, 0.3, 0.1) * 0.3
                
                wave3 = envelope(base3,
                    attacks[2], dur / 4, 0.3, 0.1) * 0.01
                
                final = mix(wave1, 
                            wave2,
                            wave3
                            )
                return final * amp
            
            self.func = func

class Horn(Instrument):
    def __init__(self, amp=1.0):
        def func(freq, dur):
            freq *= 2

            t = np.linspace(0, dur, int(SAMPLE_RATE*dur), endpoint=False)
            base = np.zeros_like(t)
            attack=0.01
            base += envelope(sine_wave(freq, dur), attack, dur-attack, 0.0, 0.0)
            return base * amp
            


            harms = 4
            freqs  = np.linspace(freq, freq*6, num=harms)


            amps = np.geomspace(1.0, 0.000001/harms, harms)
            attacks = np.geomspace(0.05, 0.15, harms)

            harms = []
            counter = 0
            for f in freqs:
                harms += [envelope(sine_wave(f, dur), attacks[counter], dur-attacks[counter], 0.0, 0.0) * amps[counter]]
                counter += 1

            # harms[0] *= 1.0
            harms[1] *= 0.0
            harms[2] *= 0.0
            harms[3] *= 0.0
            
            for h in harms:
                base += h

            return base * amp
        
        self.func = func
"""
Samples
"""

class Hey(Instrument):
    def __init__(self, amp=1.0):
        self.a = 0.0
        self.d = 0.0
        self.s = 1.0
        self.r = 0.0

        def func(frequency, duration):
            return Sampler.sample(os.path.join("samples", "Navi", "hey.wav"), duration) * amp

        self.func = func

class Go(Instrument):
    def __init__(self, amp=1.0):
        self.a = 0.0
        self.d = 0.0
        self.s = 1.0
        self.r = 0.0

        def func(frequency, duration):
            return Sampler.sample(os.path.join("samples", "go.wav"), duration) * amp

        self.func = func

class Look(Instrument):
    def __init__(self, amp=1.0):
        def func(frequency, duration):
            return Sampler.sample(os.path.join("samples", "Navi", "look.wav"), duration) * amp

        self.func = func


"""
Plucks
"""

class Acoustic1(Instrument):
    def __init__(self, amp=1.0, freq_mod = 1, dist = 0.0):
        def func(freq, dur):
            freq *= freq_mod

            #   Fundamental Waveforms   #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 1.5, dur)
            base3 = sine_wave(freq * 1.75, dur)
            base4 = sine_wave(freq * 2, dur)
            base5 = sine_wave(freq * 4, dur)



            bass1 = sine_wave(freq / 1.5, dur)
            met1 = sine_wave(freq*9, dur)


            #   Apply envelopes to fundamental waves    #
            # fain = synthesize(
            #     freq, dur, 0,
            #     10, 1, None, None,

            # )


            wave1 = envelope(base1,
                             0.02, 0.1, 0.1, 0.001) * 0.1
            
            
            wave2 = envelope(base2,
                             0.04, 0.1, 0.1, 0.001) * 0.3

            
            wave3 = envelope(base4,
                             0.06, 0.1, 0.1, 0.001) * 0.01
            
            
            
            #   Mix the final sound together    #
            final = mix(
                wave1,
                wave2,
                wave3,
            )

            final = fade_out(final, 6)

            # final = lowpass(final, 500)
            #   Apply the amp and return the wave   #
            if dist > 0:
                final = distort(final, dist)
            return final * amp
        
        self.func = func


class Acoustic2(Instrument):
    def __init__(self, amp=1.0, freq_mod = 1, dist = 0.0):
        def func(freq, dur):
            freq *= freq_mod

            #   Fundamental Waveforms   #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 1.5, dur)
            base3 = sine_wave(freq * 1.75, dur)
            base4 = sine_wave(freq * 3, dur)
            base5 = sine_wave(freq * 4, dur)



            bass1 = sine_wave(freq / 1.5, dur)
            met1 = sine_wave(freq*9, dur)


            #   Apply envelopes to fundamental waves    #
            # fain = synthesize(
            #     freq, dur, 0,
            #     10, 1, None, None,

            # )


            wave1 = envelope(base1,
                             0.01, 0.15, 0.1, 0.05)
            
            
            wave2 = envelope(base2,
                             0.03, 0.15, 0.1, 0.05)* 0.3

            
            wave3 = envelope(base3,
                             0.0155, 0.15, 0.1, 0.05)
            
            wave4 = envelope(base4,
                             0.033, 0.15, 0.1, 0.05) * 0.05
            
            wave5 = envelope(base5,
                             0.044, 0.15, 0.1, 0.05) * 0.01
            
            
            
            #   Mix the final sound together    #
            final = mix(
                wave1,
                wave2,
                # wave4

            )

            final = fade_out(final, 4)

            #   Apply the amp and return the wave   #
            if dist > 0:
                final = distort(final, dist)
            return final * amp
        
        self.func = func

class Acoustic3(Instrument):
    def __init__(self, amp=1.0, freq_mod = 1, dist = 0.0,
                 attack = 0.02, decay = 0.1, sustain = 0.1, release = 0.01,
                 harmonics = 4,
                 vol_1 = 0.0, vol_2 = 0.0, vol_3 = 0.0, vol_4 = 0.0, vol_5 = 0.0, vol_6 = 0.0, vol_7 = 0.0, vol_8 = 0.0):
        def func(freq, dur):
            freq *= freq_mod

            #   Fundamental Waveforms   #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 1.5, dur)
            base3 = sine_wave(freq * 1.75, dur)
            base4 = sine_wave(freq * 2, dur)
            base5 = sine_wave(freq * 4, dur)



            bass1 = sine_wave(freq / 1.5, dur)
            met1 = sine_wave(freq*9, dur)


            #   Apply envelopes to fundamental waves    #
            # fain = synthesize(
            #     freq, dur, 0,
            #     10, 1, None, None,

            # )
            attacks = np.geomspace(attack, 0.1, harmonics)
            freqs = np.linspace(freq, freq*harmonics, harmonics)

            t = np.linspace(0, dur, int(SAMPLE_RATE*dur), endpoint=False)
            final = np.zeros_like(t)

            length = len(freqs)
            quart = harmonics // 4

            #   Replace     #
            if vol_1 == 0 and vol_2 == 0:
                amps_1 = []
                for i in range(quart):
                    amps_1 += [0.0]
            else:
                amps_1 = np.geomspace(vol_1, vol_2, quart)
            
            if vol_3 == 0 and vol_4 == 0:
                amps_2 = []
                for i in range(quart):
                    amps_2 += [0.0]
            else:
                amps_2 = np.geomspace(vol_3, vol_4, quart)

            if vol_5 == 0 and vol_6 == 0:
                amps_3 = []
                for i in range(quart):
                    amps_3 += [0.0]
            else:
                amps_3 = np.geomspace(vol_5, vol_6, quart)

            if vol_7 == 0 and vol_8 == 0:
                amps_4 = []
                for i in range(quart):
                    amps_4 += [0.0]

            else:
                amps_4 = np.geomspace(vol_7, vol_8, quart)
            
            amps = np.append(amps_1, amps_2)
            amps = np.append(amps, amps_3)
            amps = np.append(amps, amps_4)

            count = 0
            for f in freqs:
                final += envelope(sine_wave(f, dur),
                                  attacks[count], decay, sustain, release) * amps[count]
                count += 1

            # wave1 = envelope(base1,
            #                  attack, 0.1, sustain, 0.001) * 0.1
            
            
            # wave2 = envelope(base2,
            #                  attack + 0.02, 0.1, sustain, 0.001) * 0.3

            
            # wave3 = envelope(base4,
            #                  attack + 0.04, 0.1, sustain, 0.001) * 0.01
            
            
            
            #   Mix the final sound together    #
            # final = mix(
            #     wave1,
            #     wave2,
            #     wave3,
            # )

            # final = fade_out(final, 6)

            # final = lowpass(final, 500)
            #   Apply the amp and return the wave   #
            if dist > 0:
                final = distort(final, dist)
            return final * amp

        self.func = func

    def note(self, pitch, dur, amp = 1.0, fade = False):
        if fade:
            return Note(fade_out(self.func(pitch, dur), 12), pitch, amp)
        
        else:
            return super().note(pitch, dur, amp)
    
    def n(self, pitch, dur, amp = 1.0, fade = False):
        return self.note(pitch, dur, amp, fade)
# class Acoustic4(Instrument):

"""
Percussion and Bass
"""
class Tap(Instrument):
    """A simple, percussive wave defined by an attack value"""
    def __init__(self, amp = 1.0, atk = 90, dist=0.0):

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            base = sine_wave(freq, dur)

            wave1 = base * np.exp(-t * atk)

            final = mix(wave1)

            if dist > 0.0:
                final = distort(final, dist)
            return final * amp
        
        self.func = func

class Tap2(Instrument):
    def __init__(self, amp = 1.0, atk = 90):
        """A simple, percussive wave created by slurring the frequency down to 0
        and wrapping the wave in an attack envelope"""

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            base = swell(freq, 0, dur)

            wave1 = base * np.exp(-t * atk)

            final = mix(wave1)

            return final * amp
        
        self.func = func
    
class Tap3(Instrument):
    """A simple, percussive wave created with noise and an attack"""
    def __init__(self, amp: float = 1.0, attack: int = 90, noise_start = 0.0, noise_amount: float = 0.5, dist = 0.0, low=0, high=0):

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            base = sine_wave(freq, dur)
            noise = np.random.normal(noise_start, noise_amount, base.shape)
            noise *= np.exp(-t * attack)

            wave1 = base * np.exp(-t * attack)

            final = mix(wave1, noise)

            if dist > 0.0:
                final  = distort(final, dist)

            if low > 0:
                final = lowpass(final, low)

            if high > 0:
                final = highpass(final, high)

            return final * amp
        
        self.func = func


class Tap4(Instrument):
    def __init__(self, amp: float = 1.0, attack: int = 90, noise_amount: float = 0.5):

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            base = sine_wave(freq, dur)
            noise = np.random.normal(0, noise_amount, base.shape)

            base = envelope(base,
                             0.001, 0.05, 0.0, 0.0)
            noise = envelope(noise,
                             0.001, 0.05, 0.0, 0.0)
            final = mix(base, noise)

            return final * amp
        
        self.func = func

class Tap5(Instrument):
    """A simple, percussive wave created with noise and an attack"""
    def __init__(self, amp: float = 1.0, attack: int = 90, noise_amount: float = 0.5):

        def func(freq, dur):
            delay = 0.01

            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            t2 = np.linspace(0, dur, int(44100 * (dur - delay)), endpoint=False)

            wave1 = sine_wave(freq, dur)
            wave2 = sine_wave(freq, dur - delay)


            noise = np.random.normal(0, noise_amount, wave1.shape)
            noise *= np.exp(-t * attack)

            wave1 *= np.exp(-t * attack)
            wave2 *= np.exp(-t2 * attack)

            wave1 = delaycombo(wave1, wave2, delay, False, True)
        

            final = mix(
                wave1,
                noise)

            return final * amp
        
        self.func = func

class PercussiveNoise(Instrument):
    def __init__(self, amp: float = 1.0, attack: int = 90, noise_start = 0.0, noise_amount: float = 0.5, dist = 0.0, low=0, high=0):

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            base = sine_wave(0, dur)

            noise = np.random.normal(noise_start, noise_amount, base.shape)
            noise *= np.exp(-t * attack)


            final = noise
            
            if dist > 0.0:
                final  = distort(final, dist)

            if low > 0:
                final = lowpass(final, low)

            if high > 0:
                final = highpass(final, high)

            return final * amp
        
        self.func = func

# class Cymbal(Instrument):
#     """A simple, percussive wave created with noise and an attack"""
#     def __init__(self, amp: float = 1.0, attack: int = 90, noise_start = 0.0, noise_amount: float = 0.5, dist = 0.0, low=0, high=0):

#         def func(freq, dur):
#             t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

#             base = sine_wave(freq, dur)
#             noise = np.random.normal(noise_start, noise_amount, base.shape)
#             noise *= np.exp(-t * attack)

#             wave1 = base * np.exp(-t * attack)

#             final = mix(wave1, noise)

#             if dist > 0.0:
#                 final  = distort(final, dist)

#             if low > 0:
#                 final = lowpass(final, low)

#             if high > 0:
#                 final = highpass(final, high)

#             return final * amp
        
#         self.func = func

class Hi_Hat(Instrument):
    def __init__(self, amp=1.0, noise_amount = 0.05):

        def func(freq, dur):
            wave1 = sine_wave(freq, dur)
            noise = white_noise(wave1, noise_amount)

            wave1 += noise

            final = envelope(wave1,
                             0.0, 0.05, 0.1, 0.01)
            
            final = mix(final, noise)
            return final * amp
        
        self.func = func
        
class Skirt(Instrument):
    def __init__(self, amp=1.0, noise_amount=0.5, attack = 50):
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
            
            noise = np.random.normal(0, noise_amount, wave.shape) * np.exp(-t * 50)
            

            #   Apply an exponential decay to the wave and noise    #
            wave += noise
            wave *= np.exp(-t * attack)
            noise *= np.exp(-t * attack)


            #   Wrap the wave in an envelope    #
            wave = envelope(wave, self.a, self.d, self.s, self.r)

            return wave * amp
        
        self.func = func

class Space_Skirt(Instrument):
    def __init__(self, amp = 1.0, metal_factor=-5, mod_freq = 120, mod_index = 12, noise_amount = 0.5, bit_depth = 6):
        def skirt(frequency, duration):
            t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
            
            #   Metallic Sound    #
            metal_freq = frequency / (12 * 2)

            base = np.sin(2 * np.pi * metal_freq * t + 
                            mod_index * np.sin(2 * np.pi * mod_freq * t))
            
            #   Noise #
            noise = np.random.normal(0, noise_amount, len(t)) * np.exp(-t * 50)
            base += noise

            #   Bandpass filtering for tonal shaping
            base = bandpass(base, 2000, 6000)
            
            #   Amplitude envelope (sharp attack/decay) #
            base = envelope(base,
                0.001, 0.05, 0.0, 0.0
            )

            #   Bit Crush   #
            base = np.round(base * (2**bit_depth)) / (2**bit_depth)
            

            final = base

            return final * amp
        
        self.func = skirt

class HipSkirt(Instrument):
    def __init__(self, attack = 15, amp = 1.0, low = 4000, high=0, dist = 6.0, noise_amount = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3

        def func(freq, dur):
            #   Metadata    #
            f = freq
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

            #   Fundamental Structure   #
            wave = np.zeros_like(t)
            wave += np.sin(2 * np.pi * f * 2* t)

            #   Metal   #
            m = swell(f*3, f/2, dur)
            m *= np.exp(-t * 30)
            wave += m

            #   Noise   #
            wave = white_noise(wave, noise_amount)

            #   Attack  #
            ##  Modify this last attack envelope to create longer or shorter skirts  ##
            wave = wave * np.exp(-t * attack)
            
            #   Filters #
            if low != 0:
                wave = lowpass(wave, low)
            
            if dist != 0:
                wave = distort(wave, dist)

            if high != 0:
                wave = highpass(wave, high)



            return wave * amp



        self.func = func

class KickBass(Instrument):
    """A kick drum with emphasized base tones"""
    def __init__(self, amp = 1.0, attack = 45, bass_dist = 2.5, bass_amp = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            #   Kick    #
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            #wave = np.zeros_like(t)

            wave = swell(freq * 2, 1, dur)
            wave *= np.exp(-t * attack)

            bass_wave = sine_wave(freq / 2, dur)
            bass_wave = envelope(
                bass_wave,
                0.001, dur - 0.001, 0.0, 0.0
            )

            if bass_dist > 0.0:
                bass_wave = distort(bass_wave, bass_dist)

            bass_wave *= bass_amp
            
            final = mix(
                wave,
                bass_wave
            )

            return final * amp


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

class KickBass2(Instrument):
    """A kick drum with emphasized base tones"""
    def __init__(self, amp = 1.0, attack = 15, count = 10, dist = 0.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            #   Kick    #
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            wave = np.zeros_like(t)

            wave1 = sine_wave(freq / 2, dur)
            wave1 *= np.exp(-t * attack)

            wave2 = sine_wave(freq / 4, dur)
            wave2 *= np.exp(-t * attack - 5)
            wave2 *= 1.5

            wave3 = sine_wave(freq / 6, dur)
            wave3 *= np.exp(-t * attack - 10)
            wave3 *= 2.0


            final = mix(
                wave1,
                # wave2,
                # wave3
                )

            if dist > 0.0:
                final = distort(final, dist)

            final = highpass(final, 100)
            return final * amp

        self.func = func

class Cymbal(Instrument):
    def __init__(self, amp=1.0, atk1 = 5, atk2 = 15, dist=0.0):
        self.a = 0.001
        self.d = 0.1
        self.s = 0.3
        #self.r = dur / 6

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur), endpoint=False)
            
            wave = sine_wave(15_000, dur)
            wave = envelope(wave,
                            0.001, 0.0, 0.3, dur / 6)
            

            noise = white_noise(sine_wave(1, dur), 0.5)

            noise - distort(noise, 2.0)
            noise = envelope(noise,
                             0.001, 0.0, 0.3, dur / 6)
            
            wave += noise

            if dist != 0.0:
                wave = distort(wave, dist)

            return wave * amp


        self.func = func

        
class Snare(Instrument):
        def __init__(self, amp=1.0, freq_mod = 1, attack = 5):
            self.a = 0.0
            self.d = 0.1
            self.s = 0.7
            self.r = 0.3


            def func(freq, dur):
                freq /= freq_mod
                t = np.linspace(0, dur, int(44100 * dur), endpoint=False)

                freqs = np.random.uniform(freq, freq / 2, 20)
                
                wave = np.zeros_like(t)
                for freq in freqs:
                    wave += np.sin(2 * np.pi * freq * t)

                wave = white_noise(wave, 0.01)
                wave = wave * np.exp(-t * attack)
                wave = wave / np.max(np.abs(wave))
                return wave * amp


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

class Bass_1(Instrument):
    def __init__(self, amp = 1.0, freq_mod = 1, attack = 0.01, decay = 0.1, sustain = 0.75, release = 0.2,
                 harmonics = 60, coeff = 2, freq_func = None, amp_func = lin(5)):
        def func(freq, dur):
            freq *= freq_mod
            synth1 = synthesize(freq, dur, 80,
                                    harmonics, coeff,
                                    freq_func, amp_func,
                                    attack, decay, sustain, release, custom_env=True
                                    )
            return synth1 * amp
        self.func = func

class Bass(Instrument):
    def __init__(self, octave=0, measure=0, type="", amp=1.0, freq_mod= 1, dist=0.0):
        self.a = 0.01
        self.d = 0.7
        self.s = 0.75
        self.r = 0.2
        
        def dress(frequency, duration):
            """DressB"""
            frequency /= freq_mod

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
            final = synth1 + synth2
            if dist > 0.0:
                final = distort(final, dist)

            return (synth1 + synth2) * amp
        
        self.func = dress

    def get_name(self):
        return "Bass Synth"

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

class RapBass(Instrument):
    def __init__(self, amp = 1.0, low = 350, dist = 0.0, freq_mod = 1):
        self.a = 0.1
        self.d = 0.6
        self.s = 0.0
        self.r = 0.0


        def func(freq, dur):
            #   Decide whether to make these punchy or not by modifying atk #

            freq *= freq_mod

            base1 = sine_wave(freq /2, dur)

            base2 = sine_wave(freq, dur)



            wave1 = envelope(base1,
            0.01, 0.1, 0.4, 0.1)

            wave2 = envelope(base2,
            0.05, 0.1, 0.4, 0.1) * 0.2

            


            final = mix(
                wave1,
                wave2,
                )

            if dist > 0.0:
                final = distort(final, dist)

            final = fade_out(final, 12)
            return final * amp
    
        self.func = func

        def get_name(self):
            return "TL Bass"
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
    def __init__(self, amp = 1.0, freq_mod = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            freq /= freq_mod

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

    def get_name(self):
        return "Dont Mind My Synth"


class DontMind2(Instrument):
    def __init__(self, amp = 1.0, freq_mod = 1.0):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            freq /= freq_mod

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
            wave1 = envelope(wave1,
                             0.01, 0.1, 0.2, 0.05)
            # wave1 *= np.exp(-t * 10)
            wave1 *= 0.2


            wave2 = sine_wave(freq / 4, dur)
            wave2 = distort(wave2, 6)
            wave2 = envelope(wave2,
                             0.05, 0.1, 0.2, 0.05)
            # wave2 *= np.exp(-t * 16)
            wave2 *= 0.6


            wave3 = sine_wave(freq / 6, dur)
            wave3 = distort(wave3, 6)
            wave3 = envelope(wave3,
                             0.1, 0.1, 0.2, 0.05)
            # wave3 *= np.exp(-t * 8)


            final = mix(
            # wave1,
            wave2,
            wave3
            )

            final = fade_out(final, 4)
            return final * amp
        
        self.func = func

    def get_name(self):
        return "Dont Mind My Synth"
    

class DontTell(Instrument):
    def __init__(self, amp = 1.0, octave_shift = 1):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))
            freq *= octave_shift

            #   Wave Foundation #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 2, dur)

            wave1 = base1 * np.exp(-t * 10)

            wave2 = base2 * np.exp(-t * 7)
            wave2 *= 0.3



            final = mix(
                wave1, 
                wave2
            )

            return final * amp
        
        self.func = func

    def get_name(self):
        return "Dont Tell Em Bout My Synth"

class DontTell2(Instrument):
    def __init__(self, amp = 1.0, octave_shift = 1,
                 decay = 0.1, release = 0.05):

        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))
            freq *= octave_shift

            #   Wave Foundation #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq / 2, dur)
            base3 = sine_wave(freq *2, dur)
        
            wave3 = envelope(base3,
                             0.2, decay, 0.1, release) * 0.2
            
            wave1 = envelope(base1,
                             0.1, decay, 0.5, release)

            wave2 = envelope(base2,
                             0.02, decay, 0.2, release)



            final = mix(
                wave1, 
                wave2,
                wave3
            )

            final = fade_out(final, 4)

            return final * amp
        
        self.func = func

    def get_name(self):
        return "Dont Tell Em Bout My Synth"
    

class RapSynth(Instrument):
    def __init__(self, amp = 1.0, freq_mod = 1):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))
            freq *= freq_mod

            #   Wave Foundation #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 2, dur)
            metal = sine_wave(freq*8, dur)

            wave1 = envelope(base1,
                             0.01, 0.1, 0.3, 0.1)
            
            wave2 = envelope(base2,
                             0.05, 0.1, 0.3, 0.1) * 0.3
            
            metal = envelope(metal,
                             0.05, 0.1, 0.3, 0.1) * 0.01



            final = mix(
                wave1, 
                wave2,
                metal
            )

            return final * amp
        
        self.func = func


class Plucky(Instrument):
    def __init__(self, amp = 1.0, octave_shift = 1):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            t = np.linspace(0, dur, int(44100 * dur))
            freq *= octave_shift

            #   Wave Foundation #
            base1 = sine_wave(freq, dur)
            base2 = sine_wave(freq * 2, dur)

            wave1 = envelope(base1,
                             0.01, dur - 0.01, 0.0, 0.0)
            
            wave2 = envelope(base2,
                             0.1, dur - 0.1, 0.0, 0.0) * 0.3



            final = mix(
                wave1, 
                wave2
            )

            return final * amp
        
        self.func = func


class Clean_Synth(Instrument):
    def __init__(self, amp = 1.0, freq_mod=1):
        self.a = 0.0
        self.d = 0.1
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            freq *= freq_mod
            freq *= 1.75
            harmonics = 3

            t = np.linspace(0, dur, int(SAMPLE_RATE * dur))
            base = np.zeros_like(t)

            freqs = np.linspace(freq, freq/harmonics, harmonics)
            for f in freqs:
                base += envelope(sine_wave(f, dur),
                                 0.05, 0.1, 0.7, 0.3 * dur)

            

            # wave2 = synthesize(freq, dur, 80,
            #                 harmonics, coeff,
            #                 freq_func, amp_func,
            #                 self.a, self.d, self.s, self.r)

            final = base

            return final * amp
        
        self.func = func

    def get_name(self):
        return "Clean Synth"

class WhinyBass(Instrument):
    def __init__(self, amp=1.0, freq_mod=1.0):
        def func(freq, dur):
            freq *= freq_mod
            freq *= 0.75
            harms = 4

            t = np.linspace(0, dur, int(dur*SAMPLE_RATE))
            base = np.zeros_like(t)

            freqs = np.linspace(freq, freq*harms, harms)
            attacks = np.linspace(dur-0.1-0.05, 0.01, harms)
            count = 0
            for f in freqs:
                base += envelope(sine_wave(f, dur),
                                 attacks[count], 0.1, 0.3, 0.05)
                count += 1

            return base * amp
        self.func = func

class Clean_Pluck(Instrument):
    def __init__(self, amp = 1.0, freq_mod=1.0):
        self.a = 0.0
        self.d = 0.4
        self.s = 0.0
        self.r = 0.0


        def func(freq, dur):
            freq *= freq_mod
            # freq *= 1.75
            harmonics = 3

            t = np.linspace(0, dur, int(SAMPLE_RATE * dur))
            base = np.zeros_like(t)

            freqs = np.linspace(freq, freq/harmonics, harmonics)

            amps = np.geomspace(1.0, 0.01, harmonics)

            count = 0
            for f in freqs:
                base += envelope(sine_wave(f, dur),
                                 0.01, dur - 0.01, 0.0, 0.0) * amps[count]            
                count += 1
            return base * amp
        self.func = func

class Clean_Key(Instrument):
    def __init__(self, amp = 1.0, freq_mod=1.0,
                 attack = 0.1, decay = 0.1, sustain = 0.4, release = 0.001):
        self.a = 0.0
        self.d = 0.4
        self.s = 0.0
        self.r = 0.0


        def func(freq, dur):
            freq *= freq_mod
            # freq *= 1.75
            harmonics = 1
            base = envelope(sine_wave(freq, dur),
                                 attack, decay, sustain, release)

            # t = np.linspace(0, dur, int(SAMPLE_RATE * dur))
            # base = np.zeros_like(t)

            # freqs = np.linspace(freq, freq/harmonics, harmonics)

            # amps = np.geomspace(1.0, 0.01, harmonics)
            

            # count = 0
            # for f in freqs:
            #     base += envelope(sine_wave(f, dur),
            #                      0.01, dur - 0.01, 0.0, 0.0) * amps[count]            
            #     count += 1
            
            return base * amp
        self.func = func

class Key_Harms(Instrument):
    def __init__(self, amp = 1.0, freq_mod=1.0, harmonics = 1,
                 attack = 0.01, decay = 0.1, sustain = 0.4, release = 0.05,
                 metal = False):

        def func(freq, dur):
            freq *= freq_mod

            t = np.linspace(0, dur, int(SAMPLE_RATE * dur))
            base = np.zeros_like(t)

            freqs = np.linspace(freq, freq*harmonics, harmonics)

            amps = np.geomspace(1.0, 0.001, harmonics)
            attacks = np.linspace(0.01, attack, harmonics)

            
            count = 0
            for f in freqs:
                base += envelope(sine_wave(f, dur),
                                 attacks[count], decay, sustain, release) * amps[count]            
                count += 1
            
            if metal:
                m = sine_wave(freq*8, dur)
                m = envelope(m, 0.001, dur - 0.001, 0.0, 0.0) * 0.03
                base = mix(
                    base,
                    m
                )
            return base * amp
        self.func = func

class ChimySynth(Instrument):
    def __init__(self, amp = 1.0, dist = 0.0, atk = 0.0):
        self.a = 0.4
        self.d = 0.3
        self.s = 0.7
        self.r = 0.3


        def func(freq, dur):
            #   Wave Foundation #
            wave1 = sine_wave(freq, dur)

            wave = mix(wave1)

            #   Metallic Tone  #
            metal = sine_wave(freq*9, dur)
            metal *= 0.1
            
            
            #   Final Mods  #
            final = mix(wave, metal)
            final = envelope(
                final,
                self.a * dur, self.d * dur, self.s, self.r * dur
            )

            if atk != 0.0:
                final *= np.exp(-t * atk)
            
            if dist > 0.0:
                final = distort(final, dist)
            
            return final * amp
        
        self.func = func

class LowSynth(Instrument):
    def __init__(self, amp = 1.0, dist = 0.0, atk = 0.0, freq_mod = 1):
        self.a = 0.01
        self.d = 0.5
        self.s = 0.0
        self.r = 0.0


        def func(freq, dur):
            #   Mod the frequency   #
            freq /= freq_mod

            #   Wave Foundation #
            wave1 = sine_wave(freq, dur)

            #   Bass Tone  #
            bass1 = sine_wave(freq/2, dur)
                        
            
            #   Final Mods  #
            final = wave1
            final = envelope(
                final,
                0.05, dur / 2, 0.3, 0.05
            )

            if dist > 0.0:
                final = distort(final, dist)
            
            return final * amp
        
        self.func = func

class Church(Instrument):
    """Church-like ambience"""
    def __init__(self, amp=1.0):
        self.a = 0.4
        self.d = 0.1
        self.s = 0.7
        self.r = 0.4

        def func(freq, dur):
            final = synthesize(freq, dur, 0,
                              10, 1,
                              bass_harms(2), None,
                              self.a, self.d, self.s, self.r) +\
                    synthesize(freq, dur, 0,
                               10, 1,
                               exp(2), None,
                               self.a, self.d, self.s, self.r)
            
            return final * amp
        
        self.func = func

class WhinyString(Instrument):
    """Generate a whiny string sound by creating a linear space from the
    fundamental frequency to an integer multiple of the fundamental frequency."""
    def __init__(self, amp=1.0, harmonics=4, base_attack = 0.001):
        self.a = 0.4
        self.d = 0.1
        self.s = 0.7
        self.r = 0.4

        def func(freq, dur):
            decay = 0.1
            sustain = 0.5
            release = 0.04

            t = np.linspace(0, dur, int(SAMPLE_RATE*dur), endpoint=False)
            base = np.zeros_like(t)

            harms = harmonics
            freqs = np.linspace(freq, freq * harms, harms)
            attacks = np.geomspace(base_attack, dur - decay - release, harms)
            amps = np.linspace(1.0, 0.001, harms)



            counter = 0
            for f in freqs:
                base += envelope(sine_wave(f, dur),
                                 attacks[counter], decay, sustain, release) * amps[counter]
                counter += 1
                
            return base * amp
        
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

        self.a = 0.001
        self.d = 0.0
        self.s = 0.0
        self.r = 0.0

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
    def __init__(self, amp = 1.0, dist = 0.0, atk = 0.0):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.0
        self.r = 0.01

        def func(freq, dur):
            wave = synthesize(freq * 3, dur, 0,
                            10, 1, None, None,
                            0.0, 0.2, 0.0, 0.01)

            if dist > 0.0:
                wave = distort(wave, dist)
            
            if atk != 0.0:
                t = np.linspace(0, dur, int(dur * 44100), endpoint=False)
                wave *= np.exp(-t * atk)

            return wave * amp

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

    def __init__(self, amp=1.0, freq_mod = 1.0, wave_1 = True, wave_2 = True, wave_3 = True):
        self.a = 0.0
        self.d = 0.2
        self.s = 0.5
        self.r = 0.4

        def func(freq, dur):
            
            freq *= freq_mod
            
            harmonics = 20
            coeff = 1
            freq_func = None
            amp_func = None
            
            t = np.linspace(0, dur, int(SAMPLE_RATE*dur), endpoint=False)
            base = np.zeros_like(t)

            wave1 = synthesize(freq / 4, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, self.d, self.s, self.r) * 0.5
                     
            wave2 = synthesize(freq / 2, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01) * 0.5
            
            wave3 = synthesize(freq / 2, dur, 0,
                               10, 1, bass_harms(2), None,
                               0.4, 0.1, 0.7, 0.01)
            
            if wave_1:
                base = mix(base, wave1)

            if wave_2:
                base = mix(base, wave2)

            if wave_3:
                base = mix(base, wave3)

            return base * amp
        
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
    def __init__(self, amp = 1.0, add_plucks = True):
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
                                self.a, self.d, self.s, self.r) * 0.5
            
            pluck1 = synthesize(freq, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01)
            
            #   First2, Octave Higher   #
            synth2 = synthesize(freq*2, dur, 0,
                                harmonics, coeff, freq_func, amp_func,
                                self.a, 0.0, 1.0, 0.15) * 0.5
            
            pluck2 = synthesize(freq*2, dur, 0,
                                10, 1, None, None,
                                0.0, 0.2, 0.0, 0.01)

            if add_plucks:
                synth1 += pluck1
                synth2 += pluck2

            final = synth1 + synth2
            return final * amp

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



    class Symbol(Instrument):
        def __init__(self, octave, measure, type = ""):
            super().__init__(octave, measure, symbol)

    class Skirt(Instrument):
        def __init__(self):
            self.func = skirt

    class Skirt2(Instrument):
        def __init__(self):
            self.func = skirt2