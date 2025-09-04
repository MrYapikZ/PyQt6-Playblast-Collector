import bpy

# ------------------------------------------------------------------------
# Navigation Panel Properties
# ------------------------------------------------------------------------
class NAV_PT_Panel(bpy.types.Panel):
    bl_label = "PTP Playblast"
    bl_idname = "NAV_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PTP_Playblast'
    bl_description = "Navigation panel for PTP Playblast"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pref_props = scene.pref_props
        row = layout.row()
        row.prop(pref_props, "project", text="Project")
        layout.operator("nav_ops.apply_preset", text="Apply Preset", icon='PRESET')
        layout.operator("nav_ops.render", text="Render Animation", icon='RENDER_ANIMATION')

# ------------------------------------------------------------------------
# Register
# ------------------------------------------------------------------------
def register():
    bpy.utils.register_class(NAV_PT_Panel)

def unregister():
    bpy.utils.unregister_class(NAV_PT_Panel)