import streamlit as st
import joblib


@st.cache_resource
# Load the model
def load(model_path):
    model = joblib.load(model_path)
    return model


# Make predictions
def inference(message, model):
    if message.strip():
        prediction = model.predict([message])
        if prediction[0] == "spam":
            result = "Spam"
            st.markdown('<div class="spam-message">❌ This message is SPAM!</div>', unsafe_allow_html=True)
        else:
            result = "Ham"
            st.markdown('<div class="ham-message">✅ This message is LEGIT (HAM).</div>', unsafe_allow_html=True)
    else:
        result = ""

    # Save result to a log file
    if result:
        with open('logs/prediction.log', 'a') as f:
            f.write(result + '\n')

    return result


# Page settings
st.set_page_config(
    page_title="SPAM Detector",
    page_icon="📧",
    layout="wide"
)

# Optimized CSS style
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #f0f0f0;
    }
    .main-container {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333333;
    }
    .title {
        font-family: 'Arial', sans-serif;
        color: #00b4d8;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .spam-message {
        background-color: #ffcccc;
        color: #b30000;
        border: 2px solid #ff6f61;
        padding: 20px;
        font-size: 20px;
        margin: 15px 0;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .ham-message {
        background-color: #ccffcc;
        color: #006400;
        border: 2px solid #4caf50;
        padding: 20px;
        font-size: 20px;
        margin: 15px 0;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .stat-title {
        color: #00b4d8;
        font-weight: bold;
        font-size: 24px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with basic information
with st.sidebar:
    st.title("📚 Information")
    st.write("""
    This application uses a **machine learning** model to classify 
    messages as **SPAM** or **HAM** (legitimate). 
    Here's how it works:
    - Enter a message in the text box.
    - Click the 'Predict' button.
    - View instant results, including:
        - Message length
        - Word count
        - Classification result (SPAM or HAM)
    """)

# Title of the app
st.markdown('<h1 class="title">📧 SPAM Detector</h1>', unsafe_allow_html=True)
st.write("Enter a message to find out if it's **SPAM** or **HAM (Legit)**.")

# Load the model
model = load('models/model.joblib')

# Input for message
message = st.text_input("Write a message:")

# Prediction
if st.button("Predict 🚀"):
    if message.strip():
        st.markdown('<h3 class="stat-title">📊 Message Statistics</h3>', unsafe_allow_html=True)
        st.write(f"- **Message Length:** {len(message)} characters")
        st.write(f"- **Number of Words:** {len(message.split())}")
    inference(message, model)
else:
    st.info("📝 Write a message and click **Predict 🚀** to get the result.")