import bpy
import sys

# Arguments passed from the main script
_, ply_path, fbx_path = sys.argv

# Set the render engine to Cycles (assuming Cycles supports the desired bake type)
bpy.context.scene.render.engine = 'CYCLES'

# Load the .ply file
bpy.ops.import_mesh.ply(filepath=ply_path)  # Use import_mesh.ply for .ply files

# Create a new material for the imported object
mat = bpy.data.materials.new(name="MyMaterial")
bpy.context.object.data.materials.append(mat)

# Set up baking parameters (if needed)
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.bake_type = 'NORMALS'  # Use 'NORMALS' instead of 'DIFFUSE'

# Get all objects in selection
selection = bpy.context.selected_objects

# Get the active object
active_object = bpy.context.active_object

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

for obj in selection:
    # Select each object
    obj.select_set(True)
    # Make it active
    bpy.context.view_layer.objects.active = obj
    # Toggle into Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')
    # Select the geometry
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Use Smart UV Project for UV unwrapping
    bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.02, correct_aspect=True, scale_to_bounds=True)
    
    # Toggle out of Edit Mode
    bpy.ops.object.mode_set(mode='OBJECT')
    # Deselect the object
    obj.select_set(False)

# Restore the selection
for obj in selection:
    obj.select_set(True)

# Restore the active object
bpy.context.view_layer.objects.active = active_object

# Set up baking margin
bpy.context.scene.render.bake_margin = 5

# Perform the bake
bpy.ops.object.bake(type='COMBINED')

# Export the object as an FBX file
bpy.ops.export_scene.fbx(filepath=fbx_path, use_selection=True, bake_space_transform=True, use_mesh_modifiers=True, mesh_smooth_type='OFF')

print("Conversion completed successfully.")
