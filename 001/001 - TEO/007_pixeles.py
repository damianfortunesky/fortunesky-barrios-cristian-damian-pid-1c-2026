import py5

img = None


def setup():
    global img
    py5.size(400, 400)
    py5.background(255)

    # Verificar que la imagen existe
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca una imagen en la carpeta 'img/imagen.jpg'")
        return

    # Procesar imagen en setup DESPUÉS de configurar el contexto
    if img is not None:
        procesar_imagen()


def procesar_imagen():
    """Procesa la imagen invirtiendo colores"""
    global img

    print("Procesando imagen...")

    img.load_pixels()

    for i in range(len(img.pixels)):
        # Obtener color actual
        c = img.pixels[i]

        # Extraer componentes
        r = py5.red(c)
        g = py5.green(c)
        b = py5.blue(c)

        # Invertir y asignar
        img.pixels[i] = py5.color(255 - r, 255 - g, 255 - b)

    img.update_pixels()
    print("✓ Imagen procesada")


def draw():
    py5.background(255)

    if img is not None:
        py5.image(img, 0, 0, py5.width, py5.height)
    else:
        py5.fill(255, 0, 0)
        py5.text("Error: Imagen no encontrada", 50, 200)


def key_pressed():
    if py5.key == "s" and img is not None:
        img.save("imagen_invertida.jpg")
        print("💾 Imagen guardada como 'imagen_invertida.jpg'")


if __name__ == "__main__":
    py5.run_sketch()
