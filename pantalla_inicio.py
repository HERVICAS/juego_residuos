import streamlit as st
import time

from data.residuos import residuos
from utils.seleccion_residuos import obtener_residuos


def mostrar_inicio():

    st.markdown(
        """
        <h1 style='text-align:center; color:#2E8B57;'>
            ♻️ EN CLARIOS CLASIFICANDO ANDO
        </h1>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.inicio:
        st.subheader("Es tu Turno de Clasificar Correctamente!")

        if st.button("COMENZAR"):
            st.session_state.inicio = True

            st.session_state.residuos_juego = obtener_residuos(residuos)

            st.session_state.tiempo_inicio = time.time()

            st.rerun()
