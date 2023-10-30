import bpy
import os

#os.chdir("C:\\Users\\rparm\\Documents\\GitHub\\Point-eAutomatedGit\\Point-eAutomatedFlow")

# Set the path to the directory containing your .ply files
#ply_directory = r"C:/Users/rparm/Documents/GitHub/Point-eAutomatedGit/Point-eAutomatedFlow/MeshFiles"
ply_directory = "C:\\Users\\rparm\\Documents\\GitHub\\Point-eAutomatedGit\\Point-eAutomatedFlow\\MeshFiles"

# List files in the directory
files = os.listdir(ply_directory)

# Print the list of files
print("Files in the directory:")
for file in files:
    print(file)

#ply_directory = os.path.join("C:", "Users", "rparm", "Documents", "GitHub", "Point-eAutomatedGit", "Point-eAutomatedFlow", "MeshFiles" )

#check if ply_directory exists
if os.path.exists(ply_directory):
    ply_files = [f for f in os.listdir(ply_directory) if f.endswith(".ply")]
else:
    print(f"The directory '{ply_directory}' does not exist.")


# Set the path to the Blender executable 
#blender_executable = r"C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender.exe"
#blender_executable = "C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"
#blender_executable = os.path.join("C:", "Program", "Files", "Blender Foundation", "Blender 3.6", "blender.exe")
import subprocess
blender_executable = r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"

try:
    subprocess.run([blender_executable], check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)



# List all .ply files in the directory
ply_files = [f for f in os.listdir(ply_directory) if f.endswith(".ply")]

# Loop through each .ply file and convert to .fbx
for ply_file in ply_files:
    ply_path = os.path.join(ply_directory, ply_file)
    fbx_file = os.path.splitext(ply_file)[0] + ".fbx"
    fbx_path = os.path.join(ply_directory, fbx_file)

    # Run Blender in background mode to convert the file
    cmd = f'"{blender_executable}" -b -P convert_ply_to_fbx.py -- "{ply_path}" "{fbx_path}"'
    os.system(cmd)
