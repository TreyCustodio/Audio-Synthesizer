import pygame
from modules.audio import *

class EventManager(object):
    """Originally developed for my typing game, War and Keys.
    Modified for my synthesizer app."""

    #   Dictionary of actions corresponding to each key
    actions = {(i + 97): False for i in range(26)}

    #   Priority queue of keys
    queue = []

    #   Backspace
    backspace = False
    backspace_timer = 0.0
    backspace_ready = False

    #   Startup
    startup = False
    timer = 0.0
    transitioning = False

    #   Ready
    ready = True

    def __init__(self):
        pass
    
    def buffBackspace():
        EventManager.backspace_ready = False


    def handleEvents(engine):
        """Handle events in the event queue"""

        for event in pygame.event.get():
            
            #   Pause event handling if the mouse is out of focus   #
            if event.type == pygame.WINDOWMOVED or event.type == pygame.WINDOWLEAVE or not pygame.mouse.get_focused():
                return

            #   Key Down    #
            if event.type == pygame.KEYDOWN:
                
                #  Escape - Quit    #
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                #   Octave Down #
                elif event.key == pygame.K_LSHIFT:
                    pass

                #   Octave Up   #
                elif event.key == pygame.K_RSHIFT:
                    pass

                #   C1  #
                elif event.key == pygame.K_a:
                    engine.play(A3)
                
                #   C#  #
                elif event.key == pygame.K_w:
                    pass
                
                #   D   #
                elif event.key == pygame.K_s:
                    pass
                
                #   D#  #
                elif event.key == pygame.K_e:
                    pass
                
                #   E   #
                elif event.key == pygame.K_d:
                    pass
                
                #   F   #
                elif event.key == pygame.K_f:
                    pass
                
                #   F#  #
                elif event.key == pygame.K_t:
                    pass
                
                #   G   #
                elif event.key == pygame.K_g:
                    pass

                #   G#  #
                elif event.key == pygame.K_y:
                    pass

                #   A   #
                elif event.key == pygame.K_h:
                    pass
                
                #   A#  #
                elif event.key == pygame.K_u:
                    pass
                
                #   B   #
                elif event.key == pygame.K_j:
                    pass

            #   Key Up  #
            elif event.type == pygame.KEYUP:
                pass


    def readyToUpdate():
        return True
    
    def updateTimer(seconds, engine):
        """
        Update the event manager's timer
        """
        EventManager.timer += seconds
        if EventManager.timer >= 2.0:
            EventManager.timer = 0.0
            EventManager.transitioning = True
            engine.fade_on = True

    def updateBuffer(seconds):
        if EventManager.backspace and not EventManager.backspace_ready:
            EventManager.backspace_timer += seconds
            if EventManager.backspace_timer >= 0.1:
                EventManager.backspace_timer = 0.0
                EventManager.backspace_ready = True
                