class File:
    def __init__(self, path, filename: str):
        self.path = path
        self.name = filename.split(".")[0]
        self.type = filename.split(".")[1]

