from audio import *

"""Given an octave and a measure length,
generate every possible note for each instrument."""

class Instrument:
    def __init__(self, octave, measure, func, type=""):
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

    def getADSR(self):
        return
        
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

    
class Dreamy(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, dream)

class Snare(Instrument):
    def __init__(self, octave, measure):
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

class Bass(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, bass)

class Symbol(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, symbol)

class Skirt(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, skirt)

class Skirt2(Instrument):
    def __init__(self, octave, measure):
        super().__init__(octave, measure, skirt2)