# ============================================================
# EJEMPLO PASO A PASO
# Aquí tú decides qué función correr y cuándo mostrar cada resultado.
# ============================================================

from contador_objetos import (
    listar_imagenes_demo,
    cargar_imagen_demo,
    convertir_a_gris,
    filtrar_gaussiano,
    ecualizar_histograma,
    umbralizar_otsu,
    aplicar_morfologia,
    segmentar_componentes,
    detectar_bordes_canny,
    detectar_esquinas_harris,
    mostrar_imagen,
    mostrar_comparacion,
    mostrar_resultado_final
)


print("Imágenes precargadas disponibles:", listar_imagenes_demo())

# =====================
# 1. Cargar imagen demo
# =====================
img_bgr, img_rgb, ruta = cargar_imagen_demo("img3")
print("Ruta de la imagen usada:", ruta)

mostrar_imagen(img_rgb, "1. Imagen original")

# =====================
# 2. Convertir a gris
# =====================
gray = convertir_a_gris(img_bgr)
mostrar_imagen(gray, "2. Conversión RGB/BGR a escala de grises", cmap="gray")

# =====================
# 3. Filtrado gaussiano
# =====================
blur = filtrar_gaussiano(gray, kernel_size=5, sigma=1)
mostrar_imagen(blur, "3. Preprocesamiento: filtrado Gaussiano", cmap="gray")

# =====================
# 4. Transformación de intensidad
# =====================
gray_eq = ecualizar_histograma(blur)
mostrar_imagen(gray_eq, "4. Transformación de intensidad: ecualización", cmap="gray")

# =====================
# 5. Umbralización Otsu
# =====================
umbral, binaria = umbralizar_otsu(blur, invertir=True)
print("Umbral calculado por Otsu:", umbral)
mostrar_imagen(binaria, "5. Umbralización Otsu", cmap="gray")

# =====================
# 6. Morfología
# =====================
binaria_limpia = aplicar_morfologia(
    binaria,
    kernel_size=5,
    apertura_iter=1,
    cierre_iter=1
)

mostrar_comparacion(
    binaria,
    binaria_limpia,
    "Otsu",
    "Morfología: apertura y cierre",
    "gray",
    "gray"
)

# =====================
# 7. Segmentación por regiones y conteo
# =====================
resultado, conteo, tabla, labels = segmentar_componentes(
    binaria_limpia,
    img_rgb,
    area_minima=2000
)

print("Conteo final:", conteo)
print(tabla)

mostrar_resultado_final(resultado, conteo)

# =====================
# 8. Detección de bordes
# =====================
bordes = detectar_bordes_canny(gray_eq, umbral1=50, umbral2=150)
mostrar_imagen(bordes, "8. Detección de bordes - Canny", cmap="gray")

# =====================
# 9. Detección de esquinas
# =====================
harris, harris_vis = detectar_esquinas_harris(gray_eq, img_rgb)
mostrar_imagen(harris_vis, "9. Detección de esquinas - Harris")
