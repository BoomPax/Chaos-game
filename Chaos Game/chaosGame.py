import random
import pygame


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.size = size



def chaosGame():

    # Initialize Pygame
    pygame.display.init()

    # Initialize the Clock
    clock = pygame.time.Clock()

    # Set the dimensions of the window
    windowWidth = 1925
    windowHeight = 1025
    window = pygame.display.set_mode((windowWidth, windowHeight))

    # Set the window captain and window color
    pygame.display.set_caption("Chaos Game")
    windowColor = [0, 0, 0]
    window.fill(windowColor)

    # Update the window


    
    
    p1 = Point(random.randint(0, windowWidth), random.randint(0, windowHeight))
    p2 = Point(random.randint(0, windowWidth), random.randint(0, windowHeight))
    p3 = Point(random.randint(0, windowWidth), random.randint(0, windowHeight))
    p4 = Point((p1.x + p2.x + p3.x)//3, (p1.y + p2.y+ p3.y)//3)
    
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    print(p3.x, p3.y)
    print(p4.x, p4.y)

    pygame.draw.circle(window, "green", (p1.x, p1.y), 10)
    pygame.draw.circle(window, "green", (p2.x, p2.y), 10)
    pygame.draw.circle(window, "green", (p3.x, p3.y), 10)
    pygame.draw.circle(window, "red", (p4.x, p4.y), 10)

    
    
    pygame.display.update()

    for x in range(0, 40000):
        pygame.draw.circle(window, "green", (p1.x, p1.y), 10)
        pygame.draw.circle(window, "green", (p2.x, p2.y), 10)
        pygame.draw.circle(window, "green", (p3.x, p3.y), 10)
        temp = random.randint(1, 3)
        if temp == 1:
            specialp = p1
            pygame.draw.circle(window, "blue", (p1.x, p1.y), 10)
        if temp == 2:
            specialp = p2
            pygame.draw.circle(window, "blue", (p2.x, p2.y), 10)
        if temp == 3:
            specialp = p3
            pygame.draw.circle(window, "blue", (p3.x, p3.y), 10)
        medianp = Point((p4.x + specialp.x)//2, (p4.y + specialp.y)//2)
        pygame.draw.circle(window, "white", (medianp.x, medianp.y), 10)
        p4 = Point(medianp.x, medianp.y)
        pygame.display.update()
        
    print(specialp)

    






    """Update your current coordinate point to be the median point you generated"""


if __name__ == "__main__":
    chaosGame()
