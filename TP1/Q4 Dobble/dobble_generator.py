#Simon Voglimacci Stephanopoli, 20002825
#Julie Yang, 20239909

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card

class Generator():
    def __init__(self, order = 7):
        self.order = order

    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("\n")

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        n = self.order

        #create matrix n x n
        cards = [[[] for i in range(n)] for j in range(n)]
        horizon = [[] for i in range(n+1)]



        symbols = [i+1 for i in range(n**2 + n + 1)]


        # rows
        for i in range(n):
            symbol = symbols.pop(0)
            for j in range(n):
                cards[i][j].append(symbol)
            horizon[0].append(symbol)


        # columns
        for j in range(n):
            symbol = symbols.pop(0)
            for i in range(n):
                cards[i][j].append(symbol)
            horizon[-1].append(symbol)

        symbol = symbols.pop(0)
        for i in range(n+1):
            horizon[i].append(symbol)

        # diagonals
        for i in range (n):
            for j in range(1, n):
                symbol = symbols.pop(0)
                horizon[j].append(symbol)
                for k in range(n):
                    temp = k * j + i
                    while temp > n-1:
                        temp -= n
                    cards[k][temp].append(symbol)


        cards.append(horizon)
        random.shuffle(cards)


        with open(cards_file, "w") as f:
            for row in cards:
                for i in range(len(row)):
                    f.write(" ".join(map(str, row[i])) + "\n")






