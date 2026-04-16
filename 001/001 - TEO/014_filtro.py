import py5


def setup():
    py5.size(400, 400)


def draw():
    img = py5.load_image("img/imagen.jpg")
    py5.image(img, 0, 0, 400, 400)  # Especificar el tamaño de la imagen
    py5.apply_filter(py5.DILATE)


py5.run_sketch()
