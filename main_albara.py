<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:39:11 2023

@author: above
"""

import streamlit as st
from fpdf import FPDF
import base64
import pandas as pd


# persist state of dataframe

if 'df' not in st.session_state:
	st.session_state.df = pd.DataFrame(columns=['Residu', 'Quantitat', 'Unitats'])
    


personal = st.selectbox("Qui registra l'entrada?",["","Antonio", "Ramon", "Barajas"],index=0,placeholder="Selecciona el teu nom...")


residu = st.text_input("Quin residu registres?")

unitats = st.radio(
    "Quines unitats?",
    ["Unitats", "Kg"],
    index=0,
)

quantitat = st.text_input("Quina quantitat entra?")

st.write("Entren "+ quantitat + unitats + " de " + residu)

afegir_linia = st.button("Afegir línia")



if afegir_linia:
    linia={'Residu':residu, 'Quantitat':quantitat, 'Unitats':unitats}
    linia = pd.DataFrame([linia])
    st.session_state.df=pd.concat([st.session_state.df,linia], axis=0, ignore_index=True)

st.write(st.session_state.df)



export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    # Creating document
    pdf = FPDF("P", "mm", "A4")
    pdf.set_margins(left= 10, top= 10)
    pdf.set_font("Helvetica", style= "B", size= 14)
    pdf.set_text_color(r= 0, g= 0, b= 0)
    pdf.add_page()
    y_pos=20
    pdf.cell(30, y_pos, personal)
    pdf.cell(-30,y_pos)
    
    for index, row in st.session_state.df.iterrows():
        y_pos=y_pos+30
        pdf.cell(30, y_pos, row['Residu'])
        pdf.cell(30, y_pos, row['Quantitat'])
        pdf.cell(30, y_pos, row['Unitats'])
        pdf.cell(-90,y_pos)  
                            # go to next line after each row


    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)
    
    """    

        
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:39:11 2023

@author: above
"""

import streamlit as st
from fpdf import FPDF
import base64
import pandas as pd


# persist state of dataframe

if 'df' not in st.session_state:
	st.session_state.df = pd.DataFrame(columns=['Residu', 'Quantitat', 'Unitats'])
    


personal = st.selectbox("Qui registra l'entrada?",["","Antonio", "Ramon", "Barajas"],index=0,placeholder="Selecciona el teu nom...")


residu = st.text_input("Quin residu registres?")

unitats = st.radio(
    "Quines unitats?",
    ["Unitats", "Kg"],
    index=0,
)

quantitat = st.text_input("Quina quantitat entra?")

st.write("Entren "+ quantitat + unitats + " de " + residu)

afegir_linia = st.button("Afegir línia")



if afegir_linia:
    linia={'Residu':residu, 'Quantitat':quantitat, 'Unitats':unitats}
    linia = pd.DataFrame([linia])
    st.session_state.df=pd.concat([st.session_state.df,linia], axis=0, ignore_index=True)

st.write(st.session_state.df)



export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    # Creating document
    pdf = FPDF("P", "mm", "A4")
    pdf.set_margins(left= 10, top= 10)
    pdf.set_font("Helvetica", style= "B", size= 14)
    pdf.set_text_color(r= 0, g= 0, b= 0)
    pdf.add_page()
    y_pos=20
    pdf.cell(30, y_pos, personal)
    pdf.cell(-30,y_pos)
    
    for index, row in st.session_state.df.iterrows():
        y_pos=y_pos+30
        pdf.cell(30, y_pos, row['Residu'])
        pdf.cell(30, y_pos, row['Quantitat'])
        pdf.cell(30, y_pos, row['Unitats'])
        pdf.cell(-90,y_pos)  
                            # go to next line after each row


    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)
    
    """    

        
>>>>>>> 676acb2359e6f4fc4dc412e88caf5e8fd4ea9e2b
    """   