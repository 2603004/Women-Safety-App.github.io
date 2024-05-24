from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Canvas, PhotoImage, Tk,Scrollbar,Text
from PIL import Image, ImageTk,ImageDraw
from pathlib import Path
from twilio.rest import Client
from geopy.geocoders import Nominatim
import requests
import folium
from subprocess import call
import glob

ASSETS_PATH = Path(r"C:\Users\abhay\OneDrive\Desktop\pillow\sun.jpg")

def open_window(file_path):
    call(["python", file_path])  
def open_window_1(file_path):
    call(["python", file_path]) 
def open_window_2(file_path):
    call(["python", file_path])  
      
class WomenSafetyApp:
 
    def __init__(self, root):
        
        self.root = root
        self.root.title("Safe Women Bharat")
       
        self.tabControl = ttk.Notebook(self.root, style='TNotebook')
        self.tab_home = ttk.Frame(self.tabControl)
        self.tab_emergency_features = ttk.Frame(self.tabControl)
        self.tab_safety_tips = ttk.Frame(self.tabControl)
        self.tab_community = ttk.Frame(self.tabControl)

        # Add tabs to the notebook in the desired order
        self.tabControl.add(self.tab_home, text='Home', compound=tk.LEFT)
        self.tabControl.add(self.tab_emergency_features, text='Emergency Features')
        self.tabControl.add(self.tab_safety_tips, text='Services')
        self.tabControl.add(self.tab_community, text='Community')

        # Apply a style with a black background and increased size to the Notebook widget
        self.tabControl.style = ttk.Style()
        self.tabControl.style.configure('TNotebook', background='#19264C', padding=[40, 10])

        # Configure the style for the Tab element
        self.tabControl.style.configure('TNotebook.Tab', background='#0635C6', foreground='black', padding=[25, 15], font=('Helvetica', 14))

        self.tabControl.pack(expand=1, fill="both")

        # Add content to tabs
        self.add_home_content()
        self.add_emergency_features_content()
        self.add_safety_tips_content()
        self.add_community_content()

    def add_home_content(self):
        canvas = tk.Canvas(self.tab_home, width=700, height=400)
        canvas.pack(pady=50)
        # Draw a rectangle on the canvas
        canvas.create_rectangle(6, 3, 700, 400, fill='#19264C')
        canvas.create_text(150, 50, text="WELCOME TO ", fill="white", font=('Helvetica', 19))
        canvas.create_text(330, 100, text="SafeWomen", fill="white", font=('Helvetica', 20))
        canvas.create_text(327, 140, text="Bharat", fill="white", font=('Helvetica', 20))
        canvas.create_text(350, 180, text="Fostering Empowerment, Cultivating Safety:", fill="white", font=('Helvetica', 10))
        canvas.create_text(345, 195, text="Women's Safety Hub Your Beacon for", fill="white", font=('Helvetica', 10))
        canvas.create_text(350, 210, text="Strength, Support, Security in Every Step.", fill="white", font=('Helvetica', 10))

        label = tk.Label(self.tab_home, text="Emergency-Dial 100", bg='#E91137', width=17, height=2, font=('bold', 12), fg='white')
        label.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
        label1 = tk.Label(self.tab_home, text="Child Helpline 1098", bg='#B99C53', width=17, height=2, font=('bold', 12), fg='white')
        label1.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

    def add_emergency_features_content(self):
        image_file=("image.jpeg")
        image = Image.open(image_file)
        image = image.resize((600, 550))  
        bg_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.tab_emergency_features, image=bg_image)
        background_label.image = bg_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
        panic_button = tk.Button(self.tab_emergency_features, text='PANIC BUTTON', command=self.trigger_panic, bg='red', width=35, height=4, font=('bold', 12))
        panic_button.bind("<Enter>", lambda event: panic_button.config(bg='darkred'))
        panic_button.bind("<Leave>", lambda event: panic_button.config(bg='red'))
        panic_button.bind("<Button-1>", lambda event: panic_button.config(bg='darkred'))
        panic_button.bind("<ButtonRelease-1>", lambda event: panic_button.config(bg='red'))

        location_share_button = tk.Button(self.tab_emergency_features, text='SHARE LOCATION', command=self.share_location, bg='red', width=35, height=4, font=('bold', 12))
        location_share_button.bind("<Enter>", lambda event: location_share_button.config(bg='darkred'))
        location_share_button.bind("<Leave>", lambda event: location_share_button.config(bg='red'))
        location_share_button.bind("<Button-1>", lambda event: location_share_button.config(bg='darkred'))
        location_share_button.bind("<ButtonRelease-1>", lambda event: location_share_button.config(bg='red'))

        emergency_frame = ttk.Frame(self.tab_emergency_features)
        emergency_frame.pack(padx=15, pady=15)
        emergency_contact_button = tk.Button(self.tab_emergency_features, text='EMERGENCY CONTACTS', command=self.show_emergency_contacts, bg='red', width=35, height=4, font=('bold', 12))
        emergency_contact_button.bind("<Enter>", lambda event: emergency_contact_button.config(bg='darkred'))
        emergency_contact_button.bind("<Leave>", lambda event: emergency_contact_button.config(bg='red'))
        emergency_contact_button.bind("<Button-1>", lambda event: emergency_contact_button.config(bg='darkred'))
        emergency_contact_button.bind("<ButtonRelease-1>", lambda event: emergency_contact_button.config(bg='red'))

        location_tracking_button = tk.Button(self.tab_emergency_features, text='SEND MESSAGE', command=self.toggle_location_tracking, bg='red', width=35, height=4, font=('bold', 12))
        location_tracking_button.bind("<Enter>", lambda event: location_tracking_button.config(bg='darkred'))
        location_tracking_button.bind("<Leave>", lambda event: location_tracking_button.config(bg='red'))
        location_tracking_button.bind("<Button-1>", lambda event: location_tracking_button.config(bg='darkred'))
        location_tracking_button.bind("<ButtonRelease-1>", lambda event: location_tracking_button.config(bg='red'))

        panic_button.pack(pady=24)
        location_share_button.pack(pady=24)
        emergency_contact_button.pack(pady=24)
        location_tracking_button.pack(pady=24)

        self.message_label = tk.Label(self.tab_emergency_features, text="Contacts", padx=10, pady=10)
        self.message_label.pack(expand=1, fill="both")

    def trigger_panic(self):
        try:
            account_sid = 'ACc3e8edbc6883f327704d0815b23328ce'
            auth_token = '0a21073eea0b35c1fb8302336321f1c3'
    
            client = Client(account_sid, auth_token)

            # Make a Twilio call
            call = client.calls.create(
                twiml='<Response><Say>This is an emergency call. Please take immediate action.</Say></Response>',
                to='+919425115665',
                from_='+13343453943'
            )

            # Show a message indicating the call has been triggered
            self.show_message(f"Emergency call triggered! SID: {call.sid}")

        except Exception as e:
            # Handle any exceptions that may occur during the Twilio call
            self.show_message(f"Error triggering panic: {str(e)}")
            
    def locationCoordinates(self):
        headers = {
        'Authorization': 'b0d64b3f67011a'
        }
        response = requests.get('https://ipinfo.io/json',headers=headers)
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        return lat, long

    def share_location(self):
        account_sid = 'ACc3e8edbc6883f327704d0815b23328ce'
        auth_token = '0a21073eea0b35c1fb8302336321f1c3'
        geocoding_api_key = 'AIzaSyAtyLuyvDOpIb7rcu-9rJorBPzgjs2q81E'

        lat, long = self.locationCoordinates()

        m = folium.Map(location=[lat, long])
        folium.Marker([lat, long]).add_to(m)

        client = Client(account_sid, auth_token)
        geolocator = Nominatim(user_agent=f"sender_location_app/{geocoding_api_key}")
        sender_location = geolocator.reverse(f"{lat}, {long}")
        location_url = f'https://www.google.com/maps?q={sender_location.latitude},{sender_location.longitude}'
        your_message = f'Hello! Check out my live location: {location_url}'

        message = client.messages.create(
            body=your_message,
            to='+919425115665',  
            from_='+13343453943'  
        )

        self.show_message("Location shared!")

    def show_emergency_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title('Emergency Contacts')

        emergency_contacts_listbox = tk.Listbox(contacts_window, selectmode=tk.SINGLE)
        emergency_contacts_listbox.pack(padx=20, pady=20)

        sample_contacts = ["Dad", "Mom", "Brother"]
        for contact in sample_contacts:
            emergency_contacts_listbox.insert(tk.END, contact)

        call_button = tk.Button(contacts_window, text='Call', command=lambda: self.call_selected_contact(emergency_contacts_listbox), bg='green', width=10)
        call_button.pack(pady=10)
    
    def call_selected_contact(self, Listbox):
        selected_index = Listbox.curselection()
        if selected_index:
            selected_contact = Listbox.get(selected_index)
            if selected_contact.lower() == 'dad':
                # Call Dad using Twilio or any other method
                self.call_dad()

            messagebox.showinfo("Calling", f"Calling {selected_contact}......")
            
        else:
            messagebox.showinfo("Calling", "No contact selected. Please select a contact.")

    def call_dad(self):
        try:
            account_sid = 'ACc3e8edbc6883f327704d0815b23328ce'
            auth_token = '0a21073eea0b35c1fb8302336321f1c3'
    
            client = Client(account_sid, auth_token)

            # Make a Twilio call
            call = client.calls.create(
                twiml='<Response><Say>This is an emergency call. Please take immediate action.</Say></Response>',
                to='+919425115665',
                from_='+13343453943'
            )


        except Exception as e:
            # Handle any exceptions that may occur during the Twilio call
            self.show_message(f"Error triggering panic: {str(e)}")

    def toggle_location_tracking(self):
        account_sid = 'ACc3e8edbc6883f327704d0815b23328ce'
        auth_token = '0a21073eea0b35c1fb8302336321f1c3'
        client = Client(account_sid, auth_token)

        your_message = f'This is an emergency message. Please take immediate action.'

        message = client.messages.create(
            body=your_message,
            to='+919425115665',  
            from_='+13343453943'  
        )

        self.show_message("Message Sent!!")

    def show_message(self, message):

        self.message_label.config(text=message)
        messagebox.showinfo("Information", message)
    

    def add_safety_tips_content(self):
    
      safety_tips_frame = tk.Frame(self.tab_safety_tips, padx=20, pady=20)
      safety_tips_frame.pack(expand=True, fill="both")
      heading_font = ('Helvetica', 18, 'bold')
      safety_heading = tk.Label(safety_tips_frame, text="SELF-DEFENCE WORKSHOPS & TRAINING", font=heading_font, pady=10, fg="#9EA03B")
      safety_heading.pack()

      

    
    
      canvas = Canvas(safety_tips_frame)
      canvas.pack(expand=True, fill="both")

      image_frame = Frame(canvas, bg="#19264C", padx=200, pady=10)
      canvas.create_window((0,0), window=image_frame, anchor="nw", tags="image_frame")
      image_frame.pack()

        # Load images 
      image_files = ["image1.jpg", "image2.jpg","image3.jpg"]
    
      self.images = [Image.open(file) for file in image_files]
      self.current_image_idx = 0

      self.image_label = Label(image_frame)
      self.image_label.pack()
      
       
      self.show_image()

      self.root.after(5000, self.change_image)
      safety_content = """
        📢 Under women safety & self defence workshop & training we provide a training workshop designed to keep women and children safe at all times and at places. 
        It is not a physical defense program, and has a preventive approach for safety which includes strengthening of body emotions and intuition. Ensuring the safety of 
        all women is not just a matter of personal security; it is an imperative for fostering a society built on equality, dignity, and respect.
        Some of its specific features are:

       • Women and children are made AWARE about their specific vulnerabilities.

       • They UNDERSTAND psychology of assaulters and behavior patterns.

       • Get FAMILIAR with specific on and off guard unsafe situations."""
      
      safety_text = tk.Text(safety_tips_frame, wrap=tk.WORD, height=30, width=80, font=('Helvetica', 12))
      safety_text.insert(tk.END, safety_content)
      safety_text.config(state=tk.DISABLED) 
      safety_text.pack(expand=True, fill="both")
      analytics = tk.Button(safety_tips_frame, text='SafeAnalytics', command=lambda: open_window("analytics.py"),
                                         bg='#B99C53', width=15, height=1, font=('bold', 12))
      analytics.bind("<Enter>", lambda event:  analytics.config(bg='#7E6B3B'))
      analytics.bind("<Leave>", lambda event:  analytics.config(bg='#B99C53'))
      analytics.bind("<Button-1>", lambda event: analytics.config(bg='#7E6B3B'))
      analytics.bind("<ButtonRelease-1>", lambda event:  analytics.config(bg='#B99C53'))
      analytics.place(relx=0.425, rely=0.94)
     
      report = tk.Button(safety_tips_frame, text='Feedback', command=lambda: open_window_1("feedback.py"),
                                         bg='#B99C53', width=15, height=1, font=('bold', 12))
      report.bind("<Enter>", lambda event:  report.config(bg='#7E6B3B'))
      report.bind("<Leave>", lambda event:  report.config(bg='#B99C53'))
      report.bind("<Button-1>", lambda event: report.config(bg='#7E6B3B'))
      report.bind("<ButtonRelease-1>", lambda event:  report.config(bg='#B99C53'))
      report.place(relx=0.225, rely=0.94)

      events = tk.Button(safety_tips_frame, text='Events', command=lambda: open_window_2("events.py"),
                                         bg='#B99C53', width=15, height=1, font=('bold', 12))
      events.bind("<Enter>", lambda event:  events.config(bg='#7E6B3B'))
      events.bind("<Leave>", lambda event:  events.config(bg='#B99C53'))
      events.bind("<Button-1>", lambda event: events.config(bg='#7E6B3B'))
      events.bind("<ButtonRelease-1>", lambda event:  events.config(bg='#B99C53'))
      events.place(relx=0.625, rely=0.94)
      

    def change_image(self):
        # Change to the next image
        self.current_image_idx = (self.current_image_idx + 1) % len(self.images)
        self.show_image()
        # Set a timer to change images again
        self.root.after(3000, self.change_image)

    def show_image(self):
        # Resize the image to fit the label
        resized_image = self.images[self.current_image_idx].resize((400, 200))
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.image_label.pack(anchor="center")
    def add_community_content(self):
        label = tk.Label(self.tab_community)
        label.pack(expand=1, fill="both")
        image_frame = tk.Frame(self.tab_community)
        image_frame.pack(anchor=tk.NW, side=tk.TOP) 
    
        image_path = ASSETS_PATH
        image = Image.open(image_path)
        image = image.resize((500, 300))
        photo = ImageTk.PhotoImage(image)
        
        image_label = tk.Label(image_frame, image=photo)
        image_label.image = photo
        image_label.pack(anchor=tk.NW)

        
        blog_frame = tk.Frame(self.tab_community)
        blog_frame.pack(side=tk.LEFT, padx=10, pady=20)

        blog_text = """
        📢 **Rising Voices: Women Unite for Safety**
        In the face of adversity, women across the nation are raising their voices in a powerful movement advocating women's safety. 
        From city streets to social media platforms, a wave of activism is sweeping through, demanding change.
        👩‍🦰 **Strength in Unity**
        Women from all walks of life are coming together, united by a common goal: the right to live free from fear. 
        The strength of this movement lies in the collective voice of those who refuse to be silent about the safety.
        🌐 **Digital Activism**
        Social media platforms have become a powerful tool for activism, enabling women to share stories, raise awareness. 
        Hashtags like #SafeWomenNow and #EmpowerHerSafety are trending, amplifying the message of the movement across the landscape.
        🚩 **Protests and Marches**
        Streets resonate with chants, slogans, and the unwavering spirit of women participating in protests and marches. 
        """
        blog_label = tk.Label(blog_frame, text=blog_text, font=('Helvetica', 12), justify=tk.LEFT)
        blog_label.pack(anchor=tk.W)
     

if __name__ == "__main__":
    root = tk.Tk()
    app = WomenSafetyApp(root)
    root.mainloop()
