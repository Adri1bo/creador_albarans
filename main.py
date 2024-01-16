# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:43:45 2024

@author: above
"""

import qrcode
import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner
from fpdf import FPDF
import base64
import pandas as pd

def qr_callback():
    st.session_state.qrcode_id=st.session_state.qrcode_scanner

accio=st.radio('Què vols fer?',['Crear','Llegir'])

if accio == 'Crear':
    nom = st.text_input('Nom')
    municipi = st.text_input('municipi')
    data = nom + " " + municipi
    if st.button('Crear codi'):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('qr_code.png')
    
        
        st.image('qr_code.png', caption='Codi QR', use_column_width=True)

else:
    if 'qrcode_id' not in st.session_state:
        
        qr_code = qrcode_scanner(key='qrcode_scanner')
        #qr_code = st.slider('label',key='qrcode_scanner')
        st.button('Comprovar',on_click=qr_callback)
    
    else:
        st.write(st.session_state.qrcode_id)
        
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
            pdf.set_font("Helvetica", style= "B", size= 12)
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