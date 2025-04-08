import numpy as np
import audio
import hiphop
import instruments

#   Import the songs
import writealone, blessup, unknown

"""
Hier beginnt meine hören Projekt.
Author - Trey Custodio
"""

def text_sounds():
    """Generate textbox sound effects"""

    #   (1) Generate the sounds
    close = audio.text_close()
    interact = audio.interact()
    text = audio.text()
    done = audio.text_done()

    #   (2) Save the sounds
    audio.save(close, "game" ,"close")
    audio.save(interact, "game", "interact" )
    audio.save(text, "game", "text_2" )
    audio.save(done, "game", "text_done" )

def generate_percussion():
    audio.sound_generator(envelope=audio.percussion, folder="percussion_gen", play_sounds=False)
    
def generate_snares():
    audio.sound_generator(envelope=audio.snare, folder="snare_gen")
    
def generate_strings():
    audio.sound_generator(envelope=audio.pluck, folder="string_gen", play_sounds=False)

def generate(instrument, folder, bpm = 160, octave = 4):
    instr = instrument(octave, 1/(bpm / 60) * 4)

    audio.save(instr.q_c, folder, "c")
    audio.save(instr.q_cs, folder, "c#")

    audio.save(instr.q_d, folder, "d")
    audio.save(instr.q_ds, folder, "d#")

    audio.save(instr.q_e, folder, "e")

    audio.save(instr.q_f, folder, "f")
    audio.save(instr.q_fs, folder, "f#")

    audio.save(instr.q_g, folder, "g")
    audio.save(instr.q_gs, folder, "g#")

    audio.save(instr.q_a, folder, "a")
    audio.save(instr.q_as, folder, "a#")

    audio.save(instr.q_b, folder, "b")



def main():
    """Main Function: Create any sounds you want"""

    #   (1) Components for Page One
    unknown.main()

    #   (2) Run some generations
    #generate(instruments.Skirt, "dream_gen", 160, 4)


if __name__ == '__main__':
    main()
    

    