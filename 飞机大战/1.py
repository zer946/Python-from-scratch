import pygame
pygame.init()
hero_rect=pygame.Rect(100,50,120,125)
print("英雄的原点%d  %d"%(hero_rect.x,hero_rect.y))
screen=pygame.display.set_mode()
bg=pygame.image.load(r"C:\Users\hp\PycharmProjects\untitled\Python one\Python-from-scratch-----\飞机大战\images\background2.jpg")
screen.blit(bg, (0,0))
pygame.display.update
her=pygame.image.load()

while True:
    pass
pygame.quit()