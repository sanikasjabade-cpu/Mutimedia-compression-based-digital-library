import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import main  # connects to your main.py compression code

# ================== FOLDERS ==================
UPLOAD_FOLDER = "uploaded"
COMPRESSED_FOLDER = "compressed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

# ================== MAIN WINDOW ==================
root = tk.Tk()
root.title("Digital Multimedia Library")
root.geometry("500x420")
root.configure(bg="#f0f4f7")

title_label = tk.Label(
    root,
    text="Digital Multimedia Library",
    font=("Arial", 18, "bold"),
    bg="#f0f4f7",
    fg="#1a237e"
)
title_label.pack(pady=15)

# ================== UPLOAD FUNCTION ==================
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select Media or PDF",
        filetypes=[
            ("Supported Files", "*.mp3 *.wav *.jpg *.jpeg *.png *.mp4 *.avi *.mkv *.pdf"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(UPLOAD_FOLDER, filename)

        # copy to uploaded folder
        shutil.copy2(file_path, dest_path)

        # 🔥 CALL COMPRESSION
        original_size, compressed_size, _ = main.compress_file(
            dest_path,
            COMPRESSED_FOLDER
        )

        messagebox.showinfo(
            "Success",
            f"{filename} uploaded and compressed!\n"
            f"Original: {original_size} bytes\n"
            f"Compressed: {compressed_size} bytes"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== SHOW LIBRARY ==================
def show_library():
    lib_window = tk.Toplevel(root)
    lib_window.title("Digital Library")
    lib_window.geometry("650x420")

    text_area = tk.Text(lib_window, font=("Consolas", 11))
    text_area.pack(fill="both", expand=True)

    text_area.insert("end", "DIGITAL LIBRARY CONTENT\n")
    text_area.insert("end", "-" * 60 + "\n\n")

    uploaded_files = os.listdir(UPLOAD_FOLDER)

    if not uploaded_files:
        text_area.insert("end", "No files uploaded yet.\n")
        return

    for filename in uploaded_files:
        uploaded_path = os.path.join(UPLOAD_FOLDER, filename)

        name, _ = os.path.splitext(filename)
        compressed_file = name + ".zip"
        compressed_path = os.path.join(COMPRESSED_FOLDER, compressed_file)

        # original size
        try:
            original_size = os.path.getsize(uploaded_path)
        except:
            original_size = "Not found"

        # compressed size
        if os.path.exists(compressed_path):
            compressed_size = os.path.getsize(compressed_path)
        else:
            compressed_size = "Not compressed"

        text_area.insert(
            "end",
            f"File: {filename}\n"
            f"Original Size: {original_size} bytes\n"
            f"Compressed Size: {compressed_size} bytes\n"
            f"{'-'*50}\n"
        )

# ================== BUTTONS ==================
upload_btn = tk.Button(
    root,
    text="Upload File",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#1976d2",
    fg="white",
    command=upload_file
)
upload_btn.pack(pady=10)

show_btn = tk.Button(
    root,
    text="Show Digital Library",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#388e3c",
    fg="white",
    command=show_library
)
show_btn.pack(pady=10)

exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#d32f2f",
    fg="white",
    command=root.destroy
)
exit_btn.pack(pady=20)

# ================== RUN ==================
root.mainloop()
