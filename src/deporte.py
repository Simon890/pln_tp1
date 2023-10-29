from src.noticia import Noticia

class Deporte(Noticia):
    def __init__(self, url: str, titulo: str, contenido: str) -> None:
        super().__init__(url, titulo, contenido, Noticia.Deporte)