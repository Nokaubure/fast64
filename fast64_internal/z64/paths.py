import bpy


def get_decomp_path(scene=None):
    # different path depending on OoT or MM
    if scene is None:
        scene = bpy.context.scene
    return scene.mmDecompPath if scene.gameEditorMode == "MM" else scene.ootDecompPath
