import pandas as pd

def limpiar_sesiones(data_frame_sucio):

    data_frame_limpio = data_frame_sucio.copy()

    # Limpiar textos
    columnas_texto = ["nombre", "tipo"]

    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    # Tipos válidos definidos por el backend
    tipos_validos = [
        "meditacion",
        "respiracion",
        "pausa",
        "estiramiento"
    ]

    data_frame_limpio["tipo"] = (
        data_frame_limpio["tipo"]
        .where(
            data_frame_limpio["tipo"].isin(tipos_validos),
            pd.NA
        )
    )

    # Conversión numérica
    data_frame_limpio["id"] = (
        pd.to_numeric(
            data_frame_limpio["id"],
            errors="coerce"
        )
        .astype("Int64")
    )

    data_frame_limpio["duracion"] = (
        pd.to_numeric(
            data_frame_limpio["duracion"],
            errors="coerce"
        )
        .astype("Int64")
    )

    # Duraciones válidas
    duraciones_validas = [
        5,
        10,
        15,
        20,
        25,
        30
    ]

    data_frame_limpio["duracion"] = (
        data_frame_limpio["duracion"]
        .where(
            data_frame_limpio["duracion"].isin(duraciones_validas),
            pd.NA
        )
    )

    # Campos obligatorios
    columnas_obligatorias = [
        "id",
        "nombre",
        "tipo",
        "duracion"
    ]

    data_frame_limpio = (
        data_frame_limpio
        .dropna(subset=columnas_obligatorias)
    )

    # IDs positivos
    data_frame_limpio = (
        data_frame_limpio[
            data_frame_limpio["id"] > 0
        ]
    )

    # Eliminar duplicados
    data_frame_limpio = (
        data_frame_limpio.drop_duplicates()
    )

    return data_frame_limpio