from ssl import OP_NO_TLSv1
import pygame
from pygame.locals import *
from pygame import mixer
import pickle

from button import Button
from store import Store


try:
    with open('assets/totallynotsavedata/notthesavedata.pickle', 'rb') as handle:
        myStore = pickle.load(handle)
except FileNotFoundError:
    myStore=Store()


def human_format(num, dec):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return f'%.{dec}f%s' % (num, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("OBELCLICKER 2.0 (NO WAY ONG ONG 🤪🤪🤪🤪🤪🤪)")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

clicker = pygame.image.load("assets/Obelclick.png")
xhamster = pygame.image.load("assets/XHamster1.png")
lube = pygame.image.load("assets/lube.jpg")
obelfans = pygame.image.load("assets/OnlyFans.png")
folkedans = pygame.image.load("assets/Folkedans.jpg")
speedobels = pygame.image.load("assets/speedobels.png")


size = width, height = (1280,720)
screen = pygame.display.set_mode((size))

running = True

font = pygame.font.SysFont("cambria", 45)

BG = pygame.image.load("assets/Baggrund.png")
obelClick = Button(image=clicker, pos=(300, 360), 
                text_input="", font=get_font(75), base_color="White", hovering_color="Green", turn=False)
#obelBirth = Button(image=clicker, pos=(300, 360), 
#                text_input="", font=get_font(75), base_color="White", hovering_color="Green", turn=False)

# Music 🤪
pygame.mixer.init()
pygame.mixer.music.load("assets/BLOONS.mp3")
pygame.mixer.music.play(-1)

while running:

    # Timer
    ms = clock.tick(200) / 1000

    # Obels per second
    myStore.balance += ms * myStore.ops()

    SCREEN.blit(BG, (0, 0))

    mousePos = pygame.mouse.get_pos()

    # XHamster
    obelUpgrade1 = Button(image=xhamster, pos=(1090, 195), 
            text_input=str(human_format(myStore.get("xhamster").price, 2)), font=get_font(15), base_color="White", hovering_color="Green")
    obelUpgrade1.update(SCREEN)
    # Lube
    obelUpgrade2 = Button(image=lube, pos=(1090, 285), 
        text_input=str(human_format(myStore.get("lube").price, 2)), font=get_font(15), base_color="Black", hovering_color="Green")
    obelUpgrade2.update(SCREEN)
    # ObelFans
    obelUpgrade3 = Button(image=obelfans, pos=(1090, 370), 
        text_input=str(human_format(myStore.get("obelfans").price, 2)), font=get_font(15), base_color="Black", hovering_color="Green")
    obelUpgrade3.update(SCREEN)
    #Folkedans
    obelUpgrade4 = Button(image=folkedans, pos=(1090, 460), 
        text_input=str(human_format(myStore.get("folkedans").price, 2)), font=get_font(15), base_color="Black", hovering_color="Green")
    obelUpgrade4.update(SCREEN)
    #SpeedOBels
    obelUpgrade5 = Button(image=speedobels, pos=(1090, 550), 
        text_input=str(human_format(myStore.get("speedobels").price, 2)), font=get_font(15), base_color="Black", hovering_color="Green")
    obelUpgrade5.update(SCREEN)
        

    obelClick.changeColor(mousePos)
    obelClick.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('assets/totallynotsavedata/notthesavedata.pickle', 'wb') as handle:
                pickle.dump(myStore, handle, protocol=pickle.HIGHEST_PROTOCOL)

            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if obelClick.checkForInput(mousePos):
                myStore.balance += myStore.opk()

            if obelUpgrade1.checkForInput(mousePos):
                myStore.buy("xhamster")
            if obelUpgrade2.checkForInput(mousePos):
                myStore.buy("lube")
            if obelUpgrade3.checkForInput(mousePos):
                myStore.buy("obelfans")
            if obelUpgrade4.checkForInput(mousePos):
                myStore.buy("folkedans")
            if obelUpgrade5.checkForInput(mousePos):
                myStore.buy("speedobels")

        if event.type == KEYDOWN:
            if event.key in [K_o]:
                myStore.balance += 1000000



    # Render Billeder og text
    # ObelCoins
    ObelVis = get_font(35).render(f"{human_format(myStore.balance, 1)}", 1, (0,0,0))
    ObelVisRect = ObelVis.get_rect(right=1210, top=91)
    screen.blit(ObelVis, ObelVisRect)
    # ObelPS
    ObelPSVis = get_font(35).render(f"{human_format(myStore.ops(), 1)}", 1, (0,0,0))
    ObelPSVisRect = ObelPSVis.get_rect(left=775, top=91)
    screen.blit(ObelPSVis, ObelPSVisRect)
    # ObelCoins Per Click
    ObelPKVis = get_font(35).render(f"OPK: {human_format(myStore.opk(), 1)}", 1, (0,0,0))
    ObelPKVisRect = ObelPKVis.get_rect(left=200, top=650)
    screen.blit(ObelPKVis, ObelPKVisRect)
    # Antal XHamster
    XHamster = get_font(45).render(f"{round(myStore.get('xhamster').owned):>5}", 1, (0,0,0))
    screen.blit(XHamster, (730, 175))
    # Antal Lube
    Lube = get_font(45).render(f"{round(myStore.get('lube').owned):>5}", 1, (0,0,0))
    screen.blit(Lube, (730, 265))
    # Antal ObelFans
    ObelFans = get_font(45).render(f"{round(myStore.get('obelfans').owned):>5}", 1, (0,0,0))
    screen.blit(ObelFans, (730, 355))
    # Antal FolkeDans
    FolkeDans = get_font(45).render(f"{round(myStore.get('folkedans').owned):>5}", 1, (0,0,0))
    screen.blit(FolkeDans, (730, 445))
    # Antal SpeedObels
    SpeedObels = get_font(45).render(f"{round(myStore.get('speedobels').owned):>5}", 1, (0,0,0))
    screen.blit(SpeedObels, (730, 535))
    # Vis ObelClickeren ongong 🤪
    Title = get_font(60).render("OBELCLICKER 2.0", 1, (240, 12, 217))
    screen.blit(Title, (200, 10))
    #Update display 🤪
    pygame.display.update()

            

pygame.quit