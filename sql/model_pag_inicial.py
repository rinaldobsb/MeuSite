import sqlite3
from datetime import date
from typing import Any, Callable, Dict, List


class ModelProjects:
    name: str

    def __init__(self, db_file: str, model_name: str = 'Página Inicial') -> None:
        self.name = model_name
        self.connector = sqlite3.connect(db_file)
        self.cursor = self.connector.cursor()
        self.connector.row_factory = self.dict_factory
    
    @staticmethod
    def dict_factory(cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    @staticmethod
    def commit_and_close(instance_function: Callable) -> Callable:
        def wrapper(self, *args, **kargs) -> Any:
            res: Any = instance_function(self, *args, **kargs)
            self.connector.commit()
            self.connector.close()
            return res
        return wrapper
    
    def __str__(self) -> str:
        return f"Model: {self.name}"

    # funções do ADM    
    @commit_and_close
    def insert_project(self, project: Dict) -> bool:
        return False
    
    @commit_and_close
    def delete_project(self, id=None, project_name=None) -> bool:
        return False

    @commit_and_close
    def edit_project(self, id=None, project_name=None) -> bool:
        return False
    
    # funções de consulta
    @commit_and_close
    def retrive_all_projects(self) -> List[Dict]:
        res = self.connector.execute('SELECT * FROM projetos;').fetchall()
        return res

    @commit_and_close
    def retrive_one_project(self, id=None, project_name=None) -> Dict:
        if id:
            res = self.connector.execute(f'SELECT * FROM projetos WHERE id = {id};').fetchone()
        elif project_name:
            res = self.connector.execute(f"SELECT * FROM projetos WHERE nome_projeto LIKE '%{project_name}%';").fetchone()
        return res

    @commit_and_close
    def return_3_projects(self) -> List[Dict]:
        res = self.connector.execute('SELECT * FROM projetos;').fetchall()
        return res[:3]



class ModelBlog:
    name: str

    def __init__(self, db_file: str, model_name: str = 'Blog') -> None:
        self.name = model_name
        self.connector = sqlite3.connect(db_file)
        self.cursor = self.connector.cursor()
        self.connector.row_factory = self.dict_factory
    
    @staticmethod
    def dict_factory(cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    @staticmethod
    def commit_and_close(instance_function: Callable) -> Callable:
        def wrapper(self, *args, **kargs) -> Any:
            res: Any = instance_function(self, *args, **kargs)
            self.connector.commit()
            self.connector.close()
            return res
        return wrapper
    
    def __str__(self) -> str:
        return f"Model: {self.name}"

    # funções do ADM    
    @commit_and_close
    def insert_project(self, project: Dict) -> bool:
        return False
    
    @commit_and_close
    def delete_project(self, id=None, project_name=None) -> bool:
        return False

    @commit_and_close
    def edit_project(self, id=None, project_name=None) -> bool:
        return False
    
    # funções de consulta
    @commit_and_close
    def retrive_all_posts(self) -> List[Dict]:
        res = self.connector.execute('SELECT * FROM blog;').fetchall()
        return res

    @commit_and_close
    def retrive_one_post(self, id=None, post_name=None) -> Dict:
        if id:
            res = self.connector.execute(f'SELECT * FROM blog WHERE id = {id};').fetchone()
        elif post_name:
            res = self.connector.execute(f"SELECT * FROM blog WHERE titulo_post LIKE '%{post_name}%';").fetchone()
        return res

    @commit_and_close
    def return_3_post(self) -> List[Dict]:
        res = self.connector.execute('SELECT * FROM blog;').fetchall()
        return res[:3]