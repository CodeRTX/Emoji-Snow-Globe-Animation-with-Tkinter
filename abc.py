import tkinter as tk

window = tk.Tk()
window.title("Emoji Snow Globe")
window.geometry("500x500")
window.config(bg="lightblue")

from PIL import Image, ImageTk

# Load emojis as images
santa_img = ImageTk.PhotoImage(Image.open("santa.png").resize((50, 50), Image.Resampling.LANCZOS))
mrs_claus_img = ImageTk.PhotoImage(Image.open("mrs_claus.png").resize((50, 50), Image.Resampling.LANCZOS))
reindeer_img = ImageTk.PhotoImage(Image.open("reindeer.png").resize((50, 50), Image.Resampling.LANCZOS))
snowflake_img = ImageTk.PhotoImage(Image.open("snowflake.png").resize((20, 20), Image.Resampling.LANCZOS))

import random

def move_emoji(canvas, emoji, x, y):
    dx = random.choice([-2, -1, 0, 1, 2])
    dy = random.choice([1, 2, 3])
    canvas.move(emoji, dx, dy)
    new_x, new_y = canvas.coords(emoji)
    if new_y > 500:
        new_y = 0
    if new_x > 500 or new_x < 0:
        new_x = 250
    canvas.coords(emoji, new_x, new_y)
    window.after(50, move_emoji, canvas, emoji, new_x, new_y)

canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Place emojis on canvas
santa = canvas.create_image(250, 100, image=santa_img)
mrs_claus = canvas.create_image(200, 150, image=mrs_claus_img)
reindeer = canvas.create_image(300, 150, image=reindeer_img)
snowflakes = [canvas.create_image(random.randint(0, 500), random.randint(0, 500), image=snowflake_img) for _ in range(20)]

# Animate the emojis
move_emoji(canvas, santa, 250, 100)
move_emoji(canvas, mrs_claus, 200, 150)
move_emoji(canvas, reindeer, 300, 150)
for snowflake in snowflakes:
    move_emoji(canvas, snowflake, random.randint(0, 500), random.randint(0, 500))

window.mainloop()
