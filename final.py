import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👋",
    layout="centered"
)

# --- BACKGROUND IMAGE ---
with open("Backgraound.jpg", "rb") as f:
    data = f.read()
background_b64 = base64.b64encode(data).decode()

# --- PROFILE PHOTO ---
with open("Pphoto.jpg", "rb") as f:
    photo_data = f.read()
photo_b64 = base64.b64encode(photo_data).decode()

# --- GLOBAL STYLES ---
st.markdown(f"""
<style>
/* Main background */
.stApp {{
    background-image: url("data:image/jpg;base64,{background_b64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-color: rgba(0,0,0,0.2); /* subtle overlay for readability */
}}

/* Make all content transparent so background shows */
.block-container {{
    background-color: rgba(0,0,0,0);
    color: white;
}}

/* Glass-style transparent sidebar */
[data-testid="stSidebar"] {{
    background-color: rgba(255, 255, 255, 0.2) !important;
    backdrop-filter: blur(0.2px);
    border-right: 1px solid rgba(255,255,255,0.2);
}}

/* Force sidebar text to white */
[data-testid="stSidebar"] * {{
    color: white !important;
}}

/* Hide sidebar title above radio buttons */
[data-testid="stSidebar"] .stRadio > label {{
    display: none !important;
}}

/* Remove default radio buttons */
[data-testid="stSidebar"] .stRadio input {{
    display: none !important;
}}

/* Sidebar labels (icon + text inline) */
[data-testid="stSidebar"] .stRadio label {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    border-radius: 12px;
    color: white !important;
    font-weight: bold;
    font-size: 16px;
    background-color: transparent;
    cursor: pointer;
    transition: all 0.3s ease;
}}

/* Hover effect */
[data-testid="stSidebar"] .stRadio label:hover {{
    background-color: rgba(34,197,94,0.8);
    transform: translateX(5px);
}}

/* Selected menu item */
[data-testid="stSidebar"] .stRadio input:checked + label {{
    background-color: rgba(22,163,74,0.9);
    box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
}}

/* Profile picture circle */
.profile-pic {{
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background-image: url("data:image/jpg;base64,{photo_b64}");
    background-size: cover;
    background-position: center;
    display: block;
    margin: 20px auto 0 auto;
    border: 2px solid white;
}}

/* Profile name */
.profile-name {{
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin-top: 15px;
}}

/* Typewriter Effect Line 1 */
.typewriter1 {{
    width: 0;
    max-width: 700px;
    margin: 10px auto;
    color: #22c55e;
    font-size: 20px;
    white-space: nowrap;
    overflow: hidden;
    animation: typing1 4s steps(70,end) forwards;
    text-align: center;
}}

/* Typewriter Effect Line 2 */
.typewriter2 {{
    width: 0;
    max-width: 700px;
    margin: 0 auto 20px auto;
    color: white;
    font-size: 19.2px;
    white-space: nowrap;
    overflow: hidden;
    animation: typing2 5s steps(100,end) forwards 3s;
    text-align: center;
}}

@keyframes typing1 {{ from {{ width: 0; }} to {{ width: 100%; border-right: 2px rgba(0,127,255,0.4);}} }}
@keyframes typing2 {{ from {{ width: 0; }} to {{ width: 100%; border-right: 2px rgba(0,127,255,0.4);}} }}

@keyframes blink1 {{ 0%,100%{{border-color:white;}} 50%{{border-color:white;}} }}
@keyframes blink2 {{ 0%,100%{{border-color:white;}} 50%{{border-color:white;}} }}

/* Glass Card Styles */
.glass-card {{
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 16px;
    margin: 15px 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
}}
.glass-card:hover {{
    background: rgba(34,197,94,0.1);
    transform: translateY(-5px);
}}
.glass-card-title {{
    font-size: 20px;
    font-weight: 700;
    color: #22c55e;
    margin-bottom: 10px;
}}
.glass-card-text {{
    font-size: 16px;
    color: white;
    line-height: 1.6;
}}
a {{
    color: #22c55e;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}

/* Transparent Resume Download Button */
div[data-testid="stDownloadButton"] button {{
    background-color: rgba(255, 255, 255, 0.08) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 10px 25px;
    border-radius: 12px;
    font-weight: bold;
    backdrop-filter: blur(4px);
    transition: all 0.3s ease;
}}
div[data-testid="stDownloadButton"] button:hover {{
    background-color: rgba(34,197,94,0.2) !important;
    border-color: rgba(34,197,94,0.5);
    transform: translateY(-3px);
}}

</style>
""", unsafe_allow_html=True)


