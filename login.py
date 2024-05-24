from pathlib import Path
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from subprocess import call

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abhay\OneDrive\Desktop\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open():
    email=entry_1.get()
    password=entry_2.get()

    def validate_email(email):
    # Check if the email contains "@" and "."
     if "@" in email and "." in email:
        return True
     else:
        return False

    if(email=="")or(password==""):
     messagebox.showerror("Entry Error","Enter Valid Email ID or Password!!")
    
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
    command = "SELECT * FROM loginpage WHERE email = %s AND password = %s"
    cursor.execute(command, (email, password))
    result = cursor.fetchone()
    print(result)

    if result== None:
       messagebox.showerror("Entry Error","Enter Valid Email ID or Password!!")
       return
    else:
       messagebox.showinfo("Login","Login Sucessfully!!")
    window.withdraw()  
    call(["python", "safewomen.py"])
    window.destroy()  
    
def opensign():

    window.withdraw()
    call(["python","signup.py"])
    window.destroy()

window = Tk()

window.geometry("464x482")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 482,
    width = 464,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    66.0,
    39.0,
    anchor="nw",
    text="SafeWomen Bharat",
    fill="#000000",
    font=("Arvo", 16 * -1)
)

canvas.create_text(
    23.0,
    80.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Arvo", 32 * -1)
)

canvas.create_text(
    23.0,
    120.0,
    anchor="nw",
    text="login to access your account",
    fill="#534F4F",
    font=("Arvo Italic", 11 * -1)
)

canvas.create_text(
    76.0,
    254.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Arvo", 11 * -1)
)

canvas.create_text(
    76.0,
    178.0,
    anchor="nw",
    text="Email ID",
    fill="#000000",
    font=("Arvo", 11 * -1)
)

canvas.create_text(
    271.0,
    403.0,
    anchor="nw",
    text="Forgot Password",
    fill="#F81414",
    font=("Arvo", 10 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=opensign,
    relief="flat"
)
button_1.place(
    x=37.0,
    y=422.0,
    width=164.0,
    height=12.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open,
    relief="flat"
)
button_2.place(
    x=76.0,
    y=344.0,
    width=281.0,
    height=47.0
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
    216.5,
    301.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C5C5C4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=86.0,
    y=279.0,
    width=261.0,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_100.png"))
image_1 = canvas.create_image(
    37.0,
    48.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
