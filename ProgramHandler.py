from json import load
import os 

# Run text2pointcloud notebook to create a pointcloud from text and convert pointcloud into a ply mesh
createPCloud = "Point-eAutomatedFlow/point-e/point_e/examples/text2pointcloudANDpointcloud2mesh.ipynb"
with open(createPCloud) as fp:
    nb = load(fp)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(line for line in cell['source'] if not line.startswith('%'))
        exec(source, globals(), locals())

# Run ply to fbx conversion script to bake ply mesh to fbx object file
os.system("python ply_to_fbx.py")

#Export fbx object to engine (Unreal Engine in this case)

