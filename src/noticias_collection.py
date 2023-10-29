import csv

class NoticiasCollection(list):
    def to_csv(self, filename : str):
        noticia_data = [
            ["titulo", "contenido", "seccion", "url"]
        ]
        for noticia in self:
            noticia_data.append([
                noticia.titulo, noticia.contenido, noticia.secciontxt, noticia.url
            ])
        with open(filename, mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(noticia_data)
        
    def __add__(self, data):
        return NoticiasCollection(super().__add__(data))