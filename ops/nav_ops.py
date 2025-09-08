import os.path

import bpy
from ..utils import device, filedata


# ------------------------------------------------------------------------
# Navigation Panel Operators
# ------------------------------------------------------------------------
class NAV_OT_apply_preset(bpy.types.Operator):
    bl_idname = "nav_ops.apply_preset"
    bl_label = "Apply Preset"
    bl_description = "Apply the selected preset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        scenes = bpy.data.scenes["Scene"]
        pref_props = scene.pref_props

        preset = bpy.ops.presets.apply_preset('EXEC_DEFAULT')

        # scenes.render.stamp_note_text = device.get_machine_name()

        _, _, name, _ = filedata.split_blend_filepath()
        scenes.render.stamp_note_text = name
        parts = [part for part in name.split("_") if part.strip()]
        # [0] project, [1] episode, [2] seq, [3] shot, [4] division, [5] version(optional)
        dir_path = f"/mnt/{pref_props.project}/{parts[1]}/{parts[1]}_{parts[2]}/{parts[1]}_{parts[2]}_{parts[3]}/playblast/{parts[4]}"
        # if not os.path.exists(f"/mnt/{pref_props.project}/{parts[1]}"):
        #     return {'CANCELLED'}

        final_path = os.path.join(dir_path, f"{name}.mov")

        scenes.render.filepath = final_path

        # Logic to apply the preset goes here
        self.report({'INFO'}, f"Preset applied")
        return {'FINISHED'}

class NAV_OT_render(bpy.types.Operator):
    bl_idname = "nav_ops.render"
    bl_label = "Render Animation"
    bl_description = "Render the animation with the applied preset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        scenes = bpy.data.scenes["Scene"]
        pref_props = scene.pref_props

        # Ensure the preset is applied before rendering
        bpy.ops.nav_ops.apply_preset()

        camera = bpy.context.scene.camera
        if camera:
            camera.select_set(True)
            bpy.context.view_layer.objects.active = camera
            bpy.ops.render.opengl(animation=True)
        else:
            print("Tidak ada kamera aktif di scene.")

        self.report({'INFO'}, "Rendering started")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(NAV_OT_apply_preset)
    bpy.utils.register_class(NAV_OT_render)


def unregister():
    bpy.utils.unregister_class(NAV_OT_apply_preset)
    bpy.utils.unregister_class(NAV_OT_render)
