import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
from src.noticia import Noticia
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from gensim.models import KeyedVectors

class Clasificador:
    
    seccion_lookup = {
        Noticia.Deporte: 2,
        Noticia.Tecnologia: 5,
        Noticia.Politica: 6,
        Noticia.Educacion: 7,
        2: Noticia.Deporte,
        5: Noticia.Tecnologia,
        6: Noticia.Politica,
        7: Noticia.Educacion
    }
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        nltk.download("stopwords")
        self.stop_words_esp = stopwords.words("spanish")
        self.vectorizer = TfidfVectorizer(stop_words=self.stop_words_esp)
        self.df = pd.read_csv(filename)
        self.secciones = self.df["seccion"].unique()
        self.lr = LogisticRegression(max_iter=1000)
        self.__transormar_df()
    
    def entrenar(self):
        self.__vectorizar()
    
    def __transormar_df(self):
        self.df["titulo"] = self.df["titulo"].apply(self.__lower_str)
        self.df["contenido"] = self.df["contenido"].apply(self.__lower_str)
        self.df["seccion"] = self.df["seccion"].apply(self.seccion_to_int)
        self.df.drop("url", inplace=True, axis=1)
        
    
    def __lower_str(self, string : str) -> str:
        return string.lower()
    
    def seccion_to_int(self, seccion: str) -> int:
        if seccion in self.seccion_lookup: return self.seccion_lookup[seccion]
        raise Exception(f"Tipo de noticia no soportada: '{seccion}'")
    
    def int_to_seccion(self, nro: int) -> str:
        if nro in self.seccion_lookup: return self.seccion_lookup[nro]
        raise Exception(f"ID de noticia no soportado: '{nro}'")

    def __vectorizar(self):
        print("Entrenando modelo...\n")
        X = self.df.drop(columns=["seccion", "titulo"])
        y = self.df["seccion"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        X_train_vector = self.vectorizer.fit_transform(X_train.values.flatten())
        X_test_vector = self.vectorizer.transform(X_test.values.flatten())
        self.lr.fit(X_train_vector, y_train.values.flatten())
        predicciones = self.lr.predict(X_test_vector)
        print("Métricas:")
        print("###### Accuracy Score #######")
        print(accuracy_score(y_test, predicciones))
        print("\n###### Classification Report ######")
        print(classification_report(y_test, predicciones, zero_division=1))

    def graficar_wordcloud(self):
        for seccion in self.secciones:
            plt.figure()
            seccion_df = self.df[self.df["seccion"] == self.seccion_to_int(seccion)]
            cloud = WordCloud(width=1280, height=720, background_color="white", stopwords=self.stop_words_esp, min_font_size=10).generate(" ".join(seccion_df["contenido"].values.flatten()))
            plt.imshow(cloud)
            plt.axis("off")
            plt.title(f"Sección {seccion.capitalize()}")
            plt.show()
    
    def similitud_titulos(self):
        df_politica = self.df[self.df["seccion"] == self.seccion_to_int(Noticia.Politica)]
        similitud = []
        for titulo1 in df_politica["titulo"].to_numpy()[0:6]:
            titulo1_vec = self.vectorizer.transform([titulo1])
            for titulo2 in df_politica["titulo"].to_numpy()[6:]:
                titulo2_vec = self.vectorizer.transform([titulo2])
                simcos = cosine_similarity(titulo1_vec, titulo2_vec)[0][0]
                similitud.append([titulo1, titulo2, simcos])
        df_cos = pd.DataFrame(similitud, columns=["Titulo 1", "Titulo 2", "Similitud"])
        print("\n###### SIMILITUD DEL COSENO ######")
        print(df_cos.to_string())
        