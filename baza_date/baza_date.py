import sqlite3
from sqlite3 import Connection


class BazaDate:
    """
    Clasă responsabilă pentru gestionarea conexiunii
    la baza de date SQLite.
    """

    def __init__(self, nume_db: str) -> None:
        """
        Inițializează baza de date.

        Args:
            nume_db (str):
                Numele fișierului SQLite.
        """
        self.nume_db: str = nume_db

    def conectare(self) -> Connection:
        """
        Creează conexiunea către baza de date SQLite.

        Returns:
            Connection:
                Conexiune activă SQLite.
        """
        conn: Connection = sqlite3.connect(self.nume_db)

        # Permite accesarea coloanelor după nume
        conn.row_factory = sqlite3.Row

        return conn