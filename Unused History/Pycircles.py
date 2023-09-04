import pygame
import sys
import random
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Moving Circles")
    circle_coords = []
    for i in range(10):
        circle_coords.append((random.randint(0, 640), random.randint(0, 480)))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))

        for i in circle_coords:
            i = (i[0] + random.randint(-10, 10), i[1] + random.randint(-10, 10))
            pygame.draw.circle(screen, (255, 0, 0), i, 30)


        # boundry collision detection
        for i in circle_coords:
            if i[0] < 0:
                i[0] = 0
            if i[0] > 640:
                i[0] = 640
            if i[1] < 0:
                i[1] = 0
            if i[1] > 480:
                i[1] = 480

        # circle collision detection
        for i in circle_coords:
            for j in circle_coords:
                if i != j:
                    if i[0] + 30 > j[0] - 30 and i[0] - 30 < j[0] + 30 and i[1] + 30 > j[1] - 30 and i[1] - 30 < j[1] + 30:
                        print("collision")



        time.sleep(0.1)
        pygame.display.flip()

if __name__ == "__main__":
    main()