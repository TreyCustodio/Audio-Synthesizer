#   Import Modules  #
from modules.audio import *
from modules import instruments
from os import path

#   Import the Interface    #
from UI import interface

#   Old Beats   #
# from beats import digital_storytelling, dress
# from beatsnew import second, trap, how, new, training
# from beatsnew import pan


#   Tangible Light  #
from Tangible_Light.scripts import \
    o1, o2, o3, \
    o4, o5, o6, \
    o7, o8, o9, \
    o10, o11,  \
    fpdg

#   AMTR OST    #
from AMTR.scripts import \
    title, middle, over, intro, ff, name, o7, ptw, bio, \
    silent, ice, fpdg, rev1, temp, o14, o15, o16

#   Random Projects #
# import l, sein

#   Paths for quick exporting   #
AMTR_SFX = os.path.join(os.getcwd(), os.pardir, "AMTR", "sfx")
AMTR_MENU = os.path.join(os.getcwd(), os.pardir, "AMTR", "sfx", "menu")
AMTR_TEXT = os.path.join(os.getcwd(), os.pardir, "AMTR", "sfx", "text")




"""
Hier beginnt meine hören Projekt.
Author - Trey Custodio
"""

def text_sounds():
    """Generate textbox sound effects"""

    #   (1) Generate the sounds
    close = audio.text_close()
    interact = audio.text_next()
    done = audio.text_done()


    #   (2) Save the sounds
    audio.write(close, "game" ,"text_close1")
    audio.write(interact, "game", "text_next1" )
    audio.write(done, "game", "text_done1" )

def sfx():
    """Generate a sound effect(s)"""
    instr = instruments.Menu_1()

    #   Audio 1
    sound = instr.n(F3, 0.3)()
    write(sound, "game", os.path.join(AMTR_MENU, "menu_1"), volume_factor=1_000)

    #   Audio 2
    sound = instr.n(D3, 0.3)()
    write(sound, "game", os.path.join(AMTR_MENU, "menu_2"), volume_factor=1_000)

def player():
    interface.main()

def main():
    """Main Function: Create any sounds you want"""
    #   ---------- Interface Control ----------  #
    #   Run the Interface   #
    # interface.main()
    


    #   ---------- Sound Effects ----------  #
    # sfx()
    # text_sounds()



    #   ---------- One-offs ----------  #
    #   Singles    #
    # experiments.main()
    # pan.main()
    # l.main()
    # sein.main()
    # ff.main()
    

    

    #   ---------- AMTR OST ----------  #
    # temp.main()

    #   Side A  #

    #   01 - Title Beat
    # title.main()

    #   02 - Welcome to Earth
    # intro.main()

    #   03 - Name Him
    name.main()

    #   04 - Middle Ground Main
    # middle.main()

    #   05 - Middle Ground Biotech
    # bio.main()

    #   06 - Underground Fire

    #   07 - Frozen Core
    # ice.main()

    #   08 - Overground Entrance
    # over.main()

    #   09 - Overground Peak
    

    #   Side B  #
    #   10 - Silent Dreams
    # silent.main()

    #   11 - Pave the Way
    # ptw.main()

    #   12 - Scripted Encounter
    # fpdg.main()
    
    #   13 - Reverie 1
    # rev1.main()

    #   14 - 
    # o14.main()

    #   15 -
    # o15.main()

    #   16 - Earth's Revival
    # o16.main()

    #   17 - Final Boss

    #   18 - Credits




    #   ---------- Tangible Light ----------  #
    #   01 - Title   #
    # o1.main()


    #   02 - Journaling #
    # o2.main()


    #   03 - First Up
    # o3.main()


    #   04 - 04 #
    # o4.main()
    
    #   05 - Page One
    # o5.main()


    # #   (6) Boss Theme  #
    # o6.main()

    # #   (7) Untitled    #
    # o7.main()

    # #   (8) Death by Defualt    #
    # o8.main()
    
    # #   (9) Surprise    #
    # o9.main()

    # #   (10) Surprise    #
    # o10.main()

    # #   (11) Pac type beat  #
    # o11.main()



if __name__ == '__main__':
    main()