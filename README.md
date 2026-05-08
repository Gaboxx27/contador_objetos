# contador_objetos

Librería en Python para segmentar, contar y caracterizar objetos en imágenes cenitales sobre una banda o superficie de trabajo, este proyecto corresponde al Proyecto 2, segmentación y conteo de objetos en una banda o superficie de trabajo.

La librería permite cargar imágenes de prueba, aplicar preprocesamiento, separar objetos del fondo, detectar regiones conectadas, contar objetos, obtener propiedades básicas y visualizar bordes y puntos candidatos a esquina.

---

## Objetivo

El objetivo de esta librería es procesar imágenes tomadas desde arriba para identificar objetos individuales sobre una superficie clara, separar el fondo de los objetos y obtener un conteo final fácil de interpretar.

El sistema no se queda solo en una imagen binaria, también muestra una salida visual con cajas delimitadoras, centroides y el número total de objetos detectados.

---

## Características principales

- Carga de imágenes demo incluidas en la librería
- Conversión de imagen a escala de grises
- Filtrado gaussiano para reducir ruido
- Ecualización de histograma para mejorar contraste
- Umbralización con Otsu para separar fondo y objetos
- Operaciones morfológicas de apertura y cierre
- Segmentación por componentes conectados
- Conteo final de objetos detectados
- Cálculo de propiedades básicas por objeto
- Detección de bordes con Canny
- Detección de puntos candidatos a esquina con Harris
- Pipeline automático con `procesar_demo()`

---

## Instalación

La librería puede instalarse directamente desde GitHub usando `pip`.

```bash
python -m pip install https://github.com/Gaboxx27/contador_objetos/archive/refs/heads/main.zip
```

También puede instalarse clonando el repositorio.

```bash
git clone https://github.com/Gaboxx27/contador_objetos.git
cd contador_objetos
python -m pip install .
```

---

## Verificación rápida de instalación

Después de instalar la librería, se puede verificar que el paquete funciona importando una función básica.

```bash
python -c "from contador_objetos import listar_imagenes_demo; print(listar_imagenes_demo())"
```

Si la instalación fue correcta, la consola debe mostrar las imágenes demo disponibles, por ejemplo `img1`, `img2` e `img3`.

---

## Imágenes demo

La librería incluye imágenes de prueba para ejecutar el procesamiento sin necesidad de cargar archivos externos.

Las imágenes disponibles se pueden consultar con la función `listar_imagenes_demo()`.

```python
from contador_objetos import listar_imagenes_demo

imagenes = listar_imagenes_demo()

print(imagenes)
```

---

## Uso básico con pipeline automático

La forma más rápida de probar la librería es usando `procesar_demo()`, esta función ejecuta el flujo completo de procesamiento con una sola llamada.

```python
from contador_objetos import procesar_demo

resultados = procesar_demo(
    "img3",
    area_minima=2000,
    mostrar=True,
    guardar_csv=False
)

print("Conteo final:", resultados["conteo"])
```

En este ejemplo se procesa la imagen `img3`, se muestran las etapas visuales y no se guarda ningún archivo CSV.

---

## Uso paso por paso

También es posible usar cada función de forma independiente, siempre que se entregue la entrada correcta.

El siguiente ejemplo muestra el flujo completo usado para la exposición del proyecto, no guarda imágenes, no guarda CSV y no imprime tablas completas.

```python
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
```

---

## Explicación de funciones principales

### `listar_imagenes_demo()`

Muestra las imágenes de prueba disponibles dentro de la librería.

### `cargar_imagen_demo(nombre_imagen)`

Carga una imagen demo incluida en el paquete y devuelve la imagen en formato BGR, RGB y su ruta.

### `convertir_a_gris(imagen)`

Convierte una imagen de color a escala de grises para trabajarla de forma más sencilla.

### `filtrar_gaussiano(imagen_gris, kernel_size, sigma)`

Suaviza la imagen para reducir detalles pequeños que pueden afectar el conteo.

### `ecualizar_histograma(imagen_gris)`

Mejora el contraste para que algunas diferencias de brillo se vean con más claridad.

### `umbralizar_otsu(imagen_gris, invertir=True)`

Separa los objetos del fondo mediante un valor calculado automáticamente.

### `aplicar_morfologia(imagen_binaria, kernel_size, apertura_iter, cierre_iter)`

Limpia la imagen en blanco y negro para reducir manchas pequeñas y completar partes de los objetos.

### `segmentar_componentes(imagen_binaria, imagen_rgb, area_minima)`

Busca las regiones que representan objetos, calcula el conteo y genera la imagen final con cajas y centroides.

### `detectar_bordes_canny(imagen_gris, umbral1, umbral2)`

Muestra los contornos de los objetos para observar mejor sus formas.

### `detectar_esquinas_harris(imagen_gris, imagen_rgb)`

Marca zonas donde hay cambios fuertes en la imagen, se usa como apoyo visual y no como conteo principal.

### `mostrar_imagen(imagen, titulo, cmap)`

Muestra una imagen individual con un título.

### `mostrar_comparacion(imagen1, imagen2, titulo1, titulo2, cmap1, cmap2)`

Muestra dos imágenes lado a lado para comparar el antes y el después de una etapa.

### `mostrar_resultado_final(resultado, conteo)`

Muestra la imagen final con cajas, puntos verdes, números y conteo total.

### `procesar_demo(nombre_imagen, area_minima, mostrar, guardar_csv)`

Ejecuta todo el proceso de manera automática con una imagen demo.

---

## Resultado esperado

Al ejecutar el ejemplo con la imagen `img3`, el programa muestra el procesamiento paso por paso y obtiene el conteo final de los objetos detectados.

En la imagen principal del proyecto se espera detectar 9 objetos, siempre que la separación principal se haga usando la imagen filtrada `blur`.

---

## Limitaciones

El método funciona mejor cuando los objetos están separados y existe buen contraste entre los objetos y el fondo.

Si los objetos están pegados, tienen sombras fuertes, reflejos, marcas de agua o texturas muy marcadas, algunas regiones pueden unirse o separarse de forma incorrecta.

La detección de Harris puede marcar muchos puntos en objetos con óxido o textura, por eso se usa como apoyo visual y no como método principal de conteo.

---

## Autores

Juan Carlos Valadez Muñoz  
Gabriel López Lariz  
Andrés Eduardo Gloria Márquez

---

## Proyecto académico

Asignatura, Visión Robótica  
Carrera, Ingeniería Robótica  
Mayo de 2026
