import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

df=pd.read_csv("Branko_Jankovic_Task3/data/products.csv")

#sklanjanje vodecih ili zavrsnih razmaka
df.columns = df.columns.str.strip()

#brisanje nedostajucih vrednosti
df=df.dropna()

# Zamena vrednosti
df["Category Label"] = df["Category Label"].replace("fridge", "Fridges").replace("CPU","CPUs").replace("Mobile Phone","Mobile Phones")

# Kolone koje nisu potrebne
df = df.drop(columns=[
    "product ID",
    "Merchant ID",
    "_Product Code",
    "Number_of_Views",
    "Merchant Rating",
    "Listing Date"
])

X = df["Product Title"]
y = df["Category Label"]


# Pipeline: tekst -> TF-IDF -> Linear SVM
final_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("svc", LinearSVC())
])

# Treniranje finalnog modela na kompletnom trening skupu
final_model.fit(X, y)

# Čuvanje modela i vektorizatora
joblib.dump(final_model, "model/final_linear_svm_model.pkl")

print("Sačuvan fajl: final_linear_svm_model.pkl")