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
        
        #   Bpm   #
        self.bpm = 62

        #   Instrument   #
        #self.instrument = Cymbal()
        #self.instrument = Snare()
        self.instrument = Bass()
        #self.instrument = Skirt()
        #self.instrument = First2()
        #self.instrument = Clean_Synth()

        #   Octave   #
        self.octave = 3

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

            "c2": 0,
            "c#2": 0,
            "d2": 0,
            "d#2": 0,
            "e2": 0,
            "f2": 0,
            "f#2": 0,
            "g2": 0,
            "g#2": 0,
            "a2": 0,
            "a#2": 0,
            "b2": 0,    
        }

    def stop(self):
        """Instantly stop all sounds"""
        pygame.mixer.stop()


    def set_held(self, key):
        """Set the held key"""
        if key in self.held:
            self.held[key] = 1
    
    def unset_held(self, key):
        """Unset the held key"""
        if key in self.held:
            self.held[key] = 0
            #self.stop()

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
                    delta = 54
                    if index == 1 or index == 4 or index == 5:
                        surf.blit(self.held_white2, ((index * delta), 120))
                    elif index == 2 or index == 6:
                        surf.blit(self.held_white3, ((index * delta), 120))
                    else:
                        surf.blit(self.held_white, ((index * delta), 120))

            if "#" not in i:
                index += 1
            elif index != 1:
                index_b += 1
    
    def dynamic(self, note):
        #   No release
        #wave = self.instrument.create_note_octave(note, 1.0, self.octave)
        wave = self.instrument.dynamic(note, 0.1, self.octave)
        wave = np.column_stack((wave, wave))
        wave = wave.astype(np.int16)

        #   Convert to Pygame Sound #
        sound = pygame.sndarray.make_sound(wave)
        sound.play()

        return wave

        
        
    def play(self, note):
        
        #note = self.dynamic(note)
        note = self.instrument.create_note_octave(note, get_eighth(self.bpm), self.octave)

        
        #   Convert to PCM Format   #
        ##  Pulse-Code Modulation   
        
        
        note = write(note, "", "note")
        #note = (note / np.max(np.abs(note)) * 32767).astype(np.int16)
        #note = np.column_stack((note, note))
        
        sound = pygame.mixer.Sound("note.wav")
        sound.play()


