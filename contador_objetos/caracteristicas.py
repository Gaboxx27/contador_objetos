import cv2
import numpy as np


def detectar_bordes_canny(gray, umbral1=50, umbral2=150):
    """
    Detecta bordes mediante Canny.
    """
    return cv2.Canny(gray, umbral1, umbral2)


def detectar_esquinas_harris(gray, img_rgb, block_size=2, ksize=3, k=0.04, factor=0.01):
    """
    Detecta esquinas mediante Harris.

    Retorna
    -------
    harris : numpy.ndarray
        Mapa de respuesta Harris.
    harris_vis : numpy.ndarray
        Imagen RGB con esquinas marcadas en rojo.
    """
    gray_float = np.float32(gray)

    harris = cv2.cornerHarris(
        gray_float,
        blockSize=block_size,
        ksize=ksize,
        k=k
    )

    harris = cv2.dilate(harris, None)

    harris_vis = img_rgb.copy()
    harris_vis[harris > factor * harris.max()] = [255, 0, 0]

    return harris, harris_vis
