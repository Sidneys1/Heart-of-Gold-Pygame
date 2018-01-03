import sys, pygame

from pygame.locals import *

from .background import Background

if __name__ == "__main__":
    pygame.init()

    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    b = Background('./tiles', (500, 500))
    ball = pygame.image.load("ball.bmp").convert()
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        b.draw(screen, (0, 0))
        screen.blit(ball, ballrect)
        pygame.display.flip()

