import py5


def setup():
    py5.size(800, 600)
    py5.background(255)  # Fondo blanco

    # Ajusta la velocidad de generación
    py5.frameRate(30)


def draw():
    py5.background(255)  # Limpia el lienzo en cada frame

    # Genera un patrón de Mandelbrot
    x = py5.noise(py5.width * 0.01, py5.height * 0.01)
    y = py5.noise(py5.width * 0.01, py5.height * 0.01)
    iterations = 50
    z = complex(0, 0)
    for i in range(iterations):
        z = z**2 + complex(x, y)
        if abs(z) > 2:
            break
        color = int(i * 255 / iterations)
        py5.fill(color)
        py5.rect(py5.mouse_x - 50, py5.mouse_y - 50, 100, 100)


py5.run_sketch()
