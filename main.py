bl_info = {
    "name": "PTP Playblast",
    "description": "Fast viewport playblasts with versioned filenames.",
    "author": "MrYapikZ",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "3D Viewport > N-panel > PTP_Playblast",
    "category": "Render",
}

import bpy
from bpy.types import Panel, Operator, AddonPreferences, PropertyGroup
from bpy.props import (
    StringProperty, BoolProperty, EnumProperty, IntProperty, PointerProperty
)
import os
import re
from datetime import datetime


# ------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------

def ensure_dir(path: str):
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def next_version_path(dirpath: str, basename: str, ext: str) -> str:
    """
    Find next ..._vNNN.ext in dirpath.
    """
    pattern = re.compile(rf"^{re.escape(basename)}_v(\d{{3}}){re.escape(ext)}$")
    max_v = 0
    if os.path.isdir(dirpath):
        for f in os.listdir(dirpath):
            m = pattern.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    nxt = max_v + 1
    return os.path.join(dirpath, f"{basename}_v{nxt:03d}{ext}")


def find_first_3d_view(context):
    # Prefer current area if it's a 3D View
    area = context.area if context.area and context.area.type == 'VIEW_3D' else None
    region = context.region if region_is_window(context) else None
    space = context.space_data if area else None

    if area and space:
        return area, region, space

    # Fallback: scan screen
    for area in context.window.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            return area, region, space
    return None, None, None


def region_is_window(context):
    return context.region and context.region.type == 'WINDOW'


def set_viewport_shading(space_view3d, shading_type: str):
    # Map our enum to Blender shading types
    target = {
        'RENDERED': 'RENDERED',
        'MATERIAL': 'MATERIAL',
        'SOLID': 'SOLID',
        'WIREFRAME': 'WIREFRAME',
    }[shading_type]
    current = space_view3d.shading.type
    space_view3d.shading.type = target
    return current


# ------------------------------------------------------------------------
# Properties
# ------------------------------------------------------------------------

class PlayblastSettings(PropertyGroup):
    output_dir: StringProperty(
        name="Output Folder",
        subtype='DIR_PATH',
        default="//playblasts"
    )
    base_name: StringProperty(
        name="Base Name",
        description="File base name (version or timestamp appended as needed)",
        default="playblast"
    )
    use_versioning: BoolProperty(
        name="Use Versioning",
        description="Append _v001, _v002, ...",
        default=True
    )
    timestamp_fallback: BoolProperty(
        name="Use Timestamp if exists",
        description="If versioning is off or file exists, append _YYYYMMDD_HHMMSS",
        default=True
    )
    container: EnumProperty(
        name="Output Type",
