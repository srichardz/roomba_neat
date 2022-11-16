import pygame

class Roomba:

    def __init__(self):
        self.user = False
        self.toKill = False

    def control(self):
        if self.user:
            keys = pygame.key.get_pressed()            
            if keys[pygame.K_w]:
                print("throttle")                    # ph, will add acceleration/throttle/brake/deceleration/turning later
            elif keys[pygame.K_s]:
                print("brake")
            if keys[pygame.K_a]:
                print("left")
            elif keys[pygame.K_d]:
                print("right")
