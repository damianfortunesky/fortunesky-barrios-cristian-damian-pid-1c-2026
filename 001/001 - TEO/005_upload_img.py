import py5

img = None


def setup():
    global img
    py5.size(800, 450)

    # Cargar imagen (colocar una imagen en la carpeta del proyecto)
    img = py5.load_image("img/imagen.jpg")  # Cambiar por imagen disponible


def draw():
    if img:
        # Mostrar imagen original
        py5.image(img, 0, 0, 400, 400)

        # Mostrar imagen redimensionada
        py5.image(img, 400, 0, 300, 300)

        # Información de la imagen
        py5.fill(0)
        py5.text(f"Original: {img.width} x {img.height}", 10, 420)
        py5.text(f"Redimensionada: 300 x 300", 10, 440)


py5.run_sketch()
