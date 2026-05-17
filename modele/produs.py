from dataclasses import dataclass
from typing import Optional


@dataclass
class Produs:
    """
    Model de date pentru un produs din magazinul beauty.

    Attributes:
        id_produs (Optional[int]):
            ID-ul unic al produsului din baza de date.

        nume (str):
            Numele produsului.

        brand (str):
            Brandul produsului.

        categorie (str):
            Categoria produsului
            (ex: Makeup, Skincare, Haircare).

        pret (float):
            Prețul produsului.

        stoc (int):
            Cantitatea disponibilă în stoc.
    """

    id_produs: Optional[int] = None
    nume: str = ""
    brand: str = ""
    categorie: str = ""
    pret: float = 0.0
    stoc: int = 0