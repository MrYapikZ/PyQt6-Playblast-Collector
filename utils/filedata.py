import bpy
from pathlib import Path

def split_blend_filepath(fp: str | None = None) -> tuple[str, str, str, str]:
    """
    Split a .blend filepath into:
      dir (folder), filename (with ext), name (no ext), ext (with dot).
    Falls back to 'Untitled.blend' if the file hasn't been saved yet.
    """
    if fp is None:
        fp = bpy.data.filepath or ""

    if not fp:
        return ("", "Untitled.blend", "Untitled", ".blend")

    p = Path(fp)
    return (str(p.parent), p.name, p.stem, p.suffix)