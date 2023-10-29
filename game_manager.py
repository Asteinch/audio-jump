import pygame
import threading    

from Code.Managers.audio_manager      import audioManager
from Code.Managers.collision_manager  import collisionManager

from Code.Objects.player import Player
from Code.Objects.cactus import Cacti
from Code.Objects.bird   import Bird


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TITLE = 'Audio Jump'

WHITE = (230, 230, 230)

FPS = 60

class gameManager:

    def __init__(self):

        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
    
        self.setup_classes()
        self.start_thread()

    def start_thread(self):

        # Starts Threading for audio streaming
        self.currentThread = threading.Thread(target = self.audioManager.handle_data)
        self.currentThread.start()
    
    def setup_classes(self):

        self.audioManager = audioManager()
        self.collisionManager = collisionManager()

        self.player = Player(pygame.image.load("./assets/him.png"),
                             (200, 100))
        
        self.bird = Bird()
        
        self.hostiles = [Cacti()]
        self.collisionManager.add_hostile(self.hostiles[0])
           

    def draw(self):

        self.win.fill(WHITE)

        self.player.draw(self.win)

        self.bird.draw(self.win)
        
        for hostile in self.hostiles:
            hostile.draw(self.win)

        pygame.draw.line(self.win, "black", (0, 500), (1280, 500), 5)



    def update(self):

        self.player.update()
        self.player.jump(self.audioManager)

        self.bird.update()

        for hostile in self.hostiles:
            hostile.update()
        
        self.collisionManager.update_pos(self.hostiles)
        
        #print(self.collisionManager.is_player_collideing(self.player))
       

        pygame.display.update()
        self.clock.tick(FPS)


    def event_loop(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:

                self.audioManager.terminate_streaming()
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
   
                    self.player.jump(self.audioManager)

    def main_loop(self):

        while True:

            self.event_loop()
            self.update()
            self.draw()

    def start_game(self):

        self.main_loop()


gameWindow = gameManager()
gameWindow.start_game()
    

    

