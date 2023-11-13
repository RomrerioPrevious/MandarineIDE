# Mandarine IDE

Mandaine IDE is IDE for python.

## How to install

## Credits

- [Roman Vikulin](https://github.com/RomrerioPrevious/)
- [Dmitry Ryazanov](https://github.com/dima117216)

## Librares

- Python (3.10.4)
- PyQT5 (5.15.9)
- dataclass
- subprocess

## Project structure

### Tokens

Tokens is parts of python code.

#### Token

A token is a class that stores python words

```python
@dataclass
class Token:
    name: str
    type: TokenType

    def __hash__(self):
        return self.name.__hash__()
```

#### TokenType

TokenType is class that stores standart type of token.

```python
@dataclass
class TokenType:
    name: str
    words: [str]

    def __eq__(self, other):
        if not isinstance(other, TokenType):
            raise TypeError(f"Type of object {other} is not TokenType")
        return other.name == self.name
```

#### TokenTypeList

TokenTypeList is list of all python types.

| TYPE NAME          |                              Condition                               |
| ------------------ | :------------------------------------------------------------------: |
| Reserved Words     | if word in [list](https://flexiple.com/python/python-reserved-words) |
| Comparisons        |                      if word is comparison sign                      |
| Special characters |                    if word is special characters                     |
| Function           |                if word is two positions back is "def"                |
| Class              |               if word is two positions back is "class"               |
| Variable           |                         if word none of this                         |

---

### Parsers

Parsers is analyzers of code.

#### Folder parser

Folder parser is tree analyzer of paths.

```python
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
```

#### Code parser

Code parser breaks the python code into tokens for further analysis and text coloring.

```python
def parse_code_from_line(self, line: str) -> [Token]:
     words = CodeParser.split(line)
     tokens = [TokenCreator.token_fabric(words[0])]
     if len(words) != 1:
          tokens.append(TokenCreator.token_fabric(words[1]))
     for i in range(2, len(words), 1):
          word = words[i]
          if words[i - 2] in ["def", "class"]:
               token = TokenCreator.token_fabric(word, words[i - 2])
          else:
               token = TokenCreator.token_fabric(word)
          tokens.append(token)
          if token.type.name in self.scope.keys():
               self.scope[token.type.name].add(token)
     return tokens
```

---

### Options

Options is buttons of options.

#### Project Service

Project service is api for working program with project database.

```python
import sqlite3
from bin.models.projects import Project


class Project_service:
    def __init__(self, path_of_database: str):
        self._connection = sqlite3.connect(path_of_database)
        self._cursor = self._connection.cursor()

    def create(self, project: Project):
        self._cursor.execute("""INSERT INTO projects(name, path)
                                VALUES(?, ?)""",
                             (project.name, project.path))

    def read(self, id: int) -> Project:
        name, path = self._cursor.execute("""SELECT name, path FROM projects
                                WHERE id = ?""",
                                          (id,)).fetchone()
        return Project(id, name, path)

    def read_all(self) -> [Project]:
        result = []
        answer = self._cursor.execute("""SELECT id, name, path
                                        FROM projects""").fetchall()
        for project_var in answer:
            result.append(Project(project_var[0], project_var[1], project_var[2]))
        return result

    def update(self, project: Project):
        self._cursor.execute("""UPDATE projects
                                SET name = ?, path = ?
                                WHERE id = ?""",
                             (project.name, project.path, project.id))

    def delete(self, id: int):
        self._cursor.execute("""DELETE FROM projects
                                WHERE id = ?""",
                             (id,))

    def __del__(self):
        self._connection.commit()
        self._connection.close()
```

#### Runner

Runner is small class who needs for start programm.

```python
from subprocess import call


class Runner:
    def __init__(self, path: str):
        self.path = path

    def run(self):
        call(["python", self.path])
```

---

### Structure of database

| ID  |      NAME      |       PATH        |
| --- | :------------: | :---------------: |
| 1   |  some project  |    D:/project     |
| 2   | second project | D:/second_project |
