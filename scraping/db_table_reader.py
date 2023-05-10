from typing import TypedDict

from psycopg2 import connect
from psycopg2.extras import RealDictCursor


class Options(TypedDict):
    """Options for PostgreSQL data source."""

    # dsn: str
    # schema: str
    tables: list[str]


class DataSource:
    """PostgreSQL data source."""

    def __init__(self, options: Options) -> None:
        self._connection = connect("postgresql://avp:153624@localhost:5432/avp")
        self._cursor = self._connection.cursor(cursor_factory=RealDictCursor)
        self._schema = "public"
        self._tables = iter(options.get("tables"))
        self._current_table = None

    def read(self, n: int = 1000) -> list[dict] | None:
        """
        Read and return data from requested tables.

        Returns `None` when all of the available data has been read.
        """

        if not self._current_table:
            self._current_table = next(self._tables, None)
            if not self._current_table:
                return None

            self._read_table()

        rows = self._read_rows(n)

        if not rows:
            self._current_table = None
            self._close_cursor()
        return rows

    def _read_rows(self, n: int = 1000) -> list[dict]:
        self._execute_query(f"FETCH FORWARD {n} FROM cursor")
        rows = self._cursor.fetchall()
        return [dict(row, __tablename=self._current_table) for row in rows]

    def _read_table(self):
        self._execute_query(
            "DECLARE cursor CURSOR FOR"
            f" SELECT * FROM {self._schema}.{self._current_table}"
        )

    def _execute_query(self, query: str) -> None:
        self._cursor.execute(query)

    def _close_cursor(self) -> None:
        self._execute_query("CLOSE cursor")

    def close(self) -> None:
        """Close cursor and connection."""

        self._close_cursor()
        self._cursor.close()
        self._connection.close()


if __name__ == '__main__':
    res = DataSource({'tables': ["test_1", "test_2"]})

    count = 5
    while count:
        print(res.read())
        count -= 1
