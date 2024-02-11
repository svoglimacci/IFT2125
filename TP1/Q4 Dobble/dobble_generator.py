import random

class Generator():
    def __init__(self, order=7):
        self.order = order
        self.symbols_per_card = order + 1
        self.total_cards_symbols = order**2 + order + 1

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        # Create an empty array of size (order x order) for cards
        cards = [['' for _ in range(self.order)] for _ in range(self.order)]

        # Create an empty array of size (order + 1) for the horizon
        horizon = ['' for _ in range(self.order + 1)]

        # Generate symbols for each card
        for i in range(self.order):
            for j in range(self.order):
                cards[i][j] = i * self.order + j + 1

        # Generate symbols for the horizon
        for i in range(self.order + 1):
            horizon[i] = self.order**2 + i + 1

                # Randomly shuffle symbols on each card
        for i in range(self.order):
            random.shuffle(cards[i])

        # Randomly shuffle symbols on the horizon
        random.shuffle(horizon)

        # Write cards to the cards_file
        with open(cards_file, 'w') as file:
            for i in range(self.order):
                file.write(' '.join(map(str, cards[i])) + '\n')

            # Write horizon symbols to the file
            file.write(' '.join(map(str, horizon)))

        if verbose:
            print(f"Generation complete. Cards written to {cards_file}")

# Example usage:
# generator = Generator(order=5)
# generator.generate(cards_file="cartes.txt", verbose=True)
