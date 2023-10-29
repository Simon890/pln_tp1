from src.noticia import Noticia

class Ciudad(Noticia):
    def __init__(self, url: str, titulo: str, contenido : str) -> None:
        super().__init__(url, titulo, contenido, Noticia.Ciudad)