from abc import abstractmethod
from src.noticia import Noticia
from src.deporte import Deporte
from src.politica import Politica
from src.tecnologia import Tecnologia
from src.educacion import Educacion
from src.noticias_collection import NoticiasCollection

class Scrapper:
    def __init__(self, base_url : str) -> None:
        self.base_url = base_url
    
    @abstractmethod
    def generar_noticias(self, seccion) -> NoticiasCollection:
        pass
        
    @abstractmethod    
    def __ver_noticia(self, url : str) -> str:
        pass
    
    def build_noticia(self, url : str, titulo : str, contenido : str, seccion : str) -> Noticia:
        if seccion == Noticia.Deporte: return Deporte(url, titulo, contenido)
        if seccion == Noticia.Politica: return Politica(url, titulo, contenido)
        if seccion == Noticia.Tecnologia: return Tecnologia(url, titulo, contenido)
        if seccion == Noticia.Educacion: return Educacion(url, titulo, contenido)
        raise Exception("Tipo de noticia no soportada")