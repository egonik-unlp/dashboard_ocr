import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from google.cloud import vision
import io

load_dotenv()

class Google_recognititon:
    def __init__(self, image_bytes) -> None:
        self.client= vision.ImageAnnotatorClient()
        self.image=vision.Image(content=image_bytes)         
    
    def recognition(self) -> str:
        # self.image.source.image_uri = image_url
        response = self.client.text_detection(image=self.image)
        return response.full_text_annotation.text


st.title('OCR')




st.markdown('Subir imagen abajo')

uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])


if uploaded_file:
	# with open( 'image_bytes', 'wb') as file:
		# file.write(uploaded_file.read())


	# with open('image_bytes') as file2:
		# print(file2)
	recog=Google_recognititon(uploaded_file.read()).recognition()
	print(recog)
	st.write("jason statham", recog)