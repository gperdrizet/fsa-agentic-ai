import streamlit as st
import pytesseract
from pdf2image import convert_from_path
from autogen import ConversableAgent, UserProxyAgent
import tempfile
import os

# Ensure Tesseract is correctly set up (update path if necessary)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract' 

# Step 1: Function to extract text from a PDF using OCR
def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())  # Save uploaded PDF to a temp file
        temp_file_path = temp_file.name  # Get temp file path

    try:
        images = convert_from_path(temp_file_path)  # Convert PDF to images
        text = "\n".join(pytesseract.image_to_string(img, config="--psm 6") for img in images)  # Perform OCR
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        text = ""

    os.remove(temp_file_path)  # Cleanup temp file
    return text

# Step 2: Define AutoGen Agents
user_agent = UserProxyAgent(name="User", code_execution_config={"use_docker": False})

doc_ingestor = ConversableAgent(
    name="Document_Ingestor",
    system_message="Extract key clauses from a contract document."
)

compliance_checker = ConversableAgent(
    name="Compliance_Checker",
    system_message="Review the contract for compliance with GDPR, corporate policies, and industry standards."
)

risk_assessor = ConversableAgent(
    name="Risk_Assessor",
    system_message="Analyze the contract and highlight potential risks, missing clauses, and ambiguities."
)

revision_recommender = ConversableAgent(
    name="Revision_Recommender",
    system_message="Suggest contract modifications to improve clarity, reduce risks, and ensure compliance."
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
