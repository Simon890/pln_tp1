from src.clasificador import Clasificador
from src.noticia import Noticia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import telebot

class Programa:
    
    API_KEY = "6332002951:AAHGkVuXNyaNR24eIkjDlRxJAy_mSaM5eeM"
    
    def __init__(self, clasificador : Clasificador, output = "consola") -> None:
        self.c = clasificador
        self.output = output
        nltk.download("punkt")
    
    def ejecutar(self):
        if self.output == "consola":
            self.__ejecutar_consola()
        elif self.output == "telegram":
            self.__ejecutar_bot()
        else:
            raise Exception("Output no soportado")
        
    def __ejecutar_consola(self):
        while True:
            opc = input("Elija una opción:\n1)Política\n2)Tecnología\n3)Educación\n4)Deporte\n5)Salir\n")
            if opc not in ["1", "2", "3", "4", "5"]:
                print("Opción no válida")
                continue
            
            if opc == "5":
                break
            print("\n".join(self.__eval_seccion(opc)))
    
    def __ejecutar_bot(self):
        print("Iniciando bot...")
        bot = telebot.TeleBot(self.API_KEY)
        @bot.message_handler(commands=["help"])
        def mostrar_help(mensaje):
            texto = "Revello Bot\nPara consultar sobre alguna noticia utilice el comando /noticia <tipo_noticia>\n"
            texto += "Tipos de noticia:\n1)Politica\n2)Tecnologia\n3)Educacion\n4)Deporte\n"
            texto += "Ejemplo: /noticia politica"
            bot.reply_to(mensaje, texto)
        
        @bot.message_handler(commands=["noticia"])
        def mostrar_noticia(mensaje):
            nombre = mensaje.from_user.first_name
            texto = mensaje.text
            seccion = texto.split("/noticia")[1].strip()
            for noticia in self.__eval_seccion(seccion):
                bot.reply_to(mensaje, noticia)
                
        print("Bot iniciado!")
        
        bot.infinity_polling()
    
    def __eval_seccion(self, seccion : int | str):
        if seccion in ["1", "politica"]:
            return self.__resumir(self.__get_contenido(Noticia.Politica))
        if seccion in ["2", "tecnologia"]:
            return self.__resumir(self.__get_contenido(Noticia.Tecnologia))
        if seccion in ["3", "educacion"]:
            return self.__resumir(self.__get_contenido(Noticia.Educacion))
        if seccion in ["4", "deporte"]:
            return self.__resumir(self.__get_contenido(Noticia.Deporte))
        return ["Sección no válida"]
    
    def __resumir(self, data):
        arr_res = []
        for i, texto in enumerate(data[1]):
            res = ""
            res += f"\nNoticia '{data[0][i].upper()}': "
            parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
            sum = LsaSummarizer()
            resumen = sum(parser.document, 2)
            for frase in resumen:
                res += " " + str(frase).capitalize()
            arr_res.append(res)
        return arr_res
    
    def __get_contenido(self, seccion):
        df_data = self.c.df[self.c.df["seccion"] == self.c.seccion_lookup[seccion]]
        return df_data["titulo"].values, df_data["contenido"].values