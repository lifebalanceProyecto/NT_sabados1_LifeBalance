import pandas as pd

def transformar_datos(data_frame_limpio):

    # ==============================
    # 1. Conteo de usuarios por sexo
    # Ideal para gráfica de torta o barras
    # ==============================
    filtro1 = data_frame_limpio.query("sexo.notnull()", engine="python")
    agrupacion1 = filtro1.groupby("sexo")["id"].count().reset_index(name="conteo")


    # ==============================
    # 2. Cantidad de usuarios creados por fecha
    # Ideal para gráfica de líneas
    # ==============================
    filtro2 = data_frame_limpio.query("fecha_creacion.notnull()", engine="python")
    agrupacion2 = filtro2.groupby("fecha_creacion")["id"].count().reset_index(name="conteo")


    # ==============================
    # 3. Usuarios con ID mayor a 500 millones
    # Ideal para gráfica de barras
    # ==============================
    filtro3 = data_frame_limpio.query("id >= 500000000")
    agrupacion3 = filtro3.groupby("sexo")["id"].count().reset_index(name="conteo")


    # ==============================
    # 4. Cantidad de correos por dominio
    # Ideal para gráfica de barras horizontales
    # ==============================
    filtro4 = data_frame_limpio.copy()
    filtro4["dominio_correo"] = filtro4["correo"].str.split("@").str[1]

    agrupacion4 = (
        filtro4.groupby("dominio_correo")["id"]
        .count()
        .reset_index(name="conteo")
    )


    # ==============================
    # 5. Relación sexo vs fecha de creación
    # Ideal para mapa de calor
    # ==============================
    filtro5 = data_frame_limpio.query("sexo.notnull()", engine="python")

    agrupacion5 = (
        filtro5.groupby(["fecha_creacion", "sexo"])["id"]
        .count()
        .reset_index(name="conteo")
    )


    # ==============================
    # Diccionario resumen
    # ==============================
    transformacion_resumen = {
        "conteoUsuariosPorSexo": agrupacion1,
        "usuariosPorFechaCreacion": agrupacion2,
        "usuariosIdAltoPorSexo": agrupacion3,
        "conteoCorreosPorDominio": agrupacion4,
        "relacionSexoFechaCreacion": agrupacion5
    }

    return transformacion_resumen