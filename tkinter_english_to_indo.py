import tkinter as tk
from googletrans import Translator

# Membuat instance Translator
translator = Translator()

# Variabel debounce_timer untuk menunda terjemahan
debounce_timer = None

# Fungsi untuk memulai terjemahan setelah selesai mengetik
def start_translation(event=None):
    global debounce_timer
    if debounce_timer:
        root.after_cancel(debounce_timer)  # Membatalkan debounce timer jika ada
    debounce_timer = root.after(500, update_label)  # Menunda terjemahan selama 500ms setelah selesai mengetik

# Fungsi untuk memperbarui teks pada entry
def update_entry_text(event=None):
    start_translation()  # Memulai debounce timer setiap kali ada pembaruan teks

# Fungsi untuk melakukan terjemahan
def update_label():
    text = text_entry.get("1.0", "end-1c")
    if text.strip():  # Memeriksa apakah teks tidak kosong
        translation = translator.translate(text, src='en', dest='id')
        label.config(text=translation.text)

# Fungsi untuk paste teks yang telah di-copy
def paste_text():
    text = root.clipboard_get()
    text_entry.delete(1.0, tk.END)  # Menghapus teks yang ada di entry
    text_entry.insert(tk.END, text)  # Menambahkan teks yang di-copy ke entry
    update_entry_text()  # Memperbarui terjemahan setelah paste teks

# Membuat instance dari tkinter
root = tk.Tk()
root.title("Contoh Entry dan Label")
root.attributes("-topmost", True)  # Membuat jendela selalu berada di atas

# Membuat text entry (kotak entri teks)
text_entry = tk.Text(root, font=("Helvetica", 10), width=40, height=5, wrap="word")
text_entry.pack(pady=20, padx=20)  # Menambahkan padding agar entry terlihat lebih besar
text_entry.bind("<KeyRelease>", update_entry_text)  # Mengikat event KeyRelease ke fungsi update_entry_text

# Membuat label
label = tk.Label(root, font=("Helvetica", 10), justify='left', wraplength=400)
label.pack()

# Tombol untuk "Paste Text"
paste_button = tk.Button(root, text="Paste Text", command=paste_text)
paste_button.pack()

# Menjalankan loop Tkinter
root.mainloop()
