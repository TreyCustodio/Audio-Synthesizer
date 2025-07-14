from modules import audio, instruments, sampler
#from beats import digital_storytelling, dress, firstup
from beatsnew import firstup, second, trap, how, new, training
from Tangible_Light.scripts import title

from UI import interface
from os import path


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



def main():
    """Main Function: Create any sounds you want"""

    #   Produce a beat  #
    #firstup.main()
    #second.main()
    #trap.main()
    #how.main()
    #title.main()
    #new.main()
    #training.main()


    #   Run the Interface   #
    interface.main()
    

    #   Test the Sampler    #
    # b = instruments.Bass()
    # note = b.note(audio.C1, 1.0)
    # print(note.pitch)
    # audio.write(note(), "", "test")

    #sampler.main()


if __name__ == '__main__':
    main()
    

    