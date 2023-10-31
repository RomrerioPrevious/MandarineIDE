from dataclasses import dataclass
from bin.models.folders.file import File


@dataclass
class Folder:
    files: [File]
    folders: []
    name: str

    def __str__(self):
        return f"Folder(name={self.name}, folders={self.folders}, files={self.files})"
