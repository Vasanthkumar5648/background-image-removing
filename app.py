import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Background Remover App")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open and display uploaded image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    # Remove background
    with st.spinner("Removing background..."):
        output_image = remove(input_image)

    # Display output image
    st.image(output_image, caption="Image with Background Removed", use_column_width=True)

    # Download button
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Result",
        data=byte_im,
        file_name="output.png",
        mime="image/png",
    )
