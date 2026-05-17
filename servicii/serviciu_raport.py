from typing import Dict, Any
from collections import defaultdict

from modele.produs import Produs
from repository.repository_produse import RepositoryProduse


class ServiciuRaport:
    """
    Clasă responsabilă pentru generarea rapoartelor
    privind produsele magazinului beauty.
    """

    def __init__(self, repository: RepositoryProduse) -> None:
        """
        Inițializează serviciul de raportare.

        Args:
            repository (RepositoryProduse):
                Repository pentru accesarea produselor.
        """
        self.repository: RepositoryProduse = repository

    def genereaza_raport(self) -> Dict[str, Any]:
        """
        Generează statistici despre produsele magazinului.

        Statistici generate:
        - număr total produse
        - valoare totală stoc
        - preț mediu produse
        - cel mai scump produs
        - produse fără stoc
        - număr produse pe categorii

        Returns:
            Dict[str, Any]:
                Dicționar ce conține raportul complet.
        """
        produse: list[Produs] = self.repository.obtine_produse()

        # Număr total produse
        total: int = len(produse)

        # Valoare totală stoc
        valoare_totala: float = sum(
            produs.pret * produs.stoc
            for produs in produse
        )

        # Preț mediu produse
        pret_mediu: float = (
            sum(produs.pret for produs in produse) / total
            if total else 0
        )

        # Cel mai scump produs
        produs_scump: Produs | None = max(
            produse,
            key=lambda produs: produs.pret,
            default=None
        )

        # Produse fără stoc
        produse_fara_stoc: list[Produs] = [
            produs
            for produs in produse
            if produs.stoc == 0
        ]

        # Produse grupate pe categorii
        categorii: defaultdict[str, int] = defaultdict(int)

        for produs in produse:
            categorii[produs.categorie] += 1

        # Returnare raport final
        return {
            "total_produse": total,
            "valoare_totala": round(valoare_totala, 2),
            "pret_mediu": round(pret_mediu, 2),
            "produs_scump": produs_scump,
            "produse_fara_stoc": produse_fara_stoc,
            "categorii": dict(categorii)
        }