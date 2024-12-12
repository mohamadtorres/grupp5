from ubåt import Ubåt

class Simulering:
    def __init__(self, karta, ubåtsdata):
        self.karta = karta
        self.ubåtar = [
            Ubåt(x, y, mål_x, mål_y, missiler, idx)
            for idx, (x, y, mål_x, mål_y, missiler) in enumerate(ubåtsdata)
        ]

    def kör_tidssteg(self):
        for ubåt in self.ubåtar:
            if ubåt.sprängd:
                continue  # Hoppa över sprängda ubåtar

            # Skanna omgivningen (kan användas för framtida beslut)
            omgivning = ubåt.skanna_omgivning(self.karta)
            print(f"Omgivning för {ubåt}: {omgivning}")

            # Flytta mot mål
            if ubåt.x < ubåt.mål_x:
                ubåt.flytta("höger")
            elif ubåt.x > ubåt.mål_x:
                ubåt.flytta("vänster")
            elif ubåt.y < ubåt.mål_y:
                ubåt.flytta("ner")
            elif ubåt.y > ubåt.mål_y:
                ubåt.flytta("upp")

            if ubåt.nått_mål():
                print(f"{ubåt} har nått sitt mål!")
