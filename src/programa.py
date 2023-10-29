from src.clasificador import Clasificador
from src.noticia import Noticia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

class Programa:
    def __init__(self, clasificador : Clasificador) -> None:
        self.c = clasificador
        nltk.download("punkt")
    
    def ejecutar(self):
        while True:
            opc = input("Elija una opción:\n1)Política\n2)Tecnología\n3)Educación\n4)Deporte\n5)Salir\n")
            if opc not in ["1", "2", "3", "4", "5"]:
                print("Opción no válida")
                continue
            
            if opc == "5":
                break
            
            if opc == "1":
                print(self.__resumir(self.__get_contenido(Noticia.Politica)))
                continue
            if opc == "2":
                print(self.__resumir(self.__get_contenido(Noticia.Tecnologia)))
                continue
            if opc == "3":
                print(self.__resumir(self.__get_contenido(Noticia.Educacion)))
                continue
            if opc == "4":
                print(self.__resumir(self.__get_contenido(Noticia.Deporte)))
            
    
    def __resumir(self, data):
        res = ""
        for i, texto in enumerate(data[1]):
            res += f"\nNoticia '{data[0][i].upper()}': "
            parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
            sum = LsaSummarizer()
            resumen = sum(parser.document, 3)
            for frase in resumen:
                res += " " + str(frase).capitalize()
            res += "\n"
        return res
    
    def __get_contenido(self, seccion):
        df_data = self.c.df[self.c.df["seccion"] == self.c.seccion_lookup[seccion]]
        return df_data["titulo"].values, df_data["contenido"].values