
import tkinter as tk


class Card:
    def __init__(self, rank: str, suit: str):
        if rank in ('king', 'queen', 'jack'):
            self.value = 10
        elif rank == '1':
            self.value = 11
        else:
            self.value = int(rank)
        image_name = f'cards/{rank}_{suit}.png'
        self.image = tk.PhotoImage(file=image_name)


# For testing

if __name__ == '__main__':
    win = tk.Tk()
    card1 = Card('10', 'diamond')
    card2 = Card('1', 'spade')
    tk.Label(win, compound='top', image=card1.image,
             text=str(card1.value)).grid()
    tk.Label(win, compound='top', image=card2.image,
             text=str(card2.value)).grid()
    win.mainloop()
