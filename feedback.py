from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abhay\OneDrive\Desktop\Tkinter-Designer-master\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def feedback():
  email=entry_3.get()
  message=entry_1.get()
  name=entry_2.get()

 
  conn = mysql.connector.connect( host='localhost', user='root',password='abhay@260304',database='loginpage')
  cursor = conn.cursor()
  print("Connected to database")
  command="USE loginpage"
  cursor.execute(command)
  cursor.execute("INSERT INTO feedback(name,email,message) VALUES (%s, %s, %s)", (name,email,message))
  conn.commit()
  messagebox.showinfo("Confirmation", "Your feedback is successfully registered!!")
  window.destroy() 

window = Tk()

window.geometry("496x515")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 515,
    width = 496,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    91.0,
    31.0,
    anchor="nw",
    text="Customer Feedback Form",
    fill="#000000",
    font=("Arvo", 24 * -1)
)

canvas.create_text(
    85.0,
    96.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Arvo", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_1 = canvas.create_image(
    63.0,
    102.0,
    image=image_image_1
)

canvas.create_text(
    85.0,
    171.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Arvo", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_2 = canvas.create_image(
    63.0,
    178.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_3 = canvas.create_image(
    63.0,
    255.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_1 = canvas.create_image(
    252.5,
    320.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=51.0,
    y=282.0,
    width=403.0,
    height=75.0
)

canvas.create_text(
    85.0,
    244.0,
    anchor="nw",
    text="Feedback",
    fill="#000000",
    font=("Arvo", 16 * -1)
)

canvas.create_text(
    85.0,
    375.0,
    anchor="nw",
    text="Rating",
    fill="#000000",
    font=("Arvo", 16 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_4 = canvas.create_image(
    62.0,
    383.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=feedback,
    relief="flat"
)
button_1.place(
    x=140.0,
    y=454.0,
    width=216.0,
    height=40.0
)

canvas.create_rectangle(
    52.0,
    407.0,
    74.0,
    428.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    80.0,
    407.0,
    102.0,
    428.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    107.0,
    407.0,
    129.0,
    428.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    134.0,
    407.0,
    156.0,
    428.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    162.0,
    407.0,
    184.0,
    428.0,
    fill="#000000",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_2 = canvas.create_image(
    181.5,
    143.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=51.0,
    y=127.0,
    width=261.0,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_3 = canvas.create_image(
    181.5,
    220.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=51.0,
    y=204.0,
    width=261.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
