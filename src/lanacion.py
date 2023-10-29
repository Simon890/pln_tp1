from src.noticias_collection import NoticiasCollection
from src.scrapper import Scrapper
import requests as req
from bs4 import BeautifulSoup

class LaNacion(Scrapper):
    
    def __init__(self) -> None:
        super().__init__("https://www.lanacion.com.ar")
    
    def generar_noticias(self, seccion) -> NoticiasCollection:
        noticiascoll = NoticiasCollection()
        url = self.base_url + "/" + seccion
        res = req.get(url)
        soup = BeautifulSoup(res.text, features="html5lib")
        noticias = soup.find_all("article", {"class": "mod-article"})
        for child in list(noticias)[0:10]:
            a_tag = child.find_next("a", {"class": "com-link"})
            href = a_tag.attrs["href"]
            titulo = a_tag.attrs["title"]
            contenido = self.__ver_noticia(href)
            noticiascoll.append(self.build_noticia(url, titulo, contenido, seccion))
        return noticiascoll
    
    def __ver_noticia(self, url: str) -> str:
        url = self.base_url + url
        res = req.get(url)
        soup = BeautifulSoup(res.text, features="html5lib")
        copete = soup.find("h2", {"class": "com-subhead --bajada --m-xs-"})
        contenido = soup.find("div", {"class": "col-deskxl-10 offset-deskxl-1 col-desksm-11"})
        audio_btn = contenido.find("div", {"id": "audio-player-desktop"})
        if audio_btn: audio_btn.clear()
        container = contenido.find_next("div", {"class": "col-12"})
        for child in container.children:
            if child.name == "div":
                child.clear()
        copetetxt = copete.getText().strip().replace("\n", " ") + " " if copete else ""
        texto = copetetxt + container.getText().strip().replace("\n", " ")
        return texto.strip()
            