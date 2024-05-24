from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from subprocess import call
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abhay\OneDrive\Desktop\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open():
  email=entry_3.get()
  password=entry_2.get()
  name=entry_1.get()

  def validate_email(email):
    # Check if the email contains "@" and "."
    if "@" in email and "." in email:
        return True
    else:
        return False

  if name == "" or email == "" or password == "":
        messagebox.showerror("Registration Error", "Field is empty!")
        return
  elif not validate_email(email):
        messagebox.showerror("Registration Error", "Please enter a valid email format!")
        return
  else:
    try:
     conn = mysql.connector.connect( host='localhost', user='root',password='abhay@260304',database='loginpage')
     cursor = conn.cursor()
     print("Connected to database")
    except:
        messagebox.showerror("Error","Connection not established!!")
        return
     
  command="USE loginpage"
  cursor.execute(command)
  cursor.execute("SELECT * FROM loginpage WHERE email = %s", (email,))
  if cursor.fetchone():
    messagebox.showerror("Registration Error", "Email already exists!")
    return

  cursor.execute("INSERT INTO signup (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
  conn.commit()
  cursor.execute("SELECT LAST_INSERT_ID()")
  id = cursor.fetchone()[0]

  cursor.execute("INSERT INTO loginpage(email, password) VALUES (%s, %s)", (email, password))
  conn.commit()
  messagebox.showinfo("Confirmation", "Your Account has been successfully created!")
  window.withdraw()  
  call(["python", "safewomen.py"])
  window.destroy() 



window = Tk()

window.geometry("444x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 444,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    77.0,
    40.0,
    anchor="nw",
    text="SafeWomen Bharat",
    fill="#000000",
    font=("Arvo", 32 * -1)
)

canvas.create_text(
    29.0,
    128.0,
    anchor="nw",
    text="Create Account",
    fill="#000000",
    font=("ArimoRoman Regular", 24 * -1)
)

canvas.create_text(
    77.0,
    187.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("ArimoRoman Regular", 12 * -1)
)

canvas.create_text(
    77.0,
    259.0,
    anchor="nw",
    text="Email ID",
    fill="#000000",
    font=("ArimoRoman Regular", 12 * -1)
)

canvas.create_text(
    77.0,
    332.0,
    anchor="nw",
    text="Password\n",
    fill="#000000",
    font=("ArimoRoman Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open,
    relief="flat"
)
button_1.place(
    x=77.0,
    y=418.0,
    width=280.0,
    height=46.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    216.5,
    223.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=86.0,
    y=201.0,
    width=261.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    217.5,
    368.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=87.0,
    y=346.0,
    width=261.0,
    height=42.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    216.5,
    296.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=86.0,
    y=274.0,
    width=261.0,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_100.png"))
image_1 = canvas.create_image(
    43.0,
    57.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
