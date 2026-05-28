import pandas as pd

from notebook.descripcion_recomendaciones import describir_datos_recomendaciones
from notebook.limpieza_recomendaciones import limpiar_recomendaciones
from utils.Simulacion_Recomendaciones import simulacion_recomendaciones

from utils.simulacion_usuarios import simular_usuarios
from notebook.limpieza_usuarios import limpiar_usuarios
from notebook.descripcion_usuarios import describir_datos_usuarios

from notebook.limpieza_sesiones import limpiar_sesiones
from notebook.descripcion_sesiones import describir_datos_sesiones
from notebook.transformacion_sesiones import transformar_datos
from notebook.graficacion_sesiones import (graficar_barras,graficar_lineas,graficar_torta,graficar_mapa_calor)
from notebook.consumo_sesiones import consumir_tabla_sesion

simulaciones_usuarios = simular_usuarios(100)
simulaciones_ordenadas_usuarios = pd.DataFrame(simulaciones_usuarios)
simulaciones_limpias_usuarios = limpiar_usuarios(simulaciones_ordenadas_usuarios)
print(simulaciones_limpias_usuarios)
describir_datos_usuarios(simulaciones_limpias_usuarios)

simulacion_recomendaciones = simulacion_recomendaciones(50)
simulaciones_ordenadas_recomendaciones = pd.DataFrame(simulacion_recomendaciones)
simulaciones_limpias_recomendaciones = limpiar_recomendaciones(simulaciones_ordenadas_recomendaciones)
describir_datos_recomendaciones(simulaciones_limpias_recomendaciones)


# SESIONES

sesiones = consumir_tabla_sesion()

simulacion_ordenada_sesiones = pd.DataFrame(
    sesiones
)

simulaciones_limpias_sesiones = limpiar_sesiones(
    simulacion_ordenada_sesiones
)

describir_datos_sesiones(
    simulaciones_limpias_sesiones
)

agrupaciones_sesiones = transformar_datos(
    simulaciones_limpias_sesiones
)
agrupaciones_sesiones = transformar_datos(simulaciones_limpias_sesiones)

# Gráfico de barras: cantidad de sesiones por tipo
graficar_barras(
    agrupaciones_sesiones["agrupacion1"],
    columna_categorias="tipo",
    columna_valores="conteoSesiones",
    titulo="Cantidad de sesiones por tipo",
    color_barras="#4CAF50",
    nombre_archivo="barras_sesiones_tipo.png"
)

# Gráfico de líneas: duración promedio por tipo
graficar_lineas(
    agrupaciones_sesiones["agrupacion2"],
    columna_eje_x="tipo",
    columna_eje_y="promedioDuracion",
    titulo="Duración promedio por tipo",
    color_linea="#2196F3",
    nombre_archivo="lineas_duracion_tipo.png"
)

# Gráfico de torta: distribución de sesiones por nombre
graficar_torta(
    agrupaciones_sesiones["agrupacion3"],
    columna_etiquetas="nombre",
    columna_valores="cantidadSesiones",
    titulo="Distribución de sesiones por nombre",
    nombre_archivo="torta_sesiones_nombre.png"
)

# Mapa de calor: tipo vs nombre
graficar_mapa_calor(
    agrupaciones_sesiones["agrupacion5"],
    columna_filas="tipo",
    columna_columnas="nombre",
    columna_valores="conteo",
    titulo="Cantidad de sesiones por tipo y nombre",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_sesiones.png"
)



