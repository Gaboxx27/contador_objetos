import cv2


def cargar_imagen(ruta):
    """
    Lee una imagen desde una ruta.

    Retorna
    -------
    img_bgr : numpy.ndarray
        Imagen en formato BGR, como la lee OpenCV.
    img_rgb : numpy.ndarray
        Imagen convertida a RGB para visualizar correctamente con matplotlib.
    """
    img_bgr = cv2.imread(str(ruta))

    if img_bgr is None:
        raise FileNotFoundError(f"No se pudo abrir la imagen. Revisa la ruta: {ruta}")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_bgr, img_rgb


def convertir_a_gris(img_bgr):
    """
    Convierte una imagen BGR a escala de grises.
    """
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


def filtrar_gaussiano(gray, kernel_size=5, sigma=1):
    """
    Aplica filtrado espacial gaussiano.
    """
    if kernel_size % 2 == 0:
        kernel_size += 1

    return cv2.GaussianBlur(gray, (kernel_size, kernel_size), sigma)


def ecualizar_histograma(gray):
    """
    Aplica transformación de intensidad mediante ecualización del histograma.
    """
    return cv2.equalizeHist(gray)
