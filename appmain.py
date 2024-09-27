import streamlit as st
from pyandro import Camera

st.title('相機模式')

if st.button('開啟鏡頭'):
    # Open the camera
    cam = Camera()
    
    while True:
        img = cam.get_image()
        
        if img is not None:
            st.image(img, caption='鏡頭畫面')
            
            if st.button('關閉鏡頭'):
                break