''' 
imagina que esta API es una biblioteca de peliculas
La función load_movies() es como una biblioteca de libros (peliculas) cuando se abre la biblioteca
La función get_movies() muestra todo el catalogo cuando alguien lo pide.
La fucnción get_movie(id) es como si alguien preguntara por un libro especifico es decir, por un codigo de identificación
La funcion chat bot (query) es un asistente que busca peliculas segun palabras clave y sinonimo.
La función get_movies_by_category(category) ayuda a encontrar peliculas segun su genero (acción, comedia, etc...)
'''

# Importamos las herramientas necesarias para continuar nuestra API
from fastapi import FastAPI, HTTPException # FastAPI nos ayuda a crear la API, HTTPException nos ayuda a mejorar errores
from fastapi.responses import HTMLResponse # HTMLResponse nos ayuda a mejorar respuestas HTML, JSONResponse nos ayuda a manejar respuestas
import pandas as pd # pandas nos ayuda a manejar tablas como si fuera un Excel
import nltk # nltk es una libreria para procesar texto y analizar palabras
from nltk.tokenize import word_tokenize # word_tokenize nos ayuda a tokenizar texto, es decir, a convertirlo en palabras
from nltk.corpus import wordnet # wordnet es una libreria para analizar sinonimos

# Indicamos la ruta donde nltk buscara los datos descargados en nuestro computador
nltk.data.path.append('C:\Users\Vanessa GR\AppData\Roaming\nltk_data')
nltk.download('punkt')




