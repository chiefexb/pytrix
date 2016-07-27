#!/usr/bin/python
import pygame
class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
def main():
    size = (700, 500)
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")
    done = False
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    black=(50,50,50)
    bl=    (0,1,0,
           0,1,1,
           0,0,1)
    b=Block
    b.width=50
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.fill(WHITE)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()
