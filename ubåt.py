class Ubåt:
    def __init__(self, x, y, mål_x, mål_y, missiler, id):
        self.x = x
        self.y = y
        self.mål_x = mål_x
        self.mål_y = mål_y
        self.missiler = missiler
        self.id = id
        self.sprängd = False  # Markera om ubåten har blivit förstörd

    def flytta(self, riktning):
        if riktning == "upp":
            self.y -= 1
        elif riktning == "ner":
            self.y += 1
        elif riktning == "vänster":
            self.x -= 1
        elif riktning == "höger":
            self.x += 1

    def skanna_omgivning(self, karta):
        omgivning = {}
        riktningar = {
            "upp": (self.x, self.y - 1),
            "ner": (self.x, self.y + 1),
            "vänster": (self.x - 1, self.y),
            "höger": (self.x + 1, self.y),
        }

        for riktning, (x, y) in riktningar.items():
            if 0 <= x < len(karta[0]) and 0 <= y < len(karta):
                omgivning[riktning] = karta[y][x]
            else:
                omgivning[riktning] = "x"  # Utanför kartan
        return omgivning

    def nått_mål(self):
        return self.x == self.mål_x and self.y == self.mål_y

    def __str__(self):
        return f"Ubåt {self.id} på ({self.x}, {self.y}), mål ({self.mål_x}, {self.mål_y})"
