import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Profanum Samsarae")
background = pygame.image.load("recursos/universeBackground.png")
movimentoBackground = -100
velocidadeeBackground = 0
orgulho= pygame.image.load("recursos/abstrataOrgulho.png")
luxuria = pygame.image.load("recursos/abstrataLuxuria.png")
avareza = pygame.image.load("recursos/abastrataAvareza.png")
gula = pygame.image.load("recursos/abstrataGula.png")
ira = pygame.image.load("recursos/abstrataIra.png")
inveja= pygame.image.load("recursos/abstrataInveja.png")
preguica = pygame.image.load("recursos/abstrataPreguica.png")
espirito = pygame.image.load("recursos/espirito.png")
demiurge = pygame.image.load("recursos/demiurge.png")
pecados= [orgulho, luxuria, avareza, gula, ira, inveja, preguica]
pecadoAtual = random.choice(pecados)
pecadoX = random.randint(0, 900)
pecadoY = -80
velocidadePecadoBase = 1
velocidadePecado = velocidadePecadoBase
avarezaMovimento = False
luxuriaMovimento = False
preguicaMovimento = False
espiritoX = 500
velocidadeEspirito = 0
movimentoXDemiurge = 300
movimentoYDemiurge = 100
velocidadeXdemiurge = 0
velocidadeYdemiurge = 0
primeiro_pecado = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               velocidadeEspirito = -10
               velocidadeeBackground=1
            if event.key == pygame.K_RIGHT:
                velocidadeEspirito = 10
                velocidadeeBackground = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velocidadeEspirito = 0
                velocidadeeBackground = 0
            if event.key == pygame.K_RIGHT:
                velocidadeEspirito = 0
                velocidadeeBackground = 0
    movimentoBackground += velocidadeeBackground
    espiritoX += velocidadeEspirito
    velocidadeXdemiurge=random.choice([-1, 1])
    velocidadeYdemiurge=velocidadeXdemiurge
    if movimentoXDemiurge < 0:
        movimentoXDemiurge = 0
    elif movimentoXDemiurge > 700:
        movimentoXDemiurge = 700
    if movimentoYDemiurge < 0:
        movimentoYDemiurge = 0
    elif movimentoYDemiurge > 500:
        movimentoYDemiurge = 500
    movimentoXDemiurge += velocidadeXdemiurge
    movimentoYDemiurge += velocidadeYdemiurge  
    if movimentoBackground>0:
        movimentoBackground=0
    elif movimentoBackground<-122:
        movimentoBackground=-122
    if espiritoX < -5:
        espiritoX = -5
    elif espiritoX > 875:
        espiritoX = 875
    screen.blit(background, (movimentoBackground, 0))
    screen.blit(demiurge, (movimentoXDemiurge,movimentoYDemiurge))
    if not (luxuriaMovimento and pecadoAtual == luxuria or avarezaMovimento and pecadoAtual == avareza or preguicaMovimento and pecadoAtual == preguica):
        pecadoY += velocidadePecado
        if pecadoY > 700:
            velocidadePecadoBase+=1
            velocidadePecado = velocidadePecadoBase
            pecadoAtual = random.choice(pecados)
            pecadoX=random.randint(0, 900)
            pecadoY= -80
    if not preguicaMovimento and pecadoAtual == preguica:
        pecadoX=500
        pecadoY=-700
        descendoPreguica = True
        subindoPreguica = False
        preguicaMovimento = True
    if preguicaMovimento:
        if descendoPreguica:
            pecadoY+= velocidadePecado
            if pecadoY>=-80:
                descendoPreguica=False
                subindoPreguica=True
        elif subindoPreguica:
            pecadoY-=velocidadePecado
            if pecadoY<=-800:
                preguicaMovimento = False
                pecadoAtual = random.choice(pecados)
                pecadoX = random.randint(0, 900)
                pecadoY = -80
    if not luxuriaMovimento and pecadoAtual==luxuria:
        pecadoX=1100
        pecadoY=0
        indoLuxuria=True
        voltandoLuxuria=False
        luxuriaMovimento = True
    if luxuriaMovimento:
        if indoLuxuria:
            pecadoX-=velocidadePecado
            if pecadoX<=500:
                indoLuxuria=False
                voltandoLuxuria=True
        elif voltandoLuxuria:
            pecadoX+=velocidadePecado
            if pecadoX>=1200:
                luxuriaMovimento = False
                pecadoAtual = random.choice(pecados)
                pecadoX = random.randint(0, 900)
                pecadoY = -80
    if not avarezaMovimento and pecadoAtual == avareza:
        pecadoY=800
        pecadoX=random.randint(0, 900)
        subindoAvareza = True
        descendoAvareza = False
        avarezaMovimento = True
    if avarezaMovimento:
        if subindoAvareza:
            pecadoY -= velocidadePecado
            if pecadoY <= 0:
                subindoAvareza = False
                descendoAvareza = True
        elif descendoAvareza:
            pecadoY += velocidadePecado
            if pecadoY >= 700:
                avarezaMovimento = False
                pecadoAtual = random.choice(pecados)
                pecadoX = random.randint(0, 900)
                pecadoY = -80
    screen.blit(pecadoAtual, (pecadoX, pecadoY))
    screen.blit(espirito, (espiritoX, 275))
    pygame.display.update()
