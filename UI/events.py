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
                pass
                # return if you dont want to handle events when mouse out of focus

            #   Key Down    #
            if event.type == pygame.KEYDOWN:
                
                #  Escape - Quit    #
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                #   Octave Down #
                elif event.key == pygame.K_LSHIFT:
                    engine.decrementOctave()

                #   Octave Up   #
                elif event.key == pygame.K_RSHIFT:
                    engine.incrementOctave()


                #   C1  #
                elif event.key == pygame.K_a:
                    engine.play(C1)
                    engine.set_held("c")
                
                #   C#  #
                elif event.key == pygame.K_w:
                    engine.play(Cs1)
                    engine.set_held("c#")

                
                #   D   #
                elif event.key == pygame.K_s:
                    engine.play(D1)
                    engine.set_held("d")
                    
                
                #   D#  #
                elif event.key == pygame.K_e:
                    engine.play(Ds1)
                    engine.set_held("d#")
                
                #   E   #
                elif event.key == pygame.K_d:
                    engine.play(E1)
                    engine.set_held("e")
                    
                
                #   F   #
                elif event.key == pygame.K_f:
                    engine.play(F1)
                    engine.set_held("f")
                    
                
                #   F#  #
                elif event.key == pygame.K_t:
                    engine.play(Fs1)
                    engine.set_held("f#")
                    
    
                #   G   #
                elif event.key == pygame.K_g:
                    engine.play(G1)
                    engine.set_held("g")
                    

                #   G#  #
                elif event.key == pygame.K_y:
                    engine.play(Gs1)
                    engine.set_held("g#")


                #   A   #
                elif event.key == pygame.K_h:
                    engine.play(A1)
                    engine.set_held("a")
                    
                
                #   A#  #
                elif event.key == pygame.K_u:
                    engine.play(As1)
                    engine.set_held("a#")
                    
                
                #   B   #
                elif event.key == pygame.K_j:
                    engine.play(B1)
                    engine.set_held("b")
                
                #  C    #
                elif event.key == pygame.K_k:
                    engine.play(C2)
                    engine.set_held("c2")

                #  C#   #
                elif event.key == pygame.K_o:
                    engine.play(Cs2)
                    engine.set_held("c#2")

                #  D   #
                elif event.key == pygame.K_l:
                    engine.play(D2)
                    engine.set_held("d2")

                #  D#  #
                elif event.key == pygame.K_p:
                    engine.play(Ds2)
                    engine.set_held("d#2")

                #  E   #
                elif event.key == pygame.K_SEMICOLON:
                    engine.play(E2)
                    engine.set_held("e2")

                #  F   #
                elif event.key == pygame.K_QUOTE:
                    engine.play(F2)
                    engine.set_held("f2")

                #  F#  #
                elif event.key == pygame.K_RIGHTBRACKET:
                    engine.play(Fs2)
                    engine.set_held("f#2")
                
                #  G   #
                elif event.key == pygame.K_RETURN:
                    engine.play(G2)
                    engine.set_held("g2")
                
                #  G#  #
                elif event.key == pygame.K_BACKSLASH:
                    engine.play(Gs2)
                    engine.set_held("g#2")
                
                #  A   #
                elif event.key == pygame.K_KP4:
                    engine.play(A2)
                    engine.set_held("a2")
                
                #  A#  #
                elif event.key == pygame.K_KP8:
                    engine.play(As2)
                    engine.set_held("a#2")

                #  B   #
                elif event.key == pygame.K_KP6 or event.key == pygame.K_5:
                    engine.play(B2)
                    engine.set_held("b2")
                    


            #   Key Up  #
            elif event.type == pygame.KEYUP:

                #   C1  #
                if event.key == pygame.K_a:
                    engine.unset_held("c")
                
                #   C#  #
                elif event.key == pygame.K_w:
                    engine.unset_held("c#")
                
                #   D   #
                elif event.key == pygame.K_s:
                    engine.unset_held("d")
                
                #   D#  #
                elif event.key == pygame.K_e:
                    engine.unset_held("d#")
                
                #   E   #
                elif event.key == pygame.K_d:
                    engine.unset_held("e")
                
                #   F   #
                elif event.key == pygame.K_f:
                    engine.unset_held("f")
                
                #   F#  #
                elif event.key == pygame.K_t:
                    engine.unset_held("f#")
                
                #   G   #
                elif event.key == pygame.K_g:
                    engine.unset_held("g")
                
                #   G#  #
                elif event.key == pygame.K_y:
                    engine.unset_held("g#")
                
                #   A   #
                elif event.key == pygame.K_h:
                    engine.unset_held("a")
                
                #   A#  #
                elif event.key == pygame.K_u:
                    engine.unset_held("a#")
                
                #   B   #
                elif event.key == pygame.K_j:
                    engine.unset_held("b")

                #   C2  #
                elif event.key == pygame.K_k:
                    engine.unset_held("c2")
                
                #   C#2  #
                elif event.key == pygame.K_o:
                    engine.unset_held("c#2")
                
                #   D2  #
                elif event.key == pygame.K_l:
                    engine.unset_held("d2")

                #   D#2  #
                elif event.key == pygame.K_p:
                    engine.unset_held("d#2")
                
                #   E2  #
                elif event.key == pygame.K_SEMICOLON:
                    engine.unset_held("e2")
                
                #   F2  #
                elif event.key == pygame.K_QUOTE:
                    engine.unset_held("f2")
                
                #   F#2  #
                elif event.key == pygame.K_RIGHTBRACKET:
                    engine.unset_held("f#2")
                
                #   G2  #
                elif event.key == pygame.K_RETURN:
                    engine.unset_held("g2")
                
                #   G#2  #
                elif event.key == pygame.K_BACKSLASH:
                    engine.unset_held("g#2")
                
                #   A2  #
                elif event.key == pygame.K_KP4:
                    engine.unset_held("a2")
                
                #   A#2  #
                elif event.key == pygame.K_KP8:
                    engine.unset_held("a#2")
                
                #   B2  #
                elif event.key == pygame.K_KP6 or event.key == pygame.K_5:
                    engine.unset_held("b2")

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
                