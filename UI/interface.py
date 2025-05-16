import pygame
from .engine import Engine
from .events import EventManager

"""
This file contains the main routine to pass
for each frame of the GUI.
"""

"""
(1) - Setup
"""

#   Constants   #
RESOLUTION = (776, 302)

SCALE = 1
UPSCALED = RESOLUTION * SCALE


def main():
    #   Initialize modules  #
    pygame.init()
    pygame.font.init()
    pygame.mixer.pre_init(44100, size=-16, channels = 1, allowedchanges=0)
    pygame.mixer.init()


    #   Set the screen up   #
    flags = pygame.SCALED #| pygame.NOFRAME | pygame.FULLSCREEN
    screen = pygame.display.set_mode(list(map(int, UPSCALED)), flags=flags)
    drawSurface = pygame.Surface(list(map(int, RESOLUTION)))
    drawSurface.fill((255,255,255))


    #   Set mouse visible   #
    pygame.mouse.set_visible(True)

    #   Set application icon    #
    # iconSurf = pygame.Surface((32,32))
    # image = pygame.image.load("displayIcon.png").convert()
    # iconSurf.blit(image, (0,0))
    # pygame.display.set_icon(iconSurf)


    #   Initialize the engine and eventManager  #
    engine = Engine()
    eventManager = EventManager()



    """
    (2) - Run Routine
    """

    gameClock = pygame.time.Clock()
    RUNNING = True
    while RUNNING:
        
        #   (1) Draw    #
        pygame.transform.scale(drawSurface,
                            list(map(int, UPSCALED)),
                            screen)
        pygame.display.flip()

        engine.draw(drawSurface)

        ##   For displaying logo; used in War and Keys but not here yet
        # if EventManager.startup:
        #     gameEngine.drawLogo(drawSurface)
        # else:
        #     gameEngine.draw(drawSurface)
        # gameEngine.drawFade(drawSurface)
        

        #   (2) Handle events   #
        EventManager.handleEvents(engine)


        #   (3) Update  #
        
        # if EventManager.readyToUpdate():
            
        #     gameClock.tick(60)
        #     seconds = gameClock.get_time() / 1000

        #     ##  Extra code used in war and keys for buffering and transitioning
        #     # if EventManager.startup:
        #     #     if EventManager.transitioning:
        #     #         if gameEngine.fade_on == False:
        #     #             EventManager.startup = False
        #     #             EventManager.transitioning = False
        #     #             gameEngine.fade_off = True

        #     #     else:
        #     #         EventManager.updateTimer(seconds, gameEngine)
            
        #     # EventManager.updateBuffer(seconds) 
            
        #     if EventManager.ready:
        #         gameEngine.update(seconds)
            


    #   Quit if not running
    pygame.quit()
