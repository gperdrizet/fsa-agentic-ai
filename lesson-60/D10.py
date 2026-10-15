import streamlit as st

import io
import pymupdf  # PyMuPDF
import numpy as np
from PIL import Image
import easyocr
from autogen import ConversableAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "config_list": [{
        "model": "gpt-4o-mini",
        "api_key": os.environ["OPENAI_API_KEY"],
        "base_url": os.environ["OPENAI_BASE_URL"]
    }]
}

# Step 1: Function to extract text from a PDF using OCR
def extract_text_from_pdf(uploaded_file):
    # 1. Initialize the EasyOCR reader (English language)
    # Set gpu=True if your system has a dedicated NVIDIA GPU
    reader = easyocr.Reader(['en'], gpu=False)

    # Empty string to gather pages
    text = ''

    # Create byte stream from file
    pdf_bytes = uploaded_file.read() 
    
    # Open the byte stream with PyMuPDF
    with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
        
        # Loop through each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # --- Optimization Step ---
            # Try to grab digital text first to bypass heavy OCR if possible
            existing_text = page.get_text()
            if existing_text.strip():
                text += existing_text + "\n"
                continue
            
            # --- Scanned Page Fallback ---
            # Get pixel data (zoom=2 scales up for optimal 300 DPI legibility)
            mat = pymupdf.Matrix(2, 2)
            pix = page.get_pixmap(matrix=mat)
            
            # Convert raw PyMuPDF pixels straight into a NumPy array
            image_data = pix.tobytes("png")
            image = Image.open(io.BytesIO(image_data))
            image_np = np.array(image)
            
            # Run EasyOCR (detail=0 returns raw text blocks joined by spaces)
            ocr_results = reader.readtext(image_np, detail=0)
            text += "\n".join(ocr_results) + "\n"
            
    return text

# Step 2: Define AutoGen Agents
user_agent = UserProxyAgent(name="User", code_execution_config={"use_docker": False})

doc_ingestor = ConversableAgent(
    name="Document_Ingestor",
    system_message="Extract key clauses from a contract document.",
    llm_config=llm_config
)

compliance_checker = ConversableAgent(
    name="Compliance_Checker",
    system_message="Review the contract for compliance with GDPR, corporate policies, and industry standards.",
    llm_config=llm_config
)

risk_assessor = ConversableAgent(
    name="Risk_Assessor",
    system_message="Analyze the contract and highlight potential risks, missing clauses, and ambiguities.",
    llm_config=llm_config
)

revision_recommender = ConversableAgent(
    name="Revision_Recommender",
    system_message="Suggest contract modifications to improve clarity, reduce risks, and ensure compliance.",
    llm_config=llm_config
)

# Step 3: Create Streamlit UI
st.title("AutoGen-Powered Contract Review System")
st.write("Upload a contract PDF to analyze compliance, risks, and suggested revisions.")

# Step 3.1: File Upload Mechanism
uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

if uploaded_file:
    st.write("Extracting text from PDF...")
    contract_text = extract_text_from_pdf(uploaded_file)  # Extract text from PDF

    # 3.2 Display extracted text in UI
    st.subheader("Extracted Contract Text")
    st.text_area("Contract Content", contract_text, height=200)

    if st.button("Analyze Contract"):
        with st.spinner("Processing..."):
            extracted_clauses = user_agent.initiate_chat(
                recipient=doc_ingestor,
                message=f"Extract key clauses from the following contract:\n{contract_text}"
            )
            compliance_issues = user_agent.initiate_chat(
                recipient=compliance_checker,
                message=f"Review this contract for compliance with GDPR and corporate legal policies:\n{contract_text}"
            )
            risk_analysis = user_agent.initiate_chat(
                recipient=risk_assessor,
                message=f"Analyze the contract and highlight risks or missing clauses:\n{contract_text}"
            )
            revisions = user_agent.initiate_chat(
                recipient=revision_recommender,
                message=f"Suggest modifications to improve contract clarity and compliance:\n{contract_text}"
            )

        # 3.3 : Display Analysis Results
        st.subheader("Contract Analysis Results")

        with st.expander("**Extracted Clauses**"):
            st.info(extracted_clauses)

        with st.expander("**Compliance Issues**"):
            st.warning(compliance_issues)

        with st.expander("**Risk Analysis**"):
            st.error(risk_analysis)

        with st.expander("**Suggested Revisions**"):
            st.success(revisions)
