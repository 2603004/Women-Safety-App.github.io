
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abhay\OneDrive\Desktop\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("633x392")
window.configure(bg = "#E4E4E4")


canvas = Canvas(
    window,
    bg = "#E4E4E4",
    height = 392,
    width = 633,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    25.0,
    11.0,
    anchor="nw",
    text="Current Events",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    316.0,
    83.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    316.0,
    180.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    316.0,
    327.0,
    image=image_image_3
)

canvas.create_text(
    25.0,
    236.0,
    anchor="nw",
    text="Upcoming Events\n",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    12.0,
    19.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    12.0,
    244.0,
    image=image_image_5
)

canvas.create_text(
    12.0,
    39.0,
    anchor="nw",
    text="Self-Defense for College Students",
    fill="#000000",
    font=("Underdog Regular", 16 * -1)
)

canvas.create_text(
    16.0,
    64.0,
    anchor="nw",
    text="Date: May 2/24",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    317.0,
    51.0,
    image=image_image_6
)

canvas.create_text(
    12.0,
    139.0,
    anchor="nw",
    text="Women's Safety Awareness Workshop",
    fill="#000000",
    font=("Underdog Regular ", 16 * -1)
)

canvas.create_text(
    16.0,
    159.0,
    anchor="nw",
    text="Date: May 17/24",
    fill="#000000",
    font=("Underdog Regular ", 12 * -1)
)

canvas.create_text(
    12.0,
    276.0,
    anchor="nw",
    text="Women's Safety Retreat",
    fill="#000000",
    font=("Underdog Regular", 16 * -1)
)

canvas.create_text(
    16.0,
    301.0,
    anchor="nw",
    text="Date: July 16-17, 2024",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    230.0,
    289.0,
    image=image_image_7
)

canvas.create_text(
    16.0,
    77.0,
    anchor="nw",
    text="Description: Calling all college students! Learn essential self-defense skills tailored to campus life.",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    88.0,
    anchor="nw",
    text="Location: University Student Center\n",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    102.0,
    anchor="nw",
    text="Time: 3:00 PM - 5:00 PM",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    170.0,
    anchor="nw",
    text="Description: Increase your awareness and learn personal safety strategies at our interactive workshop.",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    182.0,
    anchor="nw",
    text="Location: Dr. Bela’s Women Center\n",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    195.0,
    anchor="nw",
    text="Time: 2:00 PM - 4:00 PM",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    317.0,
    anchor="nw",
    text="Description: Escape to nature and immerse yourself in a weekend retreat focused on women's safety. Enjoy \n",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    331.0,
    anchor="nw",
    text="workshops, outdoor activities, and camaraderie in a supportive environment",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    344.0,
    anchor="nw",
    text="Location: Mountain Lodge Retreat Center\n",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

canvas.create_text(
    16.0,
    358.0,
    anchor="nw",
    text="Time: Starts at 6:00 PM on April 15, ends at 12:00 PM on April 17",
    fill="#000000",
    font=("Underdog Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=234.0,
    y=3.0,
    width=167.0,
    height=27.0
)
window.resizable(False, False)
window.mainloop()
