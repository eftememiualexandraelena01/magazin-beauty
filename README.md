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
export produse în format CSV
Tehnologii utilizate
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
├── requirements.txt
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
python -m venv venv
3. Activarea mediului virtual
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
4. Instalarea dependențelor
pip install -r requirements.txt
5. Pornirea aplicației
python aplicatie.py

Aplicația va fi disponibilă la adresa:


Baza de date

Aplicația utilizează SQLite prin fișierul:

magazin_beauty.db
Exemple de pagini
Pagina principală — listă produse
Formular adăugare produs
Formular editare produs
Raport produse
Autor

Proiect realizat pentru gestionarea unui magazin beauty folosind arhitectură modulară în Flask.

Am combinat cele două versiuni într-un README complet și organizat, păstrând:

descrierea proiectului
funcționalitățile CRUD
filtrarea și sortarea
raportul magazinului
structura proiectului
pașii de instalare și rulare
tehnologiile utilizate
informațiile despre baza de date și CSV