class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Verification des cartes***")

        # Read cards from the file
        with open(cards_file, 'r') as file:
            lines = file.readlines()

        # Extract symbols from each card
        cards = [list(map(int, line.split())) for line in lines[:-1]]  # Exclude the horizon line
        horizon = list(map(int, lines[-1].split()))

        order = len(cards)

        symbols_per_card = len(cards[0])

        # Test: the number of cards and symbols should be optimal
        optimal_cards = order**2 + order + 1
        optimal_symbols = symbols_per_card * order

        if len(cards) != optimal_cards or len(horizon) != optimal_symbols + 1:
            if verbose:
                print("Erreur: Le nombre de cartes ou de symboles n'est pas optimal.")
            return 2

        # Test: the number of symbols per card is the same for each card
        for card in cards:
            if len(card) != symbols_per_card:
                if verbose:
                    print("Erreur: Le nombre de symboles par carte n'est pas le même pour chaque carte.")
                return 2

        # Test: each pair of cards always shares one and only one symbol in common
        for i in range(order):
            for j in range(i + 1, order):
                common_symbols = set(cards[i]) & set(cards[j])
                if len(common_symbols) != 1:
                    if verbose:
                        print("Erreur: Chaque paire de cartes devrait partager un et un seul symbole en commun.")
                    return 2

        if verbose:
            print("Vérification réussie. Le jeu est valide et optimal.")

        # Return 0 if the set is valid and optimal
        # Return 1 if the set is valid but not optimal
        # Return 2 if the set is invalid
        return 0 if optimal_cards == optimal_symbols + 1 else 1
