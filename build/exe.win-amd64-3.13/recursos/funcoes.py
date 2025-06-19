import pygame
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

con=sqlite3.connect("log.dat")
cur=con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pontuacao INTEGER NOT NULL,
    data TEXT NOT NULL,
    hora TEXT NOT NULL
)
''')
def mostrar_ranking(screen,fonte,x,y,cor):
    con=sqlite3.connect("log.dat")
    con=con.cursor()
    cur.execute("SELECT pontuacao,data,hora FROM log ORDER BY id DESC LIMIT 5")
    log=cur.fetchall()
    for i, (pontos,data,hora) in enumerate(log):
        texto_pontos=fonte.render(f"{pontos} pontos, no dia {data} ás {hora}",True, cor)
        screen.blit(texto_pontos,(x,y+i*40))
