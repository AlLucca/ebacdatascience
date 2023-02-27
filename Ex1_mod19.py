import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

@st.cache(show_spinner= True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data, sep=';')
    except:
        return pd.read_excel(file_data)



def main():
    st.set_page_config(page_title='Telemarketing analisys',
                       page_icon='./Material_de_apoio_M19_Cientista de Dados/img/telmarketing_icon.png',
                       layout='wide',
                       initial_sidebar_state='expanded')
    st.write('# Telemarketing analisys')
    st.markdown('---')

    image = Image.open('./Material_de_apoio_M19_Cientista de Dados/img/Bank-Branding.jpg')
    st.sidebar.image(image)

    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank marketing data",
                                           type=['csv', 'xlsx'])

    if (data_file_1 is not None):
        bank_raw = load_data(data_file_1)
        bank = bank_raw.copy()
        st.write(data_file_1.name)
        st.write(bank_raw.head())

if __name__ == '__main__':
    main()
