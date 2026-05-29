import pandas as pd

from notebook.descripcion_recomendaciones import describir_datos_recomendaciones
from notebook.limpieza_recomendaciones import limpiar_recomendaciones
from utils.Simulacion_Recomendaciones import simulacion_recomendaciones

from utils.simulacion_usuarios import simular_usuarios
from notebook.limpieza_usuarios import limpiar_usuarios
from notebook.descripcion_usuarios import describir_datos_usuarios
from notebook.consumo_usuarios import consumir_servicios_tabla_servicios
from notebook.transformacion_usuarios import transformar_datos_usuarios
from notebook.graficacion_usuarios import (graficar_barras,graficar_lineas,graficar_torta,graficar_mapa_calor)
 

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



# ==========================================
# USUARIOS
# ==========================================
describir_datos_usuarios(
    simulaciones_limpias_usuarios
)

# ==========================================
# TRANSFORMACIONES
# ==========================================
agrupaciones_usuarios = transformar_datos(
    simulaciones_limpias_usuarios
)

# ==========================================
# GRÁFICO DE TORTA
# Usuarios por sexo
# ==========================================
graficar_torta(
    agrupaciones_usuarios["agrupacion1"],
    columna_etiquetas="sexo",
    columna_valores="conteoUsuarios",
    titulo="Distribucion de usuarios por sexo",
    nombre_archivo="torta_usuarios_sexo.png"
)

# ==========================================
# GRÁFICO DE LÍNEAS
# Usuarios por fecha creación
# ==========================================
graficar_lineas(
    agrupaciones_usuarios["agrupacion2"],
    columna_eje_x="fecha_creacion",
    columna_eje_y="conteoUsuarios",
    titulo="Usuarios creados por fecha",
    color_linea="#2196F3",
    nombre_archivo="lineas_usuarios_fecha.png"
)

# ==========================================
# GRÁFICO DE BARRAS
# Usuarios ID alto por sexo
# ==========================================
graficar_barras(
    agrupaciones_usuarios["agrupacion3"],
    columna_categorias="sexo",
    columna_valores="conteoUsuarios",
    titulo="Usuarios con ID alto por sexo",
    color_barras="#4CAF50",
    nombre_archivo="barras_usuarios_id_alto.png"
)

# ==========================================
# GRÁFICO DE BARRAS
# Correos por dominio
# ==========================================
graficar_barras(
    agrupaciones_usuarios["agrupacion4"],
    columna_categorias="dominio_correo",
    columna_valores="conteoCorreos",
    titulo="Cantidad de correos por dominio",
    color_barras="#FF9800",
    nombre_archivo="barras_correos_dominio.png"
)

# ==========================================
# MAPA DE CALOR
# Sexo vs fecha creación
# ==========================================
graficar_mapa_calor(
    agrupaciones_usuarios["agrupacion5"],
    columna_filas="fecha_creacion",
    columna_columnas="sexo",
    columna_valores="conteo",
    titulo="Relacion sexo vs fecha creacion",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_usuarios.png"
)




