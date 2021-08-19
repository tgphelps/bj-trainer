#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox as tkmb
# from tkinter import ttk


WINDOW_WIDTH = 1200
DEALER_HEIGHT = 300
PLAYER_HEIGHT = 600


class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.configure(bg='red')
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
        self.menu_help.add_command(label='About',
                                   command=self.show_about_window)

    def build_frames(self):
        self.dealer_canvas = tk.Canvas(self,
            width=WINDOW_WIDTH, height=DEALER_HEIGHT, background='green')
        self.player_canvas = tk.Canvas(self,
            width=WINDOW_WIDTH, height=PLAYER_HEIGHT, background='green')

        self.dealer_canvas.grid(row=0, column=0, sticky='news')
        self.player_canvas.grid(row=1, column=0, sticky='news')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)

    def build_bottom(self):
        pass

    def show_about_window(self):
        tkmb.showinfo(message='About message goes here')
        # print(dir(self.dealer_canvas))
        print(self.winfo_width(), self.winfo_height())
        print(self.dealer_canvas.winfo_width(),
              self.dealer_canvas.winfo_height())


if __name__ == '__main__':
    gw = GameWindow()
    gw.mainloop()
