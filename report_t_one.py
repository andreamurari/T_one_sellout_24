
import pandas as pd
import numpy as np
import streamlit as st


IT_1=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_01_gennaio_2024_vs_2023.xlsx", sheet_name="IT")
AMP_1=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_01_gennaio_2024_vs_2023.xlsx", sheet_name="complessivo")
IT_2=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_02_febbraio_2024_vs_2023.xlsx", sheet_name="IT")
AMP_2=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_02_febbraio_2024_vs_2023.xlsx", sheet_name="complessivo")
IT_3=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_03_marzo_2024_vs_2023.xlsx", sheet_name="IT")
AMP_3=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sell_out_03_marzo_2024_vs_2023.xlsx", sheet_name="Complessivo")
IT_T=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sellout_annuale_1T.xlsx", sheet_name="analisi_IT")
AMP_T=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sellout_annuale_1T.xlsx", sheet_name="analisi_ALL_MP")
EXT_T=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sellout_annuale_1T.xlsx", sheet_name="analisi_IT")
SUMMARY=pd.read_excel(r"C:\Users\filip\Desktop\report\sell_out\sellout_annuale_1T.xlsx", sheet_name="RIEPILOGATIVO")

st.header("ANALISI SELL-OUT T1 BEPER")

#GENNAIO

choice = st.selectbox('SCEGLI IL MP', ('(vuoto)','ITALIA', 'ALL MP','RIEPILOGO GENERALE','MOSTRA TUTTI'))

if choice == "ITALIA":
    if st.button('MOSTRA GENNAIO IT'):
        IT_1
        if st.button('NASCONDI GENNAIO IT'):
            st.button('MOSTRA GENNAIO IT') == False

    if st.button('MOSTRA FEBBRAIO IT'):
        IT_2
        if st.button('NASCONDI FEBBRAIO IT'):
            st.button('MOSTRA FEBBRAIO IT') == False

    if st.button('MOSTRA MARZO IT'):
        IT_3
        if st.button('NASCONDI MARZO IT'):
            st.button('MOSTRA MARZO IT') == False
   
    if st.button('MOSTRA TRIMESTRE 1 IT'):
        IT_T
        if st.button('NASCONDI TRIMESTRE 1 IT'):
            st.button('MOSTRA TRIMESTRE 1 IT') == False


if choice == "ALL MP":
    if st.button('MOSTRA GENNAIO ALL-MP'):
        AMP_1
        if st.button('NASCONDI GENNAIO ALL-MP'):
            st.button('MOSTRA GENNAIO ALL-MP') == False

    if st.button('MOSTRA FEBBRAIO ALL-MP'):
        AMP_2
        if st.button('NASCONDI FEBBRAIO ALL-MP'):
            st.button('MOSTRA FEBBRAIO ALL-MP') == False

    if st.button('MOSTRA MARZO ALL-MP'):
        AMP_3
        if st.button('NASCONDI MARZO ALL-MP'):
            st.button('MOSTRA MARZO ALL-MP') == False

    if st.button('MOSTRA TRIMESTRE 1 ALL-MP'):
        AMP_T
        if st.button('NASCONDI TRIMESTRE 1 ALL-MP'):
            st.button('MOSTRA TRIMESTRE 1 ALL-MP') == False


if choice == 'RIEPILOGO GENERALE':
    SUMMARY

if choice == "MOSTRA TUTTI":
    if st.button('MOSTRA GENNAIO IT'):
        IT_1
        if st.button('NASCONDI GENNAIO IT'):
            st.button('MOSTRA GENNAIO IT') == False

    if st.button('MOSTRA FEBBRAIO IT'):
        IT_2
        if st.button('NASCONDI FEBBRAIO IT'):
            st.button('MOSTRA FEBBRAIO IT') == False

    if st.button('MOSTRA MARZO IT'):
        IT_3
        if st.button('NASCONDI MARZO IT'):
            st.button('MOSTRA MARZO IT') == False
    
    if st.button('MOSTRA TRIMESTRE 1 IT'):
        IT_T
        if st.button('NASCONDI TRIMESTRE 1 IT'):
            st.button('MOSTRA TRIMESTRE 1 IT') == False
    
    if st.button('MOSTRA GENNAIO ALL-MP'):
        AMP_1
        if st.button('NASCONDI GENNAIO ALL-MP'):
            st.button('MOSTRA GENNAIO ALL-MP') == False

    if st.button('MOSTRA FEBBRAIO ALL-MP'):
        AMP_2
        if st.button('NASCONDI FEBBRAIO ALL-MP'):
            st.button('MOSTRA FEBBRAIO ALL-MP') == False

    if st.button('MOSTRA MARZO ALL-MP'):
        AMP_3
        if st.button('NASCONDI MARZO ALL-MP'):
            st.button('MOSTRA MARZO ALL-MP') == False    
    
    if st.button('MOSTRA TRIMESTRE 1 ALL-MP'):
        AMP_T
        if st.button('NASCONDI TRIMESTRE 1 ALL-MP'):
            st.button('MOSTRA TRIMESTRE 1 ALL-MP') == False