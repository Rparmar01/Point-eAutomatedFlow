from json import load
import os 

# Run text2pointcloud notebook to create a pointcloud from text
createPCloud = "text2pointcloud.ipynb"
with open(createPCloud) as fp:
    nb = load(fp)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(line for line in cell['source'] if not line.startswith('%'))
        exec(source, globals(), locals())

# Run pointcloud2mesh notebook to convert pointcloud into a ply mesh
createMesh = "pointcloud2mesh.ipynb"
with open(createMesh) as fp:
    nb = load(fp)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(line for line in cell['source'] if not line.startswith('%'))
        exec(source, globals(), locals())

# Run ply to fbx conversion script to bake ply mesh to fbx object file
os.system('ply_to_fbx.py')

#Export fbx object to engine (Unreal Engine in this case)