import py5


def setup():
    py5.size(400, 400)
    py5.background(0)  # RGB -> Red (rojo), Green (verde), Blue (azul)
    print("py5 funcionando correctamente")


def draw():
    py5.fill(90, 237, 221)
    py5.no_stroke()
    py5.ellipse(200, 200, 100, 100)


py5.run_sketch()
