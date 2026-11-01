
import streamlit as st

from src.rag_pipeline import get_rag_components, ask_axelia


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AXELIA Banking Assistant",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# 2. CUSTOM DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #080D18;
    color: #F0F6FF;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

.axelia-title {
    font-size: 42px;
    font-weight: 800;
    color: #F0F6FF;
    letter-spacing: 3px;
}

.axelia-subtitle {
    color: #42C8FF;
    font-size: 13px;
    letter-spacing: 3px;
}

.description {
    color: #A8B6C9;
    font-size: 16px;
}

.feature-card {
    background: #111C2D;
    border: 1px solid #263B55;
    border-radius: 12px;
    padding: 20px;
    min-height: 120px;
}

.feature-title {
    color: #42C8FF;
    font-size: 17px;
    font-weight: 700;
}

.feature-description {
    color: #A8B6C9;
    font-size: 13px;
}

section[data-testid="stSidebar"] {
    background-color: #0D1523;
    border-right: 1px solid #1D3048;
}

.stButton button {
    background-color: #087DBA;
    color: white;
    border: none;
    border-radius: 8px;
}

.stButton button:hover {
    background-color: #129FE8;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. LOAD RAG COMPONENTS
# ==========================================

@st.cache_resource
def load_axelia():

    llm, vectorstore = get_rag_components()

    return llm, vectorstore


# ==========================================
# 4. SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# 5. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## 🏦 AXELIA")
    st.caption("BANKING INTELLIGENCE")

    st.divider()

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### Navigation")

    st.markdown("💬 Banking Assistant")
    st.markdown("📚 Knowledge Base")
    st.markdown("⚙️ About AXELIA")

    st.divider()

    st.caption("SYSTEM STATUS")

    st.success("Interface online")


# ==========================================
# 6. MAIN HEADER
# ==========================================

st.markdown(
    '<div class="axelia-title">AXELIA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="axelia-subtitle">'
    'BANKING INTELLIGENCE SYSTEM'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    '<div class="description">'
    'Your intelligent companion for understanding banking, '
    'financial services and regulatory information.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")
st.divider()


# ==========================================
# 7. FEATURE CARDS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📚 RBZ Knowledge</div>
        <p class="feature-description">
        Explore banking regulations and official documents.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🧠 AI Intelligence</div>
        <p class="feature-description">
        Answers powered by retrieval-augmented generation.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🔎 Source References</div>
        <p class="feature-description">
        Explore documents used to generate responses.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# 8. SUGGESTED QUESTIONS
# ==========================================

st.write("")

st.markdown("### What would you like to know?")

st.caption("Ask AXELIA about Zimbabwean banking.")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "Requirements for opening a bank account",
        use_container_width=True
    ):
        st.session_state.pending_question = (
            "What are the requirements for opening a bank account?"
        )

with col2:

    if st.button(
        "Explain the consumer protection framework",
        use_container_width=True
    ):
        st.session_state.pending_question = (
            "Explain the consumer protection framework."
        )


# ==========================================
# 9. DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("sources"):

            with st.expander("📚 View source documents"):

                for source in message["sources"]:

                    st.markdown(
                        f"- **{source['source']}** "
                        f"— Page {source['page']}"
                    )


# ==========================================
# 10. RECEIVE USER QUESTION
# ==========================================

user_question = st.chat_input(
    "Ask AXELIA a banking question..."
)

if "pending_question" in st.session_state:

    user_question = st.session_state.pop("pending_question")


# ==========================================
# 11. CONNECT TO RAG BACKEND
# ==========================================

if user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):

        try:

            with st.spinner("AXELIA is searching banking documents..."):

                llm, vectorstore = load_axelia()

                answer, sources = ask_axelia(
                    user_question,
                    llm,
                    vectorstore
                )

            answer = answer.replace("<br>", "\n")
            answer = answer.replace("<br/>", "\n")
            answer = answer.replace("<br />", "\n")

            st.markdown(answer)

            if sources:

                with st.expander("📚 View source documents"):

                    for source in sources:

                        st.markdown(
                            f"- **{source['source']}** "
                            f"— Page {source['page']}"
                        )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })

        except Exception as e:

            error_message = (
                "Sorry, AXELIA encountered an error while "
                "processing your question."
            )

            st.error(error_message)

            st.caption(f"Technical details: {e}")
