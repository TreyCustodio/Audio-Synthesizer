from modules import audio, instruments
#from beats import digital_storytelling, dress, firstup
# from beatsnew import firstup, second, trap, how, new, training
from Tangible_Light.scripts import title, journal, firstup, \
    o4, o5, o7, o8, fpdg, trap

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
    # text = audio.text()
    done = audio.text_done()
    # sad = audio.text_sad()
    # angry = audio.text_angry()


    #   (2) Save the sounds
    audio.write(close, "game" ,"text_close1")
    audio.write(interact, "game", "text_next1" )
    # audio.write(text, "game", "text_2" )
    audio.write(done, "game", "text_done1" )
    # audio.write(sad, "game", "text_sad1" )
    # audio.write(angry, "game", "text_angry1" )



def main():
    """Main Function: Create any sounds you want"""
    
    #   Run the Interface
    # interface.main()
    # text_sounds()

    #   Ask the User if they want to run the interface  #
    # print("Run interface? y/n: ", end="")
    # prompt = input()
    # if prompt == "y" or prompt == "Y":
    #     ##   Run the Interface   #
    #     interface.main()
    # elif prompt == "n" or prompt == "N":
    #     pass
    # else:
    #     print("\nInput Error: Please type 'Y', 'y', 'N', or 'n'")


    #   Tangible Light OST  #
    #   (1) Title   #
    # title.main()


    #   (2) Journaling #
    # journal.main()


    #   (3) First Up #
    # firstup.main()


    #   (4) 04 #
    # o4.main()
    

    #   (5) Page One    #
    # o5.main()


    #   (6) Boss Theme  #
    # trap.main()

    #   (7) Untitled    #
    # o7.main()

    #   (8) Untitled    #
    o8.main()
    
    

    #   Test the Sampler    #
    # b = instruments.Bass()
    # note = b.note(audio.C1, 1.0)
    # print(note.pitch)
    # audio.write(note(), "", "test")

    #sampler.main()


if __name__ == '__main__':
    main()
    

    