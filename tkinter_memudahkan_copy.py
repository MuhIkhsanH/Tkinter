import tkinter as tk

def copy_text(letter):
    lines = entry_text.get("1.0", tk.END).splitlines()
    selected_line = None

    for line in lines:
        line_strip = line.strip()
        if line_strip.lower().startswith(f"{letter.lower()}."):
            selected_line = line[len(letter) + 1:].strip()
            break

    if selected_line:
        root.clipboard_clear()
        root.clipboard_append(selected_line)
        root.update()
    else:
        print(f"Teks untuk tombol {letter} tidak ditemukan.")

def on_enter(event, button):
    button.config(relief='sunken', bg='#45a049', fg='white')  # Mengubah relief dan warna latar belakang/teks saat pointer masuk

def on_leave(event, button):
    button.config(relief='flat', bg='#4CAF50', fg='white')  # Mengembalikan relief dan warna latar belakang/teks saat pointer keluar

root = tk.Tk()
root.title("Aplikasi Copy ABCDE")

entry_text = tk.Text(root, width=60, height=10)
entry_text.pack(pady=10)

button_copy_a = tk.Button(root, text="Copy A", command=lambda: copy_text('A'), font=('Arial', 12), padx=10, pady=5, relief='flat', bg='#4CAF50', fg='white')
button_copy_b = tk.Button(root, text="Copy B", command=lambda: copy_text('B'), font=('Arial', 12), padx=10, pady=5, relief='flat', bg='#4CAF50', fg='white')
button_copy_c = tk.Button(root, text="Copy C", command=lambda: copy_text('C'), font=('Arial', 12), padx=10, pady=5, relief='flat', bg='#4CAF50', fg='white')
button_copy_d = tk.Button(root, text="Copy D", command=lambda: copy_text('D'), font=('Arial', 12), padx=10, pady=5, relief='flat', bg='#4CAF50', fg='white')
button_copy_e = tk.Button(root, text="Copy E", command=lambda: copy_text('E'), font=('Arial', 12), padx=10, pady=5, relief='flat', bg='#4CAF50', fg='white')

# Mengaitkan event saat pointer masuk dan keluar
button_copy_a.bind("<Enter>", lambda event: on_enter(event, button_copy_a))
button_copy_a.bind("<Leave>", lambda event: on_leave(event, button_copy_a))
button_copy_b.bind("<Enter>", lambda event: on_enter(event, button_copy_b))
button_copy_b.bind("<Leave>", lambda event: on_leave(event, button_copy_b))
button_copy_c.bind("<Enter>", lambda event: on_enter(event, button_copy_c))
button_copy_c.bind("<Leave>", lambda event: on_leave(event, button_copy_c))
button_copy_d.bind("<Enter>", lambda event: on_enter(event, button_copy_d))
button_copy_d.bind("<Leave>", lambda event: on_leave(event, button_copy_d))
button_copy_e.bind("<Enter>", lambda event: on_enter(event, button_copy_e))
button_copy_e.bind("<Leave>", lambda event: on_leave(event, button_copy_e))

button_copy_a.pack(pady=5)
button_copy_b.pack(pady=5)
button_copy_c.pack(pady=5)
button_copy_d.pack(pady=5)
button_copy_e.pack(pady=5)

root.lift()
root.attributes("-topmost", True)

root.mainloop()
