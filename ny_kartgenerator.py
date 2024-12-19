# # import random

# # def generate_map_with_rocks(width, height, output_file="underground.txt"):
# #     # Säkerställ att bredd och höjd är tillräckligt stora
# #     if width < 3 or height < 3:
# #         print("Bredd och höjd måste vara minst 3 för att kunna ha en yttre ram.")
# #         return

# #     # Skapa en tom karta
# #     grid = []

# #     for row_index in range(height):
# #         row = []
# #         for col_index in range(width):
# #             # Om det är första/sista raden eller första/sista kolumnen
# #             if row_index == 0 or row_index == height - 1 or col_index == 0 or col_index == width - 1:
# #                 row.append('x')  # Yttre ram
# #             else:
# #                 # Slumpmässigt välj mellan 'x', '0', och 'B'
# #                 cell = random.choices(['X', '0', 'B'], weights=[0.2, 0.7, 0.1])[0]
# #                 row.append(cell)
# #         grid.append(row)

# #     add_rocks_with_values(grid)

# #     # Spara kartan till underground.txt
# #     with open(output_file, "w") as f:
# #         for row in grid:
# #             f.write(",".join(row) + "\n")

# #     print(f"Kartan med stenrösen har sparats till {output_file}!")


# # def add_rocks_with_values(grid):
# #     height = len(grid)
# #     width = len(grid[0])

# #     num_rocks = int(input("Hur många stenrösen vill du placera? "))
# #     for _ in range(num_rocks):
# #         while True:
# #             try:
# #                 x = int(input(f"Ange X-koordinat (1-{width - 2}): "))
# #                 y = int(input(f"Ange Y-koordinat (1-{height - 2}): "))
# #                 value = int(input("Ange antal missiler som krävs för att rensa stenröset: "))

# #                 # Kontrollera att positionen är giltig och inte redan upptagen för man kan bara ha på platser som har 0
# #                 if grid[y][x] == '0':  
# #                     grid[y][x] = str(value) 
# #                     print(f"Stenrös placerat på ({x}, {y}) med värdet {value}.")
# #                     break
# #                 else:
# #                     print("Positionen är inte tom. Försök igen.")
# #             except ValueError:
# #                 print("Ogiltigt värde. Försök igen.")


# # #funkion ifall man vill ha slumpmässigt
# # def add_random_rocks(grid, count=3):
# #     height = len(grid)
# #     width = len(grid[0])
# #     added = 0

# #     while added < count:
# #         x = random.randint(1, width - 2)
# #         y = random.randint(1, height - 2)
# #         if grid[y][x] == '0':  # Endast tomma platser
# #             value = random.randint(1, 5)  
# #             grid[y][x] = str(value)
# #             added += 1
# #             print(f"Slumpmässigt stenrös placerat på ({x}, {y}) med värdet {value}.")


# # # Använd kartgeneratorn
# # generate_map_with_rocks(10, 10)

# import random

# def generate_map_with_rocks_and_submarines(width, height, uboat_file="uboat.txt", output_file="underground.txt"):
#     # Säkerställ att bredd och höjd är tillräckligt stora
#     if width < 3 or height < 3:
#         print("Bredd och höjd måste vara minst 3 för att kunna ha en yttre ram.")
#         return

#     # Skapa en tom karta
#     grid = []

#     for row_index in range(height):
#         row = []
#         for col_index in range(width):
#             # Om det är första/sista raden eller första/sista kolumnen
#             if row_index == 0 or row_index == height - 1 or col_index == 0 or col_index == width - 1:
#                 row.append('x')  # Yttre ram
#             else:
#                 # Slumpmässigt välj mellan 'x', '0', och 'B'
#                 cell = random.choices(['x', '0', 'B'], weights=[0.2, 0.7, 0.1])[0]
#                 row.append(cell)
#         grid.append(row)

#     # Lägg till ubåtar från uboat.txt
#     add_submarines_from_file(grid, uboat_file)

#     # Lägg till stenrösen med värden
#     add_rocks_with_values(grid)

#     # Spara kartan till underground.txt
#     with open(output_file, "w") as f:
#         for row in grid:
#             f.write(",".join(row) + "\n")

#     print(f"Kartan med stenrösen och ubåtar har sparats till {output_file}!")

# def add_submarines_from_file(grid, uboat_file):
#     try:
#         with open(uboat_file, "r") as f:
#             lines = f.readlines()

#         # Ignorera första raden (rubriker)
#         for index, line in enumerate(lines[1:], start=1):
#             data = line.strip().split(",")
#             X0, Y0 = int(data[0]), int(data[1])

