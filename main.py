import pygame, sys
from pygame.locals import *
import random
import grafika      # Grafiki tła dałam do osobnego pliku bo zajmowaly duzo linii
# import time

# Funkcja losujaca 4 litery do minigierki z chapter2 (zwraca string 4 znakowy)
def losowanie_sekwencji(n):
    # Lista możliwych liter do losowania
    litery = ['W', 'S', 'A', 'D']

    # Losowanie n liter
    # Robi tablice losowych 4 liter z litery
    wylosowane_litery = random.sample(litery, n)
    wylosowane_litery = "".join(wylosowane_litery)  # Zmiana tablicy na string
    return wylosowane_litery

class Spr(pygame.sprite.Sprite):

    #Konstruktor klasy sprita dla kotka
    def __init__(self, image_path, x, y, width, height):
        super().__init__()

        self.image_path = image_path
        self.sprite_image = pygame.image.load(image_path)
        self.sprite_size = (width, height)  # wymiary sprite'a
        self.sprite_image = pygame.transform.scale(self.sprite_image, self.sprite_size)

        self.image = self.sprite_image
        self.rect = self.sprite_image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

    def update(self, image_path, width, height):
        # Wczytanie nowego obrazka sprite'a
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.sprite_size = (width, height)  # wymiary sprite'a
        self.sprite_image = pygame.transform.scale(self.image, self.sprite_size)
        self.image = self.sprite_image

# ZMIENNE OGOLNE
size = width, height = (640, 480)       # Rozmiar ekranu
zycia = 1   # Zmienna zyc kotka
gra = 'chapter3'    # Zmienna do ustawiania etapu gry
klatka = 0
zegar = pygame.time.Clock()
czas = 0

# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Purrfect Meowrder')  # Tytul

# POSTACI
# Kotek sprajt
x_kotka = width/2       # pozycja poczatkowa kotka
y_kotka = height/2 -50
kotek = Spr('grafiki/kotek.png', x_kotka, y_kotka, 110, 90)

grupa_sprajtow = pygame.sprite.Group()
grupa_sprajtow.add(kotek)

# CZCIONKI
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

# DO CHAPTER 3
worek = 0       # Zmienna pokazujaca czy zebrało sie worek czy nie
patyk = 0

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
            screen.blit(grafika.g_tytulowa, (0, 0))
        if klatka == 1:
            screen.blit(grafika.klatka1_dom, (0, 0))
        if klatka == 2:
            screen.blit(grafika.klatka2_dom, (0, 0))
        if klatka == 3:
            screen.blit(grafika.klatka3_dom, (0, 0))
        if klatka == 4:
            screen.blit(grafika.klatka4_dom, (0, 0))
        if klatka == 5:
            screen.blit(grafika.rzut1, (0, 0))
        if klatka == 6:
            screen.blit(grafika.rzut2, (0, 0))
        if klatka == 7:
            screen.blit(grafika.rzut3, (0, 0))
        if klatka == 8:
            screen.blit(grafika.rzut4, (0, 0))
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
            screen.blit(grafika.topienie1, (0, 0))
        if klatka == 2:
            screen.blit(grafika.topienie2, (0, 0))
        if klatka == 3:
            screen.blit(grafika.topienie3, (0, 0))
        if klatka == 4:
            screen.blit(grafika.topienie4, (0, 0))

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
                klatka = 0

        if zycia<1:
            gra = 'przegrana'
        screen.blit(tekst_litery, [(width / 2) - 100, height / 2 + 100])
        pygame.display.update()

# Chodzenie po lesie i szukanie patyka
    while gra == 'chapter3':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                if kotek.rect.top > 80:
                    kotek.rect.y -= 5
            if keys[pygame.K_a]:
                kotek.rect.x -= 5
                kotek.update('grafiki/kotek_l.png', 110, 90)
            if keys[pygame.K_s]:
                if kotek.rect.bottom < height:
                    kotek.rect.y += 5
            if keys[pygame.K_d]:
                kotek.update('grafiki/kotek.png', 110, 90)
                if klatka == 2:
                    if kotek.rect.right < width:
                        kotek.rect.x += 5
                else:
                    kotek.rect.x += 5


        if klatka == 0:
            screen.blit(grafika.jezioro, (0, 0))
            # Chodzenie i blokady krawedzi ekranu
            if kotek.rect.right > width:
                klatka = 1
                kotek.rect.left = 0
            # Wejscie do wody
            if kotek.rect.bottom > height-40:
                if kotek.rect.left < width-150:
                    zycia -= 1
            # Zbieranie worka
            if worek == 0:
                x_worka = 250
                y_worka = height-150
                prawa = x_worka+90
                dol = y_worka+90
                screen.blit(grafika.worek, (x_worka, y_worka))
                if kotek.rect.colliderect(pygame.Rect(x_worka, y_worka, 90, 90)):   # Sprawdzanie kolizji z pozycją worka
                    worek = 1

        if klatka == 1:
            screen.blit(grafika.las, (0, 0))
            #Chodzenie i blokady krawedzi ekranu
            if kotek.rect.left < 0:
                klatka = 0
                kotek.rect.right = width
            if kotek.rect.right > width:
                klatka = 2
                kotek.rect.left = 0
            # Zbieranie patyka
            if patyk == 0:
                x_patyka = 500
                y_patyka = 380
                prawa = x_worka + 90
                dol = y_worka + 90
                screen.blit(grafika.patyk, (x_patyka, y_patyka))
                if kotek.rect.colliderect(pygame.Rect(x_patyka, y_patyka, 90, 90)):  # Sprawdzanie kolizji z pozycją patyka
                    patyk = 1
        if klatka == 2:
            screen.blit(grafika.sciezka, (0, 0))
            if kotek.rect.left < 0:
                klatka = 1
                kotek.rect.right = width





        text_zycia_ale_bialy = font.render("zycia: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 70, 10])

        grupa_sprajtow.draw(screen)
        pygame.display.update()

# Ekran smierci
    while gra == 'przegrana':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        screen.blit(grafika.grob, (0, 0))
        text_grob = font.render("Kotek UMARŁ :'c", False, [255, 255, 255])
        screen.blit(text_grob, [width/2, height/2 +100])
        pygame.display.update()

pygame.quit()