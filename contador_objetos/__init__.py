"""
contador_objetos

Librería para segmentar, contar y caracterizar objetos en imágenes cenitales.

Esta versión permite trabajar paso por paso:
- cargar imagen
- convertir a gris
- filtrar
- ecualizar
- umbralizar
- aplicar morfología
- segmentar regiones
- detectar bordes
- detectar esquinas
- contar objetos
"""

from .datos import listar_imagenes_demo, obtener_ruta_imagen, cargar_imagen_demo
from .preprocesamiento import cargar_imagen, convertir_a_gris, filtrar_gaussiano, ecualizar_histograma
from .segmentacion import umbralizar_otsu, aplicar_morfologia, segmentar_componentes
from .caracteristicas import detectar_bordes_canny, detectar_esquinas_harris
from .visualizacion import mostrar_imagen, mostrar_comparacion, mostrar_resultado_final
from .pipeline import procesar_imagen, procesar_demo

__all__ = [
    "listar_imagenes_demo",
    "obtener_ruta_imagen",
    "cargar_imagen_demo",
    "cargar_imagen",
    "convertir_a_gris",
    "filtrar_gaussiano",
    "ecualizar_histograma",
    "umbralizar_otsu",
    "aplicar_morfologia",
    "segmentar_componentes",
    "detectar_bordes_canny",
    "detectar_esquinas_harris",
    "mostrar_imagen",
    "mostrar_comparacion",
    "mostrar_resultado_final",
    "procesar_imagen",
    "procesar_demo",
]
