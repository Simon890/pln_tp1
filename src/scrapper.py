from typing import List
from bs4 import BeautifulSoup
import requests as req
from src.noticia import Noticia
from src.ocio import Ocio
from src.deporte import Deporte
from src.policial import Policial
from src.ciudad import Ciudad
from src.politica import Politica
from src.tecnologia import Tecnologia
from src.educacion import Educacion
from src.noticias_collection import NoticiasCollection

class Scrapper:
    def __init__(self, base_url : str) -> None:
        self.base_url = base_url
    
    def generar_noticias(self, seccion) -> NoticiasCollection:
        noticias: NoticiasCollection = NoticiasCollection()
        url = self.base_url + "/seccion/" + seccion
        res = req.get(url)
        soup = BeautifulSoup(res.text, features="html5lib")
        container = soup.find("div", {"class": "grid-container grid-3-entrys with-gap"})
        for child in container.children:
            a_element = child.find_next("a", {"class": "cover-link"})
            title = a_element.attrs["title"]
            href = a_element.attrs["href"]
            contenido = self.__ver_noticia(href)
            noticias.append(self.build_noticia(url, title, contenido, seccion))
        return noticias
            
    def __ver_noticia(self, url : str) -> str:
        url = self.base_url + url
        res = req.get(url)
        soup = BeautifulSoup(res.text, features="html5lib")
        copete = soup.find("h2", {"class": "bajada font-600"})
        contenido = soup.find("div", {"class": "article-body"})
        for child in contenido.children:
            if child.name == "div":
                child.clear()
        texto = copete.getText().strip().replace("\n", " ") + " " + contenido.getText().strip().replace("\n", " ")
        return texto
    
    def build_noticia(self, url : str, titulo : str, contenido : str, seccion : str) -> Noticia:
        if seccion == Noticia.Ocio: return Ocio(url, titulo, contenido)
        if seccion == Noticia.Policial: return Policial(url, titulo, contenido)
        if seccion == Noticia.Deporte: return Deporte(url, titulo, contenido)
        if seccion == Noticia.Ciudad: return Ciudad(url, titulo, contenido)
        if seccion == Noticia.Politica: return Politica(url, titulo, contenido)
        if seccion == Noticia.Tecnologia: return Tecnologia(url, titulo, contenido)
        if seccion == Noticia.Educacion: return Educacion(url, titulo, contenido)
        raise Exception("Tipo de noticia no soportada")