# --- SIDEBAR NAVIGATION ---
page = st.sidebar.radio(
    "",
    ["🏠 Home", "👤 About Me", "💼 Experience", "🚀 Projects", "🛠 Skills", "📄 Resume", "📬 Contact"]
)

# --- PAGE CONTENT ---
if page == "🏠 Home":
    st.markdown("""
    <h1 style="
        text-align:center;
        font-size:28px;
        color:white;
        margin-top:20px;
        margin-bottom:20px;
    ">
        👋 Welcome to my portfolio
    </h1>

    <div class='profile-pic'></div>
    <div class='profile-name'>I'm Manoj Ingale</div>

    <div class="typewriter1">
        <b>I love building <b>ML models</b>, <b>AI apps</b>, and <b>data-driven solutions</b><b>.
    </div>
    <div class="typewriter2">
        This portfolio showcases my Experience, projects, skills, and achievements.
    </div>
    """, unsafe_allow_html=True)

elif page == "👤 About Me":
    st.header("👤 About Me")
    st.write("""
    I'm Manoj Ingale, passionate about technology and problem solving.  
    - 🔭 AI, ML, and Data Science projects  
    - 🌱 Learning advanced Generative AI  
    - 💬 Ask me about Python, Machine learning, Deep Learning, NLP, and Streamlit  
    """)
    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">💼 Interested Roles</div>
        <div class="glass-card-text">AI Engineer, Data Scientist, ML Engineer, Data Analyst</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">🧑‍💻 Work Type</div>
        <div class="glass-card-text">Full-time, Remote Contract, Freelance</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">🌍 Preferred Locations</div>
        <div class="glass-card-text">Pune, Mumbai, Bengaluru, Hyderabad</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">🎓 Education</div>
        <div class="glass-card-text">M.Sc in Statistics, B.Sc in Statistics</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">🎓 Certificate</div>
        <div class="glass-card-text">1️⃣ Google Google Data Analytics Professional Certificate</div>
    </div>
    """, unsafe_allow_html=True)

elif page == "💼 Experience":
    st.header("💼 Experience")
    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">🚀 Senwell Solutions (Analyst)      (Aug-23 - Jan-25)</div>
        <div class="glass-card-text">
        Project Name: Chronic Disease Risk Prediction.<br>
            - Developed models for patient risk assessment, disease progression, and treatment effectiveness.<br>
            - Conducted data preprocessing and feature engineering using Python (Pandas, NumPy) to handle large-scale datasets.<br>
            - Built machine learning models (Logistic Regression, Random Forest) to predict patient readmission rates & chronic disease risks.<br>
            - Select and engineer features to improve model accuracy and performance.<br>
            - Collaborated with clinicians, data engineers to translate medical data into actionable insights.<br>
            Environment: Python, Pandas, NumPy, Scikit-learn, Jupyter Notebook, SQL.
        </div>
    </div>


    <div class="glass-card">
        <div class="glass-card-title">💼 Zummit Infolabs  (Internship)</div>
        <div class="glass-card-text">
            Project Name : News Summarization and Text-to-Speech Application<br>
            Role: Jr. Datascientist (Interns)<br>
            Description : Develop a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool should allow users to input a company name and receive a structured sentiment report along with an audio output.<br>
            Responsibilities:<br>
            - News Extraction: Scrape title, summary, and metadata from news articles using BeautifulSoup.<br>
            - Sentiment Analysis: Analyze article sentiment (positive/negative/neutral).<br>
            - Comparative Analysis: Compare sentiment across articles for insight.<br>
            - Text-to-Speech: Convert summary to Hindi audio using open-source TTS.<br>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "🚀 Projects":
    st.header("🚀 Projects")
    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">1️⃣ Customer Support Chatbot (RAG-based)</div>
        <div class="glass-card-text">Developed a Retrieval-Augmented Generation (RAG) chatbot to answer customer queries efficiently using LangChain and HuggingFace. Integrated document embeddings and vector search to provide accurate, context-aware responses from company documentation.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">2️⃣ Healthcare Assistant</div>
        <div class="glass-card-text">Developed an AI-powered healthcare assistant to fetch research papers, treatment guidelines, and clinical insights for medical professionals. Leveraged NLP and retrieval pipelines to provide accurate, context-aware recommendations in real time.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">3️⃣ Interactive Data Dashboard</div>
        <div class="glass-card-text">Developed an interactive data dashboard using Streamlit to visualize and monitor large datasets in real time. Integrated charts, KPIs, and filters to enable data-driven decision-making and performance tracking.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">4️⃣ Drowsiness Detection by using OpenCV, dlib</div>
        <div class="glass-card-text">Developed a real-time drowsiness detection system using OpenCV and dlib to monitor eye aspect ratio (EAR) and alert drivers when signs of fatigue are detected. Integrated computer vision techniques to ensure road safety through continuous facial landmark tracking.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">5️⃣ Cat vs Dog Classification by using CNN</div>
        <div class="glass-card-text">Implemented a Convolutional Neural Network (CNN) model to classify cat and dog images with high accuracy. Utilized TensorFlow and Keras for model training, image preprocessing, and evaluation on real-world datasets.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">6️⃣ AI pdf summarization by using RAG</div>
        <div class="glass-card-text">Developed an AI-powered PDF summarization system using Retrieval-Augmented Generation (RAG) to extract key insights from documents. Integrated LangChain and OpenAI to generate concise, accurate summaries for large PDFs in real time.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">7️⃣ Generate text the by using Transformers</div>
        <div class="glass-card-text">Implemented a text generation system using Transformer-based models to create coherent and context-aware sentences. Leveraged Hugging Face models to fine-tune and generate human-like text for various applications.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">8️⃣ Gemini invoice assistant</div>
        <div class="glass-card-text">An AI-powered assistant that lets users upload invoices and ask questions directly. Built using Google Gemini to extract, understand, and summarize invoice data.</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">9️⃣ Gemini Text to SQL Query</div>
        <div class="glass-card-text">An AI-powered app that lets users ask natural language questions and automatically generates and executes SQL queries on the database.</div>
    </div>
    """, unsafe_allow_html=True)

