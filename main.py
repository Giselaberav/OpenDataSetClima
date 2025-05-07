import src.extraction as ext
import src.transformation as tr
import src.connectiondb as conndb
import os
import pandas
import datetime
import threading
import json

from sqlalchemy import create_engine
import urllib

from dotenv import load_dotenv, find_dotenv
#import streamlit as st


#load_dotenv() 
#categLibro= os.getenv("categoriaLibro")
#rutapagina = os.getenv("rutaRaiz")

path='src/.env'
load_dotenv(dotenv_path=path,verbose=True)

def periodic_task():
  #  print(f"Running at {datetime.datetime.now()}")
    # Restart the timer
    #xml_content es el xml container que baja del ayuntamiento y lo deposita en esta variable
    json_content = ext.calldownload()
    # la siguiente funcion procesa el contenido a un pandas dataframe y lo guarda en la variable dfr 
    dfr = ext.data_extraction_todf(json_content)
    # la siguiente función procesa el dataframe y lo guarda en un csv para ser subido a la bd 
    tr.savefile(dfr)
    #testing connazure
    #connaz.connect_to_azure()
    # función que envía el dataframe a la base de datos
    conndb.savedftosql(dfr)
    
   # threading.Timer(300, periodic_task).start()
   # viz.plot_afluencia(dfr)

periodic_task()






