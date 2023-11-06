from subprocess import call


class Runner:
    def __init__(self, path: str):
        self.path = path

    def run(self):
        call(["python", self.path])
