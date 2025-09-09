import os
import shutil
from pathlib import Path

class FileManager:
    def __init__(self, root_path, file_extension=None):
        self.root = Path(root_path)
        self.file_extension = file_extension

    def scan(self):
        if not self.root.exists() or not self.root.is_dir():
            raise ValueError(f"The path {self.root} is not a valid directory.")

        if self.file_extension:  # filter by extension
            files = list(self.root.rglob(f"*.{self.file_extension}"))
        else:  # no extension filter → get all files
            files = list(self.root.rglob("*"))

            for file in files:
                print(file)

        # build three parallel lists
        # full_paths = [str(f.resolve()) for f in files]
        # folders = [str(f.parent) for f in files]
        # names = [f.name for f in files]
        #
        # return full_paths, folders, names
        return [(str(f.resolve()), str(f.parent), f.name) for f in files if f.is_file()]

    import shutil
    from pathlib import Path

    def copy_file(self, src: str, destination: str) -> str:
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

        dest_path = dest_dir / src_path.name
        shutil.copy2(src_path, dest_path)

        return str(dest_path)