elif page == "🛠 Skills":
    st.header("🛠 Skills")
    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">Languages</div>
        <div class="glass-card-text">Python, R, SQL</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">ML/ DL/ NLP</div>
        <div class="glass-card-text">Scikit-learn, PyTorch, TensorFlow, Keras, NLTK, OpenCV</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">Data Tools</div>
        <div class="glass-card-text">Pandas, NumPy, Matplotlib, Plotly, BeutifulSoup(bs4)</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">Gen AI</div>
        <div class="glass-card-text">Transformers, Langchain, LLM, LIM, HuggingFace</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">Web/Apps</div>
        <div class="glass-card-text">Streamlit</div>
    </div>
    """, unsafe_allow_html=True)

elif page == "📄 Resume":
    st.header("📄 My Resume")

    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">💼 My Resume</div>
        <div class="glass-card-text">
            A concise overview of my professional journey, technical expertise, and accomplishments.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # File download button
    with open("Manoj_I.pdf", "rb") as file:
        btn = st.download_button(
            label="⬇️ Download Resume",
            data=file,
            file_name="Manoj_I.pdf",
            mime="application/pdf"
        )

elif page == "📬 Contact":
    st.header("📬 Contact Me")
    st.markdown("""
    <div class="glass-card">
        <div class="glass-card-title">📧 Email</div>
        <div class="glass-card-text">manojingale3126@gmail.com, i.manoj3126@gmail.com</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">📱 Contact No</div>
        <div class="glass-card-text">+91 8308290298</div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">🔗 LinkedIn</div>
        <div class="glass-card-text"><a href="https://www.linkedin.com/in/manoj-ingale-052a3725b" target="_blank">linkedin.com/in/manoj-ingale-052a3725b</a></div>
    </div>
    <div class="glass-card">
        <div class="glass-card-title">💻 GitHub</div>
        <div class="glass-card-text"><a href="https://github.com/manoj3126" target="_blank">github.com/manoj3126</a></div>
    </div>
    """ , unsafe_allow_html=True)

    # Contact form
    st.subheader("📨 Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"✅ Thanks {name}! I’ll get back to you at {email}.")
