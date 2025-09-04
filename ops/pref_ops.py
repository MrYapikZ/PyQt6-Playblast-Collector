import bpy

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
try:
    # Prefer the constant from the root package if you defined it there
    from .. import ADDON_ID  # in __init__.py set: ADDON_ID = __name__
except Exception:
    # Fallback to the top-level package name
    ADDON_ID = (__package__.split('.', 1)[0] if __package__
                else __name__.split('.', 1)[0])

def get_prefs():
    addons = bpy.context.preferences.addons
    mod = addons.get(ADDON_ID) or addons.get(ADDON_ID.lower())
    return mod.preferences if mod else None

# ------------------------------------------------------------
# Operators (Add/Remove/Reorder)
# ------------------------------------------------------------

class PREF_OT_project_add(bpy.types.Operator):
    bl_idname = "prefs_ops.project_add"
    bl_label = "Add Project"
    bl_options = {'INTERNAL', 'REGISTER'}

    def execute(self, context):
        prefs = get_prefs()
        it = prefs.projects.add()
        it.code = "K"
        it.label = "Jagat"
        it.tooltip = "Jagat Project"
        prefs.projects_index = len(prefs.projects) - 1
        return {'FINISHED'}

class PREF_OT_project_remove(bpy.types.Operator):
    bl_idname = "prefs_ops.project_remove"
    bl_label = "Remove Project"
    bl_options = {'INTERNAL', 'REGISTER'}

    def execute(self, context):
        prefs = get_prefs()
        idx = prefs.projects_index
        if 0 <= idx < len(prefs.projects):
            prefs.projects.remove(idx)
            prefs.projects_index = max(0, idx - 1)
        return {'FINISHED'}

class PREF_OT_project_move(bpy.types.Operator):
    bl_idname = "prefs_ops.project_move"
    bl_label = "Move Project"
    bl_options = {'INTERNAL', 'REGISTER'}

    direction: bpy.props.EnumProperty(
        items=[('UP', "Up", ""), ('DOWN', "Down", "")]
    )

    def execute(self, context):
        prefs = get_prefs()
        idx = prefs.projects_index
        if self.direction == 'UP' and idx > 0:
            prefs.projects.move(idx, idx - 1)
            prefs.projects_index -= 1
        elif self.direction == 'DOWN' and idx < len(prefs.projects) - 1:
            prefs.projects.move(idx, idx + 1)
            prefs.projects_index += 1
        return {'FINISHED'}

def register():
    bpy.utils.register_class(PREF_OT_project_add)
    bpy.utils.register_class(PREF_OT_project_remove)
    bpy.utils.register_class(PREF_OT_project_move)
def unregister():
    bpy.utils.unregister_class(PREF_OT_project_add)
    bpy.utils.unregister_class(PREF_OT_project_remove)
    bpy.utils.unregister_class(PREF_OT_project_move)