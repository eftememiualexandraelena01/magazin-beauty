Magazin Beauty

Descriere proiect

Aplicație web pentru gestionarea produselor unui magazin beauty, realizată în Python folosind Flask și SQLite.

Proiectul permite:

adăugare produse
afișare produse
editare produse
ștergere produse
căutare produse
filtrare și sortare
generare raport magazin


Tehnologii utilizate:
Python 3
Flask
SQLite3
HTML5
CSS3
Bootstrap
Jinja2

Structura proiectului
MAGAZIN_BEAUTY/
│
├── baza_date/
│   └── baza_date.py
│
├── modele/
│   └── produs.py
│
├── repository/
│   └── repository_produse.py
│
├── servicii/
│   └── serviciu_raport.py
│
├── static/
│   └── stil.css
│
├── templates/
│   ├── index.html
│   ├── adauga_produs.html
│   ├── editeaza_produs.html
│   └── raport.html
│
├── aplicatie.py
├── lista_produse.csv
├── magazin_beauty.db
└── README.md

Funcționalități
CRUD
Create
Read
Update
Delete
Filtrare și sortare
sortare după nume
sortare după preț
produse în stoc
filtrare după categorie
căutare după nume / brand / categorie

Raport magazin
număr total produse
valoare totală stoc
produs cel mai scump
produse fără stoc
preț mediu produse
produse pe categorii

Instalare și rulare

1. Clonarea proiectului
git clone <link-repository>
cd MAGAZIN_BEAUTY
2. Crearea mediului virtual
python 
3. Activarea mediului virtual
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate

5. Instalarea dependențelor
pip install

7. Pornirea aplicației
python aplicatie.py

Aplicația va fi disponibilă la adresa:

http://127.0.0.1:5000/

Baza de date

Aplicația utilizează SQLite prin fișierul:


Exemple de pagini
Pagina principală — listă produse
Formular adăugare produs
Formular editare produs
Raport produse
Autor

Proiect realizat pentru gestionarea unui magazin beauty folosind arhitectură modulară în Flask.

