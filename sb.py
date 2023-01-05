from customtkinter import *
from typing import Union, Callable

myfont = "GFS Neohellenic Bold"
color_button = "#395e9c"

class Spinbox(CTkFrame):
    def __init__(self,
                master: any,
                 *args,
                 width: int = 50,
                 height: int = 50,
                 step_size: int = 1,
                 command: Callable = None,
                 row: int = 0,
                 column: int = 0,
                 **kwargs):
        super().__init__(master=master, *args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.grid_rowconfigure((0, 2), weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.entry = CTkEntry(self, width=width, height=height, justify="right", font = (myfont, 27), validate = 'all', validatecommand = (self.register(self.callback), '%P'))
        self.entry.grid(row=1, pady = 3, sticky="ns")

        self.add_button = CTkButton(self, text="+", width=width, height=height/1.72, font=(myfont, 20), fg_color=color_button,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0)

        self.subtract_button = CTkButton(self, text="-", width=width, height=height/1.72, font=(myfont, 20), fg_color=color_button,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=2)

        self.entry.insert(0, "0")

    def callback(self, P):
        if str.isdigit(P) or P == "":
            if len(P) > 2:
                return False
            else:
                return True
        else:
            return False

    def get(self) -> Union[int, None]:
        try:
            if int(self.entry.get()) > self.limit and self.limit != None:
                self.entry_reset_insert(self.limit)

        except (ValueError, TypeError):
            self.entry.delete(0, "end")
            if self.value != self.start and self.start == None:
                self.entry.insert(0, self.value)
            else:
                self.entry.insert(0, self.start)
    
        return int(self.entry.get())

    def set(self, *args, value: int = None, start: int = None, limit: int = None, **kwargs):
        if start != None and value != None and value < start:
            value = start
        elif start != None and value == None:
            value = start
        elif start == value == None:
            value = 0

        self.limit = limit
        self.start = start
        self.value = value

        self.entry_reset_insert(value)
    
    def disable(self, state: bool = False):
        if state:
            state = "disabled"
        else:
            state = "normal"
        self.add_button.configure(state = state)
        self.subtract_button.configure(state = state)
        self.entry.configure(state = state)  

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            if self.start != None and self.limit != None and value > self.limit:
                value = self.start
            self.entry_reset_insert(value)
        except ValueError:
            if self.start != None:
                return self.entry_reset_insert(self.start)
            else:
                return self.entry_reset_insert(self.value)

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            if self.start != None and self.limit != None and value < self.start:
                value = self.limit
            self.entry_reset_insert(value)
        except ValueError:
            if self.start != None:
                return self.entry_reset_insert(self.start)
            else:
                return self.entry_reset_insert(self.value)

    def entry_reset_insert(self, data):
        self.entry.delete(0, "end")
        self.entry.insert(0, data)


