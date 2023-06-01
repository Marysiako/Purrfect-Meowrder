import pygame, sys
from pygame.locals import *
import random
import grafika      # Grafiki tła dałam do osobnego pliku bo zajmowaly duzo linii
# import time

# Funkcja losujaca 4 litery do minigierki z CHAPTER2 (zwraca string 4 znakowy)
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

class zwyrol_spr(pygame.sprite.Sprite):
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

class Przyciski(pygame.sprite.Sprite):

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
# ZMIENNE OGOLNE
size = width, height = (640, 480)       # Rozmiar ekranu
zycia = 9   # Zmienna zyc kotka
gra = 'menu'    # Zmienna do ustawiania etapu gry
klatka = 1
zegar = pygame.time.Clock()
czas = 0
clock = pygame.time.Clock()
FPS = 30

# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Purrfect Meowrder')  # Tytul

# CZCIONKI
pygame.font.init()
font = pygame.font.SysFont('8-bit-hud.ttf', 25)
font_duza = pygame.font.SysFont('8-bit-hud.ttf', 80)
font_srednia = pygame.font.SysFont('8-bit-hud.ttf', 35)
text_zycia = font.render("Lives left: "+str(zycia), False, [0, 0, 0])
text_zycia_ale_bialy = font.render("Lives left: "+str(zycia), False, [255, 255, 255])

# PRZYCISKI
grupa_przyciskow = pygame.sprite.Group()
text_start = font_srednia.render('Start', False, [180, 180, 180])
pstart = Przyciski('grafiki/pstart_ciemny.png', 120, 150, 200, 50)
grupa_przyciskow.add(pstart)

text_glos = font_srednia.render('Music', False, [180, 180, 180])
wlaczwylaczglos = Przyciski('grafiki/pstart_ciemny.png', 120, 210, 200, 50)
grupa_przyciskow.add(wlaczwylaczglos)

text_quit = font_srednia.render('Quit', False, [180, 180, 180])
pquit = Przyciski('grafiki/pstart_ciemny.png', 120, 270, 200, 50)
grupa_przyciskow.add(pquit)

text_how_to_play = font_srednia.render('How to play', False, [180, 180, 180])
p_htp = Przyciski('grafiki/pstart_ciemny.png', 120, 330, 200, 50)
grupa_przyciskow.add(p_htp)

    # przycisk nowej gry
grupa_przyciskow_restart = pygame.sprite.Group()
text_restart = font_srednia.render('Restart', False, [180, 180, 180])
text_menu = font_srednia.render('Back to menu', False, [180, 180, 180])
p_nowagra = Przyciski('grafiki/pstart_ciemny.png', width-210, 10, 200, 50)
grupa_przyciskow_restart.add(p_nowagra)

# POSTACI
# Kotek sprajt
x_kotka = width/2       # pozycja poczatkowa kotka
y_kotka = height/2 -50
kotek = Spr('grafiki/kotek.png', x_kotka, y_kotka, 110, 90)

grupa_sprajtow = pygame.sprite.Group()
grupa_sprajtow.add(kotek)

# Zyrol na rowerku
x_zwyrola = width-26*7
y_zwyrola = 60
zwyrol = zwyrol_spr('grafiki/ziomus_na_rowerku.png', x_zwyrola, y_zwyrola, 26*7, 25*7)

grupa_zwyroli = pygame.sprite.Group()
grupa_zwyroli.add(zwyrol)


# DO CHAPTER 2
wylosowana_sekwencja = losowanie_sekwencji(4)
wylosowana_sekwencja2 = wylosowana_sekwencja.replace('W', ' ^ ')
wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('S', ' v ')
wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('A', ' < ')
wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('D', ' > ')
tekst_litery = font_duza.render(wylosowana_sekwencja2, False, [255, 255, 255])
wpisana_sekwencja = ""
punkty = 0
sekwencja = 0
tekst_punkty = font_srednia.render("Points: "+str(punkty)+" /7", False, [255, 255, 255])

# DO CHAPTER 3
worek = 0       # Zmienna pokazujaca czy zebrało sie worek czy nie
patyk = 0
wyjscie_z_wody = True
text_woda_smierc = font.render('Water = Death', False, [0, 0, 20])

# DO CHAPTER 4
is_w_pressed = False

# Ucieczka 1
tlo1y = 0
tlo2y = -3*height

# apply changes
pygame.display.update()

