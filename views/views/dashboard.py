import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.title("🚀 Générateur de contenu")
    
    with st.form("form_ia"):
        biz = st.text_input("Nom du business")
        industry = st.selectbox("Secteur", ["Restaurant", "Immobilier", "Coach", "Autre"])
        goal = st.selectbox("Objectif", ["Vendre", "Plus de vues"])
        btn = st.form_submit_button("✨ Générer")
        
    if btn:
        with st.spinner("L'IA réfléchit..."):
            res = generate_social_bundle(biz, industry, "Pro", goal)
            st.write(res)
