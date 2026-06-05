import streamlit as st
from engine.classifier import IntentClassifier
from engine.rag_chatbot import RAGChatbot

st.set_page_config(page_title="JhaMobi Virtual Assistant", layout="wide")
st.title("🤖 JhaMobi Intelligent Corporate Assistant")
st.caption("Commercial-grade local AI engine powered by an explicit semantic keyword-routing matrix.")

@st.cache_resource
def load_engines():
    classifier = IntentClassifier()
    kb_path = "data/knowledge_base.txt"
    chatbot = RAGChatbot(kb_path)
    return classifier, chatbot

classifier, chatbot = load_engines()

# Manage session memory states
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! I am the JhaMobi Technologies automated system assistant. How can I guide your inquiry regarding our HealthTech software, secure cloud setups, or custom AI solutions today?"}
    ]

# Render conversational history logs
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Inquire about JhaMobi Technologies..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Processing local query alignment..."):
            
            # Step 1: Route greetings or pass directly to knowledge map
            route = classifier.predict(prompt)
            
            if route == "greeting":
                response = "Hello! I am ready to assist you. Ask me anything about JhaMobi's core services, founding year, or hospital solutions."
            elif route == "identity":
                response = "I am the JhaMobi Technologies Intelligent Virtual Assistant, built to provide secure, instantaneous answers from our local knowledge base."
            else:
                response = chatbot.ask(prompt)
            
            with st.expander("🔧 System Routing Diagnostics"):
                st.info(f"Target Sublinear Routing Path: **{route.upper()}**")
            
            st.markdown(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})