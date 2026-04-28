from importlib.resources import files
from .preprocesamiento import cargar_imagen


IMAGENES_DEMO = {
    "img1": "img1.jpg",
    "img2": "img2.jpg",
    "img3": "img3.jpg",
}


def listar_imagenes_demo():
    """
    Devuelve la lista de imágenes precargadas disponibles.
    """
    return list(IMAGENES_DEMO.keys())


def obtener_ruta_imagen(nombre):
    """
    Devuelve la ruta de una imagen precargada.

    Parámetros
    ----------
    nombre : str
        "img1", "img2" o "img3".
    """
    if nombre not in IMAGENES_DEMO:
        disponibles = ", ".join(listar_imagenes_demo())
        raise ValueError(f"Imagen no disponible: {nombre}. Usa una de estas: {disponibles}")

    recurso = files("contador_objetos").joinpath("imagenes", IMAGENES_DEMO[nombre])
    return str(recurso)


def cargar_imagen_demo(nombre):
    """
    Carga una imagen precargada y devuelve:
    img_bgr, img_rgb, ruta
    """
    ruta = obtener_ruta_imagen(nombre)
    img_bgr, img_rgb = cargar_imagen(ruta)
    return img_bgr, img_rgb, ruta
