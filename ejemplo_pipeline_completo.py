# ============================================================
# EJEMPLO COMPLETO
# Este archivo corre todo el pipeline de jalón.
# ============================================================

from contador_objetos import procesar_demo, listar_imagenes_demo

print("Imágenes demo disponibles:", listar_imagenes_demo())

resultados = procesar_demo(
    "img3",
    area_minima=2000,
    mostrar=True,
    guardar_csv=True,
    ruta_csv="resultados_img3.csv"
)

print("Conteo obtenido:", resultados["conteo"])
print(resultados["tabla"])
