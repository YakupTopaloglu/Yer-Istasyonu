from Data import *
import streamlit as st
import warnings
import pandas as pd
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
st.set_page_config(page_title="Yer Istasyonu")
tabs=["Veriler","Hakkimda"]
page=st.sidebar.radio("sekmeler",tabs)

if page=="Veriler":
    st.markdown("<h1 style=''text-align:center;'>Hoşgeldiniz</h1>",unsafe_allow_html=True)
    st.write("Grafik ve tabloya erişmek için lütfen butona basın")
    button=st.button("Start")
    if button==True:
        st.title("Yer Istasyonu")
        st.markdown("Veriler aliniyor...")

        import subprocess
        subprocess.Popen(["python", "Data.py"])
        
        data = pd.read_excel('data.xlsx', usecols='A:G')
        st.dataframe(data)
