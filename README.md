# DOC
Recomendador de Libros con Streamlit
## INTRODUCCIÓN
Esta aplicación en Streamlit permite explorar y visualizar una lista de libros extraídos del sitio web de Gonvill. Utiliza Selenium y BeautifulSoup para el web scraping, mostrando los datos obtenidos en un DataFrame interactivo y con imágenes de los libros.
Extrae un png con las gráficas de ventas de los libros
Características
	•	**Interfaz **para una mejor experiencia visual.
	•	Scraping automático de libros desde Gonvill.
	•	Muestra información clave como título, autor, precio e imagen.
	•	Enlaces directos para comprar los libros en la página oficial.
    •	Genera un csv con el listado y un png de grafico de barra de ventas.

Librerías utilizadas
	•	Python
	•	Streamlit
	•	Pandas
	•	Selenium
	•	BeautifulSoup
	•	Requests
	•	PIL (Pillow)

## Metodología
Esto extrae de LinkedIn y guarda una gráfica después de haber exportado un dataset

## Getting started
descarga este repositorio
Antes de ejecutar la aplicación, instala las dependencias necesarias con:

pip install -r requirements.txt

Requisitos adicionales
Asegúrate de tener Google Chrome instalado, ya que Selenium usa ChromeDriver.
Ejecución
Ejecuta la aplicación con el siguiente comando:
streamlit run streamlitapp.py
Captura de Pantalla
La aplicación mostrará una lista de libros con su imagen, precio y enlace de compra:


Notas Importantes
	•	El scraping puede tardar algunos segundos debido a los tiempos de espera incorporados.
	•	El código está configurado para recorrer 20** páginas** del sitio, pero se puede modificar fácilmente.
	•	Puede ser necesario actualizar el ChromeDriver si hay cambios en Chrome.

Version 1.0
    *   Los filtros no funcionan
    *   El listado no está paginado
    *   Se le coloca al código solo una categoría de la página, la idea es agregar más categorías

Desarrollado usando Streamlit y Selenium.
# OpenDataSetClima
