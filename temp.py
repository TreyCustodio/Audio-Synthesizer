#   playr Button:
        ##  Sprite Size: (46, 12)
        ##  Sheet Size: (96, 12)
        scale = 4
        size = (46, 12)
        play_full = pygame.image.load(os.path.join("UI", "images", "main", "play.png"))
        
        #   Frame 1 of play  #
        play_1 = pygame.Surface((46, 12))
        for y in range(12):
            for x in range(46):
                play_1.blit(
                    play_full, (x, y), pygame.Rect((x,y), (1,1))
                    )
        
        self.play_1 = pygame.transform.scale(play_1, (size[0] * scale, size[1] * scale))


        #   Frame 2 of play (Mouse Hovering Over)    #
        play_2 = pygame.Surface((46, 12))
        for y in range(12):
            for x in range(46, 96):
                play_2.blit(
                    play_full, (x - 46, y), pygame.Rect((x,y), (1,1))
                    )
        
        self.play_2 = pygame.transform.scale(play_2, (size[0] * scale, size[1] * scale))