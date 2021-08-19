
from Card import Card


SUITS = ['spade', 'heart', 'diamond', 'club']
FACE_CARDS = ['jack', 'queen', 'king']


def create_deck() -> list[Card]:
    cards: list[Card] = []
    for suit in SUITS:
        for rank in range(1, 10+1):
            card = Card(str(rank), suit)
            cards.append(card)
        for rank in FACE_CARDS:
            card = Card(rank, suit)
            cards.append(card)
    return cards


if __name__ == '__main__':
    import tkinter as tk
    win = tk.Tk()
    deck = create_deck()
    tk.Label(win, image=deck[0].image).grid(row=0, column=0)
    tk.Label(win, image=deck[1].image).grid(row=0, column=1)
    tk.Label(win, image=deck[51].image).grid(row=0, column=2)
    win.mainloop()
