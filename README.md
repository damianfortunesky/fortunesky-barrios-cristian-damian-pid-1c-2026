# Laboratorio de Fundamentos de Procesamiento Digital de Imágenes, Visión por Computadora, VLMs y Agentic AI

**Hacia una Visión Técnico-Humanista: Procesamiento, Algoritmos y Sociedad**

**IFTS Nº 24 — Ciencia de Datos e Inteligencia Artificial**  
**3er año — 1er cuatrimestre 2026**  
**Martes 20:30–22:30 / Miércoles 18:30–22:30**

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad  
[matiasbarreto@ifts24.edu.ar](mailto:matiasbarreto@ifts24.edu.ar)

**Ayudante de Trabajos Prácticos:** Cynthia Marcela Villagra

---

## Qué es este repositorio

Este repositorio contiene el material de laboratorio de la materia. El material se organiza en carpetas numeradas (`001/`, `002/`, `003/`, ...) que se publican semana a semana a medida que avanza la cursada.

Cada carpeta corresponde a una unidad temática y contiene notebooks (`.ipynb`) y scripts (`.py`) para trabajar en clase y fuera de ella.

**Librerías principales del curso:**
- **OpenCV (cv2):** Procesamiento de imágenes y visión computacional
- **NumPy:** Manipulación de matrices y arrays
- **Matplotlib:** Visualización de imágenes y gráficos
- **Pillow (PIL):** Manipulación básica de imágenes
- **scikit-image:** Algoritmos avanzados de procesamiento
- **py5:** Introducción a conceptos visuales (unidades iniciales únicamente)

---

## Importante: No necesitás permisos de administrador

Si trabajás en una computadora de tu empleo o no tenés permisos de admin, **esto no es un problema**. Todo el software se instala dentro de una carpeta del proyecto usando un **entorno virtual de Python**.

El entorno virtual es una instalación aislada de Python que:
- No requiere permisos de administrador
- No modifica el Python del sistema
- Todo queda dentro de la carpeta del repositorio
- Podés borrarlo y recrearlo cuando quieras

---

## Requisitos previos

Antes de arrancar, asegurate de tener instalado en tu máquina:

