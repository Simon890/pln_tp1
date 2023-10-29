from src.deporte import *
from src.noticias_collection import *
from src.clasificador import Clasificador
from src.programa import Programa
from src.lanacion import LaNacion
from src.env import env

if __name__ == "__main__":
    pais = LaNacion()
    noticias_dep = pais.generar_noticias(Noticia.Deporte)
    noticias_politica = pais.generar_noticias(Noticia.Politica)
    noticias_tecno = pais.generar_noticias(Noticia.Tecnologia)
    noticias_educacion = pais.generar_noticias(Noticia.Educacion)
    
    (noticias_dep + noticias_politica + noticias_tecno + noticias_educacion).to_csv(env("CSV_PATH"))
    clasificador = Clasificador(env("CSV_PATH"))
    clasificador.entrenar()
    clasificador.graficar_wordcloud()
    clasificador.similitud_titulos()
    programa = Programa(clasificador, env("OUTPUT"))
    programa.ejecutar()