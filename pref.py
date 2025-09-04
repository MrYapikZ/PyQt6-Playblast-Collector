import bpy
# ------------------------------------------------------------------------
# Navigation Properties
# ------------------------------------------------------------------------
class DataSettings(bpy.types.PropertyGroup):
    project: bpy.props.EnumProperty(
        name="Project",
        description="Select Project",
        items=[
            ("K", "Jagat", "RMB"),
            ("O", "Rimba", "RMB")
        ]
    )

def register():
    bpy.utils.register_class(DataSettings)
    bpy.types.Scene.pref_props = bpy.props.PointerProperty(type=DataSettings)
def unregister():
    bpy.utils.unregister_class(DataSettings)
    del bpy.types.Scene.pref_props