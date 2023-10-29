from src.scrapper import Scrapper
from src.ocio import *
from src.deporte import *
from src.policial import *
from src.noticias_collection import *
from src.clasificador import Clasificador
from src.lanacion import LaNacion
from src.programa import Programa

if __name__ == "__main__":
    # pais = LaNacion()
    # noticias_dep = pais.generar_noticias(Noticia.Deporte)
    # noticias_politica = pais.generar_noticias(Noticia.Politica)
    # noticias_tecno = pais.generar_noticias(Noticia.Tecnologia)
    # noticias_educacion = pais.generar_noticias(Noticia.Educacion)
    
    # (noticias_dep + noticias_politica + noticias_tecno + noticias_educacion).to_csv("lanacion.csv")
    clas = Clasificador("lanacion.csv")
    clas.entrenar()
    # clas.graficar_wordcloud()
    clas.similitud_titulos()
    programa = Programa(clas)
    programa.ejecutar()