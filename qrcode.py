import tkinter as tk
from PIL import Image, ImageTk

def show_image():
    image = Image.open("code.png")
    image = image.resize((400, 325))  
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()

root = tk.Tk()
show_image()
root.mainloop()