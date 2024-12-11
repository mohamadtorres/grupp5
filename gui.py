import pygame, sys
from kartgenerator import kart_generator

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

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x,y))

def start():
    pygame.display.set_caption('Game')
    while True:
        SCREEN.fill("Blue")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def main_menu():
    user_input_x = ""
    user_input_y = ""

    input_rect_x = pygame.Rect(200, 150, 140,32)
    input_rect_y = pygame.Rect(200, 200, 140,32)
    color_passive = 90, 112, 107
    color_active = 102, 87, 87
    active_x = False
    active_y = False
    start_button = Button(200, 250, start_img, 0.25)
    pygame.display.set_caption('Menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if input_rect_x.collidepoint(event.pos):
                    active_x = True
                    active_y = False
                elif input_rect_y.collidepoint(event.pos):
                    active_y = True
                    active_x = False
                elif start_button.rect.collidepoint(event.pos):
                    kart_generator(int(user_input_x), int(user_input_y))
                    #start()
                else:
                    active_x = False
                    active_y = False
                

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
                if active_y == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_input_y = user_input_y[:-1]
                    else:
                        if len(user_input_y) > 2 and event.unicode.isdigit():
                            user_input_y = user_input_y[1:]
                            user_input_y += event.unicode
                        elif event.unicode.isdigit():
                            user_input_y += event.unicode
        if active_x:
            color_x = color_active
            color_y = color_passive
        elif active_y:
            color_y = color_active
            color_x = color_passive
        else:
            color_x = color_passive 
            color_y = color_passive
        SCREEN.blit(BG, (0,0))
        draw_text("THE SUB MAZE", font, TEXT_COL, 200, 50)

        pygame.draw.rect(SCREEN,color_x, input_rect_x)
        pygame.draw.rect(SCREEN,color_y, input_rect_y)

        text_surface_x = input_font.render(user_input_x, True, TEXT_COL)
        text_surface_y = input_font.render(user_input_y, True, TEXT_COL)
        SCREEN.blit(text_surface_x, (input_rect_x.x+5, input_rect_x.y))
        SCREEN.blit(text_surface_y, (input_rect_y.x+5, input_rect_y.y))
        
        start_button.draw()
        pygame.display.update()


main_menu()
