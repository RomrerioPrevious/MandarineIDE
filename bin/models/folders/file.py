from dataclasses import dataclass


@dataclass
class File:
    file_name: str
    file_place: str

    def __str__(self):
        return self.file_name
