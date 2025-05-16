import pygame
import os

from modules.audio import *
from modules.instruments import *

import numpy as np

class Engine:
    
    
    def __init__(self):
        self.piano = pygame.image.load(os.path.join("UI","images", "piano.png"))
        self.bpm = 60
        self.instrument = Tester(get_measure(self.bpm))

    def draw(self, surf):
        surf.blit(self.piano, (0,0))

    def play(self, note):
        note = self.instrument.create_note(note, get_quarter(self.bpm))
        note = (note * 32767).astype(np.int16)
        note = note.reshape(-1, 1)

        #note = np.vstack((note, note))

        sound = pygame.sndarray.make_sound(note)
        sound.play()