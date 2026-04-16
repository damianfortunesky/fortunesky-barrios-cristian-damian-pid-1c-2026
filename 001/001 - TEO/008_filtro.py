# Crear un filtro que solo muestre un canal de color
import py5

img = None


def setup():
    global img
    py5.size(600, 200)
    img = py5.create_image(200, 200, py5.RGB)

    # Crear imagen de prueba
    img.load_pixels()
    for i in range(len(img.pixels)):
        img.pixels[i] = py5.color(py5.random(255), py5.random(255), py5.random(255))
    img.update_pixels()


def draw():
    # Imagen original
    py5.image(img, 0, 0)

    # Solo canal rojo
    py5.tint(255, 0, 0)
    py5.image(img, 200, 0)

    # Solo canal verde
    py5.tint(0, 255, 0)
    py5.image(img, 400, 0)

    py5.no_tint()


py5.run_sketch()
