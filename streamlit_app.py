import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

# Set your Gemini API key here
API_KEY = "AIzaSyC87pphG3Esb3UnRiMQiAscJ931IKk3RkM"
genai.configure(api_key=API_KEY)

# Load Gemini model
def get_model():
    return genai.GenerativeModel('gemini-2.5-flash')

# Prompt for extraction
PROMPT = (
    "just rewrite what is in the image. "
     
)

st.title("Handwriting Extraction with Gemini")
st.write("Upload an image. The app will extract text, skipping crossed-out lines.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Extract Text"):
        model = get_model()
        with st.spinner("Processing..."):
            try:
                response = model.generate_content([PROMPT, image])
                st.success("Extracted Text:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.markdown("Made with Gemini and Streamlit")
