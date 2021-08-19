
import random
from Card import Card


SUITS = ['spade', 'heart', 'diamond', 'club']
FACE_CARDS = ['jack', 'queen', 'king']


class Shoe:
    def __init__(self, num_decks: int, card_size=1) -> None:
        deck = create_deck(card_size)
        self.shoe = num_decks * deck
        self.shoe_size = 52 * num_decks
        assert len(self.shoe) == self.shoe_size
        self.next = 0
        random.seed()

    def shuffle(self) -> None:
        random.shuffle(self.shoe)
        self.next = 0

    def deal(self) -> Card:
        assert self.next < self.shoe_size
        c = self.shoe[self.next]
        self.next += 1
        return c

    def remaining(self) -> int:
        return self.shoe_size - self.next


def create_deck(card_size: int) -> list[Card]:
    cards: list[Card] = []
    for suit in SUITS:
        for rank in range(1, 10 + 1):
            card = Card(str(rank), suit, card_size)
            cards.append(card)
        for rank in FACE_CARDS:
            card = Card(rank, suit, card_size)
            cards.append(card)
    assert len(cards) == 52
    return cards


if __name__ == '__main__':
    import tkinter as tk
    win = tk.Tk()
    s = Shoe(1)
    tk.Label(win, image=s.deal().image).grid(row=0, column=0)
    tk.Label(win, image=s.deal().image).grid(row=0, column=1)
    tk.Label(win, image=s.shoe[51].image).grid(row=0, column=2)
    s.shuffle()
    tk.Label(win, image=s.deal().image).grid(row=0, column=3)
    win.mainloop()
