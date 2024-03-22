import os
import shutil

def delete_files_in_folder(folder_path):
    # Get list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file and delete it
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Folder paths
pages_folder = 'pages'
renamed_pages_folder = 'renamed_pages'

# Delete files in each folder
delete_files_in_folder(pages_folder)
delete_files_in_folder(renamed_pages_folder)

print("All files deleted successfully.")
