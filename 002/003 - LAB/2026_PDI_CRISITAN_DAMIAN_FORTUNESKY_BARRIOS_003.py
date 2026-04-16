from PIL import Image, ImageOps
import os

# =========================
# EJECUTAR
# =========================

# cd "002\003 - LAB"
# .venv\Scripts\Activate.ps1
# python 2026_PDI_CRISITAN_DAMIAN_FORTUNESKY_BARRIOS_003.py


# =========================
# CONFIGURACIÓN
# =========================

# Ruta de entrada
INPUT_PATH = r"C:\Programacion\repositorio-ingenieria-datos\ifts24\fortunesky-barrios-cristian-damian-pid-1c-2026\002\003 - LAB\img\001_ACTIVDAD_3.jpg"

# Carpeta de salida
OUTPUT_DIR = r"C:\Programacion\repositorio-ingenieria-datos\ifts24\fortunesky-barrios-cristian-damian-pid-1c-2026\002\003 - LAB\img"

# =========================
# FUNCIONES
# =========================

def pixelar_imagen(img, grid_size):
    """
    Aplica muestreo + cuantificación simulada:
    - Reduce resolución
    - Reescala con NEAREST (efecto pixelado)
    """
    width, height = img.size

    # Muestreo (reduce a grid_size x grid_size)
    small = img.resize((grid_size, grid_size), Image.Resampling.BOX)

    # Cuantificación visual (expandir píxeles)
    pixelada = small.resize((width, height), Image.Resampling.NEAREST)

    return small, pixelada


# =========================
# PROCESO PRINCIPAL
# =========================

def main():
    print("Procesando imagen...")

    # Crear carpeta si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Cargar imagen
    img = Image.open(INPUT_PATH)

    # 2. Convertir a escala de grises
    img_gray = ImageOps.grayscale(img)

    # Guardar gris
    gray_path = os.path.join(OUTPUT_DIR, "img_gray.png")
    img_gray.save(gray_path)
    print(f"✔ Imagen en gris guardada: {gray_path}")

    # 3. Pixelado 8x8
    small8, pix8 = pixelar_imagen(img_gray, 8)

    path_8 = os.path.join(OUTPUT_DIR, "pixelada_8x8.png")
    pix8.save(path_8)
    print(f"✔ Pixelado 8x8 guardado: {path_8}")

    # 4. Pixelado 16x16
    small16, pix16 = pixelar_imagen(img_gray, 16)

    path_16 = os.path.join(OUTPUT_DIR, "pixelada_16x16.png")
    pix16.save(path_16)
    print(f"✔ Pixelado 16x16 guardado: {path_16}")

    print("\nProceso terminado.")

    # OPCIONAL: mostrar imágenes
    img_gray.show(title="Grises")
    pix8.show(title="8x8")
    pix16.show(title="16x16")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main()