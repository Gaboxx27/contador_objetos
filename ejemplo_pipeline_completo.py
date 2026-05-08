# ============================================================
# EJEMPLO DE PIPELINE COMPLETO
# Librería contador_objetos
# Proyecto 2, Segmentación y conteo de objetos
# Este archivo muestra la forma rápida de usar la librería
# ============================================================

from contador_objetos import (
    listar_imagenes_demo,
    procesar_demo
)










# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    # Se muestra un título al iniciar el programa
    print("====================================================")
    print(" EJEMPLO DE PIPELINE COMPLETO")
    print(" Librería contador_objetos")
    print("====================================================")










    # ========================================================
    # 1, Revisar imágenes disponibles
    # ========================================================

    print("\n1, Revisando imágenes disponibles")

    # Se buscan las imágenes demo que vienen dentro de la librería
    imagenes = listar_imagenes_demo()

    # Se muestran las imágenes encontradas
    print("\nImágenes disponibles:")
    print(imagenes)

    # Si no se encuentran imágenes, el programa se detiene
    if len(imagenes) == 0:
        print("\nNo se encontraron imágenes demo")
        return










    # ========================================================
    # 2, Seleccionar imagen
    # ========================================================

    print("\n2, Seleccionando imagen de prueba")

    # Se elige la imagen principal del proyecto
    nombre_imagen = "img3"

    # Se muestra la imagen seleccionada
    print("Imagen seleccionada:", nombre_imagen)










    # ========================================================
    # 3, Ejecutar pipeline completo
    # ========================================================

    print("\n3, Ejecutando procesamiento completo")
    print("La función procesar_demo hace todo el flujo automáticamente")

    # Se procesa la imagen usando una sola función
    # area_minima ayuda a ignorar manchas pequeñas
    # mostrar=True permite ver las imágenes del proceso
    # guardar_csv=False evita guardar archivos
    resultados = procesar_demo(
        nombre_imagen,
        area_minima=2000,
        mostrar=True,
        guardar_csv=False
    )










    # ========================================================
    # 4, Mostrar resultado principal
    # ========================================================

    print("\n4, Resultado obtenido")

    # Se muestra solo el conteo final
    print("Conteo final:", resultados["conteo"])










    # ========================================================
    # 5, Probar todas las imágenes demo
    # ========================================================

    print("\n5, Prueba rápida con todas las imágenes demo")
    print("Esta parte revisa que la librería también funcione con las demás imágenes")

    # Se procesa cada imagen disponible
    for nombre in imagenes:

        # Se ejecuta el pipeline sin mostrar imágenes
        resultado_demo = procesar_demo(
            nombre,
            area_minima=2000,
            mostrar=False,
            guardar_csv=False
        )

        # Se muestra el conteo de cada imagen
        print(f"Imagen {nombre}, conteo detectado: {resultado_demo['conteo']} objetos")










    # ========================================================
    # 6, Cierre
    # ========================================================

    print("\n====================================================")
    print(" PIPELINE COMPLETO FINALIZADO CORRECTAMENTE")
    print("====================================================")










# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
