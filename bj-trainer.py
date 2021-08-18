#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox as tkmb
from tkinter import ttk


WINDOW_WIDTH = 1200
DEALER_HEIGHT = 300
PLAYER_HEIGHT = 300

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*tearOff', tk.FALSE)

        self.build_menu()
        self.build_frames()
        self.build_bottom()

    def build_menu(self):
        self.menu_bar = tk.Menu(self)
        self['menu'] = self.menu_bar

        self.menu_file = tk.Menu(self.menu_bar)
        self.menu_help = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_file, label='File')
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')

        self.menu_file.add_command(label='Quit', command=self.quit)
        self.menu_help.add_command(label='About', command=show_about_window)

    def build_frames(self):
        self.dealer_frame = ttk.Frame(self)
        self.player_frame = ttk.Frame(self)
        self.dealer_frame.grid(row=1)
        self.player_frame.grid(row=2)

        self.dealer_canvas = tk.Canvas(self.dealer_frame,
            width=WINDOW_WIDTH, height=DEALER_HEIGHT, background='green')
        self.player_canvas = tk.Canvas(self.player_frame, 
            width=WINDOW_WIDTH, height=PLAYER_HEIGHT, background='green')
        self.dealer_canvas.grid(sticky='news')
        self.player_canvas.grid(sticky='news')

    def build_bottom(self):
        pass


def show_about_window():
    tkmb.showinfo(message='About message goes here')


if __name__ == '__main__':
    gw = GameWindow()
    gw.mainloop()
