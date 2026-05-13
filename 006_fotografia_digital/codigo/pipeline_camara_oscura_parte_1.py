"""
pipeline_camara_oscura_parte_1.py

Parte 1 — Cámara oscura y procesamiento digital.

Pipeline completo:

1. Lee la imagen original.
2. Rota la imagen.
3. Genera histogramas RGB y escala de grises.
4. Convierte de BGR a HSV.
5. Separa canales H, S y V.
6. Ecualiza únicamente el canal V.
7. Reconstruye la imagen HSV.
8. Convierte nuevamente a BGR.
9. Guarda todos los resultados en imagenes/procesadas.

Uso:
python "006_fotografia_digital/codigo/pipeline_camara_oscura_parte_1.py"
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

ORIGINALES_DIR = BASE_DIR / "imagenes" / "originales"
PROCESADAS_DIR = BASE_DIR / "imagenes" / "procesadas"

NOMBRE_IMAGEN = "img_camara_oscura_original"

EXTENSIONES_VALIDAS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
    ".tif",
    ".tiff"
)


# ============================================================
# UTILIDADES
# ============================================================

def buscar_imagen_por_nombre(
    carpeta: Path,
    nombre_base: str
) -> Path:
    """
    Busca una imagen automáticamente usando extensiones válidas.
    """

    for extension in EXTENSIONES_VALIDAS:

        ruta = carpeta / f"{nombre_base}{extension}"

        if ruta.exists():
            return ruta

    raise FileNotFoundError(
        f"No se encontró la imagen '{nombre_base}' "
        f"en {carpeta}"
    )


def leer_imagen_bgr(ruta: Path) -> np.ndarray:
    """
    Lee una imagen usando OpenCV.
    """

    imagen = cv2.imread(
        str(ruta),
        cv2.IMREAD_COLOR
    )

    if imagen is None:
        raise ValueError(
            f"OpenCV no pudo leer la imagen: {ruta}"
        )

    return imagen


# ============================================================
# ROTACION
# ============================================================

def rotar_imagen(
    imagen: np.ndarray,
    angulo: float
) -> np.ndarray:
    """
    Rota una imagen manteniendo dimensiones.
    """

    alto, ancho = imagen.shape[:2]

    centro = (ancho // 2, alto // 2)

    matriz_rotacion = cv2.getRotationMatrix2D(
        centro,
        angulo,
        1.0
    )

    imagen_rotada = cv2.warpAffine(
        imagen,
        matriz_rotacion,
        (ancho, alto),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REPLICATE
    )

    return imagen_rotada


# ============================================================
# HISTOGRAMAS
# ============================================================

def guardar_histograma_rgb(
    imagen_bgr: np.ndarray,
    ruta_salida: Path
) -> None:
    """
    Genera histograma RGB.
    """

    colores = ("b", "g", "r")

    plt.figure(figsize=(10, 5))

    for i, color in enumerate(colores):

        histograma = cv2.calcHist(
            [imagen_bgr],
            [i],
            None,
            [256],
            [0, 256]
        )

        plt.plot(
            histograma,
            color=color
        )

    plt.title("Histograma RGB")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def guardar_histograma_grises(
    imagen_bgr: np.ndarray,
    ruta_salida: Path
) -> None:
    """
    Genera histograma en escala de grises.
    """

    gris = cv2.cvtColor(
        imagen_bgr,
        cv2.COLOR_BGR2GRAY
    )

    plt.figure(figsize=(10, 5))

    plt.hist(
        gris.ravel(),
        bins=256,
        range=(0, 256)
    )

    plt.title("Histograma escala de grises")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def guardar_histograma_v(
    v_antes: np.ndarray,
    v_despues: np.ndarray,
    ruta_salida: Path
) -> None:
    """
    Histograma comparativo del canal V.
    """

    plt.figure(figsize=(10, 5))

    plt.hist(
        v_antes.ravel(),
        bins=256,
        range=(0, 255),
        alpha=0.60,
        label="V original"
    )

    plt.hist(
        v_despues.ravel(),
        bins=256,
        range=(0, 255),
        alpha=0.60,
        label="V ecualizado"
    )

    plt.title("Histograma canal V")
    plt.xlabel("Intensidad")
    plt.ylabel("Cantidad de píxeles")

    plt.legend()

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


# ============================================================
# HSV
# ============================================================

def ecualizar_valor_hsv(
    imagen_bgr: np.ndarray
) -> dict[str, np.ndarray]:
    """
    Ecualiza únicamente el canal V.
    """

    hsv = cv2.cvtColor(
        imagen_bgr,
        cv2.COLOR_BGR2HSV
    )

    h, s, v = cv2.split(hsv)

    v_ecualizado = cv2.equalizeHist(v)

    hsv_ecualizado = cv2.merge([
        h,
        s,
        v_ecualizado
    ])

    imagen_ecualizada_bgr = cv2.cvtColor(
        hsv_ecualizado,
        cv2.COLOR_HSV2BGR
    )

    return {
        "h": h,
        "s": s,
        "v_antes": v,
        "v_despues": v_ecualizado,
        "imagen_ecualizada_bgr": imagen_ecualizada_bgr,
    }


# ============================================================
# GUARDADO DE CANALES
# ============================================================

def guardar_canales(
    etapas: dict[str, np.ndarray],
    salida_dir: Path,
    prefijo: str
) -> None:
    """
    Guarda canales HSV.
    """

    cv2.imwrite(
        str(salida_dir / f"{prefijo}_canal_h.png"),
        etapas["h"]
    )

    cv2.imwrite(
        str(salida_dir / f"{prefijo}_canal_s.png"),
        etapas["s"]
    )

    cv2.imwrite(
        str(salida_dir / f"{prefijo}_canal_v_antes.png"),
        etapas["v_antes"]
    )

    cv2.imwrite(
        str(salida_dir / f"{prefijo}_canal_v_despues.png"),
        etapas["v_despues"]
    )


# ============================================================
# COMPARACION
# ============================================================

def guardar_comparacion(
    imagen_original_bgr: np.ndarray,
    imagen_ecualizada_bgr: np.ndarray,
    ruta_salida: Path
) -> None:
    """
    Genera comparación lado a lado.
    """

    original_rgb = cv2.cvtColor(
        imagen_original_bgr,
        cv2.COLOR_BGR2RGB
    )

    ecualizada_rgb = cv2.cvtColor(
        imagen_ecualizada_bgr,
        cv2.COLOR_BGR2RGB
    )

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(ecualizada_rgb)
    plt.title("Ecualizada HSV canal V")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


# ============================================================
# PIPELINE PRINCIPAL
# ============================================================

def procesar_imagen(
    entrada: Path,
    salida_dir: Path,
    prefijo: str
) -> list[Path]:

    salida_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # ========================================================
    # LECTURA
    # ========================================================

    imagen_original = leer_imagen_bgr(entrada)

    # ========================================================
    # ROTACION
    # ========================================================

    imagen_rotada = rotar_imagen(
        imagen_original,
        180
    )

    # ========================================================
    # HISTOGRAMAS
    # ========================================================

    guardar_histograma_rgb(
        imagen_rotada,
        salida_dir / f"{prefijo}_histograma_rgb.png"
    )

    guardar_histograma_grises(
        imagen_rotada,
        salida_dir / f"{prefijo}_histograma_grises.png"
    )

    # ========================================================
    # HSV
    # ========================================================

    etapas = ecualizar_valor_hsv(
        imagen_rotada
    )

    # ========================================================
    # RUTAS
    # ========================================================

    salida_rotada = (
        salida_dir /
        f"{prefijo}_rotada.png"
    )

    salida_ecualizada = (
        salida_dir /
        f"{prefijo}_ecualizada_hsv_v.png"
    )

    salida_histograma_v = (
        salida_dir /
        f"{prefijo}_histograma_v_antes_despues.png"
    )

    salida_comparacion = (
        salida_dir /
        f"{prefijo}_comparacion_original_ecualizada.png"
    )

    # ========================================================
    # GUARDADO
    # ========================================================

    cv2.imwrite(
        str(salida_rotada),
        imagen_rotada
    )

    cv2.imwrite(
        str(salida_ecualizada),
        etapas["imagen_ecualizada_bgr"]
    )

    guardar_histograma_v(
        etapas["v_antes"],
        etapas["v_despues"],
        salida_histograma_v
    )

    guardar_canales(
        etapas,
        salida_dir,
        prefijo
    )

    guardar_comparacion(
        imagen_rotada,
        etapas["imagen_ecualizada_bgr"],
        salida_comparacion
    )

    return [
        salida_rotada,
        salida_ecualizada,
        salida_histograma_v,
        salida_comparacion,
    ]


# ============================================================
# ARGPARSE
# ============================================================

def crear_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        description="Pipeline cámara oscura Parte 1"
    )

    parser.add_argument(
        "--entrada",
        type=Path,
        default=None,
        help="Ruta de imagen de entrada."
    )

    parser.add_argument(
        "--salida-dir",
        type=Path,
        default=PROCESADAS_DIR,
        help="Carpeta de salida."
    )

    parser.add_argument(
        "--prefijo",
        default=NOMBRE_IMAGEN,
        help="Prefijo archivos."
    )

    return parser


# ============================================================
# MAIN
# ============================================================

def main() -> None:

    args = crear_parser().parse_args()

    entrada = (
        args.entrada
        or buscar_imagen_por_nombre(
            ORIGINALES_DIR,
            NOMBRE_IMAGEN
        )
    )

    archivos_generados = procesar_imagen(
        entrada,
        args.salida_dir,
        args.prefijo
    )

    print("\nProcesamiento completado.\n")

    print(f"Imagen entrada: {entrada}\n")

    print("Archivos generados:")

    for archivo in archivos_generados:
        print(f"- {archivo}")


if __name__ == "__main__":
    main()