import os

def main():
    
    # 1. Define the Dictionary (The "Rules")
    # This maps folder names to lists of file extensions.
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Installers': ['.exe', '.msi', '.dmg', '.pkg']
    }

    # 2. Getting User Input
    # We ask for the path and verify it exists to prevent errors.
    print("--- TidyByte: File Organizer (Development Mode) ---")
    target_folder = input("Please enter the path of the folder to organize: ")

    if os.path.exists(target_folder):
        print(f"\n[SUCCESS] Path found: {target_folder}")
        print("Checking for files...")
        
        # 3. Scan the directory
        # We list all items and separate files from folders.
        all_items = os.listdir(target_folder)
        files_found = [f for f in all_items if os.path.isfile(os.path.join(target_folder, f))]
        
        print(f"Total files detected: {len(files_found)}")
        
        # 4. Dry Run Logic (Identify categories without moving yet)
        for file in files_found:
            name, ext = os.path.splitext(file)
            ext = ext.lower()
            
            # Find the category
            category_found = "Others"
            for category, extensions in EXTENSION_MAP.items():
                if ext in extensions:
                    category_found = category
                    break
            
            print(f"File: {file} -> Target Category: {category_found}")

    else:
        print("[ERROR] The path provided does not exist. Please check and try again.")

if __name__ == "__main__":
    main()