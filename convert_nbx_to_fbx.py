import bpy
import sys

# Arguments passed from the main script
_, nbx_path, fbx_path = sys.argv

# Load the .nbx file
bpy.ops.import_scene.nbx(filepath=nbx_path)

# Optionally, set up baking parameters (e.g., for texture baking)
bpy.context.scene.render.image_settings.file_format = 'PNG'  # Set the desired output format
bpy.context.scene.render.bake_type = 'TEXTURE'  # Set the type of bake

# Bake the mesh
bpy.ops.object.bake(type='DIFFUSE')  # You can change 'DIFFUSE' to the desired bake type

# Export as .fbx
bpy.ops.export_scene.fbx(filepath=fbx_path)

# Close Blender
bpy.ops.wm.quit_blender()
