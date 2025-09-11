import bpy

class PRESET_OT_apply_playblast(bpy.types.Operator):
    bl_idname = "presets.apply_preset"
    bl_label = "Apply Playblast Preset"
    bl_description = "Execute the configured playblast/render settings on the active Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scenes = bpy.data.scenes["Scene"]

        scenes.render.use_simplify = True
        scenes.render.simplify_subdivision = 1

        # Format playblast
        scenes.render.resolution_x = 1920
        scenes.render.resolution_y = 1080
        scenes.render.resolution_percentage = 80
        scenes.render.use_border = False
        scenes.render.fps = 24
        scenes.render.image_settings.file_format = "FFMPEG"
        scenes.render.ffmpeg.format = "QUICKTIME"
        scenes.render.ffmpeg.audio_codec = "AAC"
        scenes.render.ffmpeg.codec = "PRORES"
        # scenes.render.filepath = "path output shot"

        # Metadata
        # scenes.render.metadata_input = "SCENE"
        scenes.render.use_stamp_date = True
        scenes.render.use_stamp_time = False
        scenes.render.use_stamp_render_time = False
        scenes.render.use_stamp_frame = True
        scenes.render.use_stamp_frame_range = False
        scenes.render.use_stamp_memory = False
        scenes.render.use_stamp_hostname = False
        scenes.render.use_stamp_camera = False
        scenes.render.use_stamp_lens = True
        scenes.render.use_stamp_scene = False
        scenes.render.use_stamp_marker = False
        scenes.render.use_stamp_filename = False
        scenes.render.use_stamp_sequencer_strip = False
        scenes.render.use_compositing = False
        scenes.render.use_sequencer = False

        # Note
        scenes.render.use_stamp_note = True
        # scenes.render.stamp_note_text = "Nama pc"

        # Burn Into Image
        scenes.render.use_stamp = True
        scenes.render.stamp_font_size = 20
        scenes.render.stamp_foreground = (0.799238, 0.715663, 0, 1)
        scenes.render.stamp_background = (0, 0, 0, 0.5)

        # Camera
        bpy.ops.view3d.view_camera_operator()

        # Set mode to Texture Preview
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # space.shading.type = 'MATERIAL'
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'TEXTURE'
                        break

        return {'FINISHED'}

class VIEW3D_OT_ViewCamera(bpy.types.Operator):
    """Switch to camera view"""
    bl_idname = "view3d.view_camera_operator"
    bl_label = "View Camera"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        region_3d = space.region_3d
                        overlay = space.overlay
                        overlay.show_overlays = False
                        region_3d.view_perspective = 'CAMERA'
                        self.report({'INFO'}, "Switched to Camera View")
        return {'FINISHED'}
        # self.report({'WARNING'}, "No 3D Viewport found")
        # return {'CANCELLED'}

def register():
    bpy.utils.register_class(VIEW3D_OT_ViewCamera)
    bpy.utils.register_class(PRESET_OT_apply_playblast)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_ViewCamera)
    bpy.utils.unregister_class(PRESET_OT_apply_playblast)
