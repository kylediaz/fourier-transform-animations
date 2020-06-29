import bpy

for scene in bpy.data.scenes: 
    if scene.sequence_editor is not None:
        strip = scene.sequence_editor.sequences_all
        if strip is not None and strip["Square Color Text"] is not None:
            text_obj = strip["Square Color Text"]
        if strip is not None and strip["Color"] is not None:
            color_obj = strip["Color"]            


def recalculate_text(scene):
    if text_obj and color_obj is not None:
        text_obj.text = str(round(100 * color_obj.color.v))
        

bpy.app.handlers.frame_change_pre.append(recalculate_text)
bpy.app.handlers.frame_change_post.append(recalculate_text)