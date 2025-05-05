from modules import audio
from beats import digital_storytelling

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

    #   (1) Produce a beat
    #unknown.main(20, noIntro=True)
    #rage.main()
    #jiggy.main()
    #yank.main()
    #test.main()
    #bnw.main()
    #digital_storytelling.main()


    #   (2) Run some generations
    # generate(instruments.PianoBass, "dream_gen", 170, 2, "4")
    #generate(instruments.Symbol, "bass_1", 165, 4)
    #generate(instruments.Bass, "bass_1", 165, 1, "h")


    
    #   (3) Produce VG SFX
    #text_sounds()


    #   (4) Run the Interface
    #interface.main()


if __name__ == '__main__':
    main()
    

    