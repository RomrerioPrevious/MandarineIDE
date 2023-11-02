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
