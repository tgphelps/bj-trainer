
import tkinter as tk
from PIL import ImageTk, Image

# NOTE: These card images are 74x107 pixels
CARDS_DIR = 'cards'


class Card:
    def __init__(self, rank: str, suit: str, card_size=1) -> None:
        if rank in ('king', 'queen', 'jack'):
            self.value = 10
        elif rank == '1':
            self.value = 11
        else:
            self.value = int(rank)
        image_name = f'{CARDS_DIR}/{rank}_{suit}.png'
        if card_size == 1:
            self.image = tk.PhotoImage(file=image_name)
        else:
            image = Image.open(image_name)
            big_image = \
                image.resize((74 * card_size, 107 * card_size),
                Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(big_image)
            self.image = new_image


if __name__ == '__main__':
    win = tk.Tk()
    card1 = Card('10', 'diamond')
    card2 = Card('1', 'spade')
    tk.Label(win, compound='top', image=card1.image,
             text=str(card1.value)).grid()
    tk.Label(win, compound='top', image=card2.image,
             text=str(card2.value)).grid()
    win.mainloop()
