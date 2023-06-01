import pygame
from pygame.locals import *
# Importowanie grafik
size = width, height = (640, 480)       # Rozmiar ekranu do rozmairu grafik

# Klatki wstepu do gry
menu = pygame.transform.scale(
    pygame.image.load("grafiki/menu.png"), (width, height))
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

# Chapter 4
sciezka_krzaki = pygame.transform.scale(
    pygame.image.load("grafiki/sciezka_krzaki.png"), (width, height))
ziomus = pygame.transform.scale(
    pygame.image.load("grafiki/ziomus_na_rowerku.png"), (26*6, 25*6))
kotek = pygame.transform.scale(
    pygame.image.load("grafiki/kotek_z_patykiem.png"), (14*6, 13*6))

# Uciekanie
tlo_uciekania1 = pygame.transform.scale(
    pygame.image.load("grafiki/tlo_ucuekaniexcf.png"), (width, height*3))
tlo_uciekania2 = pygame.transform.scale(
    pygame.image.load("grafiki/tlo_ucuekaniexcf.png"), (width, height*3))
ziomus_od_tylu = pygame.transform.scale(
    pygame.image.load("grafiki/ziomus_od_tylu.png"), (14*7, 29*7))
lis = pygame.transform.scale(
    pygame.image.load("grafiki/lis.png"), (11*7, 20*7))

# Klatki ekran przegranej
grob = pygame.transform.scale(
    pygame.image.load("grafiki/grob.png"), (width, height))

# Klatki ektranu koncowego
koncowy = pygame.transform.scale(
    pygame.image.load("grafiki/koncowy.png"), (width, height))
wypadek1 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek1.png"), (width, height))
wypadek2 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek2.png"), (width, height))
wypadek3 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek3.png"), (width, height))
wypadek4 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek4.png"), (width, height))
wypadek5 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek5.png"), (width, height))
wypadek6 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek6.png"), (width, height))
wypadek7 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek7.png"), (width, height))
wypadek8 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek8.png"), (width, height))
wypadek9 = pygame.transform.scale(
    pygame.image.load("grafiki/wypadek9.png"), (width, height))
tekst_koncowy = pygame.transform.scale(
    pygame.image.load("grafiki/tekst_koncowy.png"), (312, 476))