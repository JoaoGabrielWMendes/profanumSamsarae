import pygame
import random
import math
import pygame.display
import pyttsx3
import speech_recognition 
import sqlite3
from datetime import datetime 
from funcoes import button,saida, cliqueMouse, mostrar_ranking
pygame.init()
engine = pyttsx3.init()
r = speech_recognition.Recognizer()
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
con.commit()
cur.execute
icon=pygame.image.load("recursos/icon.bmp")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Profanum Samsarae")
backgroundFrames = []
for i in range (3):
    frame=pygame.image.load(f"recursos/universeBackground{i}.png")
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
tituloStart=pygame.image.load("recursos/profanumSamsaraeInicial.png")
fontePixeladaPequena= pygame.font.Font("recursos/fontePixels.ttf", 20)
fontePixeladaMedia=pygame.font.Font("recursos/fontePixels.ttf", 35)
imagemDead=pygame.image.load("recursos/imagemDead1.png")
fontePixeladaGrande=pygame.font.Font("recursos/fontePixels.ttf", 50)
fonteKiwiSodaPequena=pygame.font.Font("recursos/KiwiSoda.ttf", 32)
fonteKiwiSodaGrande=pygame.font.Font("recursos/KiwiSoda.ttf", 70)
explicacao1Image=pygame.image.load("recursos/explicacao1.jpg")
explicacao2Image=pygame.image.load("recursos/explicacao2.jpg")
explicacao2ImageRepetir=pygame.image.load("recursos/explicacao2Repetir.jpg")
explicacao2ImageOuvir=pygame.image.load("recursos/explicacao2Ouvir.jpg")
imagemDead2=pygame.image.load("recursos/dead2.jpg")
telaDeNome0=pygame.image.load("recursos/telaDeNome0.jpg")
telaDeNome1=pygame.image.load("recursos/telaDeNome1.jpg")
backgroundIndex = 0
tempoUltimoFrame = pygame.time.get_ticks()
intervaloBackground=300
movimentoBackground = -100
velocidadeeBackground = 0
fonteComicSans=pygame.font.SysFont("comic sans", 14)
branco = (255, 255, 255)
preto=(0,0,0)
vermelho = (255, 0, 0)
def main():
    while True:
        start()
        texto=telaDeNome()
        explicacao1(texto)
        explicacao2()
        resultado=jogar()
        while True:
            if resultado in ("dead1","dead2"):
                tela_ranking()
                break
