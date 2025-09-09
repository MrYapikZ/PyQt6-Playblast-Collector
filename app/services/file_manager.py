import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

class FileManager:
    def __init__(self, root_path, file_extension=None):
        self.root = Path(root_path)
        self.file_extension = file_extension

    def scan(self):
        # if not self.root.exists() or not self.root.is_dir():
        #     raise ValueError(f"The path {self.root} is not a valid directory.")
        #
        # if self.file_extension:  # filter by extension
        #     files = list(self.root.rglob(f"*.{self.file_extension}"))
        # else:  # no extension filter → get all files
        #     files = list(self.root.rglob("*"))
        #
        #     for file in files:
        #         print(file)

        # build three parallel lists
        # full_paths = [str(f.resolve()) for f in files]
        # folders = [str(f.parent) for f in files]
        # names = [f.name for f in files]
        #
        # return full_paths, folders, names
        # return [(str(f.resolve()), str(f.parent), f.name) for f in files if f.is_file()]
        if not self.root.exists() or not self.root.is_dir():
            raise ValueError(f"The path {self.root} is not a valid directory.")

            # gather files
        if self.file_extension:
            files = list(self.root.rglob(f"*.{self.file_extension}"))
        else:
            files = list(self.root.rglob("*"))

            # regex: capture show/ep/seq/shot/div/version
        pat = re.compile(
            r"^(?P<show>[a-z0-9]+)_ep(?P<ep>\d+)_sq(?P<seq>\d+)_sh(?P<shot>\d+)_(?P<div>[a-z]+)_v(?P<ver>\d+)\.\w+$",
            re.IGNORECASE
        )

        grouped = defaultdict(list)

        for f in files:
            if not f.is_file():
                continue
            m = pat.match(f.name)
            if not m:
                continue

            key = (
                m.group("ep"),
                m.group("seq"),
                m.group("shot"),
                m.group("div").lower()
            )
            ver = int(m.group("ver"))
            grouped[key].append((ver, f))

        # pick latest version per group
        latest = {}
        for key, versions in grouped.items():
            latest[key] = max(versions, key=lambda x: x[0])[1]  # keep file with max version

        print(latest)

        return latest

    import shutil
    from pathlib import Path

    def copy_file(self, src: str, destination: str, division: str) -> str:
        """
        Copy one file to the destination directory.

        Args:
            src: path to the source file
            destination: target directory (created if missing)

        Returns:
            Full path of the copied file in the destination
        """
        src_path = Path(src)
        dest_dir = Path(destination)

        if not src_path.is_file():
            raise FileNotFoundError(f"Source file not found: {src_path}")

        # dest_dir.mkdir(parents=True, exist_ok=True)
        if not dest_dir.exists():
            return "NOT_EXIST"

        dest_dir = dest_dir / division
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest_path = dest_dir / src_path.name
        shutil.copy2(src_path, dest_path)

        return str(dest_path)
