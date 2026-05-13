"""
Uso:
python "006_fotografia_digital/codigo/pipeline_composicion_visual_parte_2_y_3.py"
"""

from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# RUTAS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DIR_ORIGINALES = BASE_DIR / "imagenes" / "originales"
DIR_PROCESADAS = BASE_DIR / "imagenes" / "procesadas"

DIR_PROCESADAS.mkdir(parents=True, exist_ok=True)

# =========================================================
# IMAGENES
# =========================================================

IMG_ACT4_ORIGINAL = DIR_ORIGINALES / "actividad4_original.jpg"

IMG_ACT5_ORIGINAL = DIR_ORIGINALES / "actividad5_original_amplia.jpg"

IMG_ACT6_VISTA_A = DIR_ORIGINALES / "actividad6_vista_a.jpg"
IMG_ACT6_VISTA_B = DIR_ORIGINALES / "actividad6_vista_b.jpg"

IMG_ACT7_FINAL = DIR_ORIGINALES / "actividad7_luz_final.jpg"
IMG_ACT7_ALTERNATIVA = DIR_ORIGINALES / "actividad7_luz_base.jpg"

# =========================================================
# FUNCIONES
# =========================================================

def cargar_rgb(ruta):
    img_bgr = cv2.imread(str(ruta))

    if img_bgr is None:
        raise FileNotFoundError(f"No se pudo cargar: {ruta}")

    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


def guardar_rgb(ruta, imagen_rgb):
    imagen_bgr = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(ruta), imagen_bgr)


def guardar_figura(fig, ruta):
    fig.savefig(ruta, bbox_inches="tight")
    plt.close(fig)


# =========================================================
# ACTIVIDAD 4
# SIMPLICIDAD VISUAL
# =========================================================

img_act4_original = cargar_rgb(IMG_ACT4_ORIGINAL)

alto, ancho = img_act4_original.shape[:2]

crop_act4 = img_act4_original[
    int(alto * 0.10):int(alto * 0.90),
    int(ancho * 0.22):int(ancho * 0.82)
]

gris_act4 = cv2.cvtColor(crop_act4, cv2.COLOR_RGB2GRAY)

guardar_rgb(
    DIR_PROCESADAS / "actividad4_final_color.jpg",
    crop_act4
)

cv2.imwrite(
    str(DIR_PROCESADAS / "actividad4_final_grises.jpg"),
    gris_act4
)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img_act4_original)
ax[0].set_title("Actividad 4 - Original")
ax[0].axis("off")

ax[1].imshow(gris_act4, cmap="gray")
ax[1].set_title("Actividad 4 - Final")
ax[1].axis("off")

guardar_figura(
    fig,
    DIR_PROCESADAS / "actividad4_comparacion.jpg"
)

# =========================================================
# ACTIVIDAD 5
# REENCUADRE
# =========================================================

img_act5 = cargar_rgb(IMG_ACT5_ORIGINAL)

alto5, ancho5 = img_act5.shape[:2]

crop_a = img_act5[
    int(alto5 * 0.32):int(alto5 * 0.92),
    int(ancho5 * 0.48):int(ancho5 * 0.92)
]

crop_b = img_act5[
    int(alto5 * 0.18):int(alto5 * 0.78),
    int(ancho5 * 0.58):int(ancho5 * 0.82)
]

guardar_rgb(
    DIR_PROCESADAS / "actividad5_crop_a.jpg",
    crop_a
)

guardar_rgb(
    DIR_PROCESADAS / "actividad5_crop_b.jpg",
    crop_b
)

img_marcas = img_act5.copy()

cv2.rectangle(
    img_marcas,
    (int(ancho5 * 0.48), int(alto5 * 0.32)),
    (int(ancho5 * 0.92), int(alto5 * 0.92)),
    (255, 0, 0),
    5
)

cv2.rectangle(
    img_marcas,
    (int(ancho5 * 0.58), int(alto5 * 0.18)),
    (int(ancho5 * 0.82), int(alto5 * 0.78)),
    (0, 255, 0),
    5
)

