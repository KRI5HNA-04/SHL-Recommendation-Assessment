import streamlit as st
import pandas as pd
from google.generativeai import configure, GenerativeModel

# Load SHL catalog
catalog_df = pd.read_csv("shl_assessment_catalog.csv")

# Gemini API Configuration
configure(
    api_key="AIzaSyDifloDHAQeYbmtJ7gbXRqJ5UgSwfSxVvw",
    transport="rest"
)

# Gemini Model
model = GenerativeModel(
    model_name="models/gemini-2.5-pro-preview-03-25",
    generation_config={"temperature": 0.7}
)

# Generate recommendation prompt
def get_recommendations(query, df, top_k=10):
    context = "\n".join([
        f"{row['Assessment Name']} - {row['Test Type']} - {row['Assessment URL']} - {row['Duration']} - Remote: {row['Remote Testing Support']} - Adaptive: {row['Adaptive/IRT Support']}"
        for _, row in df.iterrows()
    ])

    prompt = f"""
    Based on the following assessment catalog:

    {context}

    Recommend up to {top_k} relevant SHL assessments for the following query:
    "{query}"

    Return a table with these columns:
    Assessment Name, Assessment URL, Remote Testing Support, Adaptive/IRT Support, Duration, Test Type
    """
    response = model.generate_content(prompt)
    return response.text
query_param = st.query_params.get("query", "")
if query_param:
    # Return JSON directly
    result = get_recommendations(query_param, catalog_df)
    st.json({"result": result})
    st.stop()  # Stop the rest of Streamlit from running

# Streamlit UI
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# --- Custom Modern UI CSS ---
st.markdown("""
    <style>
        html, body, .main {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            font-family: 'Segoe UI', sans-serif;
            color: #f1f2f6;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: 800;
            color: #ffffff;
            margin-top: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #dcdde1;
            margin-bottom: 30px;
        }
        .box {
            background: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 18px;
            box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.3);
            max-width: 900px;
            margin: auto;
        }
        .result-table {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 15px;
        }
        .stTextArea > div > textarea {
            font-size: 16px;
            background-color: #1e272e;
            color: #ffffff;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #00cec9;
            color: black;
            font-weight: bold;
            padding: 10px 24px;
            border: none;
            border-radius: 12px;
            transition: 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #81ecec;
            transform: scale(1.05);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #dfe6e9;
            margin-top: 50px;
        }
        a {
            color: #74b9ff;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">🔎 SHL Assessment Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart AI-Powered Matching for Hiring Assessments</div>', unsafe_allow_html=True)

# Input & Results Container
st.markdown('<div class="box">', unsafe_allow_html=True)
query = st.text_area("💼 Enter job description or hiring query:", height=150, placeholder="e.g., Hiring Java developers with strong business communication...")

if st.button("✨ Get Smart Recommendations"):
    if query.strip():
        with st.spinner("⏳ Generating your custom SHL assessment plan..."):
            result = get_recommendations(query, catalog_df)
            st.markdown(result, unsafe_allow_html=True)
    else:
        st.warning("Please enter a query to proceed.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer">🚀 Built with ❤️ by RS Krishna • Powered by Gemini & Streamlit</div>', unsafe_allow_html=True)
