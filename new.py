import os
import pygame
import sys
import math
from collections import deque

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Lagt till bilder
BG = pygame.image.load("img/Bakgrund.png")
start_img = pygame.image.load("img/Start.png")
submarine_img = pygame.image.load("img/submarine.png").convert_alpha()
sten_img = pygame.image.load("img/sten.png").convert_alpha()
stenrös_img = pygame.image.load("img/stenrös.png").convert_alpha()

font = pygame.font.Font("Font/Jersey10-Regular.ttf", 55)
input_font = pygame.font.Font("Font/Jersey10-Regular.ttf", 30)
TEXT_COL = (150, 42, 42)


class Map:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.square_width = 0
        self.square_height = 0
        self.sten_resized = None
        self.submarine_resized = None
        self.submarines = []  # För att lagra ubåtarnas positioner
    def load_submarines(self):
        """Läser in ubåtspositioner från uboat.txt och lagrar dem."""
        self.submarines = []
        if os.path.exists("uboat.txt"):
            with open("uboat.txt") as f:
                lines = f.readlines()[1:]  # Ignorera rubriken
                for line in lines:
                    X0, Y0, XE, YE, M = map(int, line.strip().split(","))
                    self.submarines.append({"start": (X0, Y0), "end": (XE, YE), "current": (X0, Y0),"missiles": (M)})
    def get_cell(self, x, y):
        """Hämtar värdet på en viss position på kartan."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]  # Förutsatt att grid är en lista av rader
        return None

    def update_cell(self, x, y, value):
        """Uppdaterar en cell på kartan."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value
    def read_map(self):
        if not os.path.exists("underground.txt"):
            print("Filen underground.txt hittades inte. Generera en karta först.")
            sys.exit()

        self.grid = []
        with open("underground.txt") as r:
            for line in r:
                row = line.strip().split(",")
                self.grid.append(row)

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        self.square_width = 1080 // self.width
        self.square_height = 720 // self.height

        # Anpassa storleken på ikonerna
        self.sten_resized = pygame.transform.scale(sten_img, (self.square_width, self.square_height))
        self.submarine_resized = pygame.transform.scale(submarine_img, (self.square_width, self.square_height))
        self.stenrös_resized = pygame.transform.scale(stenrös_img, (self.square_width, self.square_height))
        self.load_submarines()

    def move_submarines(self):
        for sub in self.submarines:
            x, y = sub["current"]
            ex, ey = sub["end"]

            # Om ubåten redan är vid sitt mål
            if (x, y) == (ex, ey):
                print(f"Ubåt vid ({x}, {y}) har nått sitt mål.")
                continue

            # Pathfinding med BFS
            path = self.find_path((x, y), (ex, ey), sub["missiles"])
            if path:
                next_step = path[1]  # Nästa steg i vägen
                sub["current"] = next_step
            else:
                print(f"Ubåt vid ({x}, {y}) kunde inte hitta en väg till målet.")

    def find_path(self, start, end, missiles):
        """Hittar en väg från start till slut med BFS."""
        queue = deque([(start, [])])  # Håll reda på position och väg
        visited = set()  # Håll reda på besökta positioner
        visited.add(start)

        while queue:
            (current, path) = queue.popleft()
            cx, cy = current

            # Om vi har nått slutdestinationen
            if current == end:
                return path + [end]

            # Skanna omgivningen
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Upp, Ner, Vänster, Höger
                nx, ny = cx + dx, cy + dy

                if (nx, ny) in visited:
                    continue

                cell = self.get_cell(nx, ny)

                if cell == "0":  # Fri väg
                    queue.append(((nx, ny), path + [current]))
                    visited.add((nx, ny))
                elif cell.isdigit() and int(cell) > 0:  # Stenrös
                    if missiles > 0:  # Använd en missil
                        self.update_cell(nx, ny, "0")
                        queue.append(((nx, ny), path + [current]))
                        visited.add((nx, ny))
                        missiles -= 1
                elif cell == "x":  # Vägg
                    continue  # Gå inte till väggar

        return None  # Ingen väg hittades

    def draw_map(self):
        with open("underground.txt") as r:
            y_cord = 0
            for line in r:
                x_cord = 200
                for char in line.replace(',', ''):
                    if char == "x":  # Vägg
                        SCREEN.blit(self.sten_resized, (x_cord, y_cord))
                    elif char.isdigit() and int(char) > 0:  # Stenrös
                        SCREEN.blit(self.stenrös_resized, (x_cord, y_cord))
                    x_cord += self.square_width
                y_cord += self.square_height

        # Rita ubåtar på deras aktuella positioner
        for sub in self.submarines:
            x, y = sub["current"]
            SCREEN.blit(self.submarine_resized, (200 + x * self.square_width, y * self.square_height))

    def place_submarines(self):
        if not os.path.exists("uboat.txt"):
            print("Filen uboat.txt hittades inte.")
            return

        with open("uboat.txt") as r:
            lines = r.readlines()
            for index, line in enumerate(lines[1:], start=1):  # Ignorera rubriken
                data = line.strip().split(",")
                X0, Y0 = int(data[0]), int(data[1])

                # Kontrollera att startpositionen är inom kartans gränser
                if 1 <= X0 < self.width - 1 and 1 <= Y0 < self.height - 1:
                    with open("underground.txt", "r+") as f:
                        content = f.readlines()
                        map_line = list(content[Y0])
                        map_line[X0] = f"U{index}"  # Markera ubåten
                        content[Y0] = "".join(map_line)
                        f.seek(0)
                        f.writelines(content)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))


def start():
    game_rect = pygame.Rect(200, 0, 1080, 720)
    menu_bar_rect = pygame.Rect(0, 0, 200, 720)
    map_obj = Map()
    map_obj.read_map()

    clock = pygame.time.Clock()

    while True:
        SCREEN.fill((200, 200, 200), menu_bar_rect)
        SCREEN.fill((0, 0, 255), game_rect)

        map_obj.draw_map()
        map_obj.move_submarines()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(10)  # Uppdatera spelet 10 gånger per sekund

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

def main_menu():
    user_input_x = ""

    input_rect_x = pygame.Rect(200, 150, 140, 32)
    color_passive = (90, 112, 107)
    color_active = (102, 87, 87)
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
                    start()
                else:
                    active_x = False

            if event.type == pygame.KEYDOWN:
                if active_x:
                    if event.key == pygame.K_BACKSPACE:
                        user_input_x = user_input_x[:-1]
                    elif event.unicode.isdigit():
                        user_input_x += event.unicode

        color_x = color_active if active_x else color_passive
        SCREEN.blit(BG, (0, 0))
        draw_text("THE SUB MAZE", font, TEXT_COL, 160, 50)

        pygame.draw.rect(SCREEN, color_x, input_rect_x)
        text_surface_x = input_font.render(user_input_x, True, TEXT_COL)
        SCREEN.blit(text_surface_x, (input_rect_x.x + 5, input_rect_x.y))

        start_button.draw()
        pygame.display.update()


main_menu()
