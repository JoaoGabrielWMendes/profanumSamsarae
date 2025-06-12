import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Profanum Samsarae")
backgroundFrames = []
for i in range (4):
    frame=pygame.image.load(f"recursos/universeBackground{i}.png").convert_alpha()
    backgroundFrames.append(frame)
backgroundIndex = 0
tempoUltimoFrame = pygame.time.get_ticks()
fps=pygame.time.Clock()
intervaloBackground=300
movimentoBackground = -100
velocidadeeBackground = 0
orgulho= pygame.image.load("recursos/abstrataOrgulho.png")
luxuria = pygame.image.load("recursos/abstrataLuxuria.png")
avareza = pygame.image.load("recursos/abstrataAvareza.png")
gula = pygame.image.load("recursos/abstrataGula.png")
ira = pygame.image.load("recursos/abstrataIra.png")
inveja= pygame.image.load("recursos/abstrataInveja.png")
preguica = pygame.image.load("recursos/abstrataPreguica.png")
espirito = pygame.image.load("recursos/espirito.png")
demiurge = pygame.image.load("recursos/demiurge.png")
tituloStart=pygame.image.load("Recursos/profanumSamsaraeInicial.png")
fontePixelada= pygame.font.Font("recursos/fontePixels.ttf", 20)
fontePixeladaStart=pygame.font.Font("recursos/fontePixels.ttf", 35)
backgroundIndex = 0
tempoUltimoFrame = pygame.time.get_ticks()
intervaloBackground=300
movimentoBackground = -100
velocidadeeBackground = 0
fonteJogo=pygame.font.SysFont("comic sans", 14)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
def jogar():
    backgroundIndex = 0
    tempoUltimoFrame = pygame.time.get_ticks()
    intervaloBackground=300
    movimentoBackground = -100
    velocidadeeBackground = 0
    pecados= [orgulho, luxuria, avareza, gula, ira, inveja, preguica]
    pecadoAtual = random.choice(pecados)
    pecadoX = random.randint(0, 840)
    pecadoY = -80
    velocidadePecadoBase = 1
    velocidadePecado = velocidadePecadoBase
    avarezaMovimento = False
    luxuriaMovimento = False
    preguicaMovimento = False
    espiritoX = 500
    velocidadeEspirito = 0
    velocidadeXdemiurge = 0
    velocidadeYdemiurge = 0
    modoDemiurge = "orbital"
    alvoOrbitaX=0
    alvoOrbitaY=0
    tempoPerseguir=0
    tempoMaximoPerseguir=random.randint(300, 1000)
    chancePerseguir=0.001
    distanciaPerseguir=100
    centroX=500
    centroY=300
    raioX=215
    raioY=260
    angulo=0
    velocidadeAngular=0.05
    contadorInversao=0
    tempoInversao=random.randint(180, 600)
    alturaEspirito=160
    larguraEspirito=120
    alturaAvareza=760
    larguraAvareza=101
    alturaLuxuria=700
    larguraLuxuria=700
    alturaPreguica=612
    larguraPreguica=338
    larguraPecado=125
    alturaPecado=160
    fonteJogoPausado=pygame.font.Font("recursos/fontePixels.ttf", 74)
    dificuldade = 30
    karmaPontos = 0
    pausado= False
    while True:
        screen.fill((0, 0, 0))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = not pausado
        if not pausado:
                agora = pygame.time.get_ticks()
                if agora - tempoUltimoFrame > intervaloBackground:
                    tempoUltimoFrame = agora
                    backgroundIndex = (backgroundIndex + 1) % len(backgroundFrames)
                if movimentoBackground>0:
                    movimentoBackground=0
                elif movimentoBackground<-122:
                    movimentoBackground=-122
                if espiritoX < -5:
                    espiritoX = -5
                elif espiritoX > 875:
                    espiritoX = 875
                movimentoBackground += velocidadeeBackground
                screen.blit(backgroundFrames[backgroundIndex], (movimentoBackground, 0))
                espiritoX += velocidadeEspirito
                if modoDemiurge == "orbital":
                    angulo+=velocidadeAngular
                    movimentoXDemiurge = centroX + math.cos(angulo)*raioX
                    movimentoYDemiurge = centroY + math.sin(angulo)*raioY
                    contadorInversao += 1
                    if contadorInversao >= tempoInversao:
                        velocidadeAngular*= -1
                        contadorInversao = 0
                        tempoInversao = random.randint(180, 600)
                    if chancePerseguir > random.random():
                        modoDemiurge = "perseguir"
                        tempoPerseguir = 0
                elif modoDemiurge == "perseguir":
                    dx= espiritoX - movimentoXDemiurge
                    dy= 275 - movimentoYDemiurge
                    distancia = math.hypot(dx, dy)
                    if distancia >distanciaPerseguir:
                        velocidadeXdemiurge = dx / distancia
                        velocidadeYdemiurge = dy / distancia
                    velocidadePerseguir=3
                    movimentoXDemiurge += velocidadeXdemiurge * velocidadePerseguir
                    movimentoYDemiurge += velocidadeYdemiurge * velocidadePerseguir
                    tempoPerseguir += 1
                    if tempoPerseguir >= tempoMaximoPerseguir:
                        alvoOrbitaX = centroX + math.cos(angulo) * raioX
                        alvoOrbitaY = centroY + math.sin(angulo) * raioY
                        modoDemiurge = "retornar"
                        tempoMaximoPerseguir = random.randint(300, 1000)
                elif modoDemiurge == "retornar":
                    dx = alvoOrbitaX - movimentoXDemiurge
                    dy = alvoOrbitaY - movimentoYDemiurge
                    distancia = math.hypot(dx, dy)
                    if distancia > 1:
                        velocidadeXdemiurge = dx / distancia
                        velocidadeYdemiurge = dy / distancia 
                        velocidadeRetorno = 3
                        movimentoXDemiurge += velocidadeXdemiurge * velocidadeRetorno
                        movimentoYDemiurge += velocidadeYdemiurge * velocidadeRetorno
                    else:
                        modoDemiurge="orbital"
                pixelsEspiritoX=list(range(espiritoX, espiritoX + larguraEspirito))
                pixelsEspiritoY=list(range(275, 275 + alturaEspirito))
                pixelsAvarezaX=list(range(pecadoX, pecadoX + larguraAvareza))
                pixelsAvarezaY=list(range(pecadoY, pecadoY + alturaAvareza))
                pixelsLuxuriaX=list(range(pecadoX, pecadoX + larguraLuxuria))
                pixelsLuxuriaY=list(range(pecadoY, pecadoY + alturaLuxuria))
                pixelsPreguicaX=list(range(pecadoX, pecadoX + larguraPreguica))
                pixelsPreguicaY=list(range(pecadoY, pecadoY + alturaPreguica))
                pixelsPecadoX=list(range(pecadoX, pecadoX + larguraPecado))
                pixelsPecadoY=list(range(pecadoY, pecadoY + alturaPecado))
                if not (luxuriaMovimento and pecadoAtual == luxuria or avarezaMovimento and pecadoAtual == avareza or preguicaMovimento and pecadoAtual == preguica):
                    pecadoY += velocidadePecado
                    if len(set(pixelsPecadoX).intersection(set(pixelsEspiritoX)))>dificuldade:
                        if len(set(pixelsPecadoY).intersection(set(pixelsEspiritoY)))>dificuldade:
                            start()
                    if pecadoY > 700:
                        karmaPontos+= 1
                        velocidadePecadoBase+=1
                        velocidadePecado = velocidadePecadoBase
                        pecadoAtual = random.choice(pecados)
                        pecadoX=random.randint(0, 840)
                        pecadoY= -80
                if not preguicaMovimento and pecadoAtual == preguica:
                    pecadoX=500
                    pecadoY=-700
                    descendoPreguica = True
                    subindoPreguica = False
                    preguicaMovimento = True
                if preguicaMovimento:
                    if len(set(pixelsPreguicaX).intersection(set(pixelsEspiritoX)))>dificuldade:
                        if len(set(pixelsPreguicaY).intersection(set(pixelsEspiritoY)))>dificuldade:
                            start()
                    if descendoPreguica:
                        pecadoY+= velocidadePecado
                        if pecadoY>=-80:
                            descendoPreguica=False
                            subindoPreguica=True
                    elif subindoPreguica:
                        pecadoY-=velocidadePecado
                        if pecadoY<=-800:
                            karmaPontos += 1
                            preguicaMovimento = False
                            pecadoAtual = random.choice(pecados)
                            pecadoX = random.randint(0, 840)
                            pecadoY = -80
                if not luxuriaMovimento and pecadoAtual==luxuria:
                    pecadoX=1100
                    pecadoY=0
                    indoLuxuria=True
                    voltandoLuxuria=False
                    luxuriaMovimento = True
                if luxuriaMovimento:
                    if len(set(pixelsLuxuriaX).intersection(set(pixelsEspiritoX)))>dificuldade:
                        if len(set(pixelsLuxuriaY).intersection(set(pixelsEspiritoY)))>dificuldade:
                            start()
                    if indoLuxuria:
                        pecadoX-=velocidadePecado
                        if pecadoX<=500:
                            indoLuxuria=False
                            voltandoLuxuria=True
                    elif voltandoLuxuria:
                        pecadoX+=velocidadePecado
                        if pecadoX>=1200:
                            karmaPontos+= 1
                            luxuriaMovimento = False
                            pecadoAtual = random.choice(pecados)
                            pecadoX = random.randint(0, 840)
                            pecadoY = -80
                if not avarezaMovimento and pecadoAtual == avareza:
                    pecadoY=800
                    pecadoX=random.randint(0, 840)
                    subindoAvareza = True
                    descendoAvareza = False
                    avarezaMovimento = True
                if avarezaMovimento:
                    if len(set(pixelsAvarezaX).intersection(set(pixelsEspiritoX)))>dificuldade:
                        if len(set(pixelsAvarezaY).intersection(set(pixelsEspiritoY)))>dificuldade:
                            start()
                    if subindoAvareza:
                        pecadoY -= velocidadePecado
                        if pecadoY <= 0:
                            subindoAvareza = False
                            descendoAvareza = True
                    elif descendoAvareza:
                        pecadoY += velocidadePecado
                        if pecadoY >= 700:
                            karmaPontos += 1
                            avarezaMovimento = False
                            pecadoAtual = random.choice(pecados)
                            pecadoX = random.randint(0, 840)
                            pecadoY = -80
                karma= fontePixelada.render("Karma: " + str(karmaPontos), True, branco)
                textoPause = fonteJogo.render("Press Space to Pause Game", True, branco)
                screen.blit(demiurge, (movimentoXDemiurge, movimentoYDemiurge))
                screen.blit(karma, (5, 5))
                screen.blit(pecadoAtual, (pecadoX, pecadoY))
                screen.blit(espirito, (espiritoX, 275))
                screen.blit(textoPause, (815, 675))
        if pausado:
            pausa = fonteJogoPausado.render("PAUSE", True, vermelho)
            screen.blit(backgroundFrames[backgroundIndex], (movimentoBackground, 0))
            screen.blit(pausa, (300, 300))
        pygame.display.update()
        fps.tick(60)
