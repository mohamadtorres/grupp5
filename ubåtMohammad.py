# def create_submarine_file(output_file="uboat.txt", map_width=10, map_height=10):
#     submarines = []
#     print("Ange ubåtarnas start- och slutpositioner samt antal missiler.")
#     print("Ange 'q' för X0 när du är klar.")

#     while True:
#         X0_input = input("Startposition X0 (eller 'q' för att avsluta): ")
#         if X0_input.lower() == 'q':
#             break
#         try:
#             X0 = int(X0_input)
#             Y0 = int(input("Startposition Y0: "))
#             XE = int(input("Slutposition XE: "))
#             YE = int(input("Slutposition YE: "))
#             M = int(input("Antal missiler M: "))

#             # Validera att positionerna är inom kartans gränser
#             if not (1 <= X0 < map_width - 1 and 1 <= Y0 < map_height - 1):
#                 print("Startpositionen är utanför kartans gränser. Försök igen.")
#                 continue
#             if not (1 <= XE < map_width - 1 and 1 <= YE < map_height - 1):
#                 print("Slutpositionen är utanför kartans gränser. Försök igen.")
#                 continue

#             submarine = (X0, Y0, XE, YE, M)
#             submarines.append(submarine)
#             print(f"Ubåt tillagd: Start ({X0},{Y0}), Mål ({XE},{YE}), Missiler {M}")
#         except ValueError:
#             print("Ogiltigt värde, försök igen.")

#     # Spara ubåtarna till uboat.txt
#     with open(output_file, "w") as f:
#         f.write("X0,Y0,XE,YE,M\n")
#         for sub in submarines:
#             f.write(f"{sub[0]},{sub[1]},{sub[2]},{sub[3]},{sub[4]}\n")
#     print(f"Ubåtsdata sparad till {output_file}")


# create_submarine_file()

import random

def create_submarine_file(output_file="uboat.txt", map_width=10, map_height=10):
    submarines = []
    print("Välj ett alternativ:")
    print("1. Ange ubåtarnas start- och slutpositioner manuellt.")
    print("2. Generera slumpmässiga ubåtar.")

    choice = input("Ditt val (1 eller 2): ")

    if choice == "1":
        print("Ange ubåtarnas start- och slutpositioner samt antal missiler.")
        print("Ange 'q' för X0 när du är klar.")

        while True:
            X0_input = input("Startposition X0 (eller 'q' för att avsluta): ")
            if X0_input.lower() == 'q':
                break
            try:
                X0 = int(X0_input)
                Y0 = int(input("Startposition Y0: "))
                XE = int(input("Slutposition XE: "))
                YE = int(input("Slutposition YE: "))
                M = int(input("Antal missiler M: "))

                # Validera att positionerna är inom kartans gränser
                if not (1 <= X0 < map_width - 1 and 1 <= Y0 < map_height - 1):
                    print("Startpositionen är utanför kartans gränser. Försök igen.")
                    continue
                if not (1 <= XE < map_width - 1 and 1 <= YE < map_height - 1):
                    print("Slutpositionen är utanför kartans gränser. Försök igen.")
                    continue

                submarine = (X0, Y0, XE, YE, M)
                submarines.append(submarine)
                print(f"Ubåt tillagd: Start ({X0},{Y0}), Mål ({XE},{YE}), Missiler {M}")
            except ValueError:
                print("Ogiltigt värde, försök igen.")

    elif choice == "2":
        num_submarines = random.randint(5, 10)
        print(f"Genererar {num_submarines} slumpmässiga ubåtar...")

        for i in range(num_submarines):
            X0 = random.randint(1, map_width - 2)
            Y0 = random.randint(1, map_height - 2)
            XE = random.randint(1, map_width - 2)
            YE = random.randint(1, map_height - 2)
            M = random.randint(1, 5)  #missiler mellan 1st till 5st

            submarine = (X0, Y0, XE, YE, M)
            submarines.append(submarine)
            print(f"Ubåt {i+1} tillagd: Start ({X0},{Y0}), Mål ({XE},{YE}), Missiler {M}")

    else:
        print("Ogiltigt val. Försök igen.")
        return

    # Spara ubåtarna till uboat.txt
    with open(output_file, "w") as f:
        f.write("X0,Y0,XE,YE,M\n")
        for sub in submarines:
            f.write(f"{sub[0]},{sub[1]},{sub[2]},{sub[3]},{sub[4]}\n")
    print(f"Ubåtsdata sparad till {output_file}")

create_submarine_file()
