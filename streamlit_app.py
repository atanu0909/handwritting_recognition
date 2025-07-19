import streamlit as st
from PIL import Image
import google.generativeai as genai
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# Load Gemini model
def get_model():
    return genai.GenerativeModel('gemini-2.5-flash')


# Default prompt for extraction
DEFAULT_PROMPT = "just rewrite what is in the image. Preserve the original line breaks and formatting exactly as shown."

st.title("Handwriting Extraction with Gemini")
st.write("Upload an image. The app will extract text, skipping crossed-out lines.")

user_prompt = st.text_area("Enter your prompt:", value=DEFAULT_PROMPT, height=120)


uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Extract Text"):
        model = get_model()
        with st.spinner("Processing..."):
            try:
                response = model.generate_content([user_prompt, image])
                st.success("Extracted Text:")
                st.code(response.text, language=None)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.markdown("Made with Gemini and Streamlit")
