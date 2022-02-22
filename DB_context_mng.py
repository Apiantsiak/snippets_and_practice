

import mysql.connector


class UseDataBase:

    def __init__(self, config: dict) -> None:
        self._config = config

    @property
    def get_config(self):
        return self._config

    def __enter__(self) -> "cursor":
        self.conn = mysql.connector.connect(**self.get_config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


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
