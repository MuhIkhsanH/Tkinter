import tkinter as tk
from tkinter import ttk

def show_checkbox_frame():
    # Menampilkan frame_checkbox dan menyembunyikan frame_button
    frame_checkbox.pack()
    frame_button.pack_forget()

def on_start():
    show_checkbox_frame()

def update_label():
    label.config(text=f"Checkbox: {checkbox_var.get()}")

def on_back():
    # Menyembunyikan frame_checkbox dan menampilkan frame_button kembali
    frame_checkbox.pack_forget()
    frame_button.pack()

def on_exit():
        window.destroy()

# Membuat jendela
window = tk.Tk()
window.title("Menu Awal Tkinter")

# Membuat variabel untuk menyimpan nilai checkbox
checkbox_var = tk.StringVar()

# Membuat frame untuk tombol "Mulai" dan "Keluar"
frame_button = ttk.Frame(window, padding=(10, 10))
frame_button.pack(pady=20)

# Tombol "Mulai" untuk menampilkan checkbox
start_button = ttk.Button(frame_button, text="Mulai", command=on_start)
start_button.grid(row=0, column=0, padx=(0, 10))

# Tombol "Keluar"
exit_button = ttk.Button(frame_button, text="Keluar", command=on_exit)
exit_button.grid(row=0, column=1)

# Membuat frame untuk checkbox
frame_checkbox = ttk.Frame(window, padding=(10, 10))

# Membuat checkbox
checkbox = ttk.Checkbutton(frame_checkbox, text="Centang Saya", variable=checkbox_var, command=update_label)
checkbox.grid(row=0, column=0, sticky='w', padx=(0, 10))

# Membuat label untuk menampilkan status checkbox
label = ttk.Label(frame_checkbox, text="Checkbox: Belum Dicentang")
label.grid(row=1, column=0, pady=(10, 0), sticky='w')

# Tombol "Kembali"
back_button = ttk.Button(frame_checkbox, text="Kembali", command=on_back)
back_button.grid(row=2, column=0, pady=(10, 0))

# Menjalankan loop utama
window.mainloop()
