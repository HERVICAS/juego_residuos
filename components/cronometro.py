import streamlit as st
import time


def mostrar_cronometro():

    tiempo_total = 30

    tiempo_transcurrido = int(
        time.time() - st.session_state.tiempo_inicio
    )

    tiempo_restante = tiempo_total - tiempo_transcurrido

    if tiempo_restante < 0:
        tiempo_restante = 0

    st.metric(
        "⏱ Tiempo restante",
        f"{tiempo_restante} segundos"
    )

    return tiempo_restante