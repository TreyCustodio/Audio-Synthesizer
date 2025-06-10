from modules import audio, instruments, sampler
#from beats import digital_storytelling, dress, firstup
from beatsnew import firstup, second, trap, how


from UI import interface

from os import path

#from UI import interface


# #import audio
# import hiphop
# import instruments

# #   Import the songs
# import writealone, blessup, unknown, rage, jiggy, yank


"""
Hier beginnt meine hören Projekt.
Author - Trey Custodio
"""

def text_sounds():
    """Generate textbox sound effects"""

    #   (1) Generate the sounds
    close = audio.text_close()
    interact = audio.text_next()
    text = audio.text()
    done = audio.text_done()
    sad = audio.text_sad()
    angry = audio.text_angry()


    #   (2) Save the sounds
    audio.write(close, "game" ,"text_close1")
    audio.write(interact, "game", "text_next1" )
    audio.write(text, "game", "text_2" )
    audio.write(done, "game", "text_done1" )
    audio.write(sad, "game", "text_sad1" )
    audio.write(angry, "game", "text_angry1" )



def generate_percussion():
    audio.sound_generator(envelope=audio.percussion, folder="percussion_gen", play_sounds=False)
    
def generate_snares():
    audio.sound_generator(envelope=audio.snare, folder="snare_gen")
    
def generate_strings():
    audio.sound_generator(envelope=audio.pluck, folder="string_gen", play_sounds=False)

def generate(instrument, folder, bpm = 160, octave = 4, typ=""):
    instr = instrument(octave, 1/(bpm / 60) * 4, typ)

    audio.write(instr.q_c, folder, "c")
    audio.write(instr.q_cs, folder, "c#")

    audio.write(instr.q_d, folder, "d")
    audio.write(instr.q_ds, folder, "d#")

    audio.write(instr.q_e, folder, "e")

    audio.write(instr.q_f, folder, "f")
    audio.write(instr.q_fs, folder, "f#")

    audio.write(instr.q_g, folder, "g")
    audio.write(instr.q_gs, folder, "g#")

    audio.write(instr.q_a, folder, "a")
    audio.write(instr.q_as, folder, "a#")

    audio.write(instr.q_b, folder, "b")



def main():
    """Main Function: Create any sounds you want"""

    #   Produce a beat  #
    #firstup.main()
    #second.main()
    #trap.main()
    #how.main()

    interface.main()


    #   Test the Sampler    #
    #sampler.main()


if __name__ == '__main__':
    main()
    

    