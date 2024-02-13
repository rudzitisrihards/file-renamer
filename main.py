import tkinter as tk
from tkinter import filedialog
import os

def update_preview(event=None):
    base_name = base_name_entry.get()
    folder_path = folder_path_entry.get()
    preview_filename = f"{base_name}-#.ext"
    preview_string.set(preview_filename)

def batch_rename_files():
    folder_path = folder_path_entry.get()
    base_name = base_name_entry.get()
    
    try:
        files = sorted(os.listdir(folder_path))
        files_amount_in_folder = len(files)
        counter = 1
        
        for filename in files:
            name, ext = os.path.splitext(filename)
            old_path = os.path.join(folder_path, filename)
            new_name = f"{base_name}-{counter}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            counter += 1
        
        warning_string.set(f"{files_amount_in_folder} files were successfully renamed!")
    
    except FileNotFoundError:
        warning_string.set(f"Folder {folder_path} not found.")
    
    except PermissionError:
        warning_string.set(f"You don't have permissions to rename files in {folder_path}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)
    update_preview()

# Create main window
window = tk.Tk()
window.title("Batch File Renamer")

# Set the icon
# window.iconbitmap("path_to_your_icon_file.ico")

# Make the window not resizable
window.resizable(False, False)

# Folder Path Label
folder_path_label = tk.Label(window, text="Folder Path:")
folder_path_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)

# Folder Path Entry
folder_path_entry = tk.Entry(window, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)
folder_path_entry.bind("<KeyRelease>", update_preview)

# Browse Button
browse_button = tk.Button(window, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Base Name Label
base_name_label = tk.Label(window, text="Base Name:")
base_name_label.grid(row=1, column=0, sticky="W", padx=10, pady=10)

# Base Name Entry
base_name_entry = tk.Entry(window, width=50)
base_name_entry.grid(row=1, column=1, padx=10, pady=10)
base_name_entry.bind("<KeyRelease>", update_preview)

# Preview Label
preview_label = tk.Label(window, text="Preview:", anchor="w")
preview_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

# Preview String
preview_string = tk.StringVar()
preview_string.set("-")
preview_string_label = tk.Label(window, textvariable=preview_string, anchor="w")
preview_string_label.grid(row=2, column=1, padx=10, pady=10, sticky="W")

# Warning Label
preview_label = tk.Label(window, text="Status:", anchor="w")
preview_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

# Warning String
warning_string = tk.StringVar()
warning_label = tk.Label(window, textvariable=warning_string, anchor="w", fg="green")
warning_label.grid(row=3, column=1, padx=10, pady=10, sticky="W")

# Rename Button
rename_button = tk.Button(window, text="Rename Files", command=batch_rename_files)
rename_button.grid(row=4, column=1, padx=10, pady=10)

# Run the application
window.mainloop()