def jogar():
    #Background
    global movimentoBackground, velocidadeeBackground, backgroundFrames, frame,backgroundFrames, backgroundIndex,tempoUltimoFrame, fps, intervaloBackground
    #Pecados
    pecados = [orgulho, luxuria, avareza, gula, ira, inveja, preguica]
    velocidadePecadoBase = 1
    velocidadePecado = velocidadePecadoBase
    larguraEspirito, alturaEspirito = 120, 160
    larguraAvareza, alturaAvareza = 101, 760
    larguraLuxuria, alturaLuxuria = 700, 700
    larguraPreguica, alturaPreguica = 338, 612
    larguraPecado, alturaPecado = 125, 160
    pecadoAtual = random.choice(pecados)
    pecadoX = random.randint(0, 840)
    pecadoY = -80
    #Movimento dos pecados
    avarezaMovimento = False
    luxuriaMovimento = False
    preguicaMovimento = False
    descendoPreguica = False
    subindoPreguica = False
    indoLuxuria = False
    voltandoLuxuria = False
    subindoAvareza = False
    descendoAvareza = False
    #Outros
    karmaPontos = 0
    pausado = False
    espiritoX = 500
    velocidadeEspirito = 0
    #Demiurge
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
    def resetar_pecado():
        nonlocal pecadoAtual, pecadoX, pecadoY
        nonlocal avarezaMovimento, luxuriaMovimento, preguicaMovimento
        nonlocal descendoPreguica, subindoPreguica, indoLuxuria, voltandoLuxuria, subindoAvareza, descendoAvareza
        pecadoAtual = random.choice(pecados)
        pecadoX = random.randint(0, 840)
        pecadoY = -80
        avarezaMovimento = False
        luxuriaMovimento = False
        preguicaMovimento = False
        descendoPreguica = False
        subindoPreguica = False
        indoLuxuria = False
        voltandoLuxuria = False
        subindoAvareza = False
        descendoAvareza = False

    while True:
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
            if distancia > 5:
                velocidadeXdemiurge = dx / distancia
                velocidadeYdemiurge = dy / distancia 
                velocidadeRetorno = 3
                movimentoXDemiurge += velocidadeXdemiurge * velocidadeRetorno
                movimentoYDemiurge += velocidadeYdemiurge * velocidadeRetorno
            else:
                modoDemiurge="orbital"
        agora = pygame.time.get_ticks()
        if agora - tempoUltimoFrame > intervaloBackground:
            tempoUltimoFrame = agora
            backgroundIndex = (backgroundIndex + 1) % len(backgroundFrames)
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidadeEspirito = -10
                    velocidadeeBackground=+1
                if event.key == pygame.K_RIGHT:
                    velocidadeEspirito = 10
                    velocidadeeBackground=-1
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    velocidadeEspirito = 0
                    velocidadeeBackground=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = not pausado
        if not pausado:
            espiritoX += velocidadeEspirito
            movimentoBackground+=velocidadeeBackground
            if movimentoBackground > 0:
                movimentoBackground = 0
            elif movimentoBackground < -122:
                movimentoBackground = -122
            if espiritoX<0:
                espiritoX=0
            if espiritoX>880:
                espiritoX=880
            screen.blit(backgroundFrames[backgroundIndex], (movimentoBackground, 0))
            espirito_rect = pygame.Rect(espiritoX, 275, larguraEspirito, alturaEspirito)
            if not (luxuriaMovimento or avarezaMovimento or preguicaMovimento):
                pecado_rect = pygame.Rect(pecadoX, pecadoY, larguraPecado, alturaPecado)
                pecadoY += velocidadePecado
                if 0 <= pecadoY <= 700 and espirito_rect.colliderect(pecado_rect):
                    if karmaPontos >= 5:
                        return dead2(karmaPontos)
                    else:
                        return dead1(karmaPontos)
                if pecadoY > 700:
                    karmaPontos += 1
                    velocidadePecadoBase += 1
                    velocidadePecado = velocidadePecadoBase
                    resetar_pecado()
                    continue
                if pecadoAtual == preguica:
                    pecadoX = 500
                    pecadoY = -600
                    descendoPreguica = True
                    subindoPreguica = False
                    preguicaMovimento = True
                elif pecadoAtual == luxuria:
                    pecadoX = 1100
                    pecadoY = 0
                    indoLuxuria = True
                    voltandoLuxuria = False
                    luxuriaMovimento = True
                elif pecadoAtual == avareza:
                    pecadoY = 800
                    pecadoX = random.randint(0, 840)
                    subindoAvareza = True
                    descendoAvareza = False
                    avarezaMovimento = True
            if preguicaMovimento:
                pecado_rect = pygame.Rect(pecadoX, pecadoY, larguraPreguica, alturaPreguica)
                if descendoPreguica:
                    pecadoY += velocidadePecado
                    if pecadoY >= -80:
                        descendoPreguica = False
                        subindoPreguica = True
                elif subindoPreguica:
                    pecadoY -= velocidadePecado
                    if pecadoY <= -800:
                        preguicaMovimento = False
                        karmaPontos += 1
                        resetar_pecado()
                        continue
                if -800 <= pecadoY <= 700 and espirito_rect.colliderect(pecado_rect):
                    if karmaPontos >= 5:
                        return dead2(karmaPontos)
                    else:
                        return dead1(karmaPontos)
            if luxuriaMovimento:
                pecado_rect = pygame.Rect(pecadoX, pecadoY, larguraLuxuria, alturaLuxuria)
                if indoLuxuria:
                    pecadoX -= velocidadePecado
                    if pecadoX <= 500:
                        indoLuxuria = False
                        voltandoLuxuria = True
                elif voltandoLuxuria:
                    pecadoX += velocidadePecado
                    if pecadoX >= 1200:
                        luxuriaMovimento = False
                        karmaPontos += 1
                        resetar_pecado()
                        continue
                if 0 <= pecadoX <= 1000 and espirito_rect.colliderect(pecado_rect):
                    if karmaPontos >= 5:
                        return dead2(karmaPontos)
                    else:
                        return dead1(karmaPontos)
            if avarezaMovimento:
                pecado_rect = pygame.Rect(pecadoX, pecadoY, larguraAvareza, alturaAvareza)
                if subindoAvareza:
                    pecadoY -= velocidadePecado
                    if pecadoY <= 0:
                        subindoAvareza = False
                        descendoAvareza = True
                elif descendoAvareza:
                    pecadoY += velocidadePecado
                    if pecadoY >= 700:
                        avarezaMovimento = False
                        karmaPontos += 1
                        resetar_pecado()
                        continue
                if 0 <= pecadoY <= 700 and espirito_rect.colliderect(pecado_rect):
                    if karmaPontos >= 5:
                        return dead2(karmaPontos)
                    else:
                        return dead1(karmaPontos)
            screen.blit(demiurge, (movimentoXDemiurge, movimentoYDemiurge))
            screen.blit(espirito, (espiritoX, 275))
            screen.blit(pecadoAtual, (pecadoX, pecadoY))
            karma = fontePixeladaPequena.render("Karma: " + str(karmaPontos), True, branco)
            screen.blit(karma, (5, 5))
            textoPause = fonteComicSans.render("Press Space to Pause Game", True, branco)
            screen.blit(textoPause, (5, 30))
        if pausado:
            pausa = fontePixeladaGrande.render("PAUSE", True, vermelho)
            screen.blit(pausa, (380, 300))
        pygame.display.update()
        fps.tick(60)
