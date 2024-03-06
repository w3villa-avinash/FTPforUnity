import os
import subprocess
import time
from aspose.threed import Scene
import aspose.threed as a3d
from UNzipper import unzip_all_files


def monitor_directory(directory_path, file_names, script_path):
    generatedMesh =False
    unzipped =False

    while True:
        files = os.listdir("/Users/apple/Documents/Python/LocalData/ZipperFile")
        
       
        # Check if all required files are present in the directory
    
        print("Waiting for the trigger ")
        if all(file in files for file in file_names):
                print("Unzipping the File")
                if(unzipped ==False):
                    unzipped =True
                    unzip_all_files("/Users/apple/Documents/Python/LocalData/ZipperFile")
                else:
                    unzipped = False
                print(f"All required files found! Triggering the shell script.")
                if(generatedMesh ==False):
                    subprocess.run(['bash', script_path])
                    print(" USDZ File Generatered ")
                    generatedMesh =True
                else:
                    print("waiting for 20  second")
                    time.sleep(20)
                files = os.listdir("/Users/apple/Documents/Python/LocalData/Output")
                if any(file.endswith(".usdz") for file in files):
                    scene = Scene.from_file("/Users/apple/Documents/Python/LocalData/Output/Bash_Test_Model_01.usdz")
                    scene.save("OutputObject/Test.stl", a3d.FileFormat.STLASCII)
                    print("Obj Ready to Download")
                    break
                else:
                    time.sleep(20)
        else:
            time.sleep(20)
         
          # Sleep for 60 seconds before checking again
def deletefile(directory_to_monitor):
    folder = directory_to_monitor
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
if __name__ == "__main__":
    # Replace these values with your actual directory, file names, and script path
    directory_to_monitor = "/Users/apple/Documents/Python/LocalData/Input"
    required_files = ["trigger.txt"]
    shell_script_path = "/Users/apple/Documents/Python/LocalData/CreateModel.sh"
    monitor_directory(directory_to_monitor, required_files, shell_script_path )
    deletefile(directory_to_monitor)
    deletefile("/Users/apple/Documents/Python/LocalData/Output")
    deletefile("/Users/apple/Documents/Python/LocalData/ZipperFile")
    
