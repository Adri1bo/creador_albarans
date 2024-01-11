# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:43:45 2024

@author: above
"""

import qrcode
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

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
    class QRCodeReader(VideoTransformerBase):
        def transform(self, frame):
            # Convertim el frame a escala de grisos
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            # Creem un objecte detectar de codis QR
            qr_code_detector = cv2.QRCodeDetector()
    
            # Detectem codis QR a la imatge
            decoded_objects, points, qr_code = qr_code_detector.detectAndDecodeMulti(gray)
    
            # Dibuixem quadrats al voltant dels codis QR detectats
            if points is not None:
                for i in range(len(points)):
                    rect_points = points[i].astype(int)
                    frame = cv2.polylines(frame, [rect_points], isClosed=True, color=(0, 255, 0), thickness=2)
    
                    # Mostrem el contingut del codi QR
                    st.write("Codi QR detectat:", decoded_objects[i])
    
            return frame
    
    def main():
        st.title("Lector de Codi QR amb Streamlit")
    
        webrtc_ctx = webrtc_streamer(
            key="example",
            video_transformer_factory=QRCodeReader,
            async_transform=True,
        )
    
        if webrtc_ctx.video_transformer:
            st.video(webrtc_ctx)
    
    if __name__ == "__main__":
        main()