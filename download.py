import base64
from datetime import datetime
import streamlit as st



def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """


    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


# Examples


def return_button(object:str) -> None:
	if st.button('Generar link de descarga'):
		date_string=datetime.strftime(datetime.now(), "%d_%m_%H:%M")
		tmp_download_link = download_link(object, 'texto_traduccion_{}'.format(date_string), 'Clic para descargar el texto reconocido')
		st.markdown(tmp_download_link, unsafe_allow_html=True)