import pygame
import time
import pyttsx3
import sqlite3
from datetime import datetime
engine = pyttsx3.init()
pygame.init()
def button(screen, x, y, largura, altura, texto , fonte, corTexto=(255,255,255)):
    botao=pygame.Rect(x,y,largura,altura)
    textoRender=fonte.render(texto,True,corTexto)
    textoRect=textoRender.get_rect(center=botao.center)
    screen.blit(textoRender,textoRect)
    return botao
def saida(event):
    if event.type == pygame.QUIT:
        quit()
def cliqueMouse(event,button,acao):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if button.collidepoint(event.pos):
            acao()
def aguarde(sec):
    time.sleep(sec)
def resetEngine():
    global engine
    try:
        engine.endLoop()
    except:
        pass
    engine = pyttsx3.init()
