# Klasifikacija proizvoda pomocu Linear SVM modela

## Opis projekta

Ovaj projekat predstavlja sistem za automatsku klasifikaciju proizvoda na osnovu njihovog naslova.

Za klasifikaciju je koriscen Linear Support Vector Machine (Linear SVM) model. Tekstualni podaci se prethodno pretvaraju u numericku reprezentaciju pomocu TF-IDF metode.

Tokom razvoja testirano je vise klasifikacionih algoritama, a kao finalno resenje izabran je model koji je ostvario najbolje rezultate na test skupu.

Finalni model je sacuvan u .pkl formatu i moze se koristiti za predvidjanje kategorije novih proizvoda bez ponovnog treniranja.

Struktura projekta
projekat/
│
├── model/
│   └── final_linear_svm_model.pkl
│
├── predict_category.py
│
├── train_model.py
│
├── requirements.txt
│
└── README.md

## Opis fajlova

train_model.py - treniranje i cuvanje finalnog modela
predict_category.py - ucitavanje modela i interaktivno testiranje
model/final_linear_svm_model.pkl - sacuvani finalni Linear SVM model
README.md - uputstvo za instalaciju i korišćenje projekta

1. Zahtevi

Za pokretanje projekta potrebno je imati instaliran:

Python 3.x
pip
Git (opciono, za preuzimanje projekta)

Korišćene Python biblioteke:

pandas
scikit-learn
joblib

2. Instalacija biblioteka

Otvorite terminal u glavnom folderu projekta i pokrenite:

pip install pandas scikit-learn joblib

Ukoliko postoji fajl requirements.txt, sve biblioteke mogu se instalirati jednom komandom:

pip install -r requirements.txt

3. Provera modela

Pre pokretanja programa proverite da li postoji fajl:

model/final_linear_svm_model.pkl

Struktura mora biti:

model/
└── final_linear_svm_model.pkl

Ako model ne postoji, potrebno je prvo pokrenuti skriptu za treniranje:

python train_model.py

Nakon uspesnog treniranja model ce biti sačuvan u:

model/final_linear_svm_model.pkl

4. Pokretanje programa

Za pokretanje interaktivne klasifikacije koristite:

python predict_category.py

Program ce ucitati prethodno sacuvani model i zatraziti unos naslova proizvoda.

Primer:

===================================
   KLASIFIKACIJA PROIZVODA
===================================

Naslov proizvoda: iphone 7 32gb gold,4,3,Apple iPhone 7 32GB
Predviđena kategorija: Mobile Phones

Program omogucava unos vise proizvoda.

Za zavrsetak programa unesite:
exit

5. Testiranje modela

Model se moze testirati unosom razlicitih naslova proizvoda.

Na primer:

Naslov proizvoda: iphone 7 32gb gold,4,3,Apple iPhone 7 32GB
Predvidjena kategorija: Mobile Phones

Drugi primer:

Naslov proizvoda: olympus e m10 mark iii geh use silber
Predviđena kategorija: Digital Cameras

Treba imati u vidu da model moze napraviti pogresnu klasifikaciju za proizvode ciji naslov nije dovoljno slican podacima iz trening skupa.

6. Kako model radi?

Proces klasifikacije odvija se u nekoliko koraka:

Naslov proizvoda
       ↓
   TF-IDF
       ↓
  Linear SVM
       ↓
Predviđena kategorija
TF-IDF

TF-IDF pretvara tekst naslova proizvoda u numericke karakteristike koje model moze da obradi.

Linear SVM

Linear SVM koristi dobijene karakteristike za odredjivanje kategorije proizvoda.

7. Treniranje modela

Tokom razvoja projekta testirano je vise klasifikacionih algoritama.

Modeli su uporedjeni pomocu metrika kao sto su:

Accuracy
Precision
Recall
F1-score

Na osnovu rezultata izabran je najbolji model.

Finalni model je zatim ponovo treniran i sacuvan pomocu biblioteke joblib.

Primer cuvanja modela:

import joblib
import os

os.makedirs("model", exist_ok=True)

joblib.dump(
    final_model,
    "model/final_linear_svm_model.pkl"
)

8. Ucitavanje modela

Sacuvani model se ucitava pomocu:

import joblib

model = joblib.load(
    "model/final_linear_svm_model.pkl"
)

Nakon toga se moze koristiti za predikciju:

prediction = model.predict([title])

print(prediction)

9. Napomena o rezultatima

Predikcija zavisi od podataka na kojima je model treniran.

Na primer, za naslov:

Bosch Serie 4 KGV39VL31G

model je vratio:

Dishwashers

Ovaj rezultat predstavlja primer pogresne klasifikacije, jer se navedeni proizvod odnosi na frižider sa zamrzivačem.

Takvi rezultati pokazuju da model moze napraviti gresku na novim proizvodima koji nisu dovoljno zastupljeni ili ciji tekstualni opis nije dovoljno karakteristican u trening skupu.

10. GitHub

Projekat se moze sacuvati i podeliti preko GitHub-a.

Nakon kreiranja ili izmene fajlova:

git add .

Napravite commit:

git commit -m "Add product classification project"

Posaljite izmene na GitHub:

git push origin main

11. Brzo pokretanje

Ako je projekat vec preuzet i model postoji, dovoljno je:

pip install -r requirements.txt
python predict_category.py

Zatim unesite naslov proizvoda:

Naslov proizvoda: Bosch Serie 4 KGV39VL31G

Model će prikazati predviđenu kategoriju.

## Zakljucak

Projekat omogucava automatsku klasifikaciju proizvoda na osnovu njihovih naslova koriscenjem TF-IDF reprezentacije i Linear SVM klasifikatora.

Finalni model je sacuvan u .pkl formatu i može se jednostavno ucitati i koristiti za klasifikaciju novih proizvoda.
