import pandas as pd

def describir_datos_usuarios(data_frame_limpio):
    print(f"Numero de filas: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles {list(data_frame_limpio.columns)}")
    print(f"estadisticas {data_frame_limpio[["id"]].describe()}")
    print(f"Valores categoricos {data_frame_limpio["nombre"].value_counts()}")
    print(f"Valores categoricos {data_frame_limpio["correo"].value_counts()}")
    print(f"Valores categoricos {data_frame_limpio["contrasena"].value_counts()}")
    print(f"Valores categoricos {data_frame_limpio["sexo"].value_counts()}")
    print(f"Fecha minima {data_frame_limpio["fecha_creacion"].min()}")
    print(f"Fecha maxima {data_frame_limpio["fecha_creacion"].max()}")
