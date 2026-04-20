import pandas as pd

def limpiar_sesiones(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    ## limpiar strings 
    columnas_texto=["nombre","tipo"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

    ## definir valores
    tipos_validos=["meditacion","respiracion","pausa","estiramiento"]
    data_frame_limpio["tipo"]=data_frame_limpio["tipo"].where(data_frame_limpio["tipo"].isin(tipos_validos),pd.NA)

    nombres_validos=["meditacion para dormir","respiracion","pausa activa oficina","estiramiento"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(data_frame_limpio["nombre"].isin(nombres_validos),pd.NA)

    ## numericas
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce").astype("Int64")
    
    data_frame_limpio["duracion"] = pd.to_numeric(data_frame_limpio["duracion"], errors="coerce").astype("Int64")
    
    ##valida duracion
    duraciones_validas=[5,10,15,20,25,30]
    data_frame_limpio["duracion"]=data_frame_limpio["duracion"].where(data_frame_limpio["duracion"].isin(duraciones_validas),pd.NA)

    ## registros nulos
    columnas_obligatorias=["id","nombre","tipo","duracion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    ## valores invalidos a nivel numerico
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]

    #valores duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio







        