import pygame
import os

from modules.audio import *
from modules.instruments import *
from .globals import *

import numpy as np

class Engine:
    
    
    def __init__(self):
        #   Piano Images   #
        self.paino = pygame.image.load(os.path.join("UI","images", "piano.png"))

        self.piano_white = pygame.image.load(os.path.join("UI","images", "piano_white.png"))
        self.piano_white.set_colorkey(self.piano_white.get_at((0,0)))

        self.piano_black = pygame.image.load(os.path.join("UI","images", "piano_black.png"))
        self.piano_black.set_colorkey(self.piano_black.get_at((0,0)))
        
        #   Playback Data   #
        self.bpm = 60
        self.instrument = First2(3, get_measure(self.bpm))
        self.octave = 4

        #   Background Images   #
        self.white = pygame.rect.Rect(0, 0, WIDTH, 120)
        self.red = pygame.rect.Rect(0, 0, WIDTH, 120)
        
        self.held_white = pygame.image.load(os.path.join("UI","images", "held_white.png"))
        self.held_white.set_colorkey(self.held_white.get_at((0,0)))

        self.held_white2 = pygame.image.load(os.path.join("UI","images", "held_white2.png"))
        self.held_white2.set_colorkey(self.held_white2.get_at((0,0)))

        self.held_white3 = pygame.image.load(os.path.join("UI","images", "held_white3.png"))
        self.held_white3.set_colorkey(self.held_white3.get_at((0,0)))
        
        self.held_black = pygame.image.load(os.path.join("UI","images", "held_black.png"))
        self.held_black.set_colorkey(self.held_black.get_at((0,0)))
        
        #   Held Keys   #
        self.held = {
            "c": 0,
            "c#": 0,
            "d": 0,
            "d#": 0,
            "e": 0,
            "f": 0,
            "f#": 0,
            "g": 0,
            "g#": 0,
            "a": 0,
            "a#": 0,
            "b": 0,            
        }


    def set_held(self, key):
        """Set the held key"""
        if key in self.held:
            self.held[key] = 1
    
    def unset_held(self, key):
        """Unset the held key"""
        if key in self.held:
            self.held[key] = 0

    def incrementOctave(self):
        self.octave += 1

    def decrementOctave(self):
        self.octave -= 1

    def draw(self, surf):
        """Draw routine"""
        #   Draw the piano  #
        surf.blit(self.paino, (0, 120))
        # surf.blit(self.piano_white, (0,120))
        # surf.blit(self.piano_black, (0,120))
        

        # Fill the rect with white color    #
        pygame.draw.rect(surf, (230, 230, 230), self.white)


        #   Display the current Octave and Instrument  #
        font = pygame.font.SysFont(None, 36)  # None for default font, 36 is the size
        octave = font.render(f"Octave: {self.octave}", True, (0, 0, 0))
        instrument = font.render(f"Instrument: Synth", True, (0, 0, 0))
        octave_bg = octave.get_rect(topleft=(10, 10))
        instrument_bg = instrument.get_rect(topleft=(10, 50))

             
        #   Blit the text to the surface    #
        pygame.draw.rect(surf, (255, 255, 255), octave_bg)
        pygame.draw.rect(surf, (255, 255, 255), instrument_bg)
        surf.blit(octave, (10, 10))
        surf.blit(instrument, (10, 50))


        #   Blit the held keys  #
        index = 0
        index_b = 0
        for i in self.held:
            if self.held[i] == 1:
                if "#" in i:
                    surf.blit(self.held_black, (((index_b+1) * 34), 120))

                else:
                    if index == 1 or index == 4 or index == 5:
                        surf.blit(self.held_white2, ((index * 56), 120))
                    elif index == 2 or index == 6:
                        surf.blit(self.held_white3, ((index * 56), 120))
                    else:
                        surf.blit(self.held_white, ((index * 56), 120))

            if "#" not in i:
                index += 1
            elif index != 1:
                index_b += 1

        
    def play(self, note):
        #   self.held[]
        note = self.instrument.create_note_octave(note, get_quarter(self.bpm), self.octave)

        
        #   Convert to PCM Format   #
        ##  Pulse-Code Modulation   
        note = (note * 32767).astype(np.int16)
        note = np.column_stack((note, note))
        
        sound = pygame.sndarray.make_sound(note)
        sound.play()