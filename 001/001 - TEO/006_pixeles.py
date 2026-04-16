import py5


def setup():
    py5.size(400, 400)
    py5.load_pixels()

    # Crear un patrón de píxeles
    for x in range(py5.width):
        for y in range(py5.height):
            # Calcular índice en el array de píxeles
            index = x + y * py5.width

            # Crear patrón de colores
            r = (x * 255) // py5.width
            g = (y * 255) // py5.height
            b = 128

            py5.pixels[index] = py5.color(r, g, b)

    py5.update_pixels()


py5.run_sketch()
