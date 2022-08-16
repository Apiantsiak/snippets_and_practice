"""This module allows use context manager with mysql connector"""

import mysql.connector


class DBConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDataBase:

    def __init__(self, config: dict) -> None:
        self._config = config

    @property
    def get_config(self):
        return self._config

    def __enter__(self) -> "cursor":
        try:
            self.conn = mysql.connector.connect(**self.get_config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise DBConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)


if __name__ == "__main__":

    dbconfig = {"host": "127.0.0.1",
                "user": "avp",
                "password": "153624",
                "database": "subnet_logDB",
                }

    subnet_log_db = UseDataBase(dbconfig)

    with subnet_log_db as cursor:
        _SQL = """show tables"""
        cursor.execute(_SQL)
        data_db = cursor.fetchall()

        for line in data_db:
            print(line)
