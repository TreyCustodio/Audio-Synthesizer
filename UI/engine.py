import pygame
import os
import sys

from modules.audio import *
from modules.instruments import *
from .globals import *
from .utils import *
from .objects import *
from .composer import *

import numpy as np

class Engine:
    """
    The Engine draws the graphical elements,
    handles input from the user,
    and updates the display accordingly.
    
    --- Mouse Events ---
    1. Check the user's mouse position
        a. Check if that position overlaps a button
        b. Set that button's state to hovered if so
    2. Check if the user has clicked a mouse button
        a. Check if any of the buttons on screen are being hovered over
        b. Set the button's state to held if so
    3. Check if the user has released a mouse button
        a. Check if any of the buttons on screen are being held
        b. Release the button and perform its operation if so
    """
    
    def __init__(self):
        #   States  #
        self.state = "main"
        self.hovering_synth = False


        #   Main Menu Images    #
        self.load_main_images()

        #   Back Button   #
        self.load_global_images()

        #   Composer Images #
        self.load_composer_images()

        #   Synthesizer Images  #
        #self.load_synthesizer_images()

        #   Piano Images   #
        self.load_piano_images()

        #   Bpm   #
        self.bpm = 38

        #   Instrument   #
        # self.instrument = Tangible_Light.Bell()
        self.instrument = Bass_1(amp=1.0, attack=0.005, attack_max = 0.003, freq_mod = 1, sustain=0.3, release= 0.01, amp_final = 0.1, top_freq = 2, harmonics=2)

        # self.instrument = First4(wave_1 = False, wave_2 = True, wave_3 = False)
        # self.instrument = Acoustic3(harmonics=12,
        #                         vol_1 = 0.01, vol_2 = 0.01, vol_3 = 0.000000000001, vol_4=1.0, vol_5 = 0.01, vol_6 = 0.01, vol_7 = 0.01, vol_8 = 0.01)

        # self.instrument = Key_Harms(harmonics=30,
        #                             attack=0.1, decay = 0.05)

        #   Octave   #
        self.octave = 1

        #   Background Images   #
        self.white = pygame.rect.Rect(0, 0, WIDTH, 120)
        self.red = pygame.rect.Rect(0, 0, WIDTH, 120)
        
        
        
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



    """
    Auxillary Methods -------------------------------------------------
    """
    

    def load_global_images(self):
        """Load images used in multiple states"""
        scale = 5
        size = (40, 17)
        back_full = pygame.image.load(os.path.join("UI", "images", "back.png"))        
        frames = load_row(back_full, size, scale, 3, 0)
        self.back = Pressable((8, 8), frames)

        scale = 3
        frames2 = load_row(back_full, size, scale, 3, 0)
        self.back2 = Pressable((8, 8), frames2)


    def load_main_images(self):
        """Load the images needed to display the main menu"""
        #   Trizzy Logo
        scale = 5
        size = (105, 19)
        trizzy_full = pygame.image.load(os.path.join("UI", "images", "main", "trizzy.png"))        
        frames = load_row(trizzy_full, size, scale, 1, 0)

        self.trizzy = Animated((WIDTH // 2 - (size[0] * scale) // 2, 8), frames)



        #   Composer Button:
        ##  Sprite Size: (46, 12)
        ##  Sheet Size: (96, 12)
        scale = 5
        size = (46, 13)
        compose_full = pygame.image.load(os.path.join("UI", "images", "main", "compose.png")).convert_alpha()
        frames = load_row(compose_full, size, scale, 3, 0)
        self.compose = Pressable((WIDTH // 2 - (size[0] * scale) // 2, HEIGHT // 1.6 - (size[1] * scale) // 2), frames)





        #   Synthesizer Button:
        ##  Sprite Size: (46, 12)
        ##  Sheet Size: (96, 12)
        size = (49, 14)
        synthesize_full = pygame.image.load(os.path.join("UI", "images", "main", "synthesize.png")).convert_alpha()
        frames = load_row(synthesize_full, size, scale, 3, 0)
        self.synthesize = Pressable((WIDTH // 2 - (size[0] * scale) // 2, HEIGHT // 2.4 - (size[1]* scale) // 2), frames)


        #   Play Button:
        ##  Sprite Size: (36, 10)
        ##  Sheet Size: (18, 10)
        size = (26, 13)
        play_full = pygame.image.load(os.path.join("UI", "images", "main", "play.png")).convert_alpha()
        frames = load_row(play_full, size, scale, 3, 0)
        self.play = Pressable((WIDTH // 2 - (size[0] * scale) // 2, HEIGHT // 1.2 - (size[1] * scale) // 2), frames)


    def load_piano_images(self):
        """Load images needed to display the piano"""
        frames = load_row(pygame.image.load(os.path.join("UI","images", "piano", "select.png")), (104, 17), 1, 3, 0)
        self.select = Pressable(vec(WIDTH - 104, 0), frames)

        self.piano = pygame.image.load(os.path.join("UI","images", "piano", "piano.png"))

        self.piano_white = pygame.image.load(os.path.join("UI","images", "piano", "piano_white.png"))
        self.piano_white.set_colorkey(self.piano_white.get_at((0,0)))

        self.piano_black = pygame.image.load(os.path.join("UI","images", "piano", "piano_black.png"))
        self.piano_black.set_colorkey(self.piano_black.get_at((0,0)))
        
        self.held_white = pygame.image.load(os.path.join("UI","images", "piano", "held_white.png"))
        self.held_white.set_colorkey(self.held_white.get_at((0,0)))

        self.held_white2 = pygame.image.load(os.path.join("UI","images", "piano", "held_white2.png"))
        self.held_white2.set_colorkey(self.held_white2.get_at((0,0)))

        self.held_white3 = pygame.image.load(os.path.join("UI","images", "piano", "held_white3.png"))
        self.held_white3.set_colorkey(self.held_white3.get_at((0,0)))
        
        self.held_black = pygame.image.load(os.path.join("UI","images", "piano", "held_black.png"))
        self.held_black.set_colorkey(self.held_black.get_at((0,0)))

    
    def load_composer_images(self):
        """Load images needed to display the composer"""
        cleft = pygame.image.load(os.path.join("UI", "images", "composer", "cleft.png"))
        self.cleft = Animated((16,16 * 6), [cleft])


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

    def get_state(self):
        return self.state

    def incrementOctave(self):
        self.octave += 1

    def decrementOctave(self):
        self.octave -= 1




    """
    Drawing ------------------------------------------------
    """

    def draw_cross(self, surf):
        """Draw lines going through the center of the screen to help with positioning"""
        rectY = pygame.Rect((WIDTH // 2, 0), (1, HEIGHT))
        pygame.draw.rect(surf, (255, 0, 0), rectY)

        rectX = pygame.Rect((0, HEIGHT // 2), (WIDTH, 1))
        pygame.draw.rect(surf, (0, 0, 255), rectX)


    def draw(self, surf):
        """Draw routine"""
        #   Main Menu   #
        if self.state == "main":
            # Background Color    #
            surf.fill((30, 70, 100))

            #   Background Outline  #
            rect = pygame.Rect((0, 0), (WIDTH, HEIGHT))
            pygame.draw.rect(surf, (0,0,0), rect, 4)

            #   Trizzy  #
            self.trizzy.draw(surf)
            
            #   Synthesize  #
            self.synthesize.draw(surf)

            #   Compose #
            self.compose.draw(surf)

            #   Play    #
            self.play.draw(surf)
            


        #   Piano Player    #
        elif self.state == "piano":
            #   Draw some background 
            surf.fill((230, 230, 230))

            #   Draw the piano  #
            surf.blit(self.piano, (0, 120))
            

            # Fill the rect with white color    #
            pygame.draw.rect(surf, (230, 230, 230), self.white)


            #   Display the current Octave and Instrument  #
            font = pygame.font.SysFont(None, 36)  # None for default font, 36 is the size
            
            octave = font.render(f"Octave: {self.octave}", True, (0, 0, 0))
            instrument = font.render(f"Instrument: " + self.instrument.get_name(), True, (0, 0, 0))

            octave_bg = octave.get_rect(topleft=(WIDTH // 2 - octave.get_size()[0] // 2, 50))
            instrument_bg = instrument.get_rect(topleft=(WIDTH // 2 - instrument.get_size()[0] // 2, 10))

            pygame.draw.rect(surf, (255, 255, 255), octave_bg)
            pygame.draw.rect(surf, (255, 255, 255), instrument_bg)

            surf.blit(octave, (WIDTH // 2 - octave.get_size()[0] // 2, 50))
            surf.blit(instrument, (WIDTH // 2 - instrument.get_size()[0] // 2, 10))


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
            
            #   Draw the Back Button   #
            self.back.draw(surf)

            #   Draw the Instruments button #
            self.select.draw(surf)


        #   Composer    #
        elif self.state == "composer":
            Composer.draw(surf)
            if Composer.STATE == "view":
                self.back2.draw(surf)

        #   Synthesizer #
        elif self.state == "synthesizer":
            return
    


    def handle_event(self, event):
        """Handle input from the user"""
        #   Global events that should be handled in any state   #
        ## Track the mouse position  #
        if event.type == pygame.MOUSEMOTION:
            self.check_mouse(event.__dict__['pos'])

        ##   Check if the mouse buttons are pressed   #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.press_down(event)

        ##   Check if the mouse buttons are released  #
        elif event.type == pygame.MOUSEBUTTONUP:
            self.press_up(event)
        
        elif event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
            pygame.quit()

        #   State-specific Events   #
        else:
            state = self.get_state()

            ##  Main Menu   #
            if state == "main":
                return


            ##  Composer    #
            elif state == "compose":
                return


            ##  Synthesizer #
            elif state == "synthesize":
                return


            ##  Piano Player    #
            elif state == "piano":
                ### Track the mouse position.
                if event.type == pygame.MOUSEMOTION:
                    self.check_mouse(event.__dict__['pos'])

                ### Play button held animation
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.press_down()

                ### Proceed to the next state
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.press_up()

                #   Key Down    #
                elif event.type == pygame.KEYDOWN:
                    
                    #  Escape - Quit    #
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

                    #   Octave Down #
                    elif event.key == pygame.K_LSHIFT:
                        self.decrementOctave()

                    #   Octave Up   #
                    elif event.key == pygame.K_RSHIFT:
                        self.incrementOctave()


                    #   C1  #
                    elif event.key == pygame.K_a:
                        self.play_note(C1)
                        self.set_held("c")
                    
                    #   C#  #
                    elif event.key == pygame.K_w:
                        self.play_note(Cs1)
                        self.set_held("c#")

                    
                    #   D   #
                    elif event.key == pygame.K_s:
                        self.play_note(D1)
                        self.set_held("d")
                        
                    
                    #   D#  #
                    elif event.key == pygame.K_e:
                        self.play_note(Ds1)
                        self.set_held("d#")
                    
                    #   E   #
                    elif event.key == pygame.K_d:
                        self.play_note(E1)
                        self.set_held("e")
                        
                    
                    #   F   #
                    elif event.key == pygame.K_f:
                        self.play_note(F1)
                        self.set_held("f")
                        
                    
                    #   F#  #
                    elif event.key == pygame.K_t:
                        self.play_note(Fs1)
                        self.set_held("f#")
                        
        
                    #   G   #
                    elif event.key == pygame.K_g:
                        self.play_note(G1)
                        self.set_held("g")
                        

                    #   G#  #
                    elif event.key == pygame.K_y:
                        self.play_note(Gs1)
                        self.set_held("g#")


                    #   A   #
                    elif event.key == pygame.K_h:
                        self.play_note(A1)
                        self.set_held("a")
                        
                    
                    #   A#  #
                    elif event.key == pygame.K_u:
                        self.play_note(As1)
                        self.set_held("a#")
                        
                    
                    #   B   #
                    elif event.key == pygame.K_j:
                        self.play_note(B1)
                        self.set_held("b")
                    
                    #  C    #
                    elif event.key == pygame.K_k:
                        self.play_note(C2)
                        self.set_held("c2")

                    #  C#   #
                    elif event.key == pygame.K_o:
                        self.play_note(Cs2)
                        self.set_held("c#2")

                    #  D   #
                    elif event.key == pygame.K_l:
                        self.play_note(D2)
                        self.set_held("d2")

                    #  D#  #
                    elif event.key == pygame.K_p:
                        self.play_note(Ds2)
                        self.set_held("d#2")

                    #  E   #
                    elif event.key == pygame.K_SEMICOLON:
                        self.play_note(E2)
                        self.set_held("e2")

                    #  F   #
                    elif event.key == pygame.K_QUOTE:
                        self.play_note(F2)
                        self.set_held("f2")

                    #  F#  #
                    elif event.key == pygame.K_RIGHTBRACKET:
                        self.play_note(Fs2)
                        self.set_held("f#2")
                    
                    #  G   #
                    elif event.key == pygame.K_RETURN:
                        self.play_note(G2)
                        self.set_held("g2")
                    
                    #  G#  #
                    elif event.key == pygame.K_BACKSLASH:
                        self.play_note(Gs2)
                        self.set_held("g#2")
                    
                    #  A   #
                    elif event.key == pygame.K_KP4:
                        self.play_note(A2)
                        self.set_held("a2")
                    
                    #  A#  #
                    elif event.key == pygame.K_KP8:
                        self.play_note(As2)
                        self.set_held("a#2")

                    #  B   #
                    elif event.key == pygame.K_KP6 or event.key == pygame.K_5:
                        self.play_note(B2)
                        self.set_held("b2")
                        


                #   Key Up  #
                elif event.type == pygame.KEYUP:

                    #   C1  #
                    if event.key == pygame.K_a:
                        self.unset_held("c")
                    
                    #   C#  #
                    elif event.key == pygame.K_w:
                        self.unset_held("c#")
                    
                    #   D   #
                    elif event.key == pygame.K_s:
                        self.unset_held("d")
                    
                    #   D#  #
                    elif event.key == pygame.K_e:
                        self.unset_held("d#")
                    
                    #   E   #
                    elif event.key == pygame.K_d:
                        self.unset_held("e")
                    
                    #   F   #
                    elif event.key == pygame.K_f:
                        self.unset_held("f")
                    
                    #   F#  #
                    elif event.key == pygame.K_t:
                        self.unset_held("f#")
                    
                    #   G   #
                    elif event.key == pygame.K_g:
                        self.unset_held("g")
                    
                    #   G#  #
                    elif event.key == pygame.K_y:
                        self.unset_held("g#")
                    
                    #   A   #
                    elif event.key == pygame.K_h:
                        self.unset_held("a")
                    
                    #   A#  #
                    elif event.key == pygame.K_u:
                        self.unset_held("a#")
                    
                    #   B   #
                    elif event.key == pygame.K_j:
                        self.unset_held("b")

                    #   C2  #
                    elif event.key == pygame.K_k:
                        self.unset_held("c2")
                    
                    #   C#2  #
                    elif event.key == pygame.K_o:
                        self.unset_held("c#2")
                    
                    #   D2  #
                    elif event.key == pygame.K_l:
                        self.unset_held("d2")

                    #   D#2  #
                    elif event.key == pygame.K_p:
                        self.unset_held("d#2")
                    
                    #   E2  #
                    elif event.key == pygame.K_SEMICOLON:
                        self.unset_held("e2")
                    
                    #   F2  #
                    elif event.key == pygame.K_QUOTE:
                        self.unset_held("f2")
                    
                    #   F#2  #
                    elif event.key == pygame.K_RIGHTBRACKET:
                        self.unset_held("f#2")
                    
                    #   G2  #
                    elif event.key == pygame.K_RETURN:
                        self.unset_held("g2")
                    
                    #   G#2  #
                    elif event.key == pygame.K_BACKSLASH:
                        self.unset_held("g#2")
                    
                    #   A2  #
                    elif event.key == pygame.K_KP4:
                        self.unset_held("a2")
                    
                    #   A#2  #
                    elif event.key == pygame.K_KP8:
                        self.unset_held("a#2")
                    
                    #   B2  #
                    elif event.key == pygame.K_KP6 or event.key == pygame.K_5:
                        self.unset_held("b2")


    def check_mouse(self, pos):
        """Check if the mouse overlaps a button.
        Highlight buttons if they are being hovered over
        """
        if self.state == "main":
            self.synthesize.check_hovering(pos)
            self.compose.check_hovering(pos)
            self.play.check_hovering(pos)
        
        elif self.state == "piano":
            self.back.check_hovering(pos)
            self.select.check_hovering
        
        elif self.state == "composer":
            if Composer.STATE == "view":
                self.back2.check_hovering(pos)
            Composer.check_mouse(pos)


    def press_down(self, event = None):
        """Press a button if it is being hovered over"""
        if self.state == "main":
            if self.synthesize.get_hovered():
                self.synthesize.hold()

            elif self.compose.get_hovered():
                self.compose.hold()

            elif self.play.get_hovered():
                self.play.hold()
        
        elif self.state == "piano":
            if self.back.get_hovered():
                self.back.hold()

            if self.select.get_hovered():
                self.select.hold()

        elif self.state == "composer":
            if self.back2.get_hovered():
                self.back2.hold()
            else:
                if event.__dict__['button'] == 3:
                    Composer.right_down(event)
                else:
                    Composer.press_down()


    def press_up(self, event = None):
        """Proceed to the next state if a button is pressed"""
        if self.state == "main":
            if self.synthesize.get_held():
                #self.state = "synthesizer"
                self.synthesize.release()

            elif self.compose.get_held():
                Composer.init()
                self.state = "composer"
                self.compose.release()

            elif self.play.get_held():
                self.state = "piano"
                self.play.release()
        
        elif self.state == "piano":
            if self.back.get_held():
                self.state = "main"
                self.back.release()

            #   Open instrument selecter    #
            elif self.select.get_held():
                self.select.release()

        elif self.state == "composer":
            if self.back2.get_held():
                Composer.reset()
                self.state = "main"
                self.back2.release()
            else:
                if event.__dict__['button'] == 3:
                    Composer.right_up(event)
                else:
                    Composer.press_up()
    
    
    """
    Note-Playing ---------------------------------------------------------
    """
    def dynamic(self, note):
        #   No release
        wave = self.instrument.dynamic(note, 0.1, self.octave)
        wave = np.column_stack((wave, wave))
        wave = wave.astype(np.int16)

        #   Convert to Pygame Sound #
        sound = pygame.sndarray.make_sound(wave)
        sound.play()

        return wave

        
        
    def play_note(self, note):
        #note = self.dynamic(note)
        note = self.instrument.create_note_octave(note, get_eighth(self.bpm), self.octave)
        
        note = write(note, "", "note")
        #note = (note / np.max(np.abs(note)) * 32767).astype(np.int16)
        #note = np.column_stack((note, note))
        
        sound = pygame.mixer.Sound("note.wav")
        sound.play()


    """
    Updating
    """
    def update(self, seconds):
        if self.state == "composer":
            Composer.update(seconds)