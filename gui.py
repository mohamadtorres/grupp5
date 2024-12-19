import pygame, sys
#from kartgenerator import kart_generator

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))  

pygame.display.set_caption("Menu")

BG = pygame.image.load("img/Bakgrund.png")
start_img = pygame.image.load("img/Start.png")

font = pygame.font.Font("Font/Jersey10-Regular.ttf", 55)
input_font = pygame.font.Font("Font/Jersey10-Regular.ttf", 30)

TEXT_COL = (150, 42, 42)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width *scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):            
            SCREEN.blit(self.image, (self.rect.x+5, self.rect.y+5))
        else:
            SCREEN.blit(self.image, (self.rect.x, self.rect.y))



class Map():
    def __init__(self):
        self.width = 0
        self.height = 0
        self.square_width = 0
        self.square_height = 0
        self.sten_img = pygame.image.load("img/sten.png").convert_alpha()
        self.resized_image = None


    def read_map(self):
        with open("underground.txt") as r:
            for line in r:
                line = line.replace(',', '') 
                width = len(line.strip())
                self.width = max(self.width, width) 
                self.height += 1

        self.square_width = 1080 // self.width  
        self.square_height = 720 // self.height  

        self.resized_image = pygame.transform.scale(self.sten_img, (self.square_width, self.square_height))
        

    def draw_map(self):
        with open("underground.txt") as r:
            y_cord = 0
            for line in r: 
                line = line.replace(',', '') 
                x_cord = 200  
                for char in line:
                    if char == "X": 
                        SCREEN.blit(self.resized_image, (x_cord, y_cord))
                    x_cord += self.square_width
                y_cord += self.square_height



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x,y))


def start():
    game_rect = pygame.Rect(200, 0, 1080, 720)
    menu_bar_rect = pygame.Rect(0, 0, 200, 720)
    map = Map()
    map.read_map()

    pygame.display.set_caption('Game')

    while True:
        SCREEN.fill((200, 200, 200), menu_bar_rect)  
        SCREEN.fill((0, 0, 255), game_rect)  

        map.draw_map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main_menu():
    user_input_x = ""

    input_rect_x = pygame.Rect(200, 150, 140,32)
    color_passive = 90, 112, 107
    color_active = 102, 87, 87
    active_x = False
    start_button = Button(200, 200, start_img, 0.25)
    pygame.display.set_caption('Menu')
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if input_rect_x.collidepoint(event.pos):
                    active_x = True
                elif start_button.rect.collidepoint(event.pos):
                    if len(user_input_x) == 0:
                        start()
                    elif 9 < int(user_input_x) < 201:
                        kart_generator(int(user_input_x), int(user_input_x))
                        start()
                    else:
                        print("Fuck")
                else:
                    active_x = False                

            if event.type == pygame.KEYDOWN:
                if active_x == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_input_x = user_input_x[:-1]
                    else:
                        if len(user_input_x) > 2 and event.unicode.isdigit():
                            user_input_x = user_input_x[1:]
                            user_input_x += event.unicode
                        elif event.unicode.isdigit():
                            user_input_x += event.unicode

        if active_x:
            color_x = color_active
        else:
            color_x = color_passive 
        SCREEN.blit(BG, (0,0))
        draw_text("THE SUB MAZE", font, TEXT_COL, 160, 50)

        pygame.draw.rect(SCREEN,color_x, input_rect_x)

        text_surface_x = input_font.render(user_input_x, True, TEXT_COL)

        SCREEN.blit(text_surface_x, (input_rect_x.x+5, input_rect_x.y))
        
        start_button.draw()
        pygame.display.update()


main_menu()
