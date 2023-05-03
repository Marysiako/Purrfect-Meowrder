import pygame
from pygame.locals import *
# Importowanie grafik
size = width, height = (640, 480)       # Rozmiar ekranu do rozmairu grafik

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
las = pygame.transform.scale(
    pygame.image.load("grafiki/las.png"), (width, height))
sciezka = pygame.transform.scale(
    pygame.image.load("grafiki/lassciezka.png"), (width, height))

# CHapter 3
worek = pygame.transform.scale(
    pygame.image.load("grafiki/worek.png"), (90, 90))  # Rozmiar worka to 9 na 9 ale robie wiekszy
patyk = pygame.transform.scale(
    pygame.image.load("grafiki/patyk.png"), (90, 90))


# Klatki ekran przegranej
grob = pygame.transform.scale(
    pygame.image.load("grafiki/grob.png"), (width, height))