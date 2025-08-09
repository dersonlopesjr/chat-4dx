# streamlit_app.py - TESTE DE SECRETS
import streamlit as st

# --- Teste de leitura dos secrets ---
st.set_page_config(page_title="🔧 Teste de Secrets", page_icon="🔧")
st.title("🔧 Teste de Chave API")

try:
    api_key = st.secrets["GROQ_API_KEY = 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"]
    st.success("✅ Chave API encontrada!")
    st.write("A chave foi carregada com sucesso.")
except Exception as e:
    st.error(f"❌ Erro ao ler a chave: {str(e)}")
    st.stop()

# Mostra os nomes das chaves (opcional, para debug)
st.write("Chaves disponíveis em `st.secrets`: ", list(st.secrets.keys()))
