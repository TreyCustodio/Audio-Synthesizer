from audio import *
from instruments import *
import wave
from abc import abstractmethod


class Beat:
    """Initializing Instance Variables"""
    def __init__(self, bpm):
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
    
    """ Getting Metadata"""





    """ Production"""
    @abstractmethod
    def produce(self):
        return