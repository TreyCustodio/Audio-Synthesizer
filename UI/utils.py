import pygame
import numpy as np

def load_row(full_image, sprite_size, scale, frames, row):
    """Load a row of sprites from a sheet.
    Returns a list of Surfaces containing each frame
    of the row.
    """
    #   Keep track of each sprite frame in the row  #
    sprites = []
    size = sprite_size

    #   Keep track of the current frame #
    frame_counter = 0

    #   Loop through each frame in the row  #
    for i in range(frames):

        #   Initialize an empty surface #
        sprite = pygame.Surface(size, pygame.SRCALPHA)

        #   Blit each pixel from the current frame of the full sheet onto the sprite #
        for y in range(size[1]):
            for x in range(size[0] * (i), size[0] * (i+1)):
                sprite.blit(
                    full_image, (x - (size[0] * frame_counter), y), pygame.Rect((x,y + (size[1] * row)), (1,1))
                    )
        
        #   Scale the image if desired  #
        sprite = pygame.transform.scale(sprite, (size[0] * scale, size[1] * scale))
        
        #   Append the sprite to the list of sprites    #
        sprites.append(sprite)
        
        #   Increment the frame counter
        frame_counter += 1
    
    return sprites


"""
Vector Utility provided by
Dr. Liz Matthews
"""

def vec(*args):
    return np.array((args)).astype(float)

def normalize(vector):
    """Normalize a numpy array."""
    mag = magnitude(vector)
    if mag == 0.0:
        return np.array((1,0,0)).astype(float)
    return vector / mag
   
def magnitude(vector):    
    """Give the magnitude of a vector."""
    return np.linalg.norm(vector)

def scale(vector, length):
   """Scales the magnitude of vec to the length.
      First normalizes then scales to appropriate size."""
   return normalize(vector) * length

def rectAdd(vector, rect):
   """Moves the pygame rect top left by vector.
      Returns a rect."""   
   newRect = pygame.Rect(rect.left + vector[0], rect.top + vector[1],
                  rect.width, rect.height)
   
   return newRect
   
