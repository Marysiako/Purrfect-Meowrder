import pygame
from pygame.locals import *
import random
# import time

# Funkcje
# Funkcja losujaca 4 litery do minigierki z chapter2 (zwraca string 4 znakowy)


def losowanie_sekwencji(n):
    # Lista możliwych liter do losowania
    litery = ['W', 'S', 'A', 'D']

    # Losowanie n liter
    # Robi tablice losowych 4 liter z litery
    wylosowane_litery = random.sample(litery, n)
    wylosowane_litery = "".join(wylosowane_litery)  # Zmiana tablicy na string
    return wylosowane_litery


# Zmienne ogólne
size = width, height = (640, 480)       # size of screen
zycia = 2
gra = 'chapter1'
klatka = 0
zegar = pygame.time.Clock()
czas = 0

pygame.init()
running = True
screen = pygame.display.set_mode(size)      # setting size of screem
pygame.display.set_caption('Purrfect Meowrder')  # tittle

# czcionka
pygame.font.init()
font = pygame.font.SysFont('8-bit-hud.ttf', 25)
font_duza = pygame.font.SysFont('8-bit-hud.ttf', 80)
text_zycia = font.render("zycia: "+str(zycia), False, [0, 0, 0])
text_zycia_ale_bialy = font.render("zycia: "+str(zycia), False, [255, 255, 255])

# Zmienne do chapter 2
wylosowana_sekwencja = losowanie_sekwencji(4)
tekst_litery = font_duza.render(wylosowana_sekwencja, False, [255, 255, 255])
wpisana_sekwencja = ""
punkty = 0
sekwencja = 0


# Importowanie grafik
# Postaci
kotek = pygame.transform.scale(
    pygame.image.load("grafiki/kotek.png"), (110, 90))


# Klatki wstepu do gry
g_tytulowa = pygame.transform.scale(
    pygame.image.load("grafiki/tytul.png"), (width, height))
klatka1_dom = pygame.transform.scale(pygame.image.load(
    "grafiki/klatka1_dom.png"), (width, height))
klatka2_dom = pygame.transform.scale(pygame.image.load(
    "grafiki/klatka2_dom.png"), (width, height))
klatka3_dom = pygame.transform.scale(pygame.image.load(
    "grafiki/klatka3_dom.png"), (width, height))
klatka4_dom = pygame.transform.scale(pygame.image.load(
    "grafiki/klatka4_dom.png"), (width, height))
rzut1 = pygame.transform.scale(pygame.image.load(
    "grafiki/rzut1.png"), (width, height))
rzut2 = pygame.transform.scale(pygame.image.load(
    "grafiki/rzut2.png"), (width, height))
rzut3 = pygame.transform.scale(pygame.image.load(
    "grafiki/rzut3.png"), (width, height))
rzut4 = pygame.transform.scale(pygame.image.load(
    "grafiki/rzut4.png"), (width, height))
# Klatki pierwszej minigierki
topienie1 = pygame.transform.scale(
    pygame.image.load("grafiki/zalany14.png"), (width, height))
topienie2 = pygame.transform.scale(
    pygame.image.load("grafiki/zalany24.png"), (width, height))
topienie3 = pygame.transform.scale(
    pygame.image.load("grafiki/zalany34.png"), (width, height))
topienie4 = pygame.transform.scale(
    pygame.image.load("grafiki/zalany.png"), (width, height))

# Klatki tła do dalszej gry
jezioro = pygame.transform.scale(
    pygame.image.load("grafiki/jezioro.png"), (width, height))
grob = pygame.transform.scale(
    pygame.image.load("grafiki/grob.png"), (width, height))

# Pozycja kotka
x_kotka = width/2
y_kotka = height/2 -50

# apply changes
pygame.display.update()

# Events
while running:

    zegar.tick(60)  # 60 fps

    # Wstep do fabuly
    while gra == 'chapter1':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    klatka = klatka + 1
        if klatka == 0:
            screen.blit(g_tytulowa, (0, 0))
        if klatka == 1:
            screen.blit(klatka1_dom, (0, 0))
        if klatka == 2:
            screen.blit(klatka2_dom, (0, 0))
        if klatka == 3:
            screen.blit(klatka3_dom, (0, 0))
        if klatka == 4:
            screen.blit(klatka4_dom, (0, 0))
        if klatka == 5:
            screen.blit(rzut1, (0, 0))
        if klatka == 6:
            screen.blit(rzut2, (0, 0))
        if klatka == 7:
            screen.blit(rzut3, (0, 0))
        if klatka == 8:
            screen.blit(rzut4, (0, 0))
        if klatka == 9:
            gra = 'chapter2'
            klatka = 1

        screen.blit(text_zycia, [width - 70, 10])
        pygame.display.update()


# Pierwsza minigra, klikanie odpowiedniej sekwencji przyciskow zeby nie utonac
    while gra == 'chapter2':

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "W"
                if event.key == pygame.K_a and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "A"
                if event.key == pygame.K_s and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "S"
                if event.key == pygame.K_d and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "D"

        #klatka = 1  # Ustawiam klatke spowrotem na 1 i teraz zmeinna bedzie do chapter2
        if klatka == 1:
            screen.blit(topienie1, (0, 0))
        if klatka == 2:
            screen.blit(topienie2, (0, 0))
        if klatka == 3:
            screen.blit(topienie3, (0, 0))
        if klatka == 4:
            screen.blit(topienie4, (0, 0))

        text_zycia_ale_bialy = font.render("zycia: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 70, 10])
        czas += zegar.get_time()

        if sekwencja<8:
            if (czas > 60000):
                if wpisana_sekwencja == wylosowana_sekwencja:
                    punkty += 1
                print(f"punkty: {punkty} wylosowana sekwencja: {wylosowana_sekwencja} wpisana sekwencja: {wpisana_sekwencja} sekwencja: {sekwencja }klatka: {klatka} ")
                wylosowana_sekwencja = losowanie_sekwencji(4)
                tekst_litery = font_duza.render(wylosowana_sekwencja, False, [255, 255, 255])
                wpisana_sekwencja = ""
                czas = 0
                sekwencja = sekwencja + 1

            if sekwencja == 2:
                 klatka = 2
            if sekwencja == 4:
                klatka = 3
            if sekwencja == 6:
                 klatka = 4

        if sekwencja>6:
            if punkty<6:
                zycia = zycia - 1
                print(f"zycia: {zycia} ")
                klatka = 1
                sekwencja = 0
            if punkty>6:
                print(f"zycia: {zycia} ")
                gra = 'chapter3'

        if zycia<1:
            gra = 'przegrana'
        screen.blit(tekst_litery, [(width / 2) - 100, height / 2 + 100])
        pygame.display.update()

    while gra == 'chapter3':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.blit(jezioro, (0, 0))
        text_zycia_ale_bialy = font.render("zycia: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 70, 10])
        screen.blit(kotek, (x_kotka, y_kotka))
        pygame.display.update()

    while gra == 'przegrana':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        screen.blit(grob, (0, 0))
        text_grob = font.render("Kotek UMARŁ :'c", False, [255, 255, 255])
        screen.blit(text_grob, [width/2, height/2 +100])
        pygame.display.update()

pygame.quit()