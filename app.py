import streamlit as st
# import time

# from data.residuos import residuos
# from utils.seleccion_residuos import obtener_residuos

from components.pantalla_inicio import mostrar_inicio

# from components.cronometro import mostrar_cronometro
from components.tablero import mostrar_tablero
from components.reinicio import reiniciar_juego


# Variables de sesión
if "inicio" not in st.session_state:
    st.session_state.inicio = False

if "residuos_juego" not in st.session_state:
    st.session_state.residuos_juego = []

if "tiempo_inicio" not in st.session_state:
    st.session_state.tiempo_inicio = 0

if "partida" not in st.session_state:
    st.session_state.partida = 0

if "mostrar_resultados" not in st.session_state:
    st.session_state.mostrar_resultados = False

# Pantalla inicial
mostrar_inicio()

if st.session_state.inicio:
    aciertos = mostrar_tablero()

    # Botones VERIFICAR y NUEVO JUEGO en la misma fila
    col_ver, col_new = st.columns(2)

    with col_ver:
        if st.button(
            "✔ VERIFICAR RESPUESTAS",
            key=f"verificar_{st.session_state.partida}",
            use_container_width=True,
        ):
            st.session_state.mostrar_resultados = True
            st.rerun()

    with col_new:
        reiniciar_juego()
