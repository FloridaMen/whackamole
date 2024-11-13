from random import randint

import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (mole_x*32) < event.pos[0] < (mole_x*32+32) and (mole_y*32) < event.pos[1] < (mole_y*32+32):
                        mole_x = randint(0, 19)
                        mole_y = randint(0, 15)
                        print(mole_x, " ", mole_y)
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*32+3, mole_y*32+3)))
            for i in range(20):
                pygame.draw.line(screen, "dark green", (i*32+32, 0), (i*32+32, 512))
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, i*32+32), (640, i*32+32))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
