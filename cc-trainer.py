#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox as tkmb
from tkinter import ttk

from Shoe import Shoe


WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300


class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Counting Trainer")
        self.option_add('*tearOff', tk.FALSE)

        self.build_menu()
        self.build_frames()
        self.build_bottom()

    def build_menu(self) -> None:
        menu_bar = tk.Menu(self)
        self['menu'] = menu_bar

        menu_file = tk.Menu(menu_bar)
        menu_edit = tk.Menu(menu_bar)
        menu_help = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_bar.add_cascade(menu=menu_edit, label='Edit')
        menu_bar.add_cascade(menu=menu_help, label='Help')

        menu_file.add_command(label='New manual session',
            command=self.start_manual)
        menu_file.add_command(label='New auto session')
        menu_file.add_command(label='Quit', command=self.quit)

        menu_edit.add_command(label='Settings')
        self.want_big_cards = tk.IntVar()
        self.want_big_cards.set(0)
        menu_edit.add_checkbutton(label='Big cards',
            variable=self.want_big_cards, onvalue=1, offvalue=0)
        menu_help.add_command(label='About',
                                   command=self.show_about_window)

    def build_frames(self) -> None:
        self.canvas = tk.Canvas(self,
                width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background='green')

        self.canvas.grid(row=0, column=0, sticky='news')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def build_bottom(self) -> None:
        button_frame = tk.Frame(self)
        button_frame.grid(row=10, column=0)
        self.button_deal = ttk.Button(button_frame, text='Deal',
            command=self.deal)
        self.button_deal.state(['disabled'])
        self.button_deal.grid()

        self.status_text = tk.StringVar()
        status_bar = ttk.Label(self, textvariable=self.status_text,
                                    anchor='w')
        status_bar.grid(row=11, column=0, sticky='ew')
        self.status_text.set('')

    def show_about_window(self) -> None:
        tkmb.showinfo(message='Card Counting Trainer 0.01')

    def start_manual(self) -> None:
        if self.want_big_cards.get():
            size = 2
        else:
            size = 1
        self.shoe = Shoe(1, card_size=size)
        self.shoe.shuffle()
        self.cards_dealt = 0
        self.status_text.set(f'Cards dealt: {self.cards_dealt}')
        self.button_deal.state(['!disabled'])

    def deal(self) -> None:
        if self.cards_dealt < 52:
            card = self.shoe.deal()
            self.canvas.delete('all')
            self.canvas.create_image(150, 150, image=card.image)
            self.cards_dealt += 1
            self.status_text.set(f'Cards dealt: {self.cards_dealt}')
        else:
            self.button_deal.state(['disabled'])


if __name__ == '__main__':
    gw = GameWindow()
    gw.mainloop()
