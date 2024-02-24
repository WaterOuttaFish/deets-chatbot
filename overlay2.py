from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con


def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)


def size_position_for_picture():
    bbox = bg.bbox(img_id)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x, y = sw / 2 - w / 2, sh / 2 - h / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    bg.configure(width=w, height=h)


root = Tk()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

root.overrideredirect(1)
root.attributes("-alpha", 0.75)
root.attributes('-transparentcolor', 'white', '-topmost', 1)
bg = Canvas(root, bg='white', highlightthickness=0)
root.config(bg='white')

setClickthrough(bg.winfo_id())

frame = ImageTk.PhotoImage(file="example.png")
img_id = bg.create_image(0,0, image=frame,anchor='nw')
bg.pack()

size_position_for_picture()
setClickthrough(bg.winfo_id())

root.mainloop()
