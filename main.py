import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox


def run_organizer_logic(target_folder):
    """
    This function contains the core movement logic. 
    It is separated from the UI so it can be tested independently.
    """
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Installers': ['.exe', '.msi', '.dmg', '.pkg']
    }
    current_time = time.time()
    seconds_in_180_days = 180 * 24 * 60 * 60

    # Listing all items in the directory
    all_items = os.listdir(target_folder)
    # Filtering out folders, only keep files
    files_to_move = [f for f in all_items if os.path.isfile(os.path.join(target_folder, f))]

    for file in files_to_move:
        source_path = os.path.join(target_folder, file)
        file_mod_time = os.path.getmtime(source_path) # Get last modified timestamp
        file_age_seconds = current_time - file_mod_time

        if file_age_seconds > seconds_in_180_days:
            # Converting the timestamp to a Year and Month name
            date_obj = datetime.fromtimestamp(file_mod_time)
            year = date_obj.strftime('%Y')       # e.g., '2023'
            month = date_obj.strftime('%B')      # e.g., 'January'
            
            # Create a nested path: Archive/2023/January
            dest_folder = os.path.join(target_folder, "Archive", year, month)
        
        else:
            _, ext = os.path.splitext(file)
        ext = ext.lower()

        # Identifying category
        category = "Others"
        for cat, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                category = cat
                break

        # Creating folder path
        dest_folder = os.path.join(target_folder, category)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Moving file
        shutil.move(source_path, os.path.join(dest_folder, file))



def select_and_organize():
    """
    This handles the button click, folder selection, 
    and gives feedback to the user.
    """
    # Opening the folder picker window
    target_folder = filedialog.askdirectory(title="Select Folder to Tidy")
    
    if not target_folder:
        return  # User clicked 'Cancel'

    try:
        # Running the logic we defined in Part 1
        run_organizer_logic(target_folder)
        
        # Showing a success popup
        messagebox.showinfo("TidyByte Success", f"Folder Organized!\nPath: {target_folder}")
    
    except Exception as e:
        # Showing an error popup if something goes wrong
        messagebox.showerror("TidyByte Error", f"An error occurred: {e}")



if __name__ == "__main__":
    # Creating the main window
    root = tk.Tk()
    root.title("TidyByte | Professional File Organizer")
    root.geometry("450x300")
    root.configure(bg="#f0f0f0") # Light grey background

    # Title
    title_label = tk.Label(root, text="TidyByte", bg="#f0f0f0", fg="#333333", 
                           font=("Segoe UI", 24, "bold"))
    title_label.pack(pady=20)

    # Subtitle
    desc_label = tk.Label(root, text="Clean up your digital chaos in one click.", 
                          bg="#f0f0f0", fg="#666666", font=("Segoe UI", 10))
    desc_label.pack(pady=5)

    # Main Action Button
    
    btn_organize = tk.Button(root, text="SELECT FOLDER", command=select_and_organize, 
                             bg="#0078d7", fg="white", font=("Segoe UI", 12, "bold"), 
                             padx=30, pady=10, relief="flat", cursor="hand2")
    btn_organize.pack(pady=30)

    # Footer
    footer = tk.Label(root, text="v1.0.0 | Portfolio Project", bg="#f0f0f0", 
                      fg="#999999", font=("Segoe UI", 8))
    footer.pack(side="bottom", pady=10)

    # Start the application
    root.mainloop()