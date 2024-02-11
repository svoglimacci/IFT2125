#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        # TODO
        # a completer
        with open(cards_file, "r") as f:

          cards_data = [list(map(int, line.split())) for line in f.readlines()]

        symbol_count = len(cards_data[0])


        # Calculate the number of rows and columns for the grid
        rows = math.ceil(math.sqrt(symbol_count))
        columns = math.ceil(symbol_count / rows)

        print(f"Rows: {rows}, Columns: {columns}")

                # Calculate the length from corner to corner (diagonal)
        diagonal = 2 * math.sqrt((self.pic_size / 2) ** 2 + (self.pic_size / 2) ** 2)

        # Calculate the size of the resized symbols so that they fit on the card even if rotated
        symbol_size = int(diagonal / (columns + 1))

        # Calculate the gap between symbols, considering the border size
        gap = int((self.pic_size - (symbol_size * columns)) / (columns + 1)) - self.border_size


        # Assign symbols to visual cards
        for i, card_symbols in enumerate(cards_data):
            card_image = Image.new("RGB", (self.pic_size, self.pic_size), "white")
            x = self.border_size
            y = self.border_size
            count = 0

            for symbol_digit in card_symbols:


                # Create the symbol image path
                symbol_path = os.path.join("images", f"{symbol_digit}.png")

                # Open the symbol image using Pillow
                symbol_image = Image.open(symbol_path)

                # Resize & Rotate the symbol image
                symbol_image = symbol_image.resize((symbol_size//2, symbol_size//2))

                symbol_image = symbol_image.rotate(random.randint(0, 360), expand=1, translate=None, fillcolor=(255, 255, 255))

                card_image.paste(symbol_image, (x, y))


                if (count + 1) % columns == 0 and count != 0:
                  y += symbol_size + gap
                  x = 10
                else:
                  x += symbol_size + gap

                count += 1

            # Save the card with a unique filename in the "results" folder
            card_filename = f"results/card{i + 1}.jpg"
            card_image.save(card_filename)



