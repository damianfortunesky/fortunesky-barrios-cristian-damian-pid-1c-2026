import py5


def setup():
    py5.size(600, 200)
    py5.color_mode(py5.RGB, 255)
    py5.no_stroke()


def draw():
    # Canal Rojo
    py5.fill(200, 0, 0)
    py5.rect(0, 0, 200, 200)

    # Canal Verde
    py5.fill(0, 200, 0)
    py5.rect(200, 0, 200, 200)

    # Canal Azul
    py5.fill(0, 0, 200)
    py5.rect(400, 0, 200, 200)


py5.run_sketch()
