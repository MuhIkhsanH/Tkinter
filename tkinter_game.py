import tkinter as tk
import random
import math

# Fungsi untuk memindahkan jendela
def move_window():
    global x, y, direction, score

    # Memperbarui posisi jendela sesuai arah yang ditentukan
    if direction == "Left":
        x -= step_size
    elif direction == "Right":
        x += step_size
    elif direction == "Up":
        y -= step_size
    elif direction == "Down":
        y += step_size

    # Memastikan jendela tetap berada dalam batas layar
    if x < 0:
        x = 0
    elif x > root.winfo_screenwidth() - window_width:
        x = root.winfo_screenwidth() - window_width
    if y < 0:
        y = 0
    elif y > root.winfo_screenheight() - window_height:
        y = root.winfo_screenheight() - window_height

    # Memeriksa apakah ular memakan makanan
    for food in foods:
        food_x = food.winfo_x() + food_size // 2
        food_y = food.winfo_y() + food_size // 2
        distance = math.sqrt((x - food_x) ** 2 + (y - food_y) ** 2)
        if distance < 100:  # Jika jarak antara ular dan makanan kurang dari 20 piksel
            food.destroy()
            foods.remove(food)
            create_food()
            score += 1
            score_label.config(text=f"Score: {score}")

    # Mengatur ulang posisi jendela
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Mengatur pembaruan posisi jendela setiap 100 milidetik
    root.after(100, move_window)

# Fungsi untuk menangani event tombol panah
def handle_arrow_keys(event):
    global direction
    if event.keysym in ["Left", "Right", "Up", "Down"]:
        direction = event.keysym

# Fungsi untuk membuat makanan (window baru)
def create_food():
    food_x = random.randint(0, root.winfo_screenwidth() - food_size)
    food_y = random.randint(0, root.winfo_screenheight() - food_size)
    food = tk.Toplevel(root)
    food.geometry(f"{food_size}x{food_size}+{food_x}+{food_y}")
    food.configure(bg="red")
    food.title("Food")
    foods.append(food)

# Membuat jendela tkinter
root = tk.Tk()
root.title("Snake Game")

# Mengatur ukuran awal jendela
window_width = 20
window_height = 20
root.geometry(f"{window_width}x{window_height}")

# Mengatur arah awal gerakan
direction = "Right"
step_size = 10  # Ukuran langkah per gerakan

# Ukuran makanan
food_size = 10

# Membuat list untuk menyimpan makanan
foods = []

# Mengatur awal posisi jendela di tengah layar
x = (root.winfo_screenwidth() - window_width) // 2
y = (root.winfo_screenheight() - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Mengatur skor awal
score = 0

# Membuat label untuk skor
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Mengikat event key press ke fungsi handle_arrow_keys
root.bind("<Key>", handle_arrow_keys)

# Fokus pada jendela agar bisa mendeteksi event key press
root.focus_set()

# Memanggil fungsi create_food untuk menampilkan makanan pertama
create_food()

# Memanggil fungsi move_window untuk memulai pergerakan jendela
move_window()

root.mainloop()
