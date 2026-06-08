import streamlit as st
import time

from data.residuos import residuos
from utils.seleccion_residuos import obtener_residuos


def reiniciar_juego():
    # Key con partida para que sea un botón nuevo cada partida
    if st.button("🔄 NUEVO JUEGO", key=f"nuevo_juego_{st.session_state.partida}"):
        st.session_state.partida += 1
        st.session_state.inicio = True
        st.session_state.residuos_juego = obtener_residuos(residuos)
        st.session_state.tiempo_inicio = time.time()
        st.session_state.mostrar_resultados = False

        for clave in list(st.session_state.keys()):
            if clave.startswith("respuesta_"):
                del st.session_state[clave]

        st.rerun()
