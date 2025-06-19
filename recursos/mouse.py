import pygame
def saida(event):
    if event.type == pygame.QUIT:
        quit()
def cliqueMouse(event,button,acao):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if button.collidepoint(event.pos):
            acao()