1. **Python 3.10 o superior** — [Descarga oficial](https://www.python.org/downloads/)
   - Durante la instalación en Windows, marcá la opción **"Add Python to PATH"**
   - **No necesitás "Install for all users"** — la instalación para tu usuario actual funciona perfectamente
2. **Git** — [Descarga oficial](https://git-scm.com/downloads)
   - Elegí la opción "Git from the command line and also from 3rd-party software"
3. **Visual Studio Code** (recomendado) — [Descarga oficial](https://code.visualstudio.com/)
   - Instalá la extensión **Python** desde el marketplace de VS Code
   - Instalá la extensión **Jupyter** para trabajar con notebooks

**Alternativa si no podés instalar nada:** Usá [Google Colab](https://colab.research.google.com) directamente. Los notebooks de este repositorio están preparados para ejecutarse en la nube.

---

## Setup inicial (una sola vez)

Abrí una terminal (en Windows: PowerShell o Git Bash) y ejecutá los siguientes comandos:

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattbarreto/ifts24-lab-pdi-2026.git
cd ifts24-lab-pdi-2026
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Esto crea una carpeta `.venv/` dentro del proyecto con una instalación limpia de Python.

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Git Bash / CMD):**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Si PowerShell muestra un error de permisos, ejecutá primero (solo una vez en tu usuario):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando el entorno esté activo, verás `(.venv)` al principio de la línea de la terminal.

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Verificar la instalación

```bash
python -c "import cv2; import numpy; print('OpenCV y NumPy instalados correctamente')"
```

---

## Cómo actualizar cada semana

Cada vez que se publique material nuevo, desde la carpeta del repositorio ejecutá:

```bash
git pull
```

Si se agregan nuevas dependencias, se anunciará en clase. En ese caso, con el entorno activado:

```bash
pip install -r requirements.txt
```

---

## Estructura del repositorio

```
ifts24-lab-pdi-2026/
├── README.md                    <- Este archivo
├── requirements.txt             <- Dependencias del entorno
├── .gitignore                   <- Archivos ignorados por git
│
├── 001/                         <- Unidad 1: Introducción con py5
│   ├── 000_intro_py5.py
│   ├── 001_basico.py
│   ├── 001b_basico_HSV.py
│   ├── 002_info.py
│   ├── 003_RGB.py
│   ├── 004_HSV.py
│   ├── 005_upload_img.py
│   ├── 006_pixeles.py
│   ├── 007_pixeles.py
│   ├── 008_filtro.py
│   ├── 009_mouse.py
│   ├── 009b_mouse.py
│   ├── 009c_mouse.py
│   ├── 010_filtro.py
│   ├── 011_filtro.py
│   ├── 012_filtro.py
│   ├── 013_filtro.py
│   ├── 014_filtro.py
│   ├── 015_dibujo.py
│   ├── img/                     <- Imágenes de ejemplo
│   ├── save/                    <- Carpeta para guardar resultados
│   └── info.txt                 <- Referencia rápida de py5
│
├── 002/                         <- Unidad 2: Fundamentos de la Imagen Digital
│   ├── 00_setup_colab.ipynb     <- Configuración para Google Colab
│   ├── 02a_fundamentos_teoria_colab.ipynb      <- Teoría (Colab)
│   ├── 02b_fundamentos_practica_local.ipynb    <- Práctica (local)
│   └── 02c_laboratorio_fundamentos.ipynb       <- Laboratorio
│
└── ...                          <- Unidades siguientes (se publican semanalmente)
```

---

## Cómo ejecutar los ejercicios

### Opción A: Trabajo local con VS Code (recomendado)

1. Abrí la carpeta del repositorio en VS Code: `Archivo > Abrir carpeta...`
2. Asegurate de tener el entorno virtual activado (ver `.venv` en la barra de estado de VS Code)
3. Abrí cualquier archivo `.py` o `.ipynb`
4. Para scripts `.py`: presioná `F5` o el botón de play
5. Para notebooks `.ipynb`: ejecutá las celdas con `Shift + Enter`

### Opción B: Google Colab (sin instalación)

1. Andá a [Google Colab](https://colab.research.google.com)
2. Subí el notebook `.ipynb` que querés ejecutar
3. Los notebooks incluyen la configuración inicial para instalar dependencias en Colab

---

## Resolución de problemas frecuentes

### "No se puede cargar el script porque la ejecución de scripts está deshabilitada en este sistema"
Ejecutá en PowerShell como administrador (solo una vez):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "python no se reconoce como comando"
Python no se agregó al PATH. Reinstalá marcando "Add Python to PATH", o usá `py` en lugar de `python` en Windows.

### "No module named 'cv2'" / "No module named 'numpy'"
Verificá que el entorno virtual esté activado (debés ver `(.venv)` al inicio de la línea). Si lo está, reinstalá las dependencias:
```bash
pip install -r requirements.txt
```

### Las imágenes no se cargan (error al leer imágenes)
Verificá que:
1. Las imágenes estén en la carpeta correspondiente
2. Estés ejecutando el script desde la carpeta correcta
3. Usás rutas relativas: `img/mi_imagen.jpg` en lugar de rutas absolutas

### py5 no abre la ventana o no muestra la imagen
En algunos sistemas operativos, py5 requiere un backend gráfico adicional. Instalá glfw:
```bash
pip install glfw
```
Si el problema persiste, consultá la [guía de instalación de py5](https://py5coding.org/content/install.html) que detalla los requisitos específicos para cada sistema operativo.

### Error de Java al ejecutar py5
py5 requiere Java para funcionar. Si ves un error relacionado con Java, instalá la versión apropiada según tu sistema operativo siguiendo las [instrucciones oficiales de instalación de py5](https://py5coding.org/content/install.html).

---

## Recursos adicionales

- [Documentación de OpenCV](https://docs.opencv.org/)
- [Documentación de NumPy](https://numpy.org/doc/)
- [Documentación de Matplotlib](https://matplotlib.org/)
- [Documentación de scikit-image](https://scikit-image.org/docs/)
- [Documentación de py5](https://py5coding.org/)
- [Guía de instalación de py5 (incluye requisitos de Java)](https://py5coding.org/content/install.html)
- [Google Colab Help](https://colab.research.google.com/notebooks/intro.ipynb)

---

## Licencia

Este material se distribuye bajo licencia [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es): podés usarlo y adaptarlo con atribución, sin fines comerciales, y compartiendo bajo la misma licencia.
