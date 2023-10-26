# Point-eAutomatedFlow
Using OpenAI's Point-e repository to automate text-to-3D object workflow. This includes a tutorial on how to convert user-inputted text into a nbx file mesh and then into a fully baked fbx file for use in game engines.

## Requirements: 
1. Clone OpenAI's point-e repository and follow all installation requirements
2. If you are running jupyter notebook files locally:
    1. It is highly recommended that you have a viable GPU available and install Tensorflow and its dependencies. Alternative options include running the notebooks on Google Colab or on a cloud service such as Azure. Tensorflow: https://www.tensorflow.org/install/pip
    2. Install Anaconda or Miniconda. Create a new environment with Tensorflow's packages and switch to the environment.   
3. Install Blender
4. Install your 3D Simulation Engine of your choice. Typically these will be Unity, Unreal Engine, or Godot. 

## Instructions:
1. (If running locally) Run Anaconda and switch to your Tensorflow environment if you haven't already done so.
3. Run text2pointcloud.ipynb
4. Run pointcloud2mesh.ipynb 
5. BAKING: Open Blender and follow these instructions: https://betterprogramming.pub/from-text-to-unreal-engine-object-using-openais-new-3d-model-generator-65e5b1019045 . Note that Unreal Engine is the final engine in the tutorial where the fbx file gets imported.

### Miscellaneous and Other Notes: 
Openai also has Shap-E: https://github.com/openai/shap-e Research Paper: https://arxiv.org/abs/2305.02463

For ideas related to AI map-generation, Video Game Cartogaphy:https://canadiangeographic.ca/articles/inside-the-intricate-world-of-video-game-cartography/

