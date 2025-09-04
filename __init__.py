bl_info = {
    "name": "PTP Playblast",
    "description": "Fast viewport playblasts with versioned filenames.",
    "author": "MrYapikZ",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > PTP_Playblast",
    "category": "Render",
}

import bpy
from . import ui, ops, pref, presets


ADDON_ID = __name__

# ------------------------------------------------------------------------
# Register
# ------------------------------------------------------------------------

modules = [
    pref,
    ops,
    presets,
    ui,
]


def register():
    for item in modules:
        item.register()


def unregister():
    for item in modules:
        item.unregister()
