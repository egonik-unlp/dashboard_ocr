from os import write
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from google.cloud import vision
from google.oauth2 import service_account
import io
import  download
load_dotenv()
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)


class Google_recognititon:
    def __init__(self, image_bytes, credentials) -> None:
        self.client= vision.ImageAnnotatorClient(credentials=credentials)
        self.image=vision.Image(content=image_bytes)         
    
    def recognition(self) -> str:
        # self.image.source.image_uri = image_url
        response = self.client.text_detection(image=self.image)
        return response.full_text_annotation.text


st.title('Reconocimiento de texto en imagenes')




st.markdown('Subir imagen abajo')

uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])


if uploaded_file:
	# with open( 'image_bytes', 'wb') as file:
		# file.write(uploaded_file.read())


	# with open('image_bytes') as file2:
		# print(file2)
	recog=Google_recognititon(uploaded_file.read(), credentials).recognition()
	print(recog)
	st.markdown(
		"""
		# Texto reconocido: 
		""")
	st.write(recog)

	download.return_button(recog)	