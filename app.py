import streamlit as st
# import time



# from data.residuos import residuos
# from utils.seleccion_residuos import obtener_residuos

from components.pantalla_inicio import mostrar_inicio

# from components.cronometro import mostrar_cronometro
from components.tablero import mostrar_tablero
#from components.reinicio import reiniciar_juego


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


# Si el juego ya comenzó
if st.session_state.inicio:
    # Cronómetro
    # tiempo_restante = mostrar_cronometro()

    # Tablero
    aciertos = mostrar_tablero()

    # Reinicio manual
    #reiniciar_juego()
    # Cronómetro
    # tiempo_restante = mostrar_cronometro()

    # Tablero
    aciertos = mostrar_tablero()
