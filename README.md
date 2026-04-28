# contador_objetos

`contador_objetos` es una librería de Python para analizar imágenes tomadas desde arriba.

La librería ayuda a:

- separar los objetos del fondo
- contar cuántos objetos hay
- mostrar cada paso del procesamiento
- obtener una tabla con datos de cada objeto

Este proyecto corresponde al **Proyecto 2: Segmentación y conteo de objetos en una banda o superficie de trabajo**.

---

# ¿Qué hace la librería?

La librería puede hacer lo siguiente:

- cargar imágenes de prueba
- convertir una imagen a escala de grises
- aplicar un filtro para reducir ruido
- mejorar el contraste de la imagen
- convertir la imagen a blanco y negro con Otsu
- limpiar la imagen usando morfología
- separar los objetos por regiones
- contar los objetos
- marcar los objetos con cuadros y números
- detectar bordes con Canny
- detectar esquinas con Harris

---

# Técnicas usadas

En este proyecto se usan estas técnicas:

- escala de grises
- filtro gaussiano
- ecualización de histograma
- umbralización de Otsu
- morfología
- componentes conectados
- detección de bordes con Canny
- detección de esquinas con Harris
- conteo de objetos

---

# Instalación desde GitHub

Para instalar la librería desde GitHub, abre CMD, PowerShell o la terminal de Visual Studio Code y escribe:

```bash
python -m pip install git+https://github.com/Gaboxx27/contador_objetos.git
```

Si el repositorio tiene otro nombre, cambia esta parte:

```bash
contador_objetos.git
```

por el nombre real del repositorio.

---

# Actualizar la librería

Si hiciste cambios en GitHub y quieres instalar la versión nueva, usa:

```bash
python -m pip install --upgrade --force-reinstall git+https://github.com/Gaboxx27/contador_objetos.git
```

---

# Desinstalar la librería

Para quitar la librería de tu computadora:

```bash
python -m pip uninstall contador_objetos
```

Cuando pregunte si deseas continuar, escribe:

```bash
y
```

---

# Probar que la instalación funcionó

Crea un archivo llamado:

```text
test_instalacion.py
```

Dentro del archivo escribe:

```python
from contador_objetos import listar_imagenes_demo

print("Imágenes disponibles:", listar_imagenes_demo())
```

Luego ejecútalo:

```bash
python test_instalacion.py
```

Si todo está bien, debe aparecer algo parecido a esto:

```text
Imágenes disponibles: ['img1', 'img2', 'img3']
```

---

# Imágenes incluidas

La librería ya trae tres imágenes de prueba:

```text
img1
img2
img3
```

Estas imágenes sirven para probar la librería sin tener que buscar imágenes externas.

---

# Uso paso por paso

A continuación se muestra cómo usar cada función de la librería por separado.

Esto es útil para entender qué hace cada parte del procesamiento.

---

## Paso 1: cargar una imagen

```python
from contador_objetos import cargar_imagen_demo, mostrar_imagen

img_bgr, img_rgb, ruta = cargar_imagen_demo("img3")

print("Imagen cargada desde:", ruta)

mostrar_imagen(img_rgb, "Paso 1: imagen original")
```

### Explicación

Esta función carga una imagen incluida en la librería.

`img_bgr` es la imagen en formato BGR, que es el formato que usa OpenCV.

`img_rgb` es la imagen en formato RGB, que sirve para mostrarla correctamente.

`ruta` es la ubicación de la imagen dentro de la librería.

---

## Paso 2: convertir a escala de grises

```python
from contador_objetos import convertir_a_gris, mostrar_comparacion

gray = convertir_a_gris(img_bgr)

mostrar_comparacion(
    img_rgb,
    gray,
    "Imagen original",
    "Paso 2: escala de grises",
    None,
    "gray"
)
```

### Explicación

Este paso convierte la imagen a escala de grises.

Esto facilita el análisis porque la imagen queda con una sola capa de intensidad.

---

## Paso 3: aplicar filtro gaussiano

```python
from contador_objetos import filtrar_gaussiano, mostrar_imagen

blur = filtrar_gaussiano(
    gray,
    kernel_size=5,
    sigma=1
)

mostrar_imagen(
    blur,
    "Paso 3: filtro gaussiano",
    cmap="gray"
)
```

### Explicación

Este filtro suaviza la imagen y ayuda a reducir ruido.

`kernel_size=5` indica el tamaño del filtro.

`sigma=1` indica qué tanto se suaviza la imagen.

---

## Paso 4: mejorar contraste

```python
from contador_objetos import ecualizar_histograma, mostrar_comparacion

gray_eq = ecualizar_histograma(blur)

mostrar_comparacion(
    blur,
    gray_eq,
    "Imagen filtrada",
    "Paso 4: ecualización",
    "gray",
    "gray"
)
```

### Explicación

