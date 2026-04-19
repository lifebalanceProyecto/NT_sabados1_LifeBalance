import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()
    
    # limpiar strings
    columnas_texto = ["nombre","correo","contrasena","sexo"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()
        
    #definir valores esperados
    nombres_validos = ["Camila Gomez", "Pedro Perez", "Juan Ramirez", "David Carvajal", "Alexander Ruiz", "Julian Cuartas"]
    correos_validos = ["camila123@yopmail.com", "hermoxx123@yopmail.com", "bebe@yopmail.com", "terreneitor@yopmail.com", "cuajo@yopmail.com", "alien@yopmail.com"]
    contrasenas_validas = ["ASD123", "DSA47", "KRE765", "KOF654", "KOL000", "POP666", "KKK898"]
    sexos_validos = ["femenino", "masculino", "no binario"]
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].where(data_frame_limpio["nombre"].isin(nombres_validos), pd.NA)
    data_frame_limpio["correo"] = data_frame_limpio["correo"].where(data_frame_limpio["correo"].isin(correos_validos), pd.NA)
    data_frame_limpio["contrasena"] = data_frame_limpio["contrasena"].where(data_frame_limpio["contrasena"].isin(contrasenas_validas), pd.NA)
    data_frame_limpio["sexo"] = data_frame_limpio["sexo"].where(data_frame_limpio["sexo"].isin(sexos_validos), pd.NA)
    
    #evaluar columnas numericas
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])
    
    # Evaluar fechas
    data_frame_limpio["fecha_creacion"] = pd.to_datetime(
    data_frame_limpio["fecha_creacion"],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

    # Reemplazar fechas malas por default
    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha_creacion"] = data_frame_limpio["fecha_creacion"].fillna(fecha_default)

    # ✅ Estandarizar todas al mismo formato
    data_frame_limpio["fecha_creacion"] = data_frame_limpio["fecha_creacion"].dt.strftime("%Y/%m/%d")
    
    #eliminar filas con datos faltantes
    columnas_obligatorios = ["id", "nombre", "correo", "contrasena", "sexo"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorios)
    
    #Eliminar valores invalidos a nivel numerico
    data_frame_limpio = data_frame_limpio[(data_frame_limpio["id"] > 20000000)]
    
    #Eliminar valores duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio
    
                                    

    