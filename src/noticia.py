from abc import abstractmethod
import csv

class Noticia:
    
    Ocio = "ocio"
    Policial = "policiales"
    Deporte = "deportes"
    Ciudad = "ciudad"
    Tecnologia = "tecnologia"
    Politica = "politica"
    Educacion = "educacion"
    
    def __init__(self, url : str, titulo : str, contenido : str, seccion : str) -> None:
        self.url = url
        self.secciontxt = seccion
        self.contenido = contenido
        self.titulo = titulo