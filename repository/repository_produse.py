import csv
from typing import List, Optional

from modele.produs import Produs
from baza_date.baza_date import BazaDate


class RepositoryProduse:
    """
    Repository responsabil pentru operațiile CRUD
    asupra produselor din magazinul beauty.
    """

    def __init__(self, baza_date: BazaDate) -> None:
        """
        Inițializează repository-ul de produse.

        Args:
            baza_date (BazaDate):
                Obiect responsabil pentru conexiunea la baza de date.
        """
        self.baza_date: BazaDate = baza_date

    # ---------------- TABEL ----------------
    def creare_tabel(self) -> None:
        """
        Creează tabela 'produse' dacă aceasta nu există.
        """
        with self.baza_date.conectare() as conn:

            conn.execute("""
                CREATE TABLE IF NOT EXISTS produse (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nume TEXT NOT NULL,
                    brand TEXT NOT NULL,
                    categorie TEXT NOT NULL,
                    pret REAL NOT NULL,
                    stoc INTEGER NOT NULL
                )
            """)

    # ---------------- MAPARE ----------------
    def _mapare(self, row) -> Produs:
        """
        Convertește un rând SQL într-un obiect Produs.

        Args:
            row:
                Rând extras din baza de date.

        Returns:
            Produs:
                Obiect de tip Produs.
        """
        return Produs(
            id_produs=row["id"],
            nume=row["nume"],
            brand=row["brand"],
            categorie=row["categorie"],
            pret=row["pret"],
            stoc=row["stoc"]
        )

    # ---------------- GET ALL ----------------
    def obtine_produse(self) -> List[Produs]:
        """
        Returnează toate produsele din baza de date.

        Returns:
            List[Produs]:
                Lista completă de produse.
        """
        with self.baza_date.conectare() as conn:

            rows = conn.execute(
                "SELECT * FROM produse"
            ).fetchall()

            return [self._mapare(row) for row in rows]

    # ---------------- GET BY ID ----------------
    def obtine_produs_dupa_id(
        self,
        id_produs: int
    ) -> Optional[Produs]:
        """
        Returnează produsul corespunzător ID-ului.

        Args:
            id_produs (int):
                ID-ul produsului.

        Returns:
            Optional[Produs]:
                Produsul găsit sau None.
        """
        with self.baza_date.conectare() as conn:

            row = conn.execute(
                """
                SELECT * FROM produse
                WHERE id = ?
                """,
                (id_produs,)
            ).fetchone()

            return self._mapare(row) if row else None

    # ---------------- ADD ----------------
    def adauga_produs(self, produs: Produs) -> None:
        """
        Adaugă un produs nou în baza de date.

        Args:
            produs (Produs):
                Produsul ce trebuie adăugat.
        """
        with self.baza_date.conectare() as conn:

            conn.execute("""
                INSERT INTO produse (
                    nume,
                    brand,
                    categorie,
                    pret,
                    stoc
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                produs.nume,
                produs.brand,
                produs.categorie,
                produs.pret,
                produs.stoc
            ))

    # ---------------- UPDATE ----------------
    def actualizeaza_produs(self, produs: Produs) -> None:
        """
        Actualizează informațiile unui produs existent.

        Args:
            produs (Produs):
                Produsul actualizat.
        """
        with self.baza_date.conectare() as conn:

            conn.execute("""
                UPDATE produse
                SET
                    nume = ?,
                    brand = ?,
                    categorie = ?,
                    pret = ?,
                    stoc = ?
                WHERE id = ?
            """, (
                produs.nume,
                produs.brand,
                produs.categorie,
                produs.pret,
                produs.stoc,
                produs.id_produs
            ))

    # ---------------- DELETE ----------------
    def sterge_produs(self, id_produs: int) -> None:
        """
        Șterge un produs din baza de date.

        Args:
            id_produs (int):
                ID-ul produsului ce trebuie șters.
        """
        with self.baza_date.conectare() as conn:

            conn.execute(
                "DELETE FROM produse WHERE id = ?",
                (id_produs,)
            )

    # ---------------- SEARCH ----------------
    def cauta_produse(self, q: str) -> List[Produs]:
        """
        Caută produse după nume, brand sau categorie.

        Args:
            q (str):
                Textul utilizat pentru căutare.

        Returns:
            List[Produs]:
                Lista produselor găsite.
        """
        with self.baza_date.conectare() as conn:

            rows = conn.execute("""
                SELECT * FROM produse
                WHERE
                    nume LIKE ?
                    OR brand LIKE ?
                    OR categorie LIKE ?
            """, (
                f"%{q}%",
                f"%{q}%",
                f"%{q}%"
            )).fetchall()

            return [self._mapare(row) for row in rows]

    # ---------------- SORT ----------------
    def sorteaza_dupa_nume(self) -> List[Produs]:
        """
        Sortează produsele alfabetic după nume.

        Returns:
            List[Produs]:
                Lista produselor sortate.
        """
        with self.baza_date.conectare() as conn:

            rows = conn.execute("""
                SELECT * FROM produse
                ORDER BY nume ASC
            """).fetchall()

            return [self._mapare(row) for row in rows]

    def sorteaza_dupa_pret(self) -> List[Produs]:
        """
        Sortează produsele descrescător după preț.

        Returns:
            List[Produs]:
                Lista produselor sortate.
        """
        with self.baza_date.conectare() as conn:

            rows = conn.execute("""
                SELECT * FROM produse
                ORDER BY pret DESC
            """).fetchall()

            return [self._mapare(row) for row in rows]

    # ---------------- CSV IMPORT ----------------
    def importa_produse_csv(self, fisier: str) -> None:
        """
        Importă produsele dintr-un fișier CSV.

        Importul se face doar dacă tabela este goală.

        Args:
            fisier (str):
                Calea către fișierul CSV.
        """
        with self.baza_date.conectare() as conn:

            count: int = conn.execute(
                "SELECT COUNT(*) FROM produse"
            ).fetchone()[0]

            # Dacă există deja produse,
            # importul nu mai este necesar
            if count > 0:
                return

        with open(
            fisier,
            newline="",
            encoding="utf-8"
        ) as fisier_csv:

            reader = csv.DictReader(fisier_csv)

            for row in reader:

                produs = Produs(
                    nume=row["nume"],
                    brand=row["brand"],
                    categorie=row["categorie"],
                    pret=float(row["pret"]),
                    stoc=int(row["stoc"])
                )

                self.adauga_produs(produs)