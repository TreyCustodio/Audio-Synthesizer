from .audio import *
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

        #   File Name
        self.fileName = name

    """ Getting Metadata"""





    """ Production"""
    @abstractmethod
    def produce(self):
        return
    
    def save(self):
        write(self.fileName)