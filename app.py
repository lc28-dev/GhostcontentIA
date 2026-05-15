import streamlit as st
from views import landing, dashboard, history, settings

st.set_page_config(page_title="GhostContent AI", page_icon="👻", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

def main():
    if st.session_state.user:
        st.sidebar.title("👻 GhostContent")
        page = st.sidebar.radio("Menu", ["Générateur", "Historique", "Mon Compte", "Déconnexion"])
        
        if page == "Générateur":
            dashboard.show()
        elif page == "Historique":
            history.show()
        elif page == "Mon Compte":
            settings.show()
        elif page == "Déconnexion":
            st.session_state.user = None
            st.rerun()
    else:
        landing.show()

if __name__ == "__main__":
    main()
