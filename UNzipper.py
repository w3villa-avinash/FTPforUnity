import os
import zipfile

def unzip_all_files(directory_path):
 
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return
    
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file and unzip if it's a zip file
    for file in files:
        file_path = os.path.join(directory_path, file)

        # Check if the file is a zip file
        if file.endswith(".zip"):
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    # Extract all contents to the same directory
                    zip_ref.extractall("/Users/apple/Documents/Python/LocalData/Input")
                print(f"File '{file}' successfully unzipped.")
            except Exception as e:
                print(f"Error unzipping file '{file}': {e}")
        else:
            print(f"Skipping '{file}' as it's not a zip file.")