Este paso mejora el contraste de la imagen.

Puede ayudar a separar mejor los objetos del fondo.

---

## Paso 5: umbralización con Otsu

```python
from contador_objetos import umbralizar_otsu, mostrar_imagen

umbral, binaria = umbralizar_otsu(
    blur,
    invertir=True
)

print("Umbral calculado por Otsu:", umbral)

mostrar_imagen(
    binaria,
    "Paso 5: Otsu",
    cmap="gray"
)
```

### Explicación

Este paso convierte la imagen a blanco y negro.

Otsu calcula automáticamente el mejor valor para separar el fondo de los objetos.

`invertir=True` se usa cuando los objetos son más oscuros que el fondo.

Si los objetos son más claros que el fondo, se puede usar:

```python
invertir=False
```

---

## Paso 6: aplicar morfología

```python
from contador_objetos import aplicar_morfologia, mostrar_comparacion

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
    "Paso 6: morfología",
    "gray",
    "gray"
)
```

### Explicación

La morfología ayuda a limpiar la imagen binaria.

La apertura elimina ruido pequeño.

El cierre rellena huecos pequeños dentro de los objetos.

---

## Paso 7: segmentación por regiones y conteo

```python
from contador_objetos import segmentar_componentes, mostrar_resultado_final

resultado, conteo, tabla, labels = segmentar_componentes(
    binaria_limpia,
    img_rgb,
    area_minima=2000
)

print("Conteo final:", conteo)
print(tabla)

mostrar_resultado_final(resultado, conteo)
```

### Explicación

Este paso busca regiones conectadas en la imagen binaria.

Cada región detectada se toma como un posible objeto.

La función entrega cuatro cosas:

- `resultado`: imagen con los objetos marcados
- `conteo`: número total de objetos detectados
- `tabla`: datos de cada objeto
- `labels`: matriz interna con etiquetas de las regiones

---

## Paso 8: detección de bordes con Canny

```python
from contador_objetos import detectar_bordes_canny, mostrar_imagen

bordes = detectar_bordes_canny(
    gray_eq,
    umbral1=50,
    umbral2=150
)

mostrar_imagen(
    bordes,
    "Paso 8: bordes con Canny",
    cmap="gray"
)
```

### Explicación

Este paso detecta los bordes de los objetos.

Sirve para observar mejor los límites de cada objeto.

---

## Paso 9: detección de esquinas con Harris

```python
from contador_objetos import detectar_esquinas_harris, mostrar_imagen

harris, harris_vis = detectar_esquinas_harris(
    gray_eq,
    img_rgb
)

mostrar_imagen(
    harris_vis,
    "Paso 9: esquinas con Harris"
)
```

### Explicación

Este paso detecta esquinas o puntos importantes en la imagen.

Es útil cuando los objetos tienen formas no circulares, como llaves, tijeras, piezas industriales u objetos rectangulares.

---

# Código completo paso por paso

Crea un archivo llamado:

```text
test_paso_a_paso.py
```

y pega este código:

```python
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

print("Imágenes disponibles:", listar_imagenes_demo())

img_bgr, img_rgb, ruta = cargar_imagen_demo("img3")
print("Imagen cargada desde:", ruta)

mostrar_imagen(img_rgb, "Paso 1: imagen original")

gray = convertir_a_gris(img_bgr)

mostrar_comparacion(
    img_rgb,
    gray,
    "Imagen original",
    "Paso 2: escala de grises",
    None,
    "gray"
)

blur = filtrar_gaussiano(
    gray,
    kernel_size=5,
    sigma=1
)

mostrar_imagen(
    blur,
    "Paso 3: filtro gaussiano",
    cmap="gray"
)

gray_eq = ecualizar_histograma(blur)

mostrar_comparacion(
    blur,
    gray_eq,
    "Imagen filtrada",
    "Paso 4: ecualización",
    "gray",
    "gray"
)

umbral, binaria = umbralizar_otsu(
    blur,
    invertir=True
)

print("Umbral calculado por Otsu:", umbral)

mostrar_imagen(
    binaria,
    "Paso 5: Otsu",
    cmap="gray"
)

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
    "Paso 6: morfología",
    "gray",
    "gray"
)

resultado, conteo, tabla, labels = segmentar_componentes(
    binaria_limpia,
    img_rgb,
    area_minima=2000
)

print("Conteo final:", conteo)
print(tabla)

mostrar_resultado_final(resultado, conteo)

bordes = detectar_bordes_canny(
    gray_eq,
    umbral1=50,
    umbral2=150
)

mostrar_imagen(
    bordes,
    "Paso 8: bordes con Canny",
    cmap="gray"
)

harris, harris_vis = detectar_esquinas_harris(
    gray_eq,
    img_rgb
)

mostrar_imagen(
    harris_vis,
    "Paso 9: esquinas con Harris"
)
```

Ejecuta el archivo con:

```bash
python test_paso_a_paso.py
```

---

# Uso rápido: ejecutar todo el procesamiento

Si quieres ejecutar todo de una sola vez, usa `procesar_demo`.

```python
from contador_objetos import procesar_demo

resultados = procesar_demo(
    "img3",
    area_minima=2000,
    mostrar=True,
    guardar_csv=True,
    ruta_csv="resultados_img3.csv"
)

print("Conteo obtenido:", resultados["conteo"])
print(resultados["tabla"])
```

---

## ¿Qué hace `procesar_demo`?

`procesar_demo` hace todo automáticamente:

1. Carga la imagen.
2. Convierte a escala de grises.
3. Aplica filtro gaussiano.
4. Mejora el contraste.
5. Aplica Otsu.
6. Aplica morfología.
7. Segmenta objetos.
8. Cuenta objetos.
9. Detecta bordes.
10. Detecta esquinas.
11. Muestra resultados.
12. Guarda una tabla CSV si se solicita.

---

# Usar otra imagen

Para usar otra imagen incluida en la librería, cambia:

```python
cargar_imagen_demo("img3")
```

por:

```python
cargar_imagen_demo("img1")
```

o:

```python
cargar_imagen_demo("img2")
```

También puedes usar:

```python
procesar_demo("img1")
procesar_demo("img2")
procesar_demo("img3")
```

---

# Procesar una imagen externa

También puedes usar una imagen que no esté incluida en la librería:

```python
from contador_objetos import procesar_imagen

resultados = procesar_imagen(
    r"C:\Users\gabri\OneDrive\Escritorio\Proyecto vision 2 parcial\mi_imagen.jpg",
    area_minima=2000,
    mostrar=True,
    guardar_csv=True,
    ruta_csv="resultados_mi_imagen.csv"
)

print(resultados["conteo"])
print(resultados["tabla"])
```

---

# Parámetros importantes

## `area_minima`

Este parámetro evita que el programa cuente manchas pequeñas o ruido como si fueran objetos.

Ejemplo:

```python
area_minima=2000
```

Si cuenta ruido como objeto, aumenta el valor:

```python
area_minima=3000
```

Si elimina objetos reales, baja el valor:

```python
area_minima=1000
```

---

## `invertir_otsu`

Este parámetro controla si la imagen binaria se invierte.

```python
invertir=True
```

Se usa cuando los objetos son más oscuros que el fondo.

```python
invertir=False
```

Se usa cuando los objetos son más claros que el fondo.

---

# Resultados generados

La librería puede generar:

- imagen original
- imagen en escala de grises
- imagen filtrada
- imagen con mejor contraste
- imagen binaria con Otsu
- imagen después de morfología
- imagen con bordes
- imagen con esquinas
- imagen final con objetos numerados
- tabla con propiedades de cada objeto

---

# Tabla de propiedades

La tabla contiene:

- número de objeto
- área en pixeles
- posición X
- posición Y
- ancho
- alto
- centroide X
- centroide Y
- relación ancho/alto

Para imprimir la tabla:

```python
print(tabla)
```

o:

```python
print(resultados["tabla"])
```

---

# Guardar resultados en CSV

Si usas el procesamiento completo, puedes guardar la tabla en un archivo CSV:

```python
resultados = procesar_demo(
    "img3",
    guardar_csv=True,
    ruta_csv="resultados_img3.csv"
)
```

Ese archivo se puede abrir en Excel.

---

# Requisitos

La librería usa:

- OpenCV
- NumPy
- Matplotlib
- Pandas

Normalmente estas dependencias se instalan automáticamente al instalar la librería desde GitHub.

Si necesitas instalarlas manualmente, usa:

```bash
python -m pip install opencv-python numpy matplotlib pandas
```

---

# Errores comunes

## Error: No module named contador_objetos

Significa que la librería no está instalada en el Python que estás usando.

Solución:

```bash
python -m pip install git+https://github.com/Gaboxx27/contador_objetos.git
```

---

## Error al cargar la imagen

Revisa que la ruta sea correcta y que la imagen exista.

---

## El conteo no coincide

Puede ocurrir por:

- objetos pegados
- sombras fuertes
- fondo con textura
- bajo contraste
- objetos muy pequeños
- valor incorrecto de `area_minima`

Puedes ajustar el valor de:

```python
area_minima
```

---

# Limitaciones

La librería funciona mejor cuando:

- los objetos están separados
- el fondo es uniforme
- hay contraste entre objetos y fondo
- la imagen está tomada desde arriba

Puede fallar cuando:

- los objetos están pegados
- hay sombras fuertes
- hay reflejos
- el fondo tiene muchas texturas
- los objetos tienen colores muy parecidos al fondo

---

# Autor

Gabriel Lopez

Proyecto desarrollado para la asignatura de procesamiento digital de imágenes.