# NAPISY KONCOWE
koncowy_y = 480

# MUZYKA
muzyka_gra = True       # Zmienna do przycisku wlaczenia i wylaczenia muzyki w menu
muzyka_start = False    # Zmienna do włączania jednokrotnie muzyki innej zaleznie od poziomu
# Dzwieki
meow_znalazl = pygame.mixer.Sound("dzwieki/delikatnymeow.mp3")
meow_angry = pygame.mixer.Sound("dzwieki/angrymeow.wav")
meow_ssss = pygame.mixer.Sound("dzwieki/ssyk.wav")
meow_die = pygame.mixer.Sound("dzwieki/uweow.wav")
meow_splash = pygame.mixer.Sound("dzwieki/splash.wav")      #pygame.mixer.Sound.play(meow_splash)
meow_out = pygame.mixer.Sound("dzwieki/coming-out-of-water.mp3")
man_scream = pygame.mixer.Sound("dzwieki/scream.wav")
man_crash = pygame.mixer.Sound("dzwieki/crash.wav")

# Events
while running:
    zegar.tick(60)
# MENU GLOWNE
    while gra == 'menu':
        if muzyka_gra:
            if muzyka_start == False:
                pygame.mixer.music.load('dzwieki/straszna.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if pstart.rect.collidepoint(pygame.mouse.get_pos()):
                pstart.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    gra = 'chapter1'
                    muzyka_start = False

            if not pstart.rect.collidepoint(pygame.mouse.get_pos()):
                pstart.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_ciemny.png'), (200, 50))

            if wlaczwylaczglos.rect.collidepoint(pygame.mouse.get_pos()):
                wlaczwylaczglos.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    if muzyka_gra:
                        muzyka_gra = False
                        pygame.mixer.music.stop()
                    else:
                        muzyka_gra = True
                        muzyka_start = False
            if not wlaczwylaczglos.rect.collidepoint(pygame.mouse.get_pos()):
                wlaczwylaczglos.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_ciemny.png'), (200, 50))

            if pquit.rect.collidepoint(pygame.mouse.get_pos()):
                pquit.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    running = False
                    pygame.quit()
            if not pquit.rect.collidepoint(pygame.mouse.get_pos()):
                pquit.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_ciemny.png'), (200, 50))

            if p_htp.rect.collidepoint(pygame.mouse.get_pos()):
                p_htp.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    gra = 'howtoplay'
            if not p_htp.rect.collidepoint(pygame.mouse.get_pos()):
                p_htp.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_ciemny.png'), (200, 50))


        screen.blit(grafika.menu, (0, 0))
        grupa_przyciskow.draw(screen)
        screen.blit(text_start, [190, 165])
        screen.blit(text_glos, [185, 225])
        screen.blit(text_quit, [190, 285])
        screen.blit(text_how_to_play, [155, 345])
        pygame.display.update()

# HOW TO PLAY
    while gra == 'howtoplay':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            mouse_buttons = pygame.mouse.get_pressed()
            if p_nowagra.rect.collidepoint(pygame.mouse.get_pos()):
                p_nowagra.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    gra = 'menu'

        screen.blit(grafika.las, (0, 0))
        text_zasady = font.render("How to play? Guess.", False, [255, 255, 255])
        screen.blit(text_zasady, [200, 200])
        grupa_przyciskow_restart.draw(screen)
        screen.blit(text_menu, [width - 188, 22])
        pygame.display.update()

# CHAPTER 1 - Wstep do fabuly
    while gra == 'chapter1':
        if muzyka_gra:
            if muzyka_start == False:
                pygame.mixer.music.load('dzwieki/spokojna1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if klatka == 6:
                        pygame.mixer.Sound.play(meow_angry)
                    if klatka == 2:
                        pygame.mixer.Sound.play(meow_ssss)
                    if klatka == 7:
                        pygame.mixer.Sound.play(meow_splash)
                    klatka = klatka + 1
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
            muzyka_start = True # Zminiam na true zeby wlaczyc nowa

        screen.blit(text_zycia, [width - 110, 10])
        pygame.display.update()

# CHAPTER 2 - Pierwsza minigra, klikanie odpowiedniej sekwencji przyciskow zeby nie utonac
    while gra == 'chapter2':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/szybka1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False
        if zycia < 1:
            muzyka_start = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(meow_die)
            gra = 'przegrana'
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "W"
                if event.key == pygame.K_a and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "A"
                if event.key == pygame.K_s and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "S"
                if event.key == pygame.K_d and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "D"
                if event.key == pygame.K_UP and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "W"
                if event.key == pygame.K_LEFT and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "A"
                if event.key == pygame.K_DOWN and len(wpisana_sekwencja) < 4:
                    wpisana_sekwencja = wpisana_sekwencja + "S"
                if event.key == pygame.K_RIGHT and len(wpisana_sekwencja) < 4:
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

        text_zycia_ale_bialy = font.render("Lives left: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 110, 10])
        czas += zegar.get_time()

        if sekwencja<8:
            if (czas > 15000):
                if wpisana_sekwencja == wylosowana_sekwencja:
                    punkty += 1
                print(f"punkty: {punkty} wylosowana sekwencja: {wylosowana_sekwencja} wpisana sekwencja: {wpisana_sekwencja} sekwencja: {sekwencja }klatka: {klatka} ")
                wylosowana_sekwencja = losowanie_sekwencji(4)
                wylosowana_sekwencja2 = wylosowana_sekwencja.replace('W', ' ^ ')
                wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('S', ' v ')
                wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('A', ' < ')
                wylosowana_sekwencja2 = wylosowana_sekwencja2.replace('D', ' > ')
                tekst_litery = font_duza.render(wylosowana_sekwencja2, False, [255, 255, 255])
                tekst_punkty = font_srednia.render("Points: " + str(punkty) + " /7", False, [255, 255, 255])
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
            if punkty<5:
                zycia = zycia - 1
                print(f"zycia: {zycia} ")
                klatka = 1
                sekwencja = 0
                punkty = 0
                tekst_punkty = font_srednia.render("Points: " + str(punkty) + " /7", False, [255, 255, 255])
            if punkty>=5:
                print(f"zycia: {zycia} ")
                gra = 'chapter3'
                klatka = 0
                muzyka_start = True

        clock.tick(FPS)
        screen.blit(tekst_litery, [(width / 2) - 125, height / 2 + 100])
        screen.blit(tekst_punkty, [(width / 2) - 80, height / 2 + 180])

        pygame.display.update()

# CHAPTER 3 - Chodzenie po lesie i szukanie patyka
    while gra == 'chapter3':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/straszna.wav')
                if wyjscie_z_wody == True:
                    pygame.mixer.Sound.play(meow_splash)
                    wyjscie_z_wody = False
                pygame.mixer.music.play(-1)
                muzyka_start = False
        if zycia < 1:
            muzyka_start = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(meow_die)
            gra = 'przegrana'
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            # Obsluga chodzenia
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
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
            screen.blit(text_woda_smierc, [70, height - 50])
            # Chodzenie i blokady krawedzi ekranu
            if kotek.rect.right > width:
                klatka = 1
                kotek.rect.left = 0
            if kotek.rect.left < 0:
                kotek.rect.left = 0
            # Wejscie do wody
            if kotek.rect.bottom > height-40:
                if kotek.rect.left < width-150:
                    zycia -= 1
            # LIS
            if kotek.rect.top < 80:
                gra = 'ucieczkalis'
                muzyka_start = True
                kotek.rect.x = (width / 2) - 40
                kotek.rect.y = height / 2
                kotek.update('grafiki/kotek_z_patykiem.png', 14 * 6, 13 * 6)
            # Zbieranie worka
            if worek == 0:
                x_worka = 250
                y_worka = height-150
                prawa = x_worka+90
                dol = y_worka+90
                screen.blit(grafika.worek, (x_worka, y_worka))
                if kotek.rect.colliderect(pygame.Rect(x_worka, y_worka, 90, 90)):   # Sprawdzanie kolizji z pozycją worka
                    worek = 1
                    pygame.mixer.Sound.play(meow_znalazl)
        if klatka == 1:
            screen.blit(grafika.las, (0, 0))
            #Chodzenie i blokady krawedzi ekranu
            if kotek.rect.left < 0:
                klatka = 0
                kotek.rect.right = width
            if kotek.rect.right > width:
                klatka = 2
                kotek.rect.left = 0
            # LIS
            if kotek.rect.top < 80:
                gra = 'ucieczkalis'
                muzyka_start = True
                kotek.rect.x = (width / 2) - 40
                kotek.rect.y = height/2
                kotek.update('grafiki/kotek_z_patykiem.png', 14 * 6, 13 * 6)
            # Zbieranie patyka
            if patyk == 0:
                x_patyka = 540
                y_patyka = 10
                prawa = x_patyka + 90
                dol = y_patyka + 90
                screen.blit(grafika.patyk, (x_patyka, y_patyka))
                if kotek.rect.colliderect(pygame.Rect(x_patyka, y_patyka, 90, 90)):  # Sprawdzanie kolizji z pozycją patyka
                    patyk = 1
                    pygame.mixer.Sound.play(meow_znalazl)
        if klatka == 2:
            screen.blit(grafika.sciezka, (0, 0))
            if kotek.rect.left < 0:
                klatka = 1
                kotek.rect.right = width
            if worek == 1 and patyk == 1:
                if kotek.rect.colliderect(pygame.Rect(600, 0, 100, 480)):
                    gra = 'chapter4'
                    muzyka_start = True
                    klatka = 1
                    kotek.rect.x = (width / 2) - 40
                    kotek.rect.y = height - 10
                    kotek.update('grafiki/kotek_z_patykiem.png', 14 * 6, 13 * 6)

        clock.tick(FPS)
        text_zycia_ale_bialy = font.render("Lives left: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 110, 10])
        grupa_sprajtow.draw(screen)
        pygame.display.update()

# CHAPTER 4 - BOSS FIGHT
    while gra == 'chapter4':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/spokojna1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False
        # Robie tak, żeby zwyrol ciągle sie poruszał w lewo
        zwyrol.rect.x -= 25
        if zwyrol.rect.x<0-zwyrol.width:
            zwyrol.rect.x = width
        if is_w_pressed:
            kotek.rect.y -= 25
            if kotek.rect.y < 0:
                is_w_pressed = False
                muzyka_start = True
                pygame.mixer.music.stop()
                gra = "ucieczkaboss"
                kotek.rect.x = (width / 2) - 6 * 6
                kotek.rect.y = (height/ 2) -140
                # Tutaj odpale minigierke z uciekaniem
            if kotek.rect.colliderect(pygame.Rect(zwyrol.rect.x+80, zwyrol.rect.y, 80, 100)):
                gra = "wygrana"
                muzyka_start = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    is_w_pressed = True

        clock.tick(FPS)
        screen.blit(grafika.sciezka_krzaki, (0, 0))
        text_zycia_ale_bialy = font.render("Lives left: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 110, 10])
        grupa_sprajtow.draw(screen)
        grupa_zwyroli.draw(screen)
        pygame.display.update()

# MINIGRA UCIEKANIE PRZED ZWYROLEM
    while gra == 'ucieczkaboss':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/szybka1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False

        kotek.rect.y += 2
        tlo1y += 5
        tlo2y += 5
        if zycia < 1:
            muzyka_start = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(meow_die)
            gra = 'przegrana'

        # Jezeli wybiegnie do gory poza ekran to wraca do wbiegania patykniem w rower
        if kotek.rect.y < -20:
            zycia += 1
            gra = 'chapter4'
            muzyka_start = True
            kotek.rect.y = height - 70
        # Jezeli dogoni go rower to traci jedno zycie i wraca do wbiegania patykniem w rower
        if kotek.rect.y > height-200:
            zycia -= 1
            gra = 'chapter4'
            muzyka_start = True
            kotek.rect.y = height-70
        if tlo1y == 1440:
            tlo1y = 0
            tlo2y = -3 * height
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    kotek.rect.y -= 15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_space_pressed = True

        clock.tick(FPS)
        screen.blit(grafika.tlo_uciekania1, (0, tlo1y))
        screen.blit(grafika.tlo_uciekania2, (0, tlo2y))
        text_zycia_ale_bialy = font.render("Lives left: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 110, 10])
        grupa_sprajtow.draw(screen)
        screen.blit(grafika.ziomus_od_tylu, [(width / 2) - 50, height - 200])
        pygame.display.update()

# MINIGRA UCIEKANIE PRZED lisEM
    while gra == 'ucieczkalis':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/szybka1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False

        kotek.rect.y += 2
        tlo1y += 5
        tlo2y += 5

        if zycia < 1:
            muzyka_start = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(meow_die)
            gra = 'przegrana'

        # Jezeli wybiegnie do gory poza ekran to wraca do wbiegania patykniem w rower
        if kotek.rect.y < -20:
            gra = 'chapter3'
            muzyka_start = True
            kotek.rect.y = height/2
            kotek.rect.x = (width / 2)
            kotek.update('grafiki/kotek.png', 110, 90)
        # Jezeli dogoni go rower to traci jedno zycie i wraca do wbiegania patykniem w rower
        if kotek.rect.y > height - 200:
            zycia -= 1
            gra = 'chapter3'
            muzyka_start = True
            kotek.rect.y = height/2
            kotek.rect.x = (width / 2)
            kotek.update('grafiki/kotek.png', 110, 90)
        if tlo1y == 1440:
            tlo1y = 0
            tlo2y = -3 * height
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    kotek.rect.y -= 15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_space_pressed = True

        clock.tick(FPS)
        screen.blit(grafika.tlo_uciekania1, (0, tlo1y))
        screen.blit(grafika.tlo_uciekania2, (0, tlo2y))
        text_zycia_ale_bialy = font.render("Lives left: " + str(zycia), False, [255, 255, 255])
        screen.blit(text_zycia_ale_bialy, [width - 110, 10])
        grupa_sprajtow.draw(screen)
        screen.blit(grafika.lis, [(width / 2) - 40, height - 130])
        pygame.display.update()

# EKRAN SMIERCI
    while gra == 'przegrana':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/straszna.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if p_nowagra.rect.collidepoint(pygame.mouse.get_pos()):
                p_nowagra.image = pygame.transform.scale(pygame.image.load('grafiki/pstart_jasny.png'), (200, 50))
                if mouse_buttons[0]:
                    gra = 'menu'
                    muzyka_start = True
                    #reset_zmiennych()
                    zycia = 9  # Zmienna zyc kotka
                    klatka = 1
                    czas = 0
                    x_kotka = width / 2  # pozycja poczatkowa kotka
                    y_kotka = height / 2 - 50
                    x_zwyrola = width - 26 * 7
                    y_zwyrola = 60
                    punkty = 0
                    sekwencja = 0
                    tekst_punkty = font_srednia.render("Punkty: " + str(punkty) + " /7", False, [255, 255, 255])
                    worek = 0  # Zmienna pokazujaca czy zebrało sie worek czy nie
                    patyk = 0
                    is_w_pressed = False
                    tlo1y = 0
                    tlo2y = -3 * height
                    text_zycia = font.render("zycia: " + str(zycia), False, [0, 0, 0])
                    text_zycia_ale_bialy = font.render("zycia: " + str(zycia), False, [255, 255, 255])
                    print(zycia)

        screen.blit(grafika.grob, (0, 0))
        text_grob = font.render("Cat DIED :'c", False, [255, 255, 255])
        screen.blit(text_grob, [width/2, height/2 +100])
        grupa_przyciskow_restart.draw(screen)
        screen.blit(text_restart, [width-150, 20])
        pygame.display.update()

# EKRAN WYGRANEJ, napisy koncowe
    while gra == 'wygrana':
        if muzyka_gra:
            if muzyka_start == True:
                pygame.mixer.music.load('dzwieki/spokojna1.wav')
                pygame.mixer.music.play(-1)
                muzyka_start = False
        if koncowy_y == -height:
            koncowy_y = height
        if klatka == 0:
            screen.blit(grafika.wypadek1, (0, 0))
        if klatka == 1:
            screen.blit(grafika.wypadek2, (0, 0))
        if klatka == 2:
            screen.blit(grafika.wypadek3, (0, 0))
        if klatka == 3:
            screen.blit(grafika.wypadek4, (0, 0))
        if klatka == 4:
            screen.blit(grafika.wypadek5, (0, 0))
        if klatka == 5:
            screen.blit(grafika.wypadek6, (0, 0))
        if klatka == 6:
            screen.blit(grafika.wypadek7, (0, 0))
        if klatka == 7:
            screen.blit(grafika.wypadek8, (0, 0))
        if klatka == 8:
            screen.blit(grafika.wypadek9, (0, 0))
        if klatka >= 9:
            koncowy_y -= 1
            screen.blit(grafika.koncowy, (0, 0))
            screen.blit(grafika.tekst_koncowy, (20, koncowy_y))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    klatka += 1
                if klatka == 2:
                    pygame.mixer.Sound.play(man_scream)
                if klatka == 4:
                    pygame.mixer.Sound.play(man_crash)

        pygame.display.update()

pygame.quit()