def start():
    larguraBotaoStart = 200
    alturaBotaoStart = 100
    larguraBotaoSair = 200
    alturaBotaoSair = 100
    while True:
        startButton = pygame.Rect(400, 300, larguraBotaoStart, alturaBotaoStart)
        sairButton = pygame.Rect(400, 450, larguraBotaoSair, alturaBotaoSair)
        startTexto= fontePixeladaStart.render("START", True, branco)
        sairTexto = fontePixeladaStart.render("SAIR", True, branco)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(event.pos):
                    larguraBotaoStart = 200
                    alturaBotaoStart = 100
                if sairButton.collidepoint(event.pos):
                    larguraBotaoSair = 200
                    alturaBotaoSair = 100
            elif event.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(event.pos):
                    larguraBotaoStart = 200
                    alturaBotaoStart = 100
                    jogar()
                if sairButton.collidepoint(event.pos):
                    larguraBotaoSair = 200
                    alturaBotaoSair = 100
                    pygame.quit()
                    exit()
        screen.blit(backgroundFrames[backgroundIndex], (0, 0))
        agora = pygame.time.get_ticks()
        screen.blit(tituloStart, (150, 60))
        screen.blit(startTexto, (410, 350))
        screen.blit(sairTexto, (425, 450))
        pygame.display.update()
start()