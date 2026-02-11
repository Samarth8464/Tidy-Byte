import os
import shutil  # Added for moving files

def main():
    
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Audio': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mov'],
        'Archives': ['.zip', '.rar']
    }

    target_folder = input("Please enter the path of the folder to organize: ")

    if os.path.exists(target_folder):
        all_items = os.listdir(target_folder)
        files_found = [f for f in all_items if os.path.isfile(os.path.join(target_folder, f))]
        
        print(f"Moving {len(files_found)} files...")

        for file in files_found:
            file_path = os.path.join(target_folder, file)
            ext = os.path.splitext(file)[1].lower()
            
            # Determining the category
            category_found = "Others"
            for category, extensions in EXTENSION_MAP.items():
                if ext in extensions:
                    category_found = category
                    break
            
            
            #Creating the destination folder path
            dest_dir = os.path.join(target_folder, category_found)
            
            # Making the folder if it doesn't exist yet
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            # Moving the file
            shutil.move(file_path, os.path.join(dest_dir, file))
            print(f" [OK] Moved {file} to {category_found}/")

        print("\nOrganization complete!")
    else:
        print("[ERROR] Path not found.")

if __name__ == "__main__":
    main()