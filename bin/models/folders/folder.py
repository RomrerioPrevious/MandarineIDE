from dataclasses import dataclass
from bin.models.folders.file import File


@dataclass
class Folder:
    files: [File]
    folders: []
    name: str
    path: str
