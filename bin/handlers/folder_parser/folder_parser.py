from bin.models.folders import *
import os


class Folder_parser:
    @staticmethod
    def check_folder(rootdir):
        folder = Folder(files=[], folders=[], name=os.path.basename(rootdir))
        for file in os.listdir(rootdir):
            direction = os.path.join(rootdir, file)
            if os.path.isfile(direction):
                file = File(os.path.basename(direction), os.path.dirname(direction))
                folder.files.append(file)
            elif os.path.isdir(direction):
                temp = Folder_parser.check_folder(direction)
                folder.folders.append(temp)
        return folder
