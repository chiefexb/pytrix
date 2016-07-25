#!/usr/bin/python
import pygame
def main():
    size = (700, 500)
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")
    done = False
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
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
