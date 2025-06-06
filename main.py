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
avarezaSubir=False
luxuriaLateral = False
velocidadeLuxuria = 0
velocidadeEspirito = 0
espiritoX = 500
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
    screen.blit(pecadoAtual, (pecadoX, pecadoY))
    pecadoY += velocidadePecado
    if pecadoAtual == luxuria:
        pecadoY = 0  # Fixa a altura da Luxúria

        # Inicialização do movimento lateral (somente na primeira vez)
        if not luxuriaLateral:
            lado = random.choice(['esquerda', 'direita'])
            if lado == 'esquerda':
                pecadoX = -luxuria.get_width()
                velocidadeLuxuria = velocidadePecadoBase
            else:
                pecadoX = screen.get_width()
                velocidadeLuxuria = -velocidadePecadoBase
            luxuriaLateral = True
            luxuriaVoltar = False  # Define para voltar depois

        pecadoX += velocidadeLuxuria

        # Quando entrar totalmente na tela, inverte direção para sair
        if not luxuriaVoltar and (0 <= pecadoX <= screen.get_width() - luxuria.get_width()):
            luxuriaVoltar = True
            velocidadeLuxuria *= -1  # Inverte direção

        # Quando sair da tela novamente, sorteia novo pecado
        if luxuriaVoltar and (pecadoX < -luxuria.get_width() or pecadoX > screen.get_width()):
            pecadoAtual = random.choice(pecados)
            pecadoX = random.randint(0, 900)
            pecadoY = -80
            velocidadePecado = velocidadePecadoBase
            luxuriaLateral = False
    if pecadoAtual == avareza:
        velocidadeAvareza = velocidadePecadoBase
        if not avarezaSubir and pecadoY <= 0:
            velocidadePecado = velocidadeAvareza  # Inverter para descer
            avarezaSubir = True
        elif avarezaSubir and pecadoY > 700:
            # Reset para novo pecado
            pecadoAtual = random.choice(pecados)
            pecadoX = random.randint(0, 900)
            if pecadoAtual == avareza:
                pecadoY = 700
                velocidadePecado = -velocidadeAvareza
                avarezaSubir = False
            else:
                pecadoY = -80
                velocidadePecado = velocidadePecadoBase
    else:
        # Pecado comum: se passou do fim da tela, troca
        if pecadoY > 700:
            velocidadePecadoBase+=1
            if primeiro_pecado:
                pecadoAtual=random.choice([pecado for pecado in pecados if pecado != avareza and pecado != luxuria])  # Evita avareza e luxuria no primeiro pecado
                primeiro_pecado = False
            else:
                pecadoAtual = random.choice(pecados)
            pecadoX = random.randint(0, 900)
            if pecadoAtual == avareza:
                velocidadeAvareza = velocidadePecadoBase
                pecadoY = 700
                velocidadePecado = -velocidadeAvareza
                avarezaSubir = False
            else:
                pecadoY = -80
                velocidadePecado = velocidadePecadoBase
    screen.blit(espirito, (espiritoX, 275))
    pygame.display.update()
