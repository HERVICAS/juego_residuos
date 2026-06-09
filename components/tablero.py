import streamlit as st
import base64


def imagen_base64(ruta):
    with open(ruta, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{data}"


def mostrar_tablero():
    st.markdown(
        """
    <style>
    /* Todos los botones de caneca base */
    div[data-testid="column"] [data-testid="stButton"] button {
        font-weight: bold !important;
        font-size: 11px !important;
        border-radius: 8px !important;
    }
    /* Blanco - 1er botón de cada grupo */
    div[data-testid="column"]:nth-child(1) [data-testid="stButton"] button {
    background-color: white !important;
    border: 3px solid #999 !important;
    height: 80px !important;
    
    /* Negro - 2do botón */
    div[data-testid="column"]:nth-child(2) [data-testid="stButton"] button {
        background-color: #333 !important;
        color: #fff !important;
        border: 2px solid #111 !important;
    }
    /* Rojo - 3er botón */
    div[data-testid="column"]:nth-child(3) [data-testid="stButton"] button {
        background-color: #cc2200 !important;
        color: #fff !important;
        border: 2px solid #aa1100 !important;
    }
    /* Verde - 4to botón */
    div[data-testid="column"]:nth-child(4) [data-testid="stButton"] button {
        background-color: #1a7a1a !important;
        color: #fff !important;
        border: 2px solid #145214 !important;
    }
    </style>
""",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("assets/imagenes/BLANCA.png", width=120)
    with col2:
        st.image("assets/imagenes/NEGRA.png", width=120)
    with col3:
        st.image("assets/imagenes/ROJA.png", width=120)
    with col4:
        st.image("assets/imagenes/VERDE.png", width=120)

    st.divider()
    st.subheader("Clasifica correctamente los siguientes residuos:")

    columnas = st.columns(2)

    aciertos = 0

    for i, residuo in enumerate(st.session_state.residuos_juego):
        with columnas[i % 2]:
            contenedor = st.container(border=True)

            with contenedor:
                st.image(residuo["imagen"], width=150)

                key_base = f"respuesta_{st.session_state.partida}_{i}"

                b1, b2, b3, b4 = st.columns(4)

                with b1:
                    if st.button("◻", key=f"{key_base}_b", use_container_width=True):
                        st.session_state[key_base] = "BLANCA"

                with b2:
                    if st.button(
                        "⬛",
                        key=f"{key_base}_n",
                        use_container_width=True,
                    ):
                        st.session_state[key_base] = "NEGRA"

                with b3:
                    if st.button(
                        "🟥",
                        key=f"{key_base}_r",
                        use_container_width=True,
                    ):
                        st.session_state[key_base] = "ROJA"

                with b4:
                    if st.button(
                        "🟩",
                        key=f"{key_base}_v",
                        use_container_width=True,
                    ):
                        st.session_state[key_base] = "VERDE"

                respuesta_actual = st.session_state.get(key_base, "")

                if respuesta_actual:
                    st.caption(f"Seleccionaste: {respuesta_actual}")

                if st.session_state.mostrar_resultados:
                    if respuesta_actual == residuo["contenedor"]:
                        st.success("✅ CORRECTO")

                        aciertos += 1

                    else:
                        st.error(f"❌ INCORRECTO — Era: {residuo['contenedor']}")

    # ==================================================
    # MENSAJE FINAL (UNA SOLA VEZ)
    # ==================================================

    if st.session_state.mostrar_resultados:
        total_residuos = len(st.session_state.residuos_juego)

        st.divider()

        if aciertos == total_residuos:
            st.balloons()

            st.markdown(
                """
                <h2 style='text-align:center;color:green'>
                🎉 EXCELENTE, CONTINÚA CON TU BUENA
                CLASIFICACIÓN DE RESIDUOS
                </h2>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(
                """
                <h2 style='text-align:center;color:orange'>
                ⚠️ SIGUE INTENTÁNDOLO,
                TEN PRESENTE SIEMPRE EL CÓDIGO DE COLORES
                </h2>
                """,
                unsafe_allow_html=True,
            )

    # ==================================================
    # BOTONES INFERIORES
    # ==================================================

    st.divider()

    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])

    with col_btn1:
        if st.button(
            "✔ VERIFICAR RESPUESTAS", key=f"verificar_{st.session_state.partida}"
        ):
            st.session_state.mostrar_resultados = True
            st.rerun()

    with col_btn2:
        if st.button("🔄 NUEVO JUEGO", key="nuevo_juego_final"):
            st.session_state.partida += 1
            st.session_state.mostrar_resultados = False

            # borrar respuestas anteriores
            for clave in list(st.session_state.keys()):
                if clave.startswith("respuesta_"):
                    del st.session_state[clave]

            st.rerun()

    return aciertos
