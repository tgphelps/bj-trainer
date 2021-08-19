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
        self.menu_bar = tk.Menu(self)
        self['menu'] = self.menu_bar

        self.menu_file = tk.Menu(self.menu_bar)
        self.menu_edit = tk.Menu(self.menu_bar)
        self.menu_help = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_file, label='File')
        self.menu_bar.add_cascade(menu=self.menu_edit, label='Edit')
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')

        self.menu_file.add_command(label='New manual session',
            command=self.start_manual)
        self.menu_file.add_command(label='New auto session')
        self.menu_file.add_command(label='Quit', command=self.quit)

        self.menu_edit.add_command(label='Settings')
        self.menu_help.add_command(label='About',
                                   command=self.show_about_window)

    def build_frames(self) -> None:
        self.canvas = tk.Canvas(self,
                width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background='green')

        self.canvas.grid(row=0, column=0, sticky='news')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def build_bottom(self) -> None:
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=10, column=0)
        self.button_deal = ttk.Button(self.button_frame, text='Deal',
            command=self.deal)
        self.button_deal.state(['disabled'])
        self.button_deal.grid()

        self.status_text = tk.StringVar()
        self.status_bar = ttk.Label(self, textvariable=self.status_text,
                                    anchor='w')
        self.status_bar.grid(row=11, column=0, sticky='ew')
        self.status_text.set('')

    def show_about_window(self) -> None:
        tkmb.showinfo(message='Card Counting Trainer 0.01')

    def start_manual(self) -> None:
        self.shoe = Shoe(1, card_size=2)
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
