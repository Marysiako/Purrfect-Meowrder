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
    wylosowane_litery = random.sample(litery, n)  # Robi tablice losowych 4 liter z litery
    wylosowane_litery = "".join(wylosowane_litery)  # Zmiana tablicy na string
    return wylosowane_litery

# Zmienne ogólne
size = width, height = (640, 480)       # size of screen
zycia = 9
gra = 'chapter1'
klatka = 0

# Zmienne do chapter 2
wylosowana_sekwencja = losowanie_sekwencji(4)
wpisana_sekwencja = ""
punkty = 0

# Importowanie grafik
# Klatki wstepu do gry
g_tytulowa = pygame.transform.scale(pygame.image.load("grafiki/tytul.png"), (width, height))
klatka1_dom = pygame.transform.scale(pygame.image.load("grafiki/klatka1_dom.png"), (width, height))
klatka2_dom = pygame.transform.scale(pygame.image.load("grafiki/klatka2_dom.png"), (width, height))
klatka3_dom = pygame.transform.scale(pygame.image.load("grafiki/klatka3_dom.png"), (width, height))
klatka4_dom = pygame.transform.scale(pygame.image.load("grafiki/klatka4_dom.png"), (width, height))
rzut1 = pygame.transform.scale(pygame.image.load("grafiki/rzut1.png"), (width, height))
rzut2 = pygame.transform.scale(pygame.image.load("grafiki/rzut2.png"), (width, height))
rzut3 = pygame.transform.scale(pygame.image.load("grafiki/rzut3.png"), (width, height))
rzut4 = pygame.transform.scale(pygame.image.load("grafiki/rzut4.png"), (width, height))
#Klatki pierwszej minigierki
topienie1 = pygame.transform.scale(pygame.image.load("grafiki/zalany14.png"), (width, height))
topienie2 = pygame.transform.scale(pygame.image.load("grafiki/zalany24.png"), (width, height))
topienie3 = pygame.transform.scale(pygame.image.load("grafiki/zalany34.png"), (width, height))
topienie4 = pygame.transform.scale(pygame.image.load("grafiki/zalany.png"), (width, height))



pygame.init()
running = True
screen = pygame.display.set_mode(size)      # setting size of screem
pygame.display.set_caption('Purrfect Meowrder')  # tittle

#czcionka
pygame.font.init()
font = pygame.font.SysFont('8-bit-hud.ttf', 25)
font_duza = pygame.font.SysFont('8-bit-hud.ttf', 80)
text_zycia = font.render("zycia: "+str(zycia), False, [0, 0, 0])



# apply changes
pygame.display.update()

# Events
while running:

# Wstep do fabuly
    while gra == 'chapter1':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
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


        screen.blit(text_zycia, [width - 70, 10])

        pygame.display.update()


# Pierwsza minigra, klikanie odpowiedniej sekwencji przyciskow zeby nie utonac
    while gra == 'chapter2':

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    wpisana_sekwencja = wpisana_sekwencja + "W"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    wpisana_sekwencja = wpisana_sekwencja + "A"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    wpisana_sekwencja = wpisana_sekwencja + "S"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    wpisana_sekwencja = wpisana_sekwencja + "D"

        teskst_litery = font_duza.render(wylosowana_sekwencja, False, [255, 255, 255])

        klatka = 1  # Ustawiam klatke spowrotem na 1 i teraz zmeinna bedzie do chapter2
        if klatka == 1:
            screen.blit(topienie1, (0, 0))
        if klatka == 2:
            screen.blit(topienie2, (0, 0))
        if klatka == 3:
            screen.blit(topienie3, (0, 0))
        if klatka == 4:
            screen.blit(topienie4, (0, 0))


        # 8 razy wpisuje sie sekwencje w czasie 3 sekund
        for x in range(8):
            # oczekiwanie 3 sekund na wpisanie sekwencji
            pygame.time.wait(3000)

            screen.blit(teskst_litery, [(width / 2) - 100, height / 2 + 100])
            wylosowana_sekwencja = losowanie_sekwencji(4)
            print(wpisana_sekwencja)
            if wpisana_sekwencja.count(wylosowana_sekwencja)>0:     # Jezeli wpisana zostala sekwencja chociaz 1 raz
                punkty = punkty + 1
            wpisana_sekwencja = ""
            if x == 3:
                klatka = 2
            if x == 5:
                klatka = 3
            if x == 7:
                klatka = 4

        if punkty<6:
            zycia = zycia - 1
        if punkty>6:
            pygame.quit()

        pygame.display.update()

pygame.quit()

