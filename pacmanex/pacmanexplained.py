import pygame

TILE_DIM = 20
LINES = 36
COL = 28
class Game(object):


    def _draw_maze(self, maze):
#       for x in range(TILE_DIM/2, COL * TILE_DIM  , TILE_DIM):
#           self.maze[(x,)]
       pass
           
       
    def get_maze(self):
        MAZE = {}
        if not self.MAZE:
            self.MAZE = _draw_maze()
        return self.MAZE
            
    def get_background(self):
        background = pygame.image.load('images/backgroundRoz.png')
        self.circle = pygame.draw.circle(background, (255, 200, 200), (190, 230), 2)
        self.circle = pygame.draw.circle(background, (255, 200, 200), (210, 230), 2)
        self.circle = pygame.draw.circle(background, (255, 200, 200), (190, 250), 2)
        self.circle = pygame.draw.circle(background, (255, 200, 200), (190, 270), 2)
        self.circle = pygame.draw.circle(background, (255, 200, 200), (30, 30), 2)
        return background

    def main(self, screen):
        # we don't want to use too much CPU in a while true loop
        # ww slow donw using a clock wihch tick (it s a sleep) ever 1/n-th second
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
#        self.player = Player(sprites)
        background = self.get_background()
    
        while 1:
            #clock.tick(20)
            dt = clock.tick(30) # gives me how long it passed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            #sprites.update()
            sprites.update(dt / 1000.)
            # we clear the screen with a fill color
#           screen.fill((200, 200, 200))
            screen.blit(background, (0,60))
#            screen.blit(image, (320, 240))
            sprites.draw(screen)
            # we draw on a buffer when ready we ask the display to start showing our new buffer
            # and the previously-dispalyed buffer it is our new drawing buffer
            pygame.display.flip()
if __name__=='__main__':
    pygame.init()
    screen= pygame.display.set_mode((560, 720))
    Game().main(screen)
    pygame.quit()
        
