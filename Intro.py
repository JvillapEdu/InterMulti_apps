import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Primera prueba")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=190)
 st.write("Este fue el primer ejercicio realizado con streamlit, un recuerdo básico.") 
 url = "https://imm1copia-htexxxgj2tsfnfbu4zg3rj.streamlit.app/#tu-audio"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5f-deq5t6yqfud4yeawxpmejj.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://f88d6cyzd5vrbetcdnz4we.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que traduce audio.") 
 url = "https://traductorc-mr5myu5tkb3vgk4m8qi6ek.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("TF-IDF")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("La siguiente aplicación usa esta medida para evaluar relevancia entre 3 preguntas.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("El siguiente enlace reconoce caracteres de fotos y procesa a texto.") 
 url = "https://ocr-audioc-3ejf7gktxq2ebkyt5nzwoa.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Convertor: Texto a Audio")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos conversión de texto input a audio") 
 url = "https://imm1copia-htexxxgj2tsfnfbu4zg3rj.streamlit.app/#tu-audio"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Análisis de Sentimientos")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("El siguiente enlace asigna valores de subjetividad y polaridad.") 
 url = "https://sentimentab-4nxap93hsdrh57cihepe6q.streamlit.app//"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("WordCloud")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Se presenta aquí una aplicación para crear Nube de ideas de textos.") 
 url = "https://wordcloudj-mahtq7qurccxdqrbtxdzxd.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


