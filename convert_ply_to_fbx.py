import bpy
import sys
import logging

# Configure logging
log_filename = "conversion.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Arguments passed from the main script
_, ply_path, fbx_path = sys.argv

# Set up a log message
log = logging.getLogger("Conversion")

try:
    log.info("Conversion started...")
    # Set the render engine to Cycles (assuming Cycles supports the desired bake type)
    bpy.context.scene.render.engine = 'CYCLES'

    # Load the .ply file
    bpy.ops.import_mesh.ply(filepath=ply_path)  # Use import_mesh.ply for .ply files

    # Set up baking parameters (if needed)
    # bpy.context.scene.render.image_settings.file_format = 'PNG'
    # bpy.context.scene.render.bake_type = 'TEXTURE'

    # Optionally, set the bake margin to 5 pixels
    # bpy.context.scene.render.bake_margin = 5

    # Export as .fbx
    bpy.ops.export_scene.fbx(filepath=fbx_path)

    # Close Blender
    bpy.ops.wm.quit_blender()

    log.info("Conversion completed successfully.")

except Exception as e:
    log.error(f"Conversion failed: {str(e)}")    
