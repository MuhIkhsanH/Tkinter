import tkinter as tk
import ctypes

# Fungsi untuk menyembunyikan jendela dari taskbar
def hide_from_taskbar(window):
    try:
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # Menghilangkan jendela
    except Exception as e:
        print("Error:", e)

# Fungsi untuk menutup aplikasi
def close_app():
    # Menyembunyikan jendela utama dari taskbar sebelum menutup
    root.withdraw()
    popup.destroy()  # Menghancurkan jendela tambahan
    # Hentikan eksekusi program atau jalankan tindakan lain yang diinginkan

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Jendela Utama")

# Menggunakan withdraw() untuk menyembunyikan jendela utama dari taskbar
root.withdraw()

# Membuat jendela tambahan yang tidak terlihat
popup = tk.Toplevel(root)
popup.attributes("-alpha", 0)  # Membuat jendela benar-benar tidak terlihat

# Menghilangkan jendela tambahan dari taskbar
hide_from_taskbar(popup)

# Mengatur event handler untuk menutup jendela utama
root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
