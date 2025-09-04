import bpy

# If this file is NOT the root __init__.py, compute the add-on id safely:
ADDON_ID = __name__.partition('.')[0]  # top-level package name (folder name)

# If this IS the root __init__.py, you can use: ADDON_ID = __name__

# ------------------------------------------------------------------------
# Preference Properties
# ------------------------------------------------------------------------
class Preference(bpy.types.AddonPreferences):
    bl_idname = ADDON_ID

    # Needed by template_list:
    projects: bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)  # replace with your ProjectItem type
    projects_index: bpy.props.IntProperty(default=0)

    # def draw(self, context):
    #     layout = self.layout
    #     col = layout.column()
    #     col.label(text="Projects (Code, Label, Tooltip):")
    #
    #     row = col.row()
    #     row.template_list(
    #         "PROJECTS_UL_list", "",  # UIList class id must be registered
    #         self, "projects",
    #         self, "projects_index",
    #         rows=4
    #     )
    #
    #     # Operator buttons (must be registered elsewhere)
    #     col2 = row.column(align=True)
    #     col2.operator("prefs_ops.project_add", text="", icon='ADD')
    #     col2.operator("prefs_ops.project_remove", text="", icon='REMOVE')
    #     col2.separator()
    #     op = col2.operator("prefs_ops.project_move", text="", icon='TRIA_UP');   op.direction = 'UP'
    #     op = col2.operator("prefs_ops.project_move", text="", icon='TRIA_DOWN'); op.direction = 'DOWN'
    #
    #     layout.separator()
    #     layout.label(text="Preview (Scene Enum using these items):")
    #     # Guard the preview so prefs don't crash if scene pref_props isn't registered yet
    #     s = context.scene
    #     if hasattr(s, "pref_props") and hasattr(s.pref_props, "project"):
    #         layout.prop(s.pref_props, "project", text="Default Project")
    #     else:
    #         layout.label(text="(scene.pref_props not registered)")

def register():
    bpy.utils.register_class(Preference)

def unregister():
    bpy.utils.unregister_class(Preference)
