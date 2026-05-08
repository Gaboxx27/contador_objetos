# contador_objetos

Librería en Python para segmentar, contar y caracterizar objetos en imágenes cenitales sobre una banda o superficie de trabajo, este proyecto corresponde al Proyecto 2, Segmentación y conteo de objetos en una banda o superficie de trabajo.

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

## Uso paso por paso para exposición

También es posible usar cada función de forma independiente, siempre que se entregue la entrada correcta.

El siguiente ejemplo muestra el flujo completo usado para la exposición del proyecto, no guarda imágenes, no guarda CSV y no imprime tablas completas.

```python
# ============================================================
# DEMOSTRACIÓN GENERAL DE LA LIBRERÍA contador_objetos
# Proyecto 2, Segmentación y conteo de objetos
# Versión para exposición
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
# FUNCIÓN PARA PAUSAR ENTRE ETAPAS
# ============================================================

def pausar(mensaje="Presiona ENTER para continuar"):
    # Esta pausa permite explicar cada etapa durante la exposición
    input(f"\n{mensaje}")









# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    # Encabezado de la demostración
    print("====================================================")
    print(" DEMOSTRACIÓN DE LA LIBRERÍA contador_objetos")
    print(" Proyecto 2, Segmentación y conteo de objetos")
    print("====================================================")









    # ========================================================
    # 1, Verificación de la librería
    # ========================================================

    print("\n1, Verificación de la librería")
    print("Se revisa si la librería puede listar sus imágenes demo")

    # Se listan las imágenes incluidas dentro de la librería
    imagenes = listar_imagenes_demo()

    # Se muestran las imágenes disponibles
    print("\nImágenes disponibles:")
    print(imagenes)

    # Si no hay imágenes demo, se detiene la ejecución
    if len(imagenes) == 0:
        print("\nNo se encontraron imágenes demo")
        return

    pausar()









    # ========================================================
    # 2, Selección y carga de imagen
    # ========================================================

    print("\n2, Carga de imagen")
    print("Se usará img3 porque es la imagen principal del proyecto")

    # Se selecciona la imagen principal de prueba
    nombre_imagen = "img3"

    # Se carga la imagen demo
    # img_bgr se usa para procesamiento con OpenCV
    # img_rgb se usa para visualización correcta con Matplotlib
    # ruta contiene la ubicación del archivo
    img_bgr, img_rgb, ruta = cargar_imagen_demo(nombre_imagen)

    # Se muestra información básica de la imagen
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
    # 3, Conversión a escala de grises
    # ========================================================

    print("\n3, Conversión a escala de grises")
    print("Se convierte la imagen de color a una sola capa de intensidad")

    # Se convierte la imagen original a escala de grises
    gray = convertir_a_gris(img_bgr)

    # Se compara la imagen original contra la imagen en escala de grises
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
    # 4, Filtrado gaussiano
    # ========================================================

    print("\n4, Filtrado gaussiano")
    print("Se reduce ruido pequeño y textura antes de segmentar")

    # Se aplica filtrado gaussiano
    # kernel_size define el tamaño del filtro
    # sigma controla la intensidad del suavizado
    blur = filtrar_gaussiano(
        gray,
        kernel_size=5,
        sigma=1
    )

    # Se muestra la imagen filtrada
    mostrar_imagen(
        blur,
        "Paso 3, filtrado gaussiano",
        cmap="gray"
    )

    pausar()









    # ========================================================
    # 5, Ecualización de histograma
    # ========================================================

    print("\n5, Ecualización de histograma")
    print("Se mejora el contraste para visualizar mejor diferencias de intensidad")
    print("Esta imagen ecualizada se usará para bordes y esquinas, no para el conteo principal")

    # Se aplica ecualización de histograma
    # Esta etapa sirve para mostrar mejora de contraste
    gray_eq = ecualizar_histograma(blur)

    # Se compara imagen filtrada contra imagen ecualizada
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
    # 6, Umbralización con Otsu
    # ========================================================

    print("\n6, Umbralización con Otsu")
    print("Se separan automáticamente los objetos del fondo")
    print("Para evitar que los objetos se unan por la ecualización, Otsu se aplica sobre la imagen filtrada")

    # IMPORTANTE:
    # Se usa blur y no gray_eq
    # Usar gray_eq puede resaltar demasiado texturas y unir regiones
    # Usar blur ayuda a mantener mejor separados los objetos
    umbral, binaria = umbralizar_otsu(
        blur,
        invertir=True
    )

    # Se muestra el umbral calculado automáticamente
    print("\nUmbral calculado por Otsu:", umbral)

    # Se muestra la máscara binaria
    mostrar_imagen(
        binaria,
        "Paso 5, umbralización con Otsu",
        cmap="gray"
    )

    pausar()









    # ========================================================
    # 7, Morfología
    # ========================================================

    print("\n7, Morfología")
    print("Se limpia la máscara binaria con apertura y cierre")
    print("La apertura elimina ruido pequeño y el cierre ayuda a rellenar huecos internos")

    # Se aplica morfología sobre la imagen binaria
    binaria_limpia = aplicar_morfologia(
        binaria,
        kernel_size=5,
        apertura_iter=1,
        cierre_iter=1
    )

    # Se compara la máscara de Otsu contra la máscara limpia
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
    # 8, Segmentación por componentes conectados
    # ========================================================

    print("\n8, Segmentación por componentes conectados")
    print("Cada región blanca válida se interpreta como un objeto")
    print("El parámetro area_minima evita contar ruido pequeño")

    # Se segmentan las regiones conectadas
    # resultado contiene la imagen con cajas y centroides
    # conteo contiene el número de objetos detectados
    # tabla contiene propiedades, pero no se imprimirá para no saturar la exposición
    # labels contiene la matriz de etiquetas
    resultado, conteo, tabla, labels = segmentar_componentes(
        binaria_limpia,
        img_rgb,
        area_minima=2000
    )

    # Se imprime solo el conteo final
    print("\nConteo final:", conteo)

    # Se muestra la imagen final con cajas, centroides y número de objetos
    mostrar_resultado_final(
        resultado,
        conteo
    )

    pausar()









    # ========================================================
    # 9, Detección de bordes con Canny
    # ========================================================

    print("\n9, Detección de bordes con Canny")
    print("Se detectan contornos externos e internos de los objetos")
    print("Esta etapa complementa el análisis geométrico")

    # Se aplica Canny sobre la imagen ecualizada
    # La ecualización ayuda a resaltar bordes y detalles
    bordes = detectar_bordes_canny(
        gray_eq,
        umbral1=50,
        umbral2=150
    )

    # Se muestra la imagen de bordes
    mostrar_imagen(
        bordes,
        "Paso 8, detección de bordes con Canny",
        cmap="gray"
    )

    pausar()









    # ========================================================
    # 10, Detección de esquinas con Harris
    # ========================================================

    print("\n10, Detección de esquinas con Harris")
    print("Se detectan puntos candidatos a esquina o zonas de alta variación")
    print("Esta etapa es complementaria, no se usa para el conteo principal")

    # Se aplica Harris sobre la imagen ecualizada
    # harris contiene la respuesta numérica del detector
    # harris_vis contiene la imagen con puntos marcados
    harris, harris_vis = detectar_esquinas_harris(
        gray_eq,
        img_rgb
    )

    # Se muestra la imagen con puntos candidatos a esquina
    mostrar_imagen(
        harris_vis,
        "Paso 9, detección de esquinas con Harris"
    )

    pausar()









    # ========================================================
    # 11, Prueba del pipeline automático
    # ========================================================

    print("\n11, Prueba del pipeline automático")
    print("Ahora se ejecuta el flujo completo usando una sola función")
    print("Esta prueba demuestra que la librería también funciona de forma automática")

    # Se ejecuta el pipeline completo sin guardar CSV
    # mostrar=True permite ver las etapas generadas por la función procesar_demo
    resultados_pipeline = procesar_demo(
        nombre_imagen,
        area_minima=2000,
        mostrar=True,
        guardar_csv=False
    )

    # Se imprime solo el conteo obtenido por el pipeline
    print("\nConteo obtenido con procesar_demo:", resultados_pipeline["conteo"])

    pausar()









    # ========================================================
    # 12, Prueba rápida con todas las imágenes demo
    # ========================================================

    print("\n12, Prueba rápida con todas las imágenes demo")
    print("Esto demuestra que la librería no depende de una sola imagen")
    print("Solo se mostrarán los conteos, no las tablas")

    # Se recorre cada imagen demo disponible
    for nombre in imagenes:

        # Se procesa cada imagen sin mostrar resultados visuales
        # Esto permite probar rápido que el pipeline funciona con todas
        resultado_demo = procesar_demo(
            nombre,
            area_minima=2000,
            mostrar=False,
            guardar_csv=False
        )

        # Se imprime el conteo obtenido para cada imagen
        print(f"Imagen {nombre}, conteo detectado: {resultado_demo['conteo']} objetos")









    # ========================================================
    # 13, Cierre de demostración
    # ========================================================

    print("\n====================================================")
    print(" DEMOSTRACIÓN FINALIZADA CORRECTAMENTE")
    print("====================================================")









# ============================================================
# EJECUCIÓN DEL PROGRAMA
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

Convierte una imagen de color a escala de grises para simplificar el procesamiento.

### `filtrar_gaussiano(imagen_gris, kernel_size, sigma)`

Aplica suavizado gaussiano para reducir ruido y pequeñas variaciones de textura.

### `ecualizar_histograma(imagen_gris)`

Mejora el contraste de la imagen mediante una transformación de intensidad.

### `umbralizar_otsu(imagen_gris, invertir=True)`

Calcula automáticamente un umbral para separar objetos y fondo, en el demo se usa sobre la imagen filtrada para evitar que los objetos se unan.

### `aplicar_morfologia(imagen_binaria, kernel_size, apertura_iter, cierre_iter)`

Limpia la imagen binaria mediante apertura y cierre morfológico.

### `segmentar_componentes(imagen_binaria, imagen_rgb, area_minima)`

Detecta regiones conectadas, cuenta objetos y genera una salida visual con cajas y centroides.

### `detectar_bordes_canny(imagen_gris, umbral1, umbral2)`

Detecta bordes externos e internos de los objetos.

### `detectar_esquinas_harris(imagen_gris, imagen_rgb)`

Detecta puntos candidatos a esquina o zonas de alta variación de intensidad.

### `mostrar_imagen(imagen, titulo, cmap)`

Muestra una imagen individual con un título.

### `mostrar_comparacion(imagen1, imagen2, titulo1, titulo2, cmap1, cmap2)`

Muestra dos imágenes lado a lado para comparar etapas del procesamiento.

### `mostrar_resultado_final(resultado, conteo)`

Muestra la salida final con cajas, centroides y conteo total.

### `procesar_demo(nombre_imagen, area_minima, mostrar, guardar_csv)`

Ejecuta el flujo completo de forma automática con una imagen demo.

---

## Resultado esperado

Al ejecutar el script de demostración con la imagen `img3`, el sistema debe mostrar el procesamiento paso por paso y obtener el conteo final de objetos detectados.

En la imagen principal del proyecto se espera detectar 9 objetos, siempre que la umbralización principal se aplique sobre la imagen filtrada `blur`.

---

## Limitaciones

El método funciona mejor cuando los objetos están separados y existe contraste claro entre objetos y fondo.

Si los objetos están pegados, tienen sombras fuertes, reflejos, marcas de agua o texturas muy intensas, algunas regiones pueden unirse o dividirse incorrectamente.

La detección de Harris puede marcar muchos puntos en objetos oxidados o con textura, por eso se usa como análisis complementario y no como método principal de conteo.

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

