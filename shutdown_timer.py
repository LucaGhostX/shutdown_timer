from time import sleep
from tkinter import Label, Spinbox, Button, Tk, PhotoImage, messagebox
from wakepy import set_keepawake
from base64 import b64decode
from subprocess import call

#############################################################

window = Tk()
icon_base64 = """
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
"""
icon = PhotoImage(data = b64decode(icon_base64))

window.geometry("181x155+850+450")
window.title("")
window.resizable(False, False)
#window.attributes('-toolwindow', True)
window.attributes('-topmost', 1)
window.wm_iconphoto(True, icon)
window.configure(background="#252525")

#############################################################

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\nYou'll cancel the timer."):
        window.destroy()

def start():

    set_keepawake(keep_screen_awake=True)

    seconds = int(seconds_input.get())
    minutes = int(minutes_input.get())
    hours = int(hours_input.get())

    result = (hours * 3600) + (minutes * 60) + seconds

    while result:
        window.protocol("WM_DELETE_WINDOW", on_closing)

        mins, secs = divmod(result, 60)
        hours, mins = divmod(mins, 60)

        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        text_out = Label(window, text = timer, bg = "#252525", fg = "#ffffff", font = (10)).grid(row = 4, columnspan = 3)
        window.update()

        sleep(1)

        result -= 1

    call(["shutdown", "-s", "-t", "10"])

############################################################# ROW 0

app_text = Label(window, text = "Shutdown Timer", bg = "#252525", fg = "#ffffff", font = (10)).grid(row = 0, columnspan = 3, pady = (5, 0))

############################################################# ROW 1

hours_text = Label(window, text = "Hours", bg = "#252525", fg = "#ffffff").grid(row = 1, column = 0, pady = (5, 0))

minutes_text = Label(window, text = "Minutes", bg = "#252525", fg = "#ffffff").grid(row = 1, column = 1, pady = (5, 0))

seconds_text = Label(window, text = "Seconds", bg = "#252525", fg = "#ffffff").grid(row = 1, column = 2, pady = (5, 0))

############################################################# ROW 2

hours_input = Spinbox(from_= 0, to = 99, wrap = True, width = 5, justify = "right")
hours_input.grid(row = 2, column = 0, padx = 10)

minutes_input = Spinbox(from_= 0, to = 59, wrap = True, width = 5, justify = "right")
minutes_input.grid(row = 2, column = 1)

seconds_input = Spinbox(from_= 0, to = 59, wrap = True, width = 5, justify = "right")
seconds_input.grid(row = 2, column = 2, padx = 10)

############################################################# ROW 3

button_start = Button(text="Start", bg = "#191919", fg = "#ffffff", command = start).grid(row = 3, columnspan = 3, padx = 10, pady = 10, sticky = "WE")

#############################################################

if __name__ == "__main__":
    window.mainloop()