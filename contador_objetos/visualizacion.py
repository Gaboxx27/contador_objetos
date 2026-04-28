import matplotlib.pyplot as plt


def mostrar_imagen(imagen, titulo="Imagen", cmap=None, figsize=(8, 6)):
    """
    Muestra una sola imagen.
    """
    plt.figure(titulo, figsize=figsize)
    plt.imshow(imagen, cmap=cmap)
    plt.title(titulo)
    plt.axis("off")
    plt.show()


def mostrar_comparacion(img1, img2, titulo1="Imagen 1", titulo2="Imagen 2",
                        cmap1=None, cmap2=None, figsize=(12, 6)):
    """
    Muestra dos imágenes lado a lado.
    """
    plt.figure(f"{titulo1} vs {titulo2}", figsize=figsize)

    plt.subplot(1, 2, 1)
    plt.imshow(img1, cmap=cmap1)
    plt.title(titulo1)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img2, cmap=cmap2)
    plt.title(titulo2)
    plt.axis("off")

    plt.show()


def mostrar_resultado_final(resultado, conteo):
    """
    Muestra la imagen final con el conteo.
    """
    plt.figure("Resultado final: segmentación por regiones y conteo", figsize=(10, 8))
    plt.imshow(resultado)
    plt.title(f"Segmentación por regiones y conteo final: {conteo} objetos")
    plt.axis("off")
    plt.show()


def mostrar_resultados(resultados):
    """
    Muestra todas las imágenes del procesamiento completo.
    """
    mostrar_comparacion(
        resultados["imagen_rgb"],
        resultados["gris"],
        "Imagen original",
        "Conversión RGB a escala de grises",
        None,
        "gray"
    )

    mostrar_comparacion(
        resultados["filtrada"],
        resultados["ecualizada"],
        "Preprocesamiento: filtrado Gaussiano",
        "Transformación de intensidad: ecualización",
        "gray",
        "gray"
    )

    mostrar_comparacion(
        resultados["binaria"],
        resultados["binaria_limpia"],
        "Umbralización Otsu",
        "Morfología: apertura y cierre",
        "gray",
        "gray"
    )

    mostrar_imagen(
        resultados["bordes"],
        "Detección de bordes - Canny",
        cmap="gray"
    )

    mostrar_imagen(
        resultados["harris_vis"],
        "Detección de esquinas - Harris"
    )

    mostrar_resultado_final(
        resultados["resultado"],
        resultados["conteo"]
    )
