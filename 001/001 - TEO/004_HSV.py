import py5


def setup():
    py5.size(400, 400)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.no_stroke()


def draw():
    for i in range(360):
        py5.fill(i, 100, 100)
        py5.rect(i, 0, 1, py5.height)


py5.run_sketch()
