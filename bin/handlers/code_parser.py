class CodeParser:
    def __init__(self, path: str):
        self.path = path

    def parse_code(self):
        with open(self.path, mode="r", encoding="UTF8") as file:
            line = file.readline()

