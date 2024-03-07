import os
import subprocess
import time
from aspose.threed import Scene
import aspose.threed as a3d
from Unzipper import unzip_all_files
import random

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
                    time.sleep(10)
                    deletefile("/Users/apple/Documents/Python/LocalData/ZipperFile")
                    
                else:
                    unzipped = False
                print(f"All required files found! Triggering the shell script.")
                if(generatedMesh ==False):
                    subprocess.run(['bash', script_path])
                    print(" USDZ File Generatered ")
                    generatedMesh =True
                else:
                    print("waiting for 20  second")
                    time.sleep(40)
                files = os.listdir("/Users/apple/Documents/Python/LocalData/Output")
                if any(file.endswith(".usdz") for file in files):
                    scene = Scene.from_file("/Users/apple/Documents/Python/LocalData/Output/Bash_Test_Model_01.usdz")
                    scene.save("OutputObject/Test.stl", a3d.FileFormat.STLASCII)
                    deletefile("/Users/apple/Documents/Python/LocalData/Output")
                    print("STL Ready to Download")
                    generatedMesh =False
                    unzipped = False
                    break
                else:
                    time.sleep(40)
        else:
            for i in range_with_status(100):
                time.sleep(random.random())
        


def range_with_status(total):
    """ iterate from 0 to total and show progress in console """
    n=0
    while n<total:
        done = '#'*(n+1)
        todo = '-'*(total-n-1)
        s = '<{0}>'.format(done+todo)
        if not todo:
            s+='\n'        
        if n>0:
            s = '\r'+s
        print(s, end='')
        yield n
        n+=1

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
    while True:
        monitor_directory(directory_to_monitor, required_files, shell_script_path )
        deletefile(directory_to_monitor)
        
       
    
