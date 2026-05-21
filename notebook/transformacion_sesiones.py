import pandas as pd

def transformar_datos(dataf_frame_limpio):

    # =========================
    # 1. Cantidad de sesiones por tipo
    # Grafica recomendada: Barras
    # =========================
    filtro1 = dataf_frame_limpio.query("duracion >= 0")
    
    agrupacion1 = (
        filtro1.groupby("tipo")["id"]
        .count()
        .reset_index(name="conteoSesiones")
    )


    # =========================
    # 2. Duración promedio por tipo
    # Grafica recomendada: Líneas
    # =========================
    filtro2 = dataf_frame_limpio.query("duracion > 20")
    
    agrupacion2 = (
        filtro2.groupby("tipo")["duracion"]
        .mean()
        .reset_index(name="promedioDuracion")
    )


    # =========================
    # 3. Cantidad de sesiones por nombre
    # Grafica recomendada: Torta
    # =========================
    filtro3 = dataf_frame_limpio.query("id > 0")
    
    agrupacion3 = (
        filtro3.groupby("nombre")["id"]
        .count()
        .reset_index(name="cantidadSesiones")
    )


    # =========================
    # 4. Duración total por nombre
    # Grafica recomendada: Barras horizontales
    # =========================
    filtro4 = dataf_frame_limpio.query("duracion >= 30")
    
    agrupacion4 = (
        filtro4.groupby("nombre")["duracion"]
        .sum()
        .reset_index(name="duracionTotal")
    )


    # =========================
    # 5. Relación tipo vs duración promedio
    # Grafica recomendada: Mapa de calor
    # =========================
    filtro5 = dataf_frame_limpio.query("duracion > 10")
    
    agrupacion5 = (
        filtro5.pivot_table(
            values="duracion",
            index="tipo",
            columns="nombre",
            aggfunc="mean"
        )
    )


    transformacion_resume = {
        "conteoSesionesPorTipo": agrupacion1,
        "promedioDuracionPorTipo": agrupacion2,
        "cantidadSesionesPorNombre": agrupacion3,
        "duracionTotalPorNombre": agrupacion4,
        "mapaCalorTipoNombre": agrupacion5
    }

    return transformacion_resume