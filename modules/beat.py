from .audio import *
from .instruments import *
from abc import abstractmethod



class Beat:
    """Directory to save beats into"""
    FOLDER = "beats"
    """Initializing Instance Variables"""
    def __init__(self, bpm : float = 180.0, name: str = ""):
        #   Bpm
        self.bpm = bpm
        beat = 1 / (bpm / 60)

        #   Note Lengths
        self.sixteenth = beat / 4
        self.eighth = beat / 2
        self.quarter = beat
        self.half = self.quarter * 2
        self.trey = self.quarter * 3
        self.whole = self.quarter * 4

        #   Note Lengths ver 2
        self.s = beat / 4
        self.e = beat / 2
        self.q = beat
        self.h = self.quarter * 2
        self.t = self.quarter * 3
        self.w = self.quarter * 4

        #   File Name
        self.fileName = name

    """ Getting Metadata"""





    """ Production"""
    @abstractmethod
    def produce(self):
        return
    
    def save(self):
        write(self.fileName)

    def metronome(self, bars=1):
        """Return a measure of a metronome"""
        n = Skirt(4, self.whole)

        m1 = build_measure(n.q_c, n.q_c, n.q_c, n.q_c)
        v1 = m1

        for i in range(bars-1):
            v1 = add_waves(v1, m1)
            
        return v1
    
    def tempo(self, sound):
        """Return 4 measures of an instrument keeping tempo"""
        m1 = build_measure(sound, sound, sound, sound,)
        v1 = build_measure(m1, m1, m1, m1)

        return v1