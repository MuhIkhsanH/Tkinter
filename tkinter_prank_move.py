import tkinter as tk
import random

def move_window(event=None):
    # Mendapatkan ukuran layar
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Mendapatkan ukuran jendela
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Mendapatkan posisi kursor
    if event:
        x, y = event.x_root, event.y_root
    else:
        x, y = screen_width // 2, screen_height // 2

    # Mendapatkan jarak kursor ke tepi layar
    distance_to_edge_x = min(x, screen_width - x)
    distance_to_edge_y = min(y, screen_height - y)

    # Mendapatkan jarak minimum antara jendela dan tepi layar
    min_distance = min(distance_to_edge_x, distance_to_edge_y)

    # Mendapatkan posisi jendela baru
    new_x = random.randint(0, screen_width - window_width)
    new_y = random.randint(0, screen_height - window_height)

    # Mengatur posisi jendela baru
    root.geometry(f"+{new_x}+{new_y}")

# Membuat jendela tkinter
root = tk.Tk()
root.title("Jendela Acak")

# Mengatur ukuran awal jendela
root.geometry("150x50")

t1 = tk.Label(root,text="VIRUS.EXE")
t1.pack()

# Menambahkan event handler untuk pergerakan kursor
root.bind("<Motion>", move_window)

# Menambahkan event handler untuk menangani tombol close
root.protocol("WM_DELETE_WINDOW", move_window)

root.mainloop()
