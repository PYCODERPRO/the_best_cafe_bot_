import sqlite3

class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data.cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None,language:str = 'uz'):

        sql = """
        INSERT INTO users (id, Name, email, language) VALUES(?, ?, ?, ?)
        """

        self.execute(sql, parameters=(id, name, email, language),commit=True)

    def select_all_user(self):
        sql = """
        SELECT * FROM users
        """
        return  self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):

        sql = "SELECT * FROM users WHERE"
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE")

def logger(statement):
    print(f"""
    ____________________________________
    Executing:
    {statement}
    ____________________________________
""")






















