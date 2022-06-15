from time import *
from random import randint
import pygame
pygame.init()
window = pygame.display.set_mode((700, 500))
a = (200, 255, 255)
b = (255, 170, 124)
z = (255, 0, 0)

f1 = pygame.font.Font(None, 40)
t1 = 'Кликни'
question = f1.render(t1, True, (z))
window.fill(a)
clock = pygame.time.Clock()
game = True
FPS = 40
c = 50
d = 150
x = 0
for i in range(4):

    rect = pygame.Rect(c, d, 100, 200)
    pygame.draw.rect(window, b, rect)
    pygame.draw.rect(window, (252, 146, 0), rect, 1)
    c = c + 150
l = time()
while time() - l < 10:

    x = randint(1, 4)
    if x == 1:
        window.blit(question, (50, 225))
        rect = pygame.Rect(c, d, 100, 200)
        pygame.draw.rect(window, b, rect)
        pygame.draw.rect(window, (252, 146, 0), rect, 1)
    if x == 2:
        window.blit(question, (200, 225))
        rect = pygame.Rect(c, d, 100, 200)
        pygame.draw.rect(window, b, rect)
        pygame.draw.rect(window, (252, 146, 0), rect, 1)
    if x == 3:
        window.blit(question, (350, 225))
        rect = pygame.Rect(c, d, 100, 200)
        pygame.draw.rect(window, b, rect)
        pygame.draw.rect(window, (252, 146, 0), rect, 1)
    if x == 4:
        window.blit(question, (500, 225))
        for i in range(3):
            rect = pygame.Rect(c, d, 100, 200)
            pygame.draw.rect(window, b, rect)
            pygame.draw.rect(window, (252, 146, 0), rect, 1)
#jfgjdjugjudghfhg








while game:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
