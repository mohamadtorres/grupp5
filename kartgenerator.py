import random

symboler = ["X", "0", "B"]

def kart_generator(width, height, output_file="underground.txt"):
    # Säkerställ att bredden och höjden är tillräckligt stora för att ha ramverk av 'x'
    if width < 3 or height < 3:
        print("Bredd och höjd måste vara minst 3 för att kunna ha en yttre ram.")
        return

    # Skapa en tom karta
    grid = []

    for row_index in range(height):
        row = []
        for col_index in range(width):
            # Om det är första/sista raden eller första/sista kolumnen
            if row_index == 0 or row_index == height - 1 or col_index == 0 or col_index == width - 1:
                row.append('X')  #Ytre ram ska ha bara X som jag har fattat
            else:
                cell = random.choices(symboler, weights=[0.2, 0.7, 0.1])[0]
                row.append(cell)
        grid.append(row)

    # Spara kartan till en fil
    with open(output_file, "w") as f:
        for row in grid:
            f.write(",".join(row) + "\n")

    print(f"Kartan har sparats till {output_file}!")
# Använd kartgeneratorn
kart_generator(100, 100)  # Generera en 10x10 karta
