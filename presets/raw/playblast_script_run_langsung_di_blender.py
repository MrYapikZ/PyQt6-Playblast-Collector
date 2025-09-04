import os
import sys
import bpy

class VIEW3D_PT_CustomTab(bpy.types.Panel):
    """Panel for custom camera view"""
    bl_label = "Custom Tab"
    bl_idname = "VIEW3D_PT_CustomTab"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "CustomTab"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("view3d.view_camera_operator", text="viewCAM")

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
                        region_3d.view_perspective = 'CAMERA'
                        self.report({'INFO'}, "Switched to Camera View")
                        return {'FINISHED'}
        self.report({'WARNING'}, "No 3D Viewport found")
        return {'CANCELLED'}

def register():
    bpy.utils.register_class(VIEW3D_PT_CustomTab)
    bpy.utils.register_class(VIEW3D_OT_ViewCamera)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_CustomTab)
    bpy.utils.unregister_class(VIEW3D_OT_ViewCamera)

if __name__ == "__main__":
    register()

file_path = bpy.data.filepath

# Jalankan operator custom untuk "viewCAM"
bpy.ops.view3d.view_camera_operator()

# Set mode ke Material Preview
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                # space.shading.type = 'MATERIAL'
                space.shading.type = 'SOLID'
                space.shading.color_type = 'TEXTURE'
                break

# Tentukan direktori output berdasarkan nama pengguna
user_name = os.getlogin()
output_dir = f"C:\\Users\\{user_name}\\Videos\\pb_batch"
os.makedirs(output_dir, exist_ok=True)

# Tentukan nama file output
output_name = os.path.splitext(os.path.basename(file_path))[0] + "_playblast.mov"
output_path = os.path.join(output_dir, output_name)

# Konfigurasi render
bpy.context.scene.render.filepath = output_path
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'  # Atau 'PNG' jika dibutuhkan

# Lakukan Viewport Render Animation
bpy.ops.render.opengl(animation=True)

