from .datos import obtener_ruta_imagen
from .preprocesamiento import cargar_imagen, convertir_a_gris, filtrar_gaussiano, ecualizar_histograma
from .segmentacion import umbralizar_otsu, aplicar_morfologia, segmentar_componentes
from .caracteristicas import detectar_bordes_canny, detectar_esquinas_harris
from .visualizacion import mostrar_resultados


def procesar_imagen(
    ruta,
    area_minima=2000,
    kernel_gaussiano=5,
    sigma=1,
    kernel_morfologia=5,
    invertir_otsu=True,
    mostrar=True,
    guardar_csv=False,
    ruta_csv="resultados_objetos.csv"
):
    """
    Ejecuta el pipeline completo de una sola vez.
    """
    img_bgr, img_rgb = cargar_imagen(ruta)
    gray = convertir_a_gris(img_bgr)
    blur = filtrar_gaussiano(gray, kernel_size=kernel_gaussiano, sigma=sigma)
    gray_eq = ecualizar_histograma(blur)
    umbral_otsu, binaria = umbralizar_otsu(blur, invertir=invertir_otsu)

    binaria_limpia = aplicar_morfologia(
        binaria,
        kernel_size=kernel_morfologia,
        apertura_iter=1,
        cierre_iter=1
    )

    resultado, conteo, tabla, labels = segmentar_componentes(
        binaria_limpia,
        img_rgb,
        area_minima=area_minima
    )

    bordes = detectar_bordes_canny(gray_eq, umbral1=50, umbral2=150)
    harris, harris_vis = detectar_esquinas_harris(gray_eq, img_rgb)

    resultados = {
        "ruta": str(ruta),
        "imagen_rgb": img_rgb,
        "gris": gray,
        "filtrada": blur,
        "ecualizada": gray_eq,
        "umbral_otsu": umbral_otsu,
        "binaria": binaria,
        "binaria_limpia": binaria_limpia,
        "labels": labels,
        "resultado": resultado,
        "conteo": conteo,
        "tabla": tabla,
        "bordes": bordes,
        "harris": harris,
        "harris_vis": harris_vis
    }

    print("Umbral calculado por Otsu:", umbral_otsu)
    print("\nNúmero total de objetos detectados:", conteo)
    print("\nPropiedades básicas de los objetos detectados:")
    print(tabla)

    if guardar_csv:
        tabla.to_csv(ruta_csv, index=False)
        print(f"\nTabla guardada en: {ruta_csv}")

    if mostrar:
        mostrar_resultados(resultados)

    return resultados


def procesar_demo(
    nombre,
    area_minima=2000,
    kernel_gaussiano=5,
    sigma=1,
    kernel_morfologia=5,
    invertir_otsu=True,
    mostrar=True,
    guardar_csv=False,
    ruta_csv="resultados_objetos.csv"
):
    """
    Procesa una de las imágenes precargadas:
    img1, img2 o img3.
    """
    ruta = obtener_ruta_imagen(nombre)

    return procesar_imagen(
        ruta,
        area_minima=area_minima,
        kernel_gaussiano=kernel_gaussiano,
        sigma=sigma,
        kernel_morfologia=kernel_morfologia,
        invertir_otsu=invertir_otsu,
        mostrar=mostrar,
        guardar_csv=guardar_csv,
        ruta_csv=ruta_csv
    )
