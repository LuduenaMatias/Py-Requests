# Librerias necesarias a importar
from bs4 import BeautifulSoup
import requests

# Variables a utilizar
web = "https://matias.acoslegacy.com"                                           # Asignamos la ruta de la web a una variable
resultado = requests.get(web)                                                   # Utilizamos la funcion get() de la libreria requests
contenido = resultado.text                                                      # Extraemos todo el contenido en formato texto

soup = BeautifulSoup(contenido, 'lxml')                                         # Utilizamos la clase de BeautifulSoup la cual permite manejar los elementos HTML o XML mediante en este caso la libreria lxml

contenedor1 = soup.find('div', id="hero")                                       # Mediante .find() localizamos el "div" con el id "hero"
nombre = contenedor1.find("h1").get_text()                                      # Realizamos nuevamente un .find() a la variable anterior para localizar un elemento especifico y extraemos su texto

contenedor2 = soup.find('div', id="contact")
sobre_mi = contenedor2.find('p').get_text(strip=True, separator=' ')            # Reemplaza saltos de linea por espacios en blanco

with open(f'{nombre}.txt', 'w') as pagina:                                      # Crea un archivo de texto con el nombre extraido en el contenedor1
    pagina.write(f'{nombre} \n {sobre_mi}')                                     # Añade el texto extraido anteriormente al .txt