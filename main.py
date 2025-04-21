import numpy as np
import audio
import hiphop
import instruments

#   Import the songs
import writealone, blessup, unknown, rage, jiggy, yank

from beats import test

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
    audio.save(close, "game" ,"text_close1")
    audio.save(interact, "game", "text_next1" )
    audio.save(text, "game", "text_2" )
    audio.save(done, "game", "text_done1" )
    audio.save(sad, "game", "text_sad1" )
    audio.save(angry, "game", "text_angry1" )



def generate_percussion():
    audio.sound_generator(envelope=audio.percussion, folder="percussion_gen", play_sounds=False)
    
def generate_snares():
    audio.sound_generator(envelope=audio.snare, folder="snare_gen")
    
def generate_strings():
    audio.sound_generator(envelope=audio.pluck, folder="string_gen", play_sounds=False)

def generate(instrument, folder, bpm = 160, octave = 4, typ=""):
    instr = instrument(octave, 1/(bpm / 60) * 4, typ)

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

    #   (1) Produce a beat
    #unknown.main(20, noIntro=True)
    #rage.main()
    #jiggy.main()
    yank.main()
    #test.main()


    #   (2) Run some generations
    # generate(instruments.PianoBass, "dream_gen", 170, 2, "4")
    #generate(instruments.Symbol, "bass_1", 165, 4)
    #generate(instruments.Bass, "bass_1", 165, 1, "h")


    
    #   (3) Produce VG SFX
    #text_sounds()

if __name__ == '__main__':
    main()
    

    