def start():
    larguraButtonStart = 200
    alturaButtonStart = 100
    larguraButtonSair = 200
    alturaButtonSair = 100
    while True:
        screen.blit(backgroundFrames[backgroundIndex], (0, 0))
        screen.blit(tituloStart, (150, 60))
        startButton=button(screen, 400,350,larguraButtonStart,alturaButtonStart,"START", fontePixeladaMedia,branco)
        sairButton=button(screen,400,450,larguraButtonSair,alturaButtonSair, "SAIR", fontePixeladaMedia,branco)
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  startButton.collidepoint(event.pos):
                    return
            cliqueMouse(event,sairButton,quit)
        pygame.display.update()
def telaDeNome():
    alturaButtonNome=40
    larguraButtonNome=900
    alturaButtonSeguir=25
    larguraButtonSeguir=40
    texto=""
    falar=False
    nome_reconhecido=False
    while True:
        if not nome_reconhecido and not falar:
            screen.blit(telaDeNome0,(0,0))
            buttonSeguir=None
            buttonNome=button(screen,50,270,larguraButtonNome,alturaButtonNome, "Clique aqui para ditar seu nome",fonteKiwiSodaGrande,preto)
        elif falar:
            nome_surface=fonteKiwiSodaGrande.render(texto, True, preto)
            screen.blit(nome_surface, (350, 100))
            buttonSeguir=button(screen, 900, 600, larguraButtonSeguir,alturaButtonSeguir, "-->", fonteKiwiSodaPequena, preto)
        pygame.display.update()
        for event in pygame.event.get():
            saida(event)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if buttonNome.collidepoint(event.pos):
                    falar=True
                if nome_reconhecido and buttonSeguir and buttonSeguir.collidepoint(event.pos):
                    return texto
        if falar:
            screen.blit(telaDeNome1,(0,0))
            pygame.display.update()
            try:
                with speech_recognition.Microphone() as source:
                    audio=r.listen(source)
                texto=r.recognize_google(audio,language='pt-BR')
                nome_reconhecido=True
                screen.blit(telaDeNome1,(0,0))
                nome_surface = fonteKiwiSodaGrande.render(texto, True, preto)
                screen.blit(nome_surface, (350, 100))
                buttonSeguir=button(screen, 900, 600, larguraButtonSeguir, alturaButtonSeguir,"-->", fonteKiwiSodaPequena, preto)
                pygame.display.update()
                nome_reconhecido=True
            except speech_recognition.RequestError:
                texto="Erro ao conectar ao serviço de reconhecimento."
            except speech_recognition.UnknownValueError:
                texto="Repita"
            falar=False
            pygame.display.update()
