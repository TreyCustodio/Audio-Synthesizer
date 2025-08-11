import os
import pygame

from .globals import *
from .utils import *
from .objects import *

from modules.beat import *
from modules.instruments import *
from modules.audio import *
# import matplotlib.pyplot as plt

from beatsnew import training


class Composer:
    """
    Handles the UI display and the back-end composition of the user's tracks
    """
    CURRENT_TRACK = training.TD(90)  # The track currently being edited: a Beat object
    WORKING_DIRECTORY = os.path.join("UI", "tracks")  # The directory where the track is being worked on
    EXPORT_DIRECTORY = None  # The directory where the track will be exported
    CURRENT_PAGE = 0
    PAGE = None
    NUMBERS = None
    SAVE = None
    EDIT = None
    VIEW = None
    SAVING = None  # The saving animation that displays when the track is being saved
        
    BUTTON = None
    INSTRUMENT = None
    TO_INSTRUMENTS = None
    INSTRUMENT_TEXT = None
    BEAT_INFO = None

    NEXT = None
    PREV = None
    JUMP = None

    M1 = None
    M2 = None

    #   Dictionary of Pressable Objects
    INSTRUMENTS = []
    BARS = []

    STATE = "view"


    """
    ------- UI Display -------
    """
    def init():
        """
        Initialize the Composer
        """
        #   Get the text that shows the current beat's metadata #
        if Composer.CURRENT_TRACK != None:
            track = Composer.CURRENT_TRACK
            font = pygame.font.Font(None, 24)
            text = font.render(f"Track: {track.fileName} | BPM: {track.bpm}", True, (0, 0, 0))
            Composer.BEAT_INFO = text
        else:
            Composer.BEAT_INFO = "Select a Beat to Edit"

        #   Get a reference to the current Beat's instrument dictionary #
        instruments = Composer.CURRENT_TRACK.instruments
        for i in instruments:

            #   Instrument 1    #
            frames = load_row(
                pygame.image.load(os.path.join("UI", "images", "composer", "instrument.png")),
                (69, 17), 4, 3, 0
            )

            ##  Blit the instrument name with an outline effect ##

            count = 0
            for frame in frames:
                #   (1) Get the Text Image  #
                font = pygame.font.Font(None, 36)

                if count == 0:
                    text = font.render(instruments[i][0].get_name(), True, (255,255,255))
                elif count == 1:
                    text = font.render(instruments[i][0].get_name(), True, (251,242,54))
                elif count == 2:
                    text = font.render(instruments[i][0].get_name(), True, (245,21,34))
                count += 1
                
                outline = font.render(instruments[i][0].get_name(), True, (0,0,0))

                img = Surface((text.get_width() + 2, text.get_height() + 2), pygame.SRCALPHA)

                ### Outline double for loop ###
                for dx in [-2, -1, 0, 1, 2]:
                    for dy in [-2, -1, 0, 1, 2]:
                        if dx != 0 or dy != 0:
                            img.blit(outline, (dx+1, dy+1))
                img.blit(text, (1,1))

                #   (2) Blit the text images to the background  #
                x,y = img.get_size()
                frame_x,frame_y = frame.get_size()
                frame.blit(img, vec(frame_x // 2 - x // 2, frame_y // 2 - y // 2))


            button = (Pressable((8, 96 * (i + 1)), frames))

            Composer.INSTRUMENTS.append(button)



        #   Page Display    #
        page_full = pygame.image.load(os.path.join("UI", "images", "composer", "page.png"))

        frames = load_row(
            page_full, (56, 17), 3, 1, 0
        )

        Composer.PAGE = Animated((WIDTH - frames[0].get_size()[0] - 8, 8), frames)

        #   Number Display   #
        frames = load_row(
            page_full, (14, 17), 3, 10, 1
        )
        Composer.NUMBERS = Animated((WIDTH - frames[0].get_size()[0] - 8, 11), frames)

        #   Edit    #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "edit.png")),
            (64, 18), 3, 3, 0
        )

        Composer.EDIT = Pressable((WIDTH - frames[0].get_size()[0] - 8, 8), frames)
        
        #   View    #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "view.png")),
            (69, 17), 3, 3, 0
        )

        Composer.VIEW = Pressable((8,8), frames)

        #   Save    #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "save.png")),
            (29, 16), 4, 3, 0
        )

        Composer.SAVE = Pressable((WIDTH // 2 - frames[0].get_size()[0] // 2, HEIGHT - frames[0].get_size()[1] - 8), frames)

        #   Saving...   #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "saving.png")),
            (68, 24), 6, 8, 1
        )
        Composer.SAVING = Animated((WIDTH // 2 - frames[0].get_size()[0] // 2, HEIGHT // 2 - frames[0].get_size()[1] // 2), frames)

        #   Back to Instruments #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "instruments.png")),
            (69, 17), 3, 3, 0
        )
        Composer.TO_INSTRUMENTS = Pressable((8,8), frames)

        #   Next Page   #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "next.png")),
            (56, 17), 4, 3, 0
        )
        Composer.NEXT = Pressable((WIDTH - 8 - frames[0].get_size()[0], HEIGHT - 8 - frames[0].get_size()[1]), frames)
        
        #   Prev Page   #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "next.png")),
            (56, 17), 4, 3, 1
        )
        Composer.PREV = Pressable((8, HEIGHT - 8 - frames[0].get_size()[1]), frames)

        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "next.png")),
            (56, 17), 4, 3, 2
        )
        Composer.JUMP = Pressable((WIDTH // 2 - frames[0].get_size()[0] // 2, HEIGHT - 8 - frames[0].get_size()[1]), frames)

        



        #   Generic Button for Testing  #
        frames = load_row(
            pygame.image.load(os.path.join("UI", "images", "composer", "button.png")),
            (27, 17), 4, 3, 0
        )
        Composer.BUTTON = Pressable((WIDTH // 2 - frames[0].get_size()[0] // 2, HEIGHT - frames[0].get_size()[1] * 2), frames)

        
    def reset():
        """
        Reset the Composer and free up memory
        """
        Composer.CURRENT_TRACK = training.TD(90)  # The track currently being edited: a Beat object
        Composer.WORKING_DIRECTORY = os.path.join("UI", "tracks")  # The directory where the track is being worked on
        
        Composer.EXPORT_DIRECTORY = None  # The directory where the track will be exported
        Composer.CURRENT_PAGE = 0
        Composer.PAGE = None
        Composer.NUMBERS = None
        Composer.SAVE = None
        Composer.EDIT = None
        Composer.VIEW = None
        Composer.SAVING = None  # The saving animation that displays when the track is being saved
        
        Composer.BUTTON = None
        Composer.TO_INSTRUMENTS = None
        Composer.INSTRUMENT = None
        Composer.INSTRUMENTS = []
        Composer.INSTRUMENT_TEXT = None
        Composer.BEAT_INFO = None



        Composer.NEXT = None
        Composer.PREV = None
        Composer.M1 = None
        Composer.M2 = None
        Composer.JUMP = None
        Composer.BARS = []
        Composer.STATE = "view"
    
    def draw(surf):
        """Display the UI"""
        # Background Color    #
        surf.fill((235, 235, 210))

        #   Background Outline  #
        rect = pygame.Rect((0, 0), (WIDTH, HEIGHT))
        pygame.draw.rect(surf, (0,0,0), rect, 4)

        #   Buttons #
        for i in Composer.get_buttons():
            i.draw(surf)

        #   Track Name and Metadata #
        text = Composer.BEAT_INFO
        surf.blit(text, (WIDTH // 2 - text.get_size()[0] // 2, 10))


        #   Viewing the Final Mix   #
        if Composer.STATE == "view":
            pass
            

        #   Editing the Track; Selecting Instruments    #
        elif Composer.STATE == "edit":
            pass


        #   Composing the instrument's section  #
        elif Composer.STATE == "instrument":
            text = Composer.INSTRUMENT_TEXT
            surf.blit(text, (WIDTH // 2 - text.get_size()[0] // 2, 32))

        
    

    """
    ------- Getters for the Composer Class -------
    """
    def get_working_directory():
        """
        Get the directory where the track is being worked on
        """
        return Composer.WORKING_DIRECTORY
    
    def get_export_directory():
        """
        Get the directory where the track will be exported
        """
        return Composer.EXPORT_DIRECTORY
    
    def get_current_track():
        """
        Get the current track being edited
        """
        return Composer.CURRENT_TRACK
    
    def get_current_track_name():
        """
        Get the name of the current track being edited
        """
        if Composer.CURRENT_TRACK != None:
            return Composer.CURRENT_TRACK.fileName
        return ""

    def get_bars():
        #   Get the current page    #
        page = Composer.CURRENT_PAGE

        #   Edge case; 2 bars on page 0 #
        if page == 0:
            if len(Composer.BARS) == 1:
                bars = [Composer.BARS[page]]
            else:
                bars = [Composer.BARS[page], Composer.BARS[page+1]]
                
        #   Otherwise check we only need to display 1 bar   #
        elif page+2 == len(Composer.BARS):
            bars = [Composer.BARS[page+1]]

        #   Display both bars on the page   #
        else:
            bars = [Composer.BARS[page+1], Composer.BARS[page+2]]

        return bars
    
    def get_buttons():
        state = Composer.STATE
        if state == "view":
            return [
                Composer.EDIT,
                Composer.SAVE
                ]

        elif state == "edit":
            return Composer.INSTRUMENTS +\
                  [
                    Composer.VIEW,
                    Composer.SAVE
                   ] 
        
        elif state == "instrument":
            #   Get the bars to display #
            bars = Composer.get_bars()

            return [
                Composer.TO_INSTRUMENTS,
                Composer.NEXT,
                Composer.PREV,
                Composer.PAGE,
                Composer.SAVE
            ] + bars

        else:
            return []
    
    """
    ------- Setters for the Composer Class -------
    """
    def set_working_directory(path=""):
        """
        Set the directory where the track is being worked on
        """
        Composer.WORKING_DIRECTORY = path

    def set_export_directory(path=""):
        """
        Set the directory where the track will be exported
        """
        Composer.EXPORT_DIRECTORY = path
    
    def set_current_track(track: Beat):
        """
        Set the current track being edited
        """
        Composer.CURRENT_TRACK = track


    """
    ------- Event Handling -------
    """
    def check_mouse(pos):
        Composer.SAVE.check_hovering(pos)

        for button in Composer.get_buttons():
            button.check_hovering(pos)


    def press_down():
        """Handle mouse press down events"""

        #   Save is always on screen    #
        if Composer.SAVE.get_hovered():
            Composer.SAVE.hold()
        
        else:
            for button in Composer.get_buttons():
                if button.get_hovered():
                    button.hold()

    def right_down(event):
        """Right click down"""
        if Composer.STATE == "instrument":
            for b in Composer.BARS:
                b.right_down(event)
        return
    

    def right_up(event):
        """Right click up"""
        if Composer.STATE == "instrument":
            for b in Composer.BARS:
                b.right_up(event)
        return

    
    def press_up():
        """Handle mouse press up events"""
        #   Save is always on screen    #
        if Composer.SAVE.get_held():
            Composer.SAVE.release()
            Composer.save()
        
        else:
            for button in Composer.get_buttons():
                if button.get_held():
                    button.release()

                    #   On View Screen  #
                    if Composer.STATE == "view":
                        ##  Transition to Edit State    #
                        if button == Composer.EDIT:
                            Composer.STATE = "edit"


                    #   On Edit Screen  #
                    elif Composer.STATE == "edit":
                        ## Transition to View State  #
                        if button == Composer.VIEW:
                            Composer.STATE = "view"
                    
                        ##  Transition to Instrument State  #
                        elif button in Composer.INSTRUMENTS:

                            #   Set the State and Instrument    #
                            Composer.STATE = "instrument"
                            Composer.INSTRUMENT = Composer.INSTRUMENTS.index(button)
                            
                            #   Set the Text    #
                            instr = Composer.CURRENT_TRACK.instruments[Composer.INSTRUMENT][0]
                            font = pygame.font.Font(None, 24)
                            Composer.INSTRUMENT_TEXT = font.render(f"Instrument: {instr.get_name()}", True, (225, 0, 0))

                            #   Load the bars from the beat into the Composer to create Buttons #
                            track = Composer.CURRENT_TRACK
                            instrument = track.instruments[Composer.INSTRUMENT][0]
                            bpm = track.bpm
                            bar_length = len(sine_wave(0, get_measure(bpm)))

                            ##  Temporary Vars length and notes track the bar's contents    #
                            length = 0.0
                            notes = []
                            bar_count = 1
                            counter = 0 # Track parity of the iteration
                            bar_num = 1 # Count each bar

                            wave1 = track.instruments[Composer.INSTRUMENT][1]
                            if wave1:
                                for note in wave1:
                                    notes.append(note)
                                    length += len(note)

                                    if length >= bar_length:

                                        ##   Check if the bar is overfilled  #
                                        if length > bar_length:
                                            print("BAR LENGTH WARNING: The current bar exceeds the maximum bar length")
                                        
                                        ##   Add the bar to the list of bars #
                                        if counter == 0:
                                            Composer.BARS.append(
                                                Bar((8, 64), bar_num, instrument, bpm, notes, full=True)
                                            )
                                            counter = 1

                                        elif counter == 1:
                                            Composer.BARS.append(
                                                Bar((WIDTH // 2, 64), bar_num, instrument, bpm, notes, full=True)
                                            )
                                            counter = 0
                                        
                                        ##  Reset notes and length; Increment bar count
                                        notes = []
                                        length = 0.0
                                        bar_count += 1
                                        bar_num += 1
                                
                                if notes:
                                    Composer.BARS.append(
                                                Bar((8, 64), bar_num, instrument, bpm, notes)
                                            )
                            else:
                                pass

                    #   On Instrument Screen    #
                    elif Composer.STATE == "instrument":
                        ##  Transition to Edit State    #
                        if button == Composer.TO_INSTRUMENTS:
                            Composer.STATE = "edit"
                            Composer.BARS = []
                            Composer.CURRENT_PAGE = 0
                        
                        ##  Click Next  #
                        elif button == Composer.NEXT:

                            # (1) Last page must be full
                            # (2) Current page + 1 < (number of bars / 2)
                                ##  e.g. 14 bars needs 7 pages
                                ##  page count starts at 0, so last page is really page 6
                                ##  Is 6+1 < 14 / 2?
                                ##  Is 7 < 7? -> NO; so there are no more pages

                            #   Edge case 1; 2 bars with 1 page
                            #   Is 0+1 < 2 /2?
                            #   Is 1 < 1? Nope

                            #   Edge case 2; 1 bars with 1 page
                            #   Is 0+1 < 1/2?
                            #   Is 1 < 0.5? Nope

                            #   Edge case 3; 3 bars with 2 pages
                            #   Is 1+1 < 3 / 2?
                            #   Is 2 < 1.5? Nope

                            if Composer.CURRENT_PAGE+1 < len(Composer.BARS) / 2:
                                Composer.CURRENT_PAGE += 1

                        ##  Click Prev  #
                        elif button == Composer.PREV:
                            if Composer.CURRENT_PAGE != 0:
                                Composer.CURRENT_PAGE -= 1
                
                
            
            
                

    """
    ------- Track Production -------
    """
    def save():
        """Save the current track to the working directory"""
        #   Get the Composer's Sate #
        state = Composer.STATE

        #   Get the Current Track   #
        track = Composer.CURRENT_TRACK

        #   Save the Instrument's sound wave    #
        if state == "instrument":
            #   Get Each Bar's notes #
            notes = []
            for bar in Composer.BARS:
                notes += bar.get_notes()
            
            #   Send the notes to the Beat  #
            print("Saving Instrument...")
            track.save_instrument(Composer.INSTRUMENT, notes)
            print("Save Complete")


        #   Produce the full beat #
        elif state == "view" or state == "edit":
            #   Produce the Full Beat   #
            track.produce_full()

            #   Save the Wave   #
            print("Saving Track...")
            write(track.get_production(), Composer.WORKING_DIRECTORY, track.fileName)
            print("Save Complete")

        

    def export():
        """Save and export the current track to the export directory"""
        track = Composer.CURRENT_TRACK
        write(track.get_production(), Composer.EXPORT_DIRECTORY, track.fileName)
    

    """
    ------- Updating -------
    """
    def update(seconds):
        if Composer.STATE == "saving":
            Composer.SAVING.update(seconds)
        return