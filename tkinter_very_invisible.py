import tkinter as tk
import win32gui
import win32con
import time

# Fungsi untuk menampilkan jendela Tkinter dan kemudian menyembunyikannya
def show_and_hide_window():
    root.deiconify()  # Menampilkan jendela Tkinter
    time.sleep(5)  # Menunggu selama 5 detik
    root.withdraw()  # Menyembunyikan jendela Tkinter

# Membuat jendela utama Tkinter dan langsung menyembunyikannya
root = tk.Tk()
root.title("Jendela Utama")
root.withdraw()

# Menjalankan fungsi untuk menampilkan dan menyembunyikan jendela
show_and_hide_window()

root.mainloop()
