from bin.models.folders import *
import os


class Folder_parser:
    @staticmethod
    def check_folder(root_dir: str) -> Folder:
        folder = Folder(files=[], folders=[], name=os.path.basename(root_dir), path=root_dir)
        for file in os.listdir(root_dir):
            direction = os.path.join(root_dir, file)
            if os.path.isfile(direction):
                file = File(os.path.basename(direction), os.path.dirname(direction))
                folder.files.append(file)
            elif os.path.isdir(direction):
                temp = Folder_parser.check_folder(direction)
                folder.folders.append(temp)
        return folder
