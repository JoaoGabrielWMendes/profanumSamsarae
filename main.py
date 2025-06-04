import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Profanum Samsarae")
background = pygame.image.load("recursos/universeBackground.png")
orgulho= pygame.image.load("recursos/abstrataOrgulho.png")
luxuria = pygame.image.load("recursos/abstrataLuxuria.png")
avareza = pygame.image.load("recursos/abstrataAvareza.png")
gula = pygame.image.load("recursos/abstrataGula.png")
ira = pygame.image.load("recursos/abstrataIra.png")
inveja= pygame.image.load("recursos/abstrataInveja.png")
preguica = pygame.image.load("recursos/abstrataPreguica.png")
espirito = pygame.image.load("recursos/espirito.png")
demiurge = pygame.image.load("recursos/demiurge_no_bg.png")
pecados= [orgulho, luxuria, avareza, gula, ira, inveja, preguica]
pecadoAtual = random.choice(pecados)
pecadoX = random.randint(0, 900)
pecadoY = -100
velocidade_pecado = 5
velocidadeEspirito = 0
espiritoX = 500
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               velocidadeEspirito = -10
            if event.key == pygame.K_RIGHT:
                velocidadeEspirito = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velocidadeEspirito = 0
            if event.key == pygame.K_RIGHT:
                velocidadeEspirito = 0
    espiritoX += velocidadeEspirito
    if espiritoX < -15:
        espiritoX = -15
    elif espiritoX > 925:
        espiritoX = 925
    screen.blit(background, (0, 0))
    screen.blit(demiurge, (200, 50))
    screen.blit(pecadoAtual, (pecadoX, pecadoY))
    pecadoY += velocidade_pecado
    if pecadoY > 700:
        pecadoAtual = random.choice(pecados)
        pecadoX = random.randint(0, 900)
        pecadoY = -100
    screen.blit(espirito, (espiritoX, 350))
    pygame.display.update()
