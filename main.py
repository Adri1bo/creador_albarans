# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:43:45 2024

@author: above
"""

import qrcode
import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

accio=st.radio('Què vols fer?',['Crear','Llegir'])

if accio == 'Crear':
    data = "ID_USUARI_123"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')
    
    
    
    st.image('qr_code.png', caption='Codi QR', use_column_width=True)

else:
    
    qr_code = qrcode_scanner(key='qrcode_scanner')
    
    if qr_code:
        st.write(qr_code)