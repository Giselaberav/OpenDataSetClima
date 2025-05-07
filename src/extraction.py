import pandas as pd
import os
import random
import re
import time
import datetime
import requests
import ast
import json



def calldownload():
    urlppal = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/"
    urlfecini="/fechaini/"
    varfechaini= "2025-04-01T00:00:00UTC"
    urlfecfin="/fechafin/"
    varfecfin="2025-05-02T23:59:59UTC"
    urlestacion="/estacion/3195/"
    varapi="?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJnaXNlbGEuYmVyYXZAZ21haWwuY29tIiwianRpIjoiZGMyZDBmNDktYjAwMi00OWI2LWFmYmMtMzM5YTZhMTcyMDczIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NDYxMzY0OTgsInVzZXJJZCI6ImRjMmQwZjQ5LWIwMDItNDliNi1hZmJjLTMzOWE2YTE3MjA3MyIsInJvbGUiOiIifQ.vT-9wbHU-5MPdr462ZFeu1pMesnpBnGljOjwaCQLnTg"

    json_content = download_json(urlppal+urlfecini+varfechaini+urlfecfin+varfecfin+urlestacion+varapi)
    return json_content

def download_json(url):
    """Download JSON content from the given URL"""
    try:
        response = requests.get(url)

        if response.status_code == 200:
            initial_data = response.json()
            if initial_data['estado'] == 200:
                # Second request to get the actual data
                data_url = initial_data['datos']
                data_response = requests.get(data_url)
        
                if data_response.status_code == 200:
                    # Parse the JSON data
                    actual_data = data_response.json()
                else:
                    print(f"Error fetching actual data: {data_response.status_code}")
            else:
                print(f"API returned error: {initial_data['descripcion']}")
        else:
            print(f"Initial request failed: {response.status_code}")
        return actual_data
    
    except requests.RequestException as e:
        print(f"Error downloading JSON: {e}")
        return None


def data_extraction_todf(actual_data):
   df = pd.DataFrame(actual_data)
   return df




    