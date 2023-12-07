import tkinter as tk

def on_enter(event):
    button.config(bg='#45a049', fg='white')  # Mengubah warna latar belakang dan teks saat pointer masuk

def on_leave(event):
    button.config(bg='#4CAF50', fg='white')  # Mengembalikan warna latar belakang dan teks saat pointer keluar

def on_button_click():
    label.config(text="Tombol Diklik!")

# Membuat jendela
window = tk.Tk()
window.title("Contoh Tombol Tkinter")

# Membuat tombol
button = tk.Button(window, text="Klik Saya!", command=on_button_click, bg='#4CAF50', fg='white', font=('Arial', 12), padx=10, pady=5, relief='flat')

# Mengaitkan event saat pointer masuk dan keluar
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

button.pack(pady=20)

# Membuat label untuk menampilkan pesan setelah tombol diklik
label = tk.Label(window, text="")
label.pack()

# Menjalankan loop utama
window.mainloop()
