import streamlit as st

def show():
    st.markdown("<h1 style='text-align: center; color: #6366f1;'>GhostContent AI 👻</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Générez votre contenu réseaux sociaux en 30 secondes.</h3>", unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎁 Plan Gratuit\nAccès limité")
        if st.button("Essayer gratuitement"):
            st.session_state.user = {"email": "demo@test.com"}
            st.rerun()
    with col2:
        st.success("### 🚀 Plan Pro\nContenu illimité")
        st.button("S'abonner (Stripe)")
