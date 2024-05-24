import tkinter as tk
from PIL import Image, ImageTk

class ImageSlideshow(tk.Tk):
    def __init__(self, image_files, delay=5000):
        super().__init__()
        self.image_files = image_files
        self.delay = delay
        self.current_image_index = 0

        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack()

        self.load_image()

    def load_image(self):
        image_file = self.image_files[self.current_image_index]
        image = Image.open(image_file)
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.after(self.delay, self.next_image)

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        self.load_image()

if __name__ == "__main__":
    image_files = ["sun.jpg", "code.png"]  # Add your image file paths here
    app = ImageSlideshow(image_files)
    app.mainloop()
