import tkinter as tk
from tkinter import filedialog
import os

def update_preview(event=None):
    base_name = base_name_entry.get()
    folder_path = folder_path_entry.get()
    start_counter = counter_entry.get().strip()  # Get and strip any leading/trailing spaces
    
    # Check if counter entry is empty
    if not start_counter:
        warning_string.set("Counter cannot be blank!")
        rename_button.config(state=tk.DISABLED)  # Disable the button
        return
    
    # Check for invalid characters
    invalid_characters = set('\\/:*?"<>|')
    if any(char in invalid_characters for char in base_name):
        warning_string.set("Invalid characters in base filename!")
        rename_button.config(state=tk.DISABLED)  # Disable the button
    else:
        clear_warning_message()  # Clear any existing warning message
        counter_length = len(start_counter)  # Get length of counter value
        preview_filename = f"{base_name}-{start_counter.zfill(counter_length)}.ext"  # Update preview string with counter value
        preview_string.set(preview_filename)
        rename_button.config(state=tk.NORMAL)  # Enable the button

def batch_rename_files():
    folder_path = folder_path_entry.get()
    base_name = base_name_entry.get()
    start_counter = counter_entry.get().strip()  # Get and strip any leading/trailing spaces
    
    # Check if counter entry is empty
    if not start_counter:
        warning_string.set("Counter cannot be blank!")
        return
    
    try:
        files = sorted(os.listdir(folder_path))
        files_amount_in_folder = len(files)
        counter = int(start_counter)  # Convert start counter to integer
        counter_length = len(start_counter)  # Get length of counter value
        
        for filename in files:
            name, ext = os.path.splitext(filename)
            old_path = os.path.join(folder_path, filename)
            new_name = f"{base_name}-{counter:0{counter_length}}{ext}" # Use formatted string to pad zeros based on counter length
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            counter += 1
        
        warning_string.set(f"{files_amount_in_folder} files were successfully renamed!")
    
    except FileNotFoundError:
        warning_string.set(f"Folder not found!")
    
    except PermissionError:
        warning_string.set(f"You don't have the permission to rename these files!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)
    update_preview()

def clear_warning_message(event=None):
    warning_string.set("")

def validate_counter_input(new_value):
    # Check if the new value is empty or consists only of numeric characters
    if new_value.isdigit() or new_value == "":
        return True
    else:
        return False

# Create main window
window = tk.Tk()
window.title("Batch File Renamer")

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

# Counter Label
counter_label = tk.Label(window, text="Start Counter:")
counter_label.grid(row=2, column=0, sticky="W", padx=10, pady=10)

# Create a validation command for the counter entry widget
validate_counter = window.register(validate_counter_input)

# Counter Entry
counter_entry = tk.Entry(window, width=10, validate="key", validatecommand=(validate_counter, "%P"))
counter_entry.grid(row=2, column=1, sticky="W", padx=10, pady=10)
counter_entry.insert(0, "1")  # Default value for start counter
counter_entry.bind("<KeyRelease>", update_preview)

# Preview Label
preview_label = tk.Label(window, text="Preview:", anchor="w")
preview_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

# Preview String
preview_string = tk.StringVar()
preview_string.set("-1.ext")

preview_string_label = tk.Label(window, textvariable=preview_string, anchor="w")
preview_string_label.grid(row=3, column=1, padx=10, pady=10, sticky="W")

# Warning Label
preview_label = tk.Label(window, text="Status:", anchor="w")
preview_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

# Warning String
warning_string = tk.StringVar()
warning_label = tk.Label(window, textvariable=warning_string, anchor="w", fg="blue")
warning_label.grid(row=4, column=1, padx=10, pady=10, sticky="W")

# Rename Button
rename_button = tk.Button(window, text="Rename Files", command=batch_rename_files) 
rename_button.grid(row=5, column=1, padx=10, pady=10)

# Run the application
window.mainloop()
