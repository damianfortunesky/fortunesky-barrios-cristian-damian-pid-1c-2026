import py5


def setup():
    # Diferentes resoluciones
    py5.size(800, 600)  # HD 4:3
    py5.background(0)

    # Mostrar información de la ventana
    print(f"Ancho: {py5.width} píxeles")
    print(f"Alto: {py5.height} píxeles")
    print(f"Total píxeles: {py5.width * py5.height}")


py5.run_sketch()
