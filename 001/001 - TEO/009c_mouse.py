import py5


def setup():
    py5.size(400, 300)
    py5.background(255)
    print("py5 funcionando correctamente")


def draw():
    py5.background(255)

    # Solo dibujar cuando el mouse esté presionado
    if py5.is_mouse_pressed:
        py5.fill(255, 0, 0)
        py5.circle(py5.mouse_x, py5.mouse_y, 20)


py5.run_sketch()
