#Simon Voglimacci Stephanopoli, 20002825
#Julie Yang, 20239909

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

        with open(cards_file, "r") as file:
            cards = file.readlines()

        # remove the "\n" character at the end of each line
        cards = [card.strip() for card in cards]

        # convert each line into a list of integers
        cards = [list(map(int, card.split())) for card in cards]


        card_count = len(cards) # number of rows
        order = len(cards[0]) -1   # number of columns

        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        img_path = "images/"
        images = [] # list of image objects

        # nb of cards = nb of symbols
        for i in range(0, card_count):
            img_name = f"{i+1}.png"
            if os.path.exists(img_path + img_name):
                images.append(Image.open(img_path + img_name))
            else:
                print(f"ERROR: image file not found")
                return

        results_path = "results/"

        #card per row
        cards_per_row = 3
        if order > 9:
            cards_per_row = 3 + (order+2) % 3


        # card dimensions
        width = self.pic_size * cards_per_row
        height = self.pic_size * cards_per_row

        # card dimensions + border
        new_width = width + 2 * self.border_size
        new_height = height + 2 * self.border_size

        # for each card
        for i in range(card_count):
            border = Image.new("RGB", (new_width, new_height), "gray")
            card = Image.new("RGB", (width, height), "white")
            # placement of images on visual cards, rotations appreciated
            for j, sym in enumerate(cards[i]):
                symbol = images[sym-1].rotate(random.randint(0,360), expand=True, fillcolor="white")
                symbol = symbol.resize((self.pic_size, self.pic_size))
                img_offset = (j % cards_per_row) * self.pic_size, (j // cards_per_row) * self.pic_size
                card.paste(symbol, img_offset)


            # added border on visual cards
            border.paste(card, (self.border_size, self.border_size))


            # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            border.save(results_path + f"card{i+1}.jpg")