import bpy
import os
import subprocess


# Set the path to the directory containing your .ply files
ply_directory = "Path to Ply file goes here"

# List files in the directory
ply_files = [f for f in os.listdir(ply_directory) if f.endswith(".ply")]

# Print the list of files (For Debugging purposes)
#print(ply_files)
external_script_path = "Path to convert_ply_to_fbx.py goes here"

for ply_file in ply_files:
    ply_path = os.path.join(ply_directory, ply_file)
    fbx_file = os.path.splitext(ply_file)[0] + ".fbx"
    fbx_path = os.path.join(ply_directory, fbx_file + ".fbx")

    try:
        #print(ply_path)
        bpy.ops.import_mesh.ply(filepath=ply_path)
        subprocess.run(["python", external_script_path, ply_path, fbx_path], check=True)
    except Exception as e:
        print("Error:", e)
