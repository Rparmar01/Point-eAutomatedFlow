import bpy
import os

# Set the path to the directory containing your .nbx files
nbx_directory = "C:/Users/rparm/Documents/GitHub/Point-eAutomatedGit/Point-eAutomatedFlow/MeshFiles/"

# Set the path to the Blender executable (change this to the correct path)
blender_executable = "C:/Users/rparm/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/blender/"

# List all .nbx files in the directory
nbx_files = [f for f in os.listdir(nbx_directory) if f.endswith(".nbx")]

# Loop through each .nbx file and convert to .fbx
for nbx_file in nbx_files:
    nbx_path = os.path.join(nbx_directory, nbx_file)
    fbx_file = os.path.splitext(nbx_file)[0] + ".fbx"
    fbx_path = os.path.join(nbx_directory, fbx_file)

    # Run Blender in background mode to convert the file
    cmd = f"{blender_executable} -b -P convert_nbx_to_fbx.py -- {nbx_path} {fbx_path}"
    os.system(cmd)
