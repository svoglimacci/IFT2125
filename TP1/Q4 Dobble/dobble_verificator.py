#Nom, Matricule
#Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file = "cartes.txt", verbose = False):

        if verbose :
            print("***Verification des cartes***")

        is_optimal = True

        with open(cards_file, "r") as f:
            cards = f.readlines()

        for i in range(len(cards)):
            cards[i] = cards[i].split()

        horizon = cards[-1]

        card_count = len(cards)

        order = len(horizon) - 1


        optimal_count = order ** 2 + order + 1

        symbol_count = order + 1

        # test : le nombre de carte devrait être optimal
        if card_count != optimal_count:
            is_optimal = False

        # test : le nombre de symboles par carte est le même pour chaque carte
        for card in cards:
            if len(card) != symbol_count:
                return 2


        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
        for i in range(card_count):
            for j in range(i+1, card_count):
                common = set(cards[i]) & set(cards[j])
                if len(common) != 1:
                    return 2

        # test : le nombre de symbole total devrait être optimal
        symbols = set.union(*[set(card) for card in cards])
        if len(symbols) != optimal_count:
            is_optimal = False



        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide


        if is_optimal:
            return 0
        else:
            return 1



