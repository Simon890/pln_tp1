# Trabajo Práctico - Procesamiento del Lenguaje Natural
## Profesores:
* Juan Pablo Manson
* Andrea Carolina Leon Cavallo
* Alan Geary
* Ariel D'Alessandro
## Alumnos:
* Simón Revello
* Ezequiel Arévalo
---
En este proyecto se utiliza el sitio web de La Nación para obtener información sobre las noticias. Las categorías a utilizar son:
* Política
* Deporte
* Tecnología
* Educación
<br>

Una vez obtenidas 10 noticias de cada categoría se genera un csv que más adelante es utilizado para crear una regresión logística.

### Bot Telegram
**IMPORTANTE** <br>
Para hacer uso del bot de telegram es necesario contar con un api key el cual se puede setear en el archivo .env en la propiedad BOT_KEY

**¿Qué pasa si no tengo una API KEY?** <br>
Para conseguir tu API KEY es necesario que en telegram inicies una conversación con el bot *BotFather* y con el comando */newbot* telegram te va a dar una KEY

### .ENV
**BOT_KEY** -> Key del bot de telegram <br>
**OUTPUT** -> Determina el output de los resúmenes de las noticias. Valores posibles: *telegram* o *consola* <br>
**CSV_PATH** -> Path en donde guardar el archivo csv