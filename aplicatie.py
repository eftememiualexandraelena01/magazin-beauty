from flask import Flask, render_template, request, redirect, Response
from baza_date.baza_date import BazaDate
from repository.repository_produse import RepositoryProduse
from servicii.serviciu_raport import ServiciuRaport
from modele.produs import Produs

app = Flask(__name__)

db = BazaDate("magazin_beauty.db")
repo = RepositoryProduse(db)

repo.creare_tabel()
repo.importa_produse_csv("lista_produse.csv")

raport_service = ServiciuRaport(repo)


# ---------------- HOME ----------------
@app.route("/")
def home() -> str:
    """
    Afișează pagina principală cu lista produselor.

    Funcționalități:
    - căutare produse
    - sortare după nume
    - sortare după preț

    Returns:
        str: Pagina HTML randată.
    """
    filtru: str | None = request.args.get("filtru")
    q: str | None = request.args.get("q")

    if q:
        produse = repo.cauta_produse(q)
    elif filtru == "nume":
        produse = repo.sorteaza_dupa_nume()
    elif filtru == "pret":
        produse = repo.sorteaza_dupa_pret()
    else:
        produse = repo.obtine_produse()

    return render_template("index.html", produse=produse)


# ---------------- ADD ----------------
@app.route("/adauga", methods=["GET", "POST"])
def adauga() -> str | Response:
    """
    Adaugă un produs nou în baza de date.

    Returns:
        str | Response:
            - formular HTML pentru metoda GET
            - redirect către pagina principală pentru metoda POST
    """
    if request.method == "POST":
        produs = Produs(
            nume=request.form["nume"],
            brand=request.form["brand"],
            categorie=request.form["categorie"],
            pret=float(request.form["pret"]),
            stoc=int(request.form["stoc"])
        )

        repo.adauga_produs(produs)

        return redirect("/")

    return render_template("adauga_produs.html")


# ---------------- EDIT ----------------
@app.route("/editeaza/<int:id>", methods=["GET", "POST"])
def edit(id: int) -> str | Response:
    """
    Editează un produs existent.

    Args:
        id (int): ID-ul produsului.

    Returns:
        str | Response:
            - formular HTML cu datele produsului
            - redirect după actualizare
    """
    if request.method == "POST":
        produs_actualizat = Produs(
            id_produs=id,
            nume=request.form["nume"],
            brand=request.form["brand"],
            categorie=request.form["categorie"],
            pret=float(request.form["pret"]),
            stoc=int(request.form["stoc"])
        )

        repo.actualizeaza_produs(produs_actualizat)

        return redirect("/")

    produs = repo.obtine_produs_dupa_id(id)

    return render_template(
        "editeaza_produs.html",
        produs=produs
    )


# ---------------- UPDATE ----------------
@app.route("/update/<int:id>", methods=["POST"])
def update(id: int) -> Response:
    """
    Actualizează informațiile unui produs.

    Args:
        id (int): ID-ul produsului.

    Returns:
        Response: Redirect către pagina principală.
    """
    produs_actualizat = Produs(
        id_produs=id,
        nume=request.form["nume"],
        brand=request.form["brand"],
        categorie=request.form["categorie"],
        pret=float(request.form["pret"]),
        stoc=int(request.form["stoc"])
    )

    repo.actualizeaza_produs(produs_actualizat)

    return redirect("/")


# ---------------- DELETE ----------------
@app.route("/sterge/<int:id>")
def sterge(id: int) -> Response:
    """
    Șterge un produs din baza de date.

    Args:
        id (int): ID-ul produsului.

    Returns:
        Response: Redirect către pagina principală.
    """
    repo.sterge_produs(id)

    return redirect("/")


# ---------------- RAPORT ----------------
@app.route("/raport")
def raport() -> str:
    """
    Generează și afișează raportul magazinului.

    Returns:
        str: Pagina HTML cu raportul.
    """
    return render_template(
        "raport.html",
        raport=raport_service.genereaza_raport()
    )


if __name__ == "__main__":
    """
    Punctul de intrare al aplicației Flask.
    """
    app.run(debug=True)