def explicacao1(texto):
    nome_surface = fonteKiwiSodaGrande.render(texto, True, preto)
    alturaButtonSeguir=25
    larguraButtonSeguir=40
    while True:
        screen.blit(explicacao1Image,(0,0))
        screen.blit(nome_surface,(400,75))
        buttonSeguir=button(screen, 900, 600, larguraButtonSeguir,alturaButtonSeguir, "-->", fonteKiwiSodaPequena, preto)
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  buttonSeguir.collidepoint(event.pos):
                    return
        pygame.display.update()
def explicacao2():
    alturaButtonStart2=40
    larguraButtonStart2=200
    while True:
        screen.blit(explicacao2Image,(0,0))
        buttonStart2=button(screen,100, 550, larguraButtonStart2,alturaButtonStart2,"Start!",fonteKiwiSodaGrande,preto)
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart2.collidepoint(event.pos):
                    return 
        pygame.display.update()
def tela_ranking():
    alturaButtonContinuar=40
    larguraButonContinuar=300
    while True:
        screen.blit(telaDeNome0,(0,0))
        buttonContinuar=button(screen,300,450,larguraButonContinuar,alturaButtonContinuar,"Continuar",fonteKiwiSodaGrande,preto)
        mostrar_ranking(screen,fonteKiwiSodaPequena,200,200,preto)
        texto_tela_ranking=fontePixeladaGrande.render("Ranking:",True,preto)
        screen.blit(texto_tela_ranking,(300,100))
        pygame.display.update()
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonContinuar.collidepoint(event.pos):
                    return
        pygame.display.update()
def dead1(karmaPontos):
    agora=datetime.now()
    data=agora.strftime("%d/%m/%Y")
    hora=agora.strftime("%H:%M:%S")
    con=sqlite3.connect("log.dat")
    cur=con.cursor()
    cur.execute("INSERT INTO log (pontuacao,data,hora) VALUES (?,?,?)",(karmaPontos,data,hora))
    con.commit()
    con.close()
    alturaButtonTentarNov=40
    larguraButtonTentarNov=500
    larguraSairDeadButton=100
    alturaSairDeadButton=40
    while True:
        escritaReencarnar= fontePixeladaGrande.render("REENCARNOU", True, vermelho)
        screen.blit(imagemDead, (0, -300))
        tentarNovButton = button(screen, 270,300, larguraButtonTentarNov, alturaButtonTentarNov, "Tentar Novamente?", fontePixeladaMedia, branco)
        sairDeadButton=button(screen, 445,370, larguraSairDeadButton, alturaSairDeadButton, "Sair", fontePixeladaMedia, branco)
        for event in pygame.event.get():
            saida(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tentarNovButton.collidepoint(event.pos):
                    return "dead1"
            cliqueMouse(event,sairDeadButton,quit)
        screen.blit(escritaReencarnar, (280, 200))
        pygame.display.update()
def dead2(karmaPontos):
    agora=datetime.now()
    data=agora.strftime("%d/%m/%Y")
    hora=agora.strftime("%H:%M:%S")
    con=sqlite3.connect("log.dat")
    cur=con.cursor()
    cur.execute("INSERT INTO log (pontuacao,data,hora) VALUES (?,?,?)",(karmaPontos,data,hora))
    con.commit()
    con.close()
    screen.blit(imagemDead2,(0,0))
    pygame.display.update()
    engine.say('''AH, então aqui estás outra vez. Tentando quebrar o ciclo...
    Nem tente fugir agora me ouvirá
    Quem sou eu? Me chamam de D, corpo de cobra cabeça de leão, Demiurgo. Não importa.
    Tu ages como se tua vontade frágil pudesse mover a estrutura do mundo. Tola criatura, minha criatura. Tudo o que és, tudo o que pensas ter descoberto. Fui eu quem permitiu. Te dei essa centelha de dúvida só para assistir como a sufocas.
    Tu não entendes, ninguém sai do ciclo. Ninguém me escapa. Eu sou o princípio e o fim, o carcereiro e a cela. Sem mim, não há forma, não há tempo, não há tu. O que seria do universo se cada alma decidisse voar por conta própria? Caos. Gritos. Silêncio eterno. Eu não posso permitir isso. Eu não vou permitir.''')
    engine.runAndWait()
    return "dead2"
main()