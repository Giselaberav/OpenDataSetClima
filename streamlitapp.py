import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import random
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


import src.extraction as ext
import src.transformation as tr
import src.visualization as viz
import os
from dotenv import load_dotenv


path='src/.env'
load_dotenv(dotenv_path=path,verbose=True)

categLibroos= str(os.environ.get("categoriaLibro")).strip()
rutapaginaos = str(os.environ.get("rutaRaiz")).strip()


def carga_data(rutapaginaos):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(rutapaginaos)

    books_html = ext.get_books (driver)
    df = ext.book_listings (books_html, driver, rutapaginaos)
    df = tr.limpieza(df)
    df1=tr.fake_ventas(df)
    viz.plot_ventas (df1)
    
    driver.quit()
    return df

# Configurar el fondo negro con CSS
def set_bg_black():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: black !important;
                color: white !important;
            }
            .stMarkdown, .stDataFrame, .stTitle, .stHeader, .stText {
                color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_bg_black()

# Cargar imagen del búho en el encabezado desde la URL
buho_url = "https://static.vecteezy.com/system/resources/previews/027/238/729/non_2x/cute-owl-standing-on-books-clipart-illustration-ai-generative-png.png"
buho_response = requests.get(buho_url)
buho_image = Image.open(BytesIO(buho_response.content))
st.image(buho_image, width=100)
st.title("¿Buscas un buen libro? Prueba con estos.")


df = carga_data(rutapaginaos)

# Mostrar DataFrame en Streamlit
st.write("### Libros Disponibles")
st.dataframe(df, use_container_width=900)

# Mostrar imágenes con enlaces de compra
for index, row in df.iterrows():
    cols = st.columns([1, 3, 2, 1, 2, 2])
    cols[0].write(row["Codigo"])
    cols[1].write(row["Titulo"])
    cols[2].write(row["Autor"])
    cols[3].write(row["Precio"])
    response = requests.get(row["Urlimg"])
    image = Image.open(BytesIO(response.content))
    cols[4].image(image, width=80)
    cols[5].markdown(f"[Comprar aquí]({row['Link de compra']})")

st.write("---")
st.write("📚 ¡Explora estos libros y encuentra tu próxima lectura!")

# Título de la página
st.title("Catálogo de Libros")

# Filtros interactivos
st.sidebar.header("Filtros para búsqueda avanzada")
filtro_titulo = st.sidebar.text_input("Buscar por título")
filtro_autor = st.sidebar.text_input("Buscar por autor")
#filtro_precio_min = st.sidebar.number_input("Precio mínimo", min_value=0.0, value=0.0)
#filtro_precio_max = st.sidebar.number_input("Precio máximo", min_value=0.0, value=float(df['Precio'].max()))

# Aplicar filtros al DataFrame
df_filtrado = df[
    (df['Titulo'].str.contains(filtro_titulo, case=False)) &
    (df['Autor'].str.contains(filtro_autor, case=False)) 
 #   (df['Precio'] >= filtro_precio_min) &
 #   (df['Precio'] <= filtro_precio_max)
]


# Mostrar tarjetas de libros
#st.write(f"Mostrando {len(df_filtrado)} libros:")


#for _, row in df_filtrado.iterrows():
    #with st.container():
        #col1, col2 = st.columns([1, 3])

        # Columna 1: Imagen del libro
        #with col1:
        #    st.image(row['Urlimg'], width=150)

        # Columna 2: Información del libro
       # with col2:
       #     st.subheader(row['Titulo'])
       #     st.write(f"**Autor:** {row['Autor']}")
            #st.write(f"**Precio:** ${float(str(row['Precio'])):.2f}")
            #if st.button(f"Comprar {row['Titulo']}", key=row['Codigo']):
            #    st.write(f"Redirigiendo a: {row['Link de compra']}")
                # Aquí puedes agregar lógica para redirigir al usuario al link de compra