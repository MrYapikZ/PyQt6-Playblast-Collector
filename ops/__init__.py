from . import pref_ops, nav_ops

def register():
    pref_ops.register()
    nav_ops.register()
def unregister():
    pref_ops.unregister()
    nav_ops.unregister()