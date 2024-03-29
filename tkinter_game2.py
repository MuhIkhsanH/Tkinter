import tkinter as tk
import random
import math

# Fungsi untuk memindahkan jendela
def move_window():
    global x, y, score

    # Memperbarui posisi jendela sesuai arah yang ditentukan
    if moving_left:
        x -= step_size
    if moving_right:
        x += step_size
    if moving_up:
        y -= step_size
    if moving_down:
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
        if distance < 100:  # Jika jarak antara ular dan makanan kurang dari 100 piksel
            food.destroy()
            foods.remove(food)
            create_food()
            score += 1
            score_label.config(text=f"Score: {score}")

    # Mengatur ulang posisi jendela
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Mengatur pembaruan posisi jendela setiap 50 milidetik
    root.after(10, move_window)  # Mengubah waktu interval menjadi lebih kecil untuk mempercepat pergerakan

# Fungsi untuk menangani event tombol panah
def handle_arrow_keys(event):
    global moving_left, moving_right, moving_up, moving_down
    if event.keysym == "Left":
        moving_left = True
    elif event.keysym == "Right":
        moving_right = True
    elif event.keysym == "Up":
        moving_up = True
    elif event.keysym == "Down":
        moving_down = True

# Fungsi untuk menangani event lepas tombol panah
def handle_arrow_release(event):
    global moving_left, moving_right, moving_up, moving_down
    if event.keysym == "Left":
        moving_left = False
    elif event.keysym == "Right":
        moving_right = False
    elif event.keysym == "Up":
        moving_up = False
    elif event.keysym == "Down":
        moving_down = False

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
moving_left = moving_right = moving_up = moving_down = False
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
root.bind("<KeyPress>", handle_arrow_keys)
root.bind("<KeyRelease>", handle_arrow_release)

# Fokus pada jendela agar bisa mendeteksi event key press
root.focus_set()

# Memanggil fungsi create_food untuk menampilkan makanan pertama
create_food()

# Memanggil fungsi move_window untuk memulai pergerakan jendela
move_window()

root.mainloop()