guardar_rgb(
    DIR_PROCESADAS / "actividad5_marcas.jpg",
    img_marcas
)

# =========================================================
# ACTIVIDAD 6
# PUNTO DE VISTA
# =========================================================

img_vista_a = cargar_rgb(IMG_ACT6_VISTA_A)
img_vista_b = cargar_rgb(IMG_ACT6_VISTA_B)

guardar_rgb(
    DIR_PROCESADAS / "actividad6_vista_a.jpg",
    img_vista_a
)

guardar_rgb(
    DIR_PROCESADAS / "actividad6_vista_b.jpg",
    img_vista_b
)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img_vista_a)
ax[0].set_title("Vista A")
ax[0].axis("off")

ax[1].imshow(img_vista_b)
ax[1].set_title("Vista B")
ax[1].axis("off")

guardar_figura(
    fig,
    DIR_PROCESADAS / "actividad6_comparacion.jpg"
)

# =========================================================
# ACTIVIDAD 7
# LUZ
# =========================================================

img_luz_final = cargar_rgb(IMG_ACT7_FINAL)
img_luz_alt = cargar_rgb(IMG_ACT7_ALTERNATIVA)

guardar_rgb(
    DIR_PROCESADAS / "actividad7_luz_final.jpg",
    img_luz_final
)

guardar_rgb(
    DIR_PROCESADAS / "actividad7_luz_alternativa.jpg",
    img_luz_alt
)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img_luz_alt)
ax[0].set_title("Luz alternativa")
ax[0].axis("off")

ax[1].imshow(img_luz_final)
ax[1].set_title("Luz final")
ax[1].axis("off")

guardar_figura(
    fig,
    DIR_PROCESADAS / "actividad7_comparacion.jpg"
)

# =========================================================
# ACTIVIDAD 8
# SELECCION CRITICA
# =========================================================

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

desc1 = cargar_rgb(IMG_ACT6_VISTA_A)
desc2 = cargar_rgb(IMG_ACT7_ALTERNATIVA)
elegida = cargar_rgb(IMG_ACT7_FINAL)

ax[0].imshow(desc1)
ax[0].set_title("Descartada 1")
ax[0].axis("off")

ax[1].imshow(desc2)
ax[1].set_title("Descartada 2")
ax[1].axis("off")

ax[2].imshow(elegida)
ax[2].set_title("Imagen elegida")
ax[2].axis("off")

guardar_figura(
    fig,
    DIR_PROCESADAS / "actividad8_seleccion_critica.jpg"
)

# =========================================================
# ACTIVIDAD 10
# ANEXO TECNICO
# =========================================================

img_tecnica = cargar_rgb(IMG_ACT7_FINAL)

# RGB -> HSV
img_hsv = cv2.cvtColor(img_tecnica, cv2.COLOR_RGB2HSV)

# Ecualizacion canal V
h, s, v = cv2.split(img_hsv)

v_eq = cv2.equalizeHist(v)

img_hsv_eq = cv2.merge((h, s, v_eq))

img_rgb_eq = cv2.cvtColor(img_hsv_eq, cv2.COLOR_HSV2RGB)

# Escala de grises
img_grises = cv2.cvtColor(img_tecnica, cv2.COLOR_RGB2GRAY)

guardar_rgb(
    DIR_PROCESADAS / "actividad10_hsv_ecualizado.jpg",
    img_rgb_eq
)

cv2.imwrite(
    str(DIR_PROCESADAS / "actividad10_grises.jpg"),
    img_grises
)

# Histograma
fig = plt.figure(figsize=(8, 5))

plt.hist(v.ravel(), bins=256)

plt.title("Histograma canal V")
plt.xlabel("Intensidad")
plt.ylabel("Cantidad de pixeles")

guardar_figura(
    fig,
    DIR_PROCESADAS / "actividad10_histograma.jpg"
)

print("===================================")
print("PIPELINE FINALIZADO CORRECTAMENTE")
print("===================================")