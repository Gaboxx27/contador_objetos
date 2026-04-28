import cv2
import numpy as np
import pandas as pd


def umbralizar_otsu(gray, invertir=True):
    """
    Aplica umbralización automática con Otsu.

    Parámetros
    ----------
    gray : numpy.ndarray
        Imagen en escala de grises.
    invertir : bool
        True usa THRESH_BINARY_INV.
        False usa THRESH_BINARY.

    Retorna
    -------
    umbral : float
        Valor de umbral calculado por Otsu.
    binaria : numpy.ndarray
        Imagen binaria.
    """
    tipo = cv2.THRESH_BINARY_INV if invertir else cv2.THRESH_BINARY

    umbral, binaria = cv2.threshold(
        gray,
        0,
        255,
        tipo + cv2.THRESH_OTSU
    )

    return umbral, binaria


def aplicar_morfologia(binaria, kernel_size=5, apertura_iter=1, cierre_iter=1):
    """
    Aplica morfología matemática.

    Apertura:
        elimina ruido pequeño.
    Cierre:
        rellena huecos pequeños.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    limpia = cv2.morphologyEx(
        binaria,
        cv2.MORPH_OPEN,
        kernel,
        iterations=apertura_iter
    )

    limpia = cv2.morphologyEx(
        limpia,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=cierre_iter
    )

    return limpia


def segmentar_componentes(binaria_limpia, img_rgb, area_minima=2000):
    """
    Segmenta objetos mediante componentes conectados.

    Parámetros
    ----------
    binaria_limpia : numpy.ndarray
        Imagen binaria después de limpieza.
    img_rgb : numpy.ndarray
        Imagen original en RGB para dibujar resultados.
    area_minima : int
        Regiones menores a este valor se ignoran.

    Retorna
    -------
    resultado : numpy.ndarray
        Imagen RGB con cajas, centroides y números.
    conteo : int
        Número de objetos detectados.
    tabla : pandas.DataFrame
        Propiedades básicas de los objetos.
    labels : numpy.ndarray
        Matriz de etiquetas.
    """
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binaria_limpia,
        8
    )

    resultado = img_rgb.copy()
    conteo = 0
    datos = []

    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]
        cx, cy = centroids[i]

        if area > area_minima:
            conteo += 1

            cv2.rectangle(
                resultado,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            cv2.circle(
                resultado,
                (int(cx), int(cy)),
                5,
                (0, 255, 0),
                -1
            )

            cv2.putText(
                resultado,
                str(conteo),
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )

            relacion_aspecto = round(w / h, 3) if h != 0 else 0

            datos.append({
                "Objeto": conteo,
                "Area_px": int(area),
                "X": int(x),
                "Y": int(y),
                "Ancho": int(w),
                "Alto": int(h),
                "Centroide_X": round(float(cx), 2),
                "Centroide_Y": round(float(cy), 2),
                "Relacion_ancho_alto": relacion_aspecto
            })

    tabla = pd.DataFrame(datos)

    return resultado, conteo, tabla, labels
