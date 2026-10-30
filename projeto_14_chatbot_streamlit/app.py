
import streamlit as st
from backend import gerar_resposta

st.set_page_config(
    page_title="Meu Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Estilo visual
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}
h1 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    st.title("🤖 Meu Chatbot")
    st.caption("Seu assistente de inteligência artificial")

    if st.button("➕ Nova conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.divider()
    st.markdown("### Navegação")
    pagina = st.radio(
        "Escolha uma aba",
        ["💬 Chat", "ℹ️ Sobre"]
    )

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if pagina == "💬 Chat":
    st.title("Como posso ajudar?")
    st.write("Converse comigo sobre programação, estudos e muito mais.")

    # Mostrar histórico
    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

    # Campo para enviar mensagens
    pergunta = st.chat_input("Digite sua mensagem...")

    if pergunta:
        st.session_state.mensagens.append({
            "role": "user",
            "content": pergunta
        })

        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    resposta = gerar_resposta(
                        st.session_state.mensagens
                    )
                    st.markdown(resposta)

                    st.session_state.mensagens.append({
                        "role": "assistant",
                        "content": resposta
                    })

                except Exception:
                    st.error(
                        "Não consegui gerar uma resposta. "
                        "Verifique sua chave da Groq e a conexão."
                    )

elif pagina == "ℹ️ Sobre":
    st.title("Sobre o projeto")
    st.write("""
    Este chatbot foi desenvolvido com:

    - Python
    - Streamlit
    - Groq API
    - Inteligência artificial

    O backend processa as mensagens e a interface
    apresenta a conversa.
    """)
