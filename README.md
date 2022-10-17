# Scraping--with-Selenium-and-beautifulSoup

En el siguiente proyecto se meustra la técnica del web scraping para extraer información de un sitio web en particular.

El codigo fue hecho con Python, es por eso que antes de descargar el proyecto es necesario tener instalado este lenguaje de programación, ademas contar con las librerias
o paquetes como Selenium, Beautiful Soup y lxlm, en caso de no tenerlas podemos abrir la terminal en visual studio code y escribir lo siguiente: 

$pip install selenium,   $pip install bs4,    $pip install lxml

La libreria Selenium utiliza a ChromeDriver, en caso de no tenerlo nos dirigimos al siguiente link https://chromedriver.chromium.org/
seleccionamos la versión adecuada a nuestro Google Chrome y el sistema operativo que tiene nuestro computador, de acuerdo a esto requerimientos procedemos a la instalación. Es importante 
que despues de descargar el ChromeDriver guardemos el archivo .exe (ejecutable) en la misma carpeta del proyecto o en su defecto agregarle la ruta donde esta guardada.

webdriver.Chrome('chromedriver') => si esta guardada en la carpeta del mismo archivo 

webdriver.Chrome('La ruta donde se guardo') => si esta guardado por fuera de la carpeta 
Ejemplo: webdriver.Chrome("C:\path\to\chromedriver.exe")


Luego de contar con todo lo anterior podemos pasar a la descarga del proyecto, abrirlo y ejecutarlo en nuestro editor de codigo, cmo por ejemplo Visual Studio Code.

El objetivo de este proyecto es realizar un scraping de productos y devolverlos como un archivo web_scraper.csv organisados por Titulo,Precio y Descripción. 
