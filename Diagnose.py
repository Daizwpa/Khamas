
import pandas as pd
import streamlit as st
from PIL import Image
import io
from Controller.Classify import Classifier
from utils.image_core import imread
import numpy as np


def Page(dataset: pd.DataFrame = None):
    st.header(" Identifcation de genre Meloidogyne Spp.:", divider='rainbow')
    st.markdown("### Saisir l'image du microscope optique:")

    uploaded_Image = st.file_uploader(" ", type=[
        "png", "jpg", "dcm", "nii"], accept_multiple_files=False)
    image = None
    if uploaded_Image is not None:
        bytes = uploaded_Image.read()
        image = Image.open(io.BytesIO(bytes))
        st.image(image)
    else:
        st.image("https://img.lovepik.com/element/40217/7532.png_1200.png")

    st.divider()

    result = None
    if st.button("identifier", type="primary", use_container_width=True):

        c = Classifier(
            wieghts_path="./Extraction/model/7model.keras",

        )
        result = c.Classify(
            image=np.array(image)

        )

    st.divider()
    st.markdown("### Result:")
    if (result is not None):
        if result < 0.5:
            st.markdown("#### *Meloidogyne :green[incognita]*")
        else:
            st.markdown("#### *Meloidogyne :green[javanica]*")


Page()
