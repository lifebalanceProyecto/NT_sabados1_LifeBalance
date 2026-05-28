# Se importa matplotlib para crear los gráficos
import matplotlib.pyplot as plt

# Se importa seaborn para crear mapas de calor con mejor visualización
import seaborn as sns

# Se importa os para manejar rutas y carpetas
import os


# Ruta donde se almacenarán las imágenes generadas
RUTA_GRAFICOS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "LifeBalanceFrontend",
    "output_frontend",
    "public",
    "graficos"
)


def crear_ruta_si_no_existe(ruta_destino):

    # Se crea la carpeta destino en caso de que no exista
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_lineas(
        datos_agrupados,
        columna_eje_x,
        columna_eje_y,
        titulo="Grafico de lineas",
        color_linea="#2196F3",
        nombre_archivo="lineas.png",
        ruta_destino=RUTA_GRAFICOS):

    # Dibuja un gráfico de líneas para visualizar tendencias
    # Recibe un DataFrame agrupado y las columnas para cada eje

    # Se asegura de que la carpeta donde se guardará la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se crea la figura y el área de dibujo
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Se dibuja la línea con marcadores circulares
    area_dibujo.plot(
        datos_agrupados[columna_eje_x],
        datos_agrupados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2
    )

    # Se establece el título del gráfico
    area_dibujo.set_title(titulo, fontsize=14)

    # Se establece el nombre del eje X
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)

    # Se establece el nombre del eje Y
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)

    # Se activa una cuadrícula para facilitar la lectura
    area_dibujo.grid(True, linestyle="--", alpha=0.6)

    # Se rotan las etiquetas del eje X para evitar sobreposición
    plt.xticks(rotation=45)

    # Se ajustan los espacios automáticamente
    plt.tight_layout()

    # Se construye la ruta completa donde se guardará la imagen
    ruta_completa = os.path.join(
        ruta_destino,
        nombre_archivo
    )

    # Se guarda la imagen
    figura.savefig(ruta_completa)

    # Se libera memoria cerrando la figura
    plt.close(figura)

    # Se informa dónde quedó almacenado el gráfico
    print(f"Grafico de lineas guardado en: {ruta_completa}")


def graficar_barras(
        datos_agrupados,
        columna_categorias,
        columna_valores,
        titulo="Grafico de barras",
        color_barras="#4CAF50",
        nombre_archivo="barras.png",
        ruta_destino=RUTA_GRAFICOS):

    # Dibuja un gráfico de barras para comparar categorías
    # Recibe un DataFrame agrupado con categorías y valores

    # Se asegura de que la carpeta donde se guardará la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se crea la figura y el área de dibujo
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Se dibujan las barras utilizando el color indicado
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )

    # Se establece el título del gráfico
    area_dibujo.set_title(titulo, fontsize=14)

    # Se establece el nombre del eje X
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)

    # Se establece el nombre del eje Y
    area_dibujo.set_ylabel(columna_valores, fontsize=12)

    # Se rotan las etiquetas del eje X para evitar sobreposición
    plt.xticks(rotation=45)

    # Se ajustan automáticamente los espacios
    plt.tight_layout()

    # Se construye la ruta completa del archivo
    ruta_completa = os.path.join(
        ruta_destino,
        nombre_archivo
    )

    # Se guarda la imagen
    figura.savefig(ruta_completa)

    # Se libera memoria cerrando la figura
    plt.close(figura)

    # Se informa dónde quedó almacenado el gráfico
    print(f"Grafico de barras guardado en: {ruta_completa}")


def graficar_torta(
        datos_agrupados,
        columna_etiquetas,
        columna_valores,
        titulo="Grafico de torta",
        lista_colores=None,
        nombre_archivo="torta.png",
        ruta_destino=RUTA_GRAFICOS):

    # Dibuja un gráfico de torta para visualizar proporciones
    # Recibe etiquetas y valores numéricos

    # Se asegura de que la carpeta donde se guardará la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Si no se especifican colores se utiliza una paleta por defecto
    if lista_colores is None:
        lista_colores = [
            "#FF9800",
            "#2196F3",
            "#4CAF50",
            "#E91E63",
            "#9C27B0"
        ]

    # Se crea la figura y el área de dibujo
    figura, area_dibujo = plt.subplots(figsize=(8, 8))

    # Se obtiene la cantidad de categorías
    cantidad_categorias = len(datos_agrupados)

    # Se construye el gráfico de torta
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={
            "edgecolor": "black",
            "linewidth": 0.5
        }
    )

    # Se establece el título del gráfico
    area_dibujo.set_title(titulo, fontsize=14)

    # Se ajustan automáticamente los espacios
    plt.tight_layout()

    # Se construye la ruta completa del archivo
    ruta_completa = os.path.join(
        ruta_destino,
        nombre_archivo
    )

    # Se guarda la imagen
    figura.savefig(ruta_completa)

    # Se libera memoria cerrando la figura
    plt.close(figura)

    # Se informa dónde quedó almacenado el gráfico
    print(f"Grafico de torta guardado en: {ruta_completa}")


def graficar_mapa_calor(
        datos_agrupados,
        columna_filas,
        columna_columnas,
        columna_valores,
        titulo="Mapa de calor",
        paleta_color="YlOrRd",
        nombre_archivo="mapa_calor.png",
        ruta_destino=RUTA_GRAFICOS):

    # Dibuja un mapa de calor utilizando una tabla pivote
    # Recibe columnas para filas, columnas y valores

    # Se asegura de que la carpeta donde se guardará la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se construye una tabla pivote para organizar los datos
    tabla_pivote = datos_agrupados.pivot_table(
    index=columna_filas,
    columns=columna_columnas,
    values=columna_valores,
    aggfunc="sum",
    fill_value=0
    )

    # Convertir todos los valores a float para seaborn
    tabla_pivote = tabla_pivote.astype(float)

    # Se crea la figura y el área de dibujo
    figura, area_dibujo = plt.subplots(figsize=(10, 6))

    # Se dibuja el mapa de calor
    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap=paleta_color,
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )

    # Se establece el título del gráfico
    area_dibujo.set_title(titulo, fontsize=14)

    # Se rotan las etiquetas del eje X
    plt.xticks(rotation=45)

    # Se ajustan automáticamente los espacios
    plt.tight_layout()

    # Se construye la ruta completa del archivo
    ruta_completa = os.path.join(
        ruta_destino,
        nombre_archivo
    )

    # Se guarda la imagen
    figura.savefig(ruta_completa)

    # Se libera memoria cerrando la figura
    plt.close(figura)

    # Se informa dónde quedó almacenado el gráfico
    print(f"Mapa de calor guardado en: {ruta_completa}")