#             # Kontrollera att startpositionen är giltig och inte blockerad
#             if grid[Y0][X0] == '0':
#                 grid[Y0][X0] = f"U{index}"  # Markera ubåten med en unik symbol
#                 print(f"Ubåt {index} placerad på ({X0}, {Y0}).")
#             else:
#                 print(f"Positionen ({X0}, {Y0}) för ubåt {index} är blockerad. Kan inte placera ubåten.")
#     except FileNotFoundError:
#         print(f"Filen {uboat_file} hittades inte.")
#     except Exception as e:
#         print(f"Ett fel inträffade vid läsning av ubåtar: {e}")

# def add_rocks_with_values(grid):
#     height = len(grid)
#     width = len(grid[0])

#     num_rocks = int(input("Hur många stenrösen vill du placera? "))
#     for _ in range(num_rocks):
#         while True:
#             try:
#                 x = int(input(f"Ange X-koordinat (1-{width - 2}): "))
#                 y = int(input(f"Ange Y-koordinat (1-{height - 2}): "))
#                 value = int(input("Ange antal missiler som krävs för att rensa stenröset: "))

#                 # Kontrollera att positionen är giltig och inte redan upptagen
#                 if grid[y][x] == '0':
#                     grid[y][x] = str(value)
#                     print(f"Stenrös placerat på ({x}, {y}) med värdet {value}.")
#                     break
#                 else:
#                     print("Positionen är inte tom. Försök igen.")
#             except ValueError:
#                 print("Ogiltigt värde. Försök igen.")

# # Använd kartgeneratorn
# generate_map_with_rocks_and_submarines(10, 10)


import random

def generate_map_with_rocks_and_submarines(width, height, uboat_file="uboat.txt", output_file="underground.txt"):
    # Säkerställ att bredd och höjd är tillräckligt stora
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
                row.append('x')  # Yttre ram
            else:
                # Slumpmässigt välj mellan 'x', '0', och 'B'
                cell = random.choices(['x', '0', 'B'], weights=[0.2, 0.7, 0.1])[0]
                row.append(cell)
        grid.append(row)

    # Lägg till ubåtar från uboat.txt
    add_submarines_from_file(grid, uboat_file)

    # Lägg till stenrösen med värden
    add_rocks(grid)

    # Spara kartan till underground.txt
    with open(output_file, "w") as f:
        for row in grid:
            f.write(",".join(row) + "\n")

    print(f"Kartan med stenrösen och ubåtar har sparats till {output_file}!")

def add_submarines_from_file(grid, uboat_file):
    try:
        with open(uboat_file, "r") as f:
            lines = f.readlines()

        # Ignorera första raden (rubriker)
        for index, line in enumerate(lines[1:], start=1):
            data = line.strip().split(",")
            X0, Y0 = int(data[0]), int(data[1])

            # Kontrollera att startpositionen är giltig och inte blockerad
            if grid[Y0][X0] == '0':
                grid[Y0][X0] = f"U{index}"  # Markera ubåten med en unik symbol
                print(f"Ubåt {index} placerad på ({X0}, {Y0}).")
            else:
                print(f"Positionen ({X0}, {Y0}) för ubåt {index} är blockerad. Kan inte placera ubåten.")
    except FileNotFoundError:
        print(f"Filen {uboat_file} hittades inte.")
    except Exception as e:
        print(f"Ett fel inträffade vid läsning av ubåtar: {e}")

def add_rocks(grid):
    choice = input("Vill du placera stenrösen manuellt (1) eller slumpmässigt (2)? ")

    if choice == "1":
        height = len(grid)
        width = len(grid[0])

        num_rocks = int(input("Hur många stenrösen vill du placera? "))
        for _ in range(num_rocks):
            while True:
                try:
                    x = int(input(f"Ange X-koordinat (1-{width - 2}): "))
                    y = int(input(f"Ange Y-koordinat (1-{height - 2}): "))
                    value = int(input("Ange antal missiler som krävs för att rensa stenröset: "))

                    # Kontrollera att positionen är giltig och inte redan upptagen
                    if grid[y][x] == '0':
                        grid[y][x] = str(value)
                        print(f"Stenrös placerat på ({x}, {y}) med värdet {value}.")
                        break
                    else:
                        print("Positionen är inte tom. Försök igen.")
                except ValueError:
                    print("Ogiltigt värde. Försök igen.")
    elif choice == "2":
        num_rocks = random.randint(5, 10)
        print(f"Genererar {num_rocks} slumpmässiga stenrösen...")
        height = len(grid)
        width = len(grid[0])

        for _ in range(num_rocks):
            while True:
                x = random.randint(1, width - 2)
                y = random.randint(1, height - 2)
                value = random.randint(1, 5)

                if grid[y][x] == '0':
                    grid[y][x] = str(value)
                    print(f"Stenrös placerat på ({x}, {y}) med värdet {value}.")
                    break
    else:
        print("Ogiltigt val. Försök igen.")

# Använd kartgeneratorn
generate_map_with_rocks_and_submarines(10, 10)
