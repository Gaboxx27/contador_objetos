# ============================================================
# EJEMPLO PASO A PASO DE LA LIBRERÍA contador_objetos
# Proyecto 2, Segmentación y conteo de objetos
# Este archivo muestra cómo usar la librería paso por paso
# No guarda imágenes
# No guarda CSV
# No imprime tablas completas
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
    mostrar_resultado_final,
    procesar_demo
)










# ============================================================
# FUNCIÓN PARA HACER PAUSAS
# ============================================================

def pausar(mensaje="Presiona ENTER para continuar"):
    # Esta pausa sirve para poder explicar cada paso antes de avanzar
    input(f"\n{mensaje}")










# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    # Se muestra un título al iniciar el programa
    print("====================================================")
    print(" EJEMPLO PASO A PASO DE contador_objetos")
    print(" Proyecto 2, Segmentación y conteo de objetos")
    print("====================================================")










    # ========================================================
    # 1, Revisar que la librería funcione
    # ========================================================

    print("\n1, Verificación de la librería")
    print("Primero se revisa si la librería encuentra sus imágenes de prueba")

    # Se buscan las imágenes que vienen incluidas en la librería
    imagenes = listar_imagenes_demo()

    # Se muestran las imágenes encontradas
    print("\nImágenes disponibles:")
    print(imagenes)

    # Si no se encuentran imágenes, el programa se detiene
    if len(imagenes) == 0:
        print("\nNo se encontraron imágenes demo")
        return

    pausar()










    # ========================================================
    # 2, Cargar una imagen
    # ========================================================

    print("\n2, Carga de imagen")
    print("Se usará img3 porque es la imagen principal del proyecto")

    # Aquí se elige la imagen que se va a usar
    nombre_imagen = "img3"

    # Se carga la imagen desde la librería
    # img_bgr se usa para trabajar la imagen internamente
    # img_rgb se usa para mostrar la imagen con colores correctos
    # ruta guarda la ubicación de la imagen
    img_bgr, img_rgb, ruta = cargar_imagen_demo(nombre_imagen)

    # Se muestra información básica de la imagen cargada
    print("\nImagen seleccionada:", nombre_imagen)
    print("Ruta:", ruta)
    print("Tamaño:", img_bgr.shape)

    # Se muestra la imagen original
    mostrar_imagen(
        img_rgb,
        "Paso 1, imagen original"
    )

    pausar()










    # ========================================================
    # 3, Convertir a escala de grises
    # ========================================================

    print("\n3, Conversión a escala de grises")
    print("La imagen se convierte a blanco y negro para trabajarla más fácil")

    # Se convierte la imagen original a escala de grises
    gray = convertir_a_gris(img_bgr)

    # Se muestra la imagen original junto a la imagen en gris
    mostrar_comparacion(
        img_rgb,
        gray,
        "Imagen original",
        "Escala de grises",
        None,
        "gray"
    )

    pausar()










    # ========================================================
    # 4, Aplicar filtro gaussiano
    # ========================================================

    print("\n4, Filtrado gaussiano")
    print("Este paso suaviza la imagen para reducir detalles pequeños que pueden estorbar")

    # Se aplica un filtro para suavizar la imagen
    # kernel_size indica qué tan grande será el filtro
    # sigma ayuda a controlar qué tanto se suaviza
    blur = filtrar_gaussiano(
        gray,
        kernel_size=5,
        sigma=1
    )

    # Se muestra la imagen después del filtro
    mostrar_imagen(
        blur,
        "Paso 3, filtrado gaussiano",
        cmap="gray"
    )

    pausar()










    # ========================================================
    # 5, Mejorar contraste
    # ========================================================

    print("\n5, Ecualización de histograma")
    print("Este paso ayuda a que se noten mejor algunas diferencias de brillo")
    print("Esta imagen se usará para bordes y esquinas, no para el conteo principal")

    # Se mejora el contraste de la imagen filtrada
    gray_eq = ecualizar_histograma(blur)

    # Se compara la imagen filtrada con la imagen mejorada
    mostrar_comparacion(
        blur,
        gray_eq,
        "Imagen filtrada",
        "Ecualización de histograma",
        "gray",
        "gray"
    )

    pausar()










    # ========================================================
    # 6, Separar objetos del fondo
    # ========================================================

    print("\n6, Umbralización con Otsu")
    print("Aquí se separan los objetos del fondo de forma automática")
    print("Se usa la imagen filtrada para evitar que algunos objetos se junten por error")

    # Se aplica Otsu sobre blur y no sobre gray_eq
    # Esto ayuda a que los objetos queden mejor separados
    umbral, binaria = umbralizar_otsu(
        blur,
        invertir=True
    )

    # Se muestra el valor que Otsu calculó automáticamente
    print("\nUmbral calculado por Otsu:", umbral)

    # Se muestra la imagen donde los objetos quedan en blanco y el fondo en negro
    mostrar_imagen(
        binaria,
        "Paso 5, umbralización con Otsu",
        cmap="gray"
    )

    pausar()










    # ========================================================
    # 7, Limpiar la imagen binaria
    # ========================================================

    print("\n7, Morfología")
    print("Este paso limpia la imagen en blanco y negro")
    print("Ayuda a quitar manchas pequeñas y a completar partes de los objetos")

    # Se limpia la imagen binaria
    binaria_limpia = aplicar_morfologia(
        binaria,
        kernel_size=5,
        apertura_iter=1,
        cierre_iter=1
    )

    # Se compara la imagen antes y después de limpiarla
    mostrar_comparacion(
        binaria,
        binaria_limpia,
        "Otsu",
        "Morfología, apertura y cierre",
        "gray",
        "gray"
    )

    pausar()










    # ========================================================
    # 8, Contar objetos
    # ========================================================

    print("\n8, Segmentación por componentes conectados")
    print("Aquí se buscan las zonas blancas que representan objetos")
    print("Las zonas muy pequeñas se ignoran para no contar ruido")

    # Se buscan las regiones blancas de la imagen limpia
    # resultado es la imagen con cajas y puntos verdes
    # conteo es el número de objetos encontrados
    # tabla guarda datos de cada objeto, pero no se imprimirá completa
    # labels guarda las etiquetas internas de cada región
    resultado, conteo, tabla, labels = segmentar_componentes(
        binaria_limpia,
        img_rgb,
        area_minima=2000
    )

    # Se muestra solo el número final de objetos
    print("\nConteo final:", conteo)

    # Se muestra la imagen final con cajas, puntos verdes y números
    mostrar_resultado_final(
        resultado,
        conteo
    )

    pausar()










    # ========================================================
    # 9, Detectar bordes
    # ========================================================

    print("\n9, Detección de bordes con Canny")
    print("Este paso muestra los contornos de los objetos")
    print("Sirve como apoyo para ver mejor la forma de las piezas")

    # Se detectan los bordes de la imagen
    bordes = detectar_bordes_canny(
        gray_eq,
        umbral1=50,
        umbral2=150
    )

    # Se muestra la imagen con bordes
    mostrar_imagen(
        bordes,
        "Paso 8, detección de bordes con Canny",
        cmap="gray"
    )

    pausar()










    # ========================================================
    # 10, Detectar esquinas
    # ========================================================

    print("\n10, Detección de esquinas con Harris")
    print("Este paso marca zonas donde hay cambios fuertes en la imagen")
    print("No se usa para contar objetos, solo sirve como apoyo visual")

    # Se buscan puntos candidatos a esquina
    harris, harris_vis = detectar_esquinas_harris(
        gray_eq,
        img_rgb
    )

    # Se muestra la imagen con los puntos marcados
    mostrar_imagen(
        harris_vis,
        "Paso 9, detección de esquinas con Harris"
    )

    pausar()










    # ========================================================
    # 11, Probar el proceso automático
    # ========================================================

    print("\n11, Prueba del pipeline automático")
    print("Ahora se prueba la función que hace todo el proceso de una vez")
    print("Esto demuestra que la librería también puede usarse de forma rápida")

    # Se ejecuta el proceso completo con una sola función
    resultados_pipeline = procesar_demo(
        nombre_imagen,
        area_minima=2000,
        mostrar=True,
        guardar_csv=False
    )

    # Se muestra solo el conteo que dio el proceso automático
    print("\nConteo obtenido con procesar_demo:", resultados_pipeline["conteo"])

    pausar()










    # ========================================================
    # 12, Probar todas las imágenes demo
    # ========================================================

    print("\n12, Prueba rápida con todas las imágenes demo")
    print("Esto demuestra que la librería puede trabajar con varias imágenes")
    print("Solo se mostrarán los conteos para no saturar la pantalla")

    # Se procesa cada imagen demo disponible
    for nombre in imagenes:

        # Se ejecuta el proceso completo sin mostrar imágenes
        resultado_demo = procesar_demo(
            nombre,
            area_minima=2000,
            mostrar=False,
            guardar_csv=False
        )

        # Se muestra el conteo obtenido en cada imagen
        print(f"Imagen {nombre}, conteo detectado: {resultado_demo['conteo']} objetos")










    # ========================================================
    # 13, Cierre del ejemplo
    # ========================================================

    print("\n====================================================")
    print(" EJEMPLO FINALIZADO CORRECTAMENTE")
    print("====================================